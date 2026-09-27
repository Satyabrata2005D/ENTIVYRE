"""
Multi-Pass Candidate Generation Engine for ENTIVYRE.
Phase 14: Multi-pass candidate union, deduplication, provenance tracking,
and candidate-pair contract enforcement.

Guarantees:
- Multi-pass retrieval:
    Pass 1: Deterministic Standard Inverted Index (exact, sorted tokens, postal code).
    Pass 2: Sparse Character N-Gram TF-IDF (sub-word typo and OCR error tolerance).
- Multi-source provenance: records which pass(es) retrieved each candidate.
- Strict Candidate-Pairs Invariant:
    - Exactly 0 self-matches.
    - Only Target Source entities (S2 & S3).
    - No duplicate candidate IDs per anchor.
    - Global cap K <= max_candidates (default 50).
- Candidate recall auditing against GroundTruthStore.
"""
from __future__ import annotations

import time
from collections import defaultdict
from dataclasses import dataclass, asdict
from typing import Dict, Iterable, List, Optional, Set, Tuple, Any

from entivyre.utils.logger import get_logger
from ber.blocking.standard_blocker import StandardBlocker, BlockingRecord
from ber.retrieval.tfidf_retriever import SparseCharTfidfRetriever, RetrievalCandidate
from ber.labels.ground_truth import GroundTruthStore

logger = get_logger("ber.blocking.candidate_generator", stage="14_multi_pass_candidate_generation")


