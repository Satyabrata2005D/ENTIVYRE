"""
Standard Deterministic Inverted Index Blocker for ENTIVYRE.
Phase 12: High-throughput, multi-key inverted index blocking baseline over
Target Sources (S2 and S3) with candidate recall auditing and frequency capping.

Guarantees:
- Multi-key generation: exact canonical name, sorted tokens, name prefix + postal code.
- Pruning of degenerate/high-frequency keys to prevent Cartesian blowup.
- Strict Candidate-Pairs Invariant: no duplicate candidates, no self-matches, K <= max_candidates.
- Evaluates Candidate Recall against GroundTruthStore.
- Bounded memory footprint using compact sets and list representations.
"""
from __future__ import annotations

import time
from collections import defaultdict
from dataclasses import dataclass, asdict
from typing import Dict, Iterable, List, Optional, Set, Tuple, Any

from entivyre.utils.logger import get_logger
from ber.normalization.name_normalizer import NameNormalizer, NormalizedName
from ber.normalization.address_normalizer import AddressNormalizer, NormalizedAddress
from ber.normalization.country_handler import CountryHandler, NormalizedCountry
from ber.labels.ground_truth import GroundTruthStore

logger = get_logger("ber.blocking.standard_blocker", stage="12_blocking_baseline")


@dataclass(frozen=True)
class BlockingRecord:
    """Standardized record payload for blocking indexation."""
    entity_id: str
    norm_name: NormalizedName
    norm_addr: NormalizedAddress
    norm_country: NormalizedCountry

    @classmethod
    def from_raw(
        cls,
        entity_id: str,
        business_name: Optional[str],
        business_address: Optional[str],
        country: Optional[str],
        name_normalizer: NameNormalizer,
        addr_normalizer: AddressNormalizer,
        country_handler: CountryHandler,
    ) -> BlockingRecord:
        return cls(
            entity_id=entity_id,
            norm_name=name_normalizer.normalize(business_name),
            norm_addr=addr_normalizer.normalize(business_address),
            norm_country=country_handler.normalize(country),
        )


