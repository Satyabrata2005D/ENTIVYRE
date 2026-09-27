"""
Ground-Truth Engineering and Label Resolution Engine for ENTIVYRE.
Phase 10: Anchor-to-targets indexing, reverse target-to-anchor mapping,
singleton isolation, candidate recall measurement, and pair-level label resolution.

Guarantees:
- O(1) pairwise label lookup: compute_pair_label(anchor_id, candidate_id).
- Inverted mapping: target_to_anchor for reverse entity alignment.
- Accurate candidate recall audit against true targets.
- Preserves empty target lists for singletons without forcing matches.
- Memory-bounded representation using immutable tuples and compact sets.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple, Any

from entivyre.utils.logger import get_logger
from ber.io.ingestion import stream_ground_truth_chunks

logger = get_logger("ber.labels.ground_truth", stage="10_ground_truth")


@dataclass(frozen=True)
class GroundTruthStats:
    """Summary metrics for the ground truth dataset."""
    total_anchors: int
    total_targets: int
    singleton_count: int
    multi_match_count: int
    s2_target_count: int
    s3_target_count: int
    mean_targets_per_anchor: float
    max_targets_per_anchor: int

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class GroundTruthStore:
    """
    High-performance, in-memory store for ground-truth entity alignments.
    Provides fast O(1) pair validation and candidate recall calculation.
    """

    def __init__(
        self,
        anchor_to_targets: Dict[str, Tuple[str, ...]],
        target_to_anchor: Optional[Dict[str, str]] = None,
    ):
        self._anchor_to_targets = anchor_to_targets
        
        # Precompute target set for fast membership test
        self._anchor_to_target_sets: Dict[str, Set[str]] = {
            aid: set(tgts) for aid, tgts in anchor_to_targets.items()
        }

        # Build or verify reverse target index
        if target_to_anchor is not None:
            self._target_to_anchor = target_to_anchor
        else:
            self._target_to_anchor = {}
            for aid, targets in anchor_to_targets.items():
                for tid in targets:
                    self._target_to_anchor[tid] = aid

        # Compute summary metrics
        total_anchors = len(self._anchor_to_targets)
        total_targets = len(self._target_to_anchor)
        singletons = 0
        multi_matches = 0
        s2_count = 0
        s3_count = 0
        max_targets = 0

        for aid, targets in self._anchor_to_targets.items():
            cnt = len(targets)
            if cnt == 0:
                singletons += 1
            else:
                if cnt >= 2:
                    multi_matches += 1
                if cnt > max_targets:
                    max_targets = cnt
                for tid in targets:
                    if tid.startswith("S2-") or tid.startswith("train_source2_"):
                        s2_count += 1
                    elif tid.startswith("S3-") or tid.startswith("train_source3_"):
                        s3_count += 1

        mean_targets = (total_targets / total_anchors) if total_anchors > 0 else 0.0

        self._stats = GroundTruthStats(
            total_anchors=total_anchors,
            total_targets=total_targets,
            singleton_count=singletons,
            multi_match_count=multi_matches,
            s2_target_count=s2_count,
            s3_target_count=s3_count,
            mean_targets_per_anchor=round(mean_targets, 4),
            max_targets_per_anchor=max_targets,
        )

    @property
    def stats(self) -> GroundTruthStats:
        return self._stats

    def __len__(self) -> int:
        return len(self._anchor_to_targets)

    def contains_anchor(self, anchor_id: str) -> bool:
        return anchor_id in self._anchor_to_targets

    def get_targets(self, anchor_id: str) -> Tuple[str, ...]:
        """Return tuple of target IDs for an anchor. Empty tuple if singleton or unknown."""
        return self._anchor_to_targets.get(anchor_id, ())

    def get_target_set(self, anchor_id: str) -> Set[str]:
        """Return set of target IDs for an anchor."""
        return self._anchor_to_target_sets.get(anchor_id, set())

    def get_anchor_for_target(self, target_id: str) -> Optional[str]:
        """Reverse lookup: return anchor ID for a target ID, or None."""
        return self._target_to_anchor.get(target_id)

    def is_singleton(self, anchor_id: str) -> bool:
        """True if the anchor has zero ground truth matches."""
        tgts = self._anchor_to_targets.get(anchor_id)
        if tgts is None:
            return True
        return len(tgts) == 0

    def is_match(self, anchor_id: str, candidate_id: str) -> bool:
        """Fast O(1) check if a candidate ID is a true match for the anchor ID."""
        target_set = self._anchor_to_target_sets.get(anchor_id)
        if not target_set:
            return False
        return candidate_id in target_set

    def compute_pair_label(self, anchor_id: str, candidate_id: str) -> int:
        """Binary label for supervised training: 1 if true match, 0 if negative."""
        return 1 if self.is_match(anchor_id, candidate_id) else 0

    def evaluate_candidate_recall(
        self,
        anchor_id: str,
        candidates: Iterable[str],
    ) -> Tuple[int, int, float]:
        """
        Evaluate candidate retrieval recall for a given anchor.
        Returns: (found_count, true_count, recall_rate).
        For singletons (true_count == 0), recall is defined as 1.0 (no true targets missed).
        """
        true_targets = self._anchor_to_target_sets.get(anchor_id, set())
        true_count = len(true_targets)
        if true_count == 0:
            return 0, 0, 1.0

        cand_set = set(candidates)
        found_count = len(true_targets & cand_set)
        recall = found_count / true_count
        return found_count, true_count, recall

    @classmethod
    def from_dict(cls, mapping: Dict[str, Iterable[str]]) -> GroundTruthStore:
        """Construct a GroundTruthStore from an in-memory dictionary."""
        anchor_to_targets = {
            aid: tuple(targets) for aid, targets in mapping.items()
        }
        return cls(anchor_to_targets=anchor_to_targets)

    @classmethod
    def from_file(
        cls,
        tsv_path: Path,
        max_rows: Optional[int] = None,
        chunk_size: int = 50_000,
    ) -> GroundTruthStore:
        """
        Stream a ground truth TSV file and build an in-memory store.
        """
        logger.info(
            f"Loading ground truth store from {tsv_path}",
            extra={"payload": {"tsv_path": str(tsv_path), "max_rows": max_rows}},
        )

        anchor_to_targets: Dict[str, Tuple[str, ...]] = {}
        target_to_anchor: Dict[str, str] = {}
        row_count = 0

        for chunk, _ in stream_ground_truth_chunks(tsv_path, chunk_size=chunk_size):
            for row in chunk:
                anchor_id = row.entity_id
                target_ids = tuple(row.matched_entity_ids)
                anchor_to_targets[anchor_id] = target_ids
                for tid in target_ids:
                    target_to_anchor[tid] = anchor_id
                row_count += 1
                if max_rows and row_count >= max_rows:
                    break
            if max_rows and row_count >= max_rows:
                break

        store = cls(anchor_to_targets=anchor_to_targets, target_to_anchor=target_to_anchor)
        logger.info(
            f"Loaded {len(store)} ground truth anchors",
            extra={"payload": {"stats": store.stats.to_dict()}},
        )
        return store