@dataclass(frozen=True)
class EnrichedCandidate:
    """A retrieved candidate with provenance tracking and retrieval features."""
    target_id: str
    retrieval_sources: Tuple[str, ...]
    tfidf_similarity: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class CandidateGenerationAuditMetrics:
    """Summary metrics evaluating the multi-pass candidate generation run."""
    total_anchors: int
    total_candidate_pairs: int
    mean_candidates_per_anchor: float
    max_candidates_per_anchor: int
    zero_candidate_anchor_count: int
    pass1_exclusive_count: int
    pass2_exclusive_count: int
    both_passes_count: int
    candidate_recall: float
    elapsed_time_s: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class MultiPassCandidateGenerator:
    """
    Combines Standard Inverted Index Blocker and Sparse Character N-Gram TF-IDF Retriever
    into a unified, deduplicated candidate generation pipeline.
    """

    def __init__(
        self,
        max_candidates: int = 50,
        standard_blocker_top_k: int = 35,
        tfidf_top_k: int = 25,
        tfidf_min_similarity: float = 0.35,
        enable_tfidf_pass: bool = True,
    ):
        self.max_candidates = max_candidates
        self.standard_blocker_top_k = standard_blocker_top_k
        self.tfidf_top_k = tfidf_top_k
        self.tfidf_min_similarity = tfidf_min_similarity
        self.enable_tfidf_pass = enable_tfidf_pass

        self.standard_blocker = StandardBlocker(
            max_candidates_per_anchor=self.standard_blocker_top_k,
            max_key_frequency=1000,
        )
        self.tfidf_retriever = SparseCharTfidfRetriever(ngram_size=3, min_df=1)
        self._target_count: int = 0

    def __len__(self) -> int:
        return self._target_count

    def index_targets(self, targets: List[BlockingRecord]) -> None:
        """
        Index target records into both standard inverted index and TF-IDF index.
        """
        self._target_count = len(targets)
        logger.info(
            f"Indexing {len(targets)} targets across standard blocker and TF-IDF retriever",
            extra={"payload": {"total_targets": len(targets)}},
        )

        # 1. Index in Standard Blocker
        self.standard_blocker.index_targets_batch(targets)

        # 2. Index in Character TF-IDF Retriever
        if self.enable_tfidf_pass:
            tfidf_corpus: List[Tuple[str, str]] = []
            for t in targets:
                # Text for TF-IDF: canonical name + address tokens
                text = t.norm_name.canonical
                if t.norm_addr.clean:
                    text = f"{text} {t.norm_addr.clean}"
                tfidf_corpus.append((t.entity_id, text))

            self.tfidf_retriever.fit_and_index(tfidf_corpus)

    def generate_candidates(self, anchor: BlockingRecord) -> List[EnrichedCandidate]:
        """
        Generate, merge, and deduplicate candidates for a single anchor entity.
        Returns a sorted, prioritized list of EnrichedCandidate objects capped at max_candidates.
        """
        # Pass 1: Standard Inverted Index Blocker
        pass1_ids = self.standard_blocker.retrieve_candidates(anchor)
        pass1_set = set(pass1_ids)

        # Pass 2: Sparse Character TF-IDF Retriever
        pass2_map: Dict[str, float] = {}
        if self.enable_tfidf_pass:
            query_text = anchor.norm_name.canonical
            if anchor.norm_addr.clean:
                query_text = f"{query_text} {anchor.norm_addr.clean}"

            tfidf_cands = self.tfidf_retriever.retrieve_top_k(
                query_text=query_text,
                k=self.tfidf_top_k,
                min_similarity=self.tfidf_min_similarity,
            )
            for c in tfidf_cands:
                if c.target_id != anchor.entity_id:
                    pass2_map[c.target_id] = c.similarity_score

        # Merge and track provenance
        all_target_ids = set(pass1_set) | set(pass2_map.keys())
        # Prevent self match
        all_target_ids.discard(anchor.entity_id)

        candidates: List[EnrichedCandidate] = []
        for tid in all_target_ids:
            in_pass1 = tid in pass1_set
            in_pass2 = tid in pass2_map
            sources: List[str] = []
            if in_pass1:
                sources.append("standard_blocker")
            if in_pass2:
                sources.append("tfidf_retriever")

            sim_score = pass2_map.get(tid, 0.0)

            candidates.append(
                EnrichedCandidate(
                    target_id=tid,
                    retrieval_sources=tuple(sources),
                    tfidf_similarity=sim_score,
                )
            )

        # Priority Ranking:
        # 1. Retrieved by both passes (highest confidence)
        # 2. Highest TF-IDF similarity
        # 3. Deterministic target_id tie-breaker
        def sort_key(c: EnrichedCandidate):
            both_passes = 1 if len(c.retrieval_sources) >= 2 else 0
            return (-both_passes, -c.tfidf_similarity, c.target_id)

        candidates.sort(key=sort_key)
        return candidates[: self.max_candidates]

    def generate_candidate_pairs_map(
        self,
        anchors: Iterable[BlockingRecord],
    ) -> Dict[str, List[str]]:
        """
        Generate a mapping of anchor_id -> List[candidate_id] for downstream models.
        """
        pair_map: Dict[str, List[str]] = {}
        for anchor in anchors:
            cands = self.generate_candidates(anchor)
            pair_map[anchor.entity_id] = [c.target_id for c in cands]
        return pair_map

    def audit_candidate_generation(
        self,
        anchors: Iterable[BlockingRecord],
        ground_truth: GroundTruthStore,
    ) -> CandidateGenerationAuditMetrics:
        """
        Full audit of multi-pass candidate generation quality, volume, and recall.
        """
        t0 = time.perf_counter()
        total_anchors = 0
        total_candidate_pairs = 0
        max_candidates = 0
        zero_candidates = 0

        pass1_exclusive = 0
        pass2_exclusive = 0
        both_passes = 0

        total_true_targets = 0
        found_true_targets = 0

        for anchor in anchors:
            total_anchors += 1
            cands = self.generate_candidates(anchor)
            n_cands = len(cands)
            total_candidate_pairs += n_cands
            if n_cands == 0:
                zero_candidates += 1
            if n_cands > max_candidates:
                max_candidates = n_cands

            cand_ids = set()
            for c in cands:
                cand_ids.add(c.target_id)
                if len(c.retrieval_sources) >= 2:
                    both_passes += 1
                elif "standard_blocker" in c.retrieval_sources:
                    pass1_exclusive += 1
                elif "tfidf_retriever" in c.retrieval_sources:
                    pass2_exclusive += 1

            true_targets = ground_truth.get_target_set(anchor.entity_id)
            if true_targets:
                total_true_targets += len(true_targets)
                found_true_targets += len(true_targets & cand_ids)

        elapsed = time.perf_counter() - t0
        mean_cands = (total_candidate_pairs / total_anchors) if total_anchors > 0 else 0.0
        recall = (found_true_targets / total_true_targets) if total_true_targets > 0 else 1.0

        metrics = CandidateGenerationAuditMetrics(
            total_anchors=total_anchors,
            total_candidate_pairs=total_candidate_pairs,
            mean_candidates_per_anchor=round(mean_cands, 4),
            max_candidates_per_anchor=max_candidates,
            zero_candidate_anchor_count=zero_candidates,
            pass1_exclusive_count=pass1_exclusive,
            pass2_exclusive_count=pass2_exclusive,
            both_passes_count=both_passes,
            candidate_recall=round(recall, 4),
            elapsed_time_s=round(elapsed, 4),
        )

        logger.info(
            f"Multi-pass candidate generation audit: {total_candidate_pairs} pairs, recall={metrics.candidate_recall}",
            extra={"payload": metrics.to_dict()},
        )
        return metrics