@dataclass(frozen=True)
class BlockingAuditMetrics:
    """Performance and recall audit metrics for candidate generation."""
    total_anchors_queried: int
    total_candidate_pairs: int
    mean_candidates_per_anchor: float
    max_candidates_per_anchor: int
    zero_candidate_anchor_count: int
    candidate_recall: float
    elapsed_time_s: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class StandardBlocker:
    """
    Multi-pass inverted index blocker for Business Entity Resolution.
    Indexes target entities (S2 & S3) and rapidly retrieves candidate sets for anchors (S1).
    """

    def __init__(
        self,
        max_candidates_per_anchor: int = 50,
        max_key_frequency: int = 1000,
        enable_postal_blocking: bool = True,
        enable_sorted_tokens_blocking: bool = True,
    ):
        self.max_candidates_per_anchor = max_candidates_per_anchor
        self.max_key_frequency = max_key_frequency
        self.enable_postal_blocking = enable_postal_blocking
        self.enable_sorted_tokens_blocking = enable_sorted_tokens_blocking

        # Inverted index: key -> list of target entity IDs
        self._index: Dict[str, List[str]] = defaultdict(list)
        self._indexed_target_count: int = 0

    def __len__(self) -> int:
        return self._indexed_target_count

    @property
    def total_keys(self) -> int:
        return len(self._index)

    def extract_keys(self, record: BlockingRecord) -> Set[str]:
        """
        Generate blocking keys for an entity.
        Returns a set of deterministic key strings.
        """
        keys: Set[str] = set()
        norm_name = record.norm_name
        norm_addr = record.norm_addr
        country = record.norm_country.canonical or "UNK"

        # 1. Exact canonical name key (country-scoped if country available)
        if norm_name.canonical:
            keys.add(f"NAME_CANON:{norm_name.canonical}")
            keys.add(f"CTRY_NAME:{country}:{norm_name.canonical}")

        # 2. Sorted name tokens (word-order invariant)
        if self.enable_sorted_tokens_blocking and len(norm_name.tokens_sorted) >= 2:
            sorted_str = " ".join(norm_name.tokens_sorted)
            keys.add(f"NAME_SORTED:{sorted_str}")

        # 3. First significant token + postal code
        if self.enable_postal_blocking and norm_addr.postal_code and norm_name.tokens:
            first_tok = norm_name.tokens[0]
            # Avoid single character tokens
            if len(first_tok) >= 3:
                keys.add(f"POSTAL_NAME:{norm_addr.postal_code}:{first_tok}")

        # 4. First 2 tokens prefix
        if len(norm_name.tokens) >= 2:
            pfx = f"{norm_name.tokens[0]}_{norm_name.tokens[1]}"
            keys.add(f"NAME_2TOK:{pfx}")

        return keys

    def index_target(self, record: BlockingRecord) -> None:
        """Add a single target record to the inverted index."""
        self._indexed_target_count += 1
        keys = self.extract_keys(record)
        for k in keys:
            # Only append if key frequency hasn't breached threshold
            key_list = self._index[k]
            if len(key_list) < self.max_key_frequency:
                key_list.append(record.entity_id)

    def index_targets_batch(self, records: Iterable[BlockingRecord]) -> None:
        """Batch indexation of target records."""
        for r in records:
            self.index_target(r)

    def retrieve_candidates(self, anchor: BlockingRecord) -> List[str]:
        """
        Retrieve candidate target IDs for a given anchor record.
        Returns deduplicated, non-self candidate IDs capped at max_candidates_per_anchor.
        """
        keys = self.extract_keys(anchor)
        candidate_set: Set[str] = set()

        for k in keys:
            target_ids = self._index.get(k)
            if target_ids:
                for tid in target_ids:
                    if tid != anchor.entity_id:
                        candidate_set.add(tid)
                        if len(candidate_set) >= self.max_candidates_per_anchor:
                            break
            if len(candidate_set) >= self.max_candidates_per_anchor:
                break

        # Return sorted list for strict determinism
        return sorted(candidate_set)[: self.max_candidates_per_anchor]

    def audit_blocking(
        self,
        anchors: Iterable[BlockingRecord],
        ground_truth: GroundTruthStore,
    ) -> BlockingAuditMetrics:
        """
        Audit blocking performance, candidate volume, and candidate recall against ground truth.
        """
        t0 = time.perf_counter()
        total_anchors = 0
        total_candidate_pairs = 0
        max_candidates = 0
        zero_candidate_anchors = 0

        total_true_targets = 0
        found_true_targets = 0

        for anchor in anchors:
            total_anchors += 1
            candidates = self.retrieve_candidates(anchor)
            n_cands = len(candidates)
            total_candidate_pairs += n_cands
            if n_cands == 0:
                zero_candidate_anchors += 1
            if n_cands > max_candidates:
                max_candidates = n_cands

            # Candidate recall against true targets
            true_targets = ground_truth.get_target_set(anchor.entity_id)
            if true_targets:
                total_true_targets += len(true_targets)
                found_true_targets += len(true_targets & set(candidates))

        elapsed = time.perf_counter() - t0
        mean_cands = (total_candidate_pairs / total_anchors) if total_anchors > 0 else 0.0
        recall = (found_true_targets / total_true_targets) if total_true_targets > 0 else 1.0

        metrics = BlockingAuditMetrics(
            total_anchors_queried=total_anchors,
            total_candidate_pairs=total_candidate_pairs,
            mean_candidates_per_anchor=round(mean_cands, 4),
            max_candidates_per_anchor=max_candidates,
            zero_candidate_anchor_count=zero_candidate_anchors,
            candidate_recall=round(recall, 4),
            elapsed_time_s=round(elapsed, 4),
        )

        logger.info(
            f"Blocking audit complete: {total_candidate_pairs} pairs, recall={metrics.candidate_recall}",
            extra={"payload": metrics.to_dict()},
        )
        return metrics
