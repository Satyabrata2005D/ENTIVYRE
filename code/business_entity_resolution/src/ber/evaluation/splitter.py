"""
Entity-Grouped Stratified Validation Splitter for ENTIVYRE.
Phase 11: Reproducible train/validation partitioning with zero anchor leakage,
balanced country representation, and multiplicity stratification.

Guarantees:
- Strict entity-grouped disjointness: train anchors ∩ val anchors = ∅.
- Target disjointness verification: train targets ∩ val targets = ∅.
- Stratification across country and match multiplicity (singletons vs multi-matches).
- Fully deterministic with configurable random seed.
- Persistent split manifests for clean-room reproducibility.
"""
from __future__ import annotations

import json
import random
from collections import defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple, Any

from entivyre.utils.logger import get_logger
from ber.labels.ground_truth import GroundTruthStore

logger = get_logger("ber.evaluation.splitter", stage="11_validation_split")


@dataclass(frozen=True)
class SplitManifest:
    """Detailed audit metrics confirming leak-free split properties."""
    split_id: str
    seed: int
    val_ratio: float
    total_anchors: int
    train_anchor_count: int
    val_anchor_count: int
    train_singleton_ratio: float
    val_singleton_ratio: float
    train_country_dist: Dict[str, int]
    val_country_dist: Dict[str, int]
    anchor_overlap_count: int
    target_overlap_count: int
    is_leak_free: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class DatasetSplit:
    """In-memory representation of partitioned dataset."""
    train_anchors: Tuple[str, ...]
    val_anchors: Tuple[str, ...]
    manifest: SplitManifest

    @property
    def train_anchor_set(self) -> Set[str]:
        return set(self.train_anchors)

    @property
    def val_anchor_set(self) -> Set[str]:
        return set(self.val_anchors)


class EntityGroupedSplitter:
    """
    Partitions anchors into train and validation sets with zero leakage
    and balanced stratifications.
    """

    def __init__(
        self,
        val_ratio: float = 0.20,
        seed: int = 42,
        stratify_by_country: bool = True,
        stratify_by_multiplicity: bool = True,
    ):
        if not (0.0 < val_ratio < 1.0):
            raise ValueError(f"val_ratio must be between 0 and 1, got {val_ratio}")
        self.val_ratio = val_ratio
        self.seed = seed
        self.stratify_by_country = stratify_by_country
        self.stratify_by_multiplicity = stratify_by_multiplicity

    def create_split(
        self,
        anchors_metadata: List[Dict[str, Any]],
        ground_truth: GroundTruthStore,
        split_id: str = "default_split",
    ) -> DatasetSplit:
        """
        Partition anchors into train and validation subsets.
        anchors_metadata: list of dicts with at minimum 'entity_id' and optionally 'country'.
        """
        logger.info(
            f"Creating entity-grouped split for {len(anchors_metadata)} anchors (val_ratio={self.val_ratio}, seed={self.seed})",
            extra={"payload": {"val_ratio": self.val_ratio, "seed": self.seed}},
        )

        # 1. Stratify anchors into buckets
        strata: Dict[Tuple[str, str], List[str]] = defaultdict(list)

        for item in anchors_metadata:
            aid = item["entity_id"]
            country = item.get("country", "UNKNOWN") if self.stratify_by_country else "ALL"
            
            if self.stratify_by_multiplicity:
                tgts = ground_truth.get_targets(aid)
                tgt_cnt = len(tgts)
                if tgt_cnt == 0:
                    mult_bucket = "0"
                elif tgt_cnt == 1:
                    mult_bucket = "1"
                elif tgt_cnt <= 3:
                    mult_bucket = "2-3"
                else:
                    mult_bucket = "4+"
            else:
                mult_bucket = "ALL"

            strata[(country, mult_bucket)].append(aid)

        # 2. Deterministic partitioned assignment
        rng = random.Random(self.seed)
        train_list: List[str] = []
        val_list: List[str] = []

        # Sort strata keys for deterministic iteration
        for stratum_key in sorted(strata.keys()):
            bucket = strata[stratum_key]
            # Sort IDs before shuffling to ensure platform/order invariance
            bucket.sort()
            rng.shuffle(bucket)

            n_val = int(round(len(bucket) * self.val_ratio))
            # Ensure at least 1 val sample if bucket has >= 4 items
            if n_val == 0 and len(bucket) >= 4 and self.val_ratio > 0:
                n_val = 1

            val_subset = bucket[:n_val]
            train_subset = bucket[n_val:]

            val_list.extend(val_subset)
            train_list.extend(train_subset)

        # 3. Zero-Leakage Forensic Audit
        train_set = set(train_list)
        val_set = set(val_list)
        anchor_overlap = train_set & val_set

        train_targets: Set[str] = set()
        for aid in train_set:
            train_targets.update(ground_truth.get_targets(aid))

        val_targets: Set[str] = set()
        for aid in val_set:
            val_targets.update(ground_truth.get_targets(aid))

        target_overlap = train_targets & val_targets
        is_leak_free = (len(anchor_overlap) == 0) and (len(target_overlap) == 0)

        # 4. Stratification balance metrics
        train_singletons = sum(1 for aid in train_set if ground_truth.is_singleton(aid))
        val_singletons = sum(1 for aid in val_set if ground_truth.is_singleton(aid))

        train_sing_ratio = (train_singletons / len(train_set)) if train_set else 0.0
        val_sing_ratio = (val_singletons / len(val_set)) if val_set else 0.0

        country_map = {item["entity_id"]: item.get("country", "UNKNOWN") for item in anchors_metadata}
        train_country_dist: Dict[str, int] = defaultdict(int)
        for aid in train_set:
            train_country_dist[country_map.get(aid, "UNKNOWN")] += 1

        val_country_dist: Dict[str, int] = defaultdict(int)
        for aid in val_set:
            val_country_dist[country_map.get(aid, "UNKNOWN")] += 1

        manifest = SplitManifest(
            split_id=split_id,
            seed=self.seed,
            val_ratio=self.val_ratio,
            total_anchors=len(anchors_metadata),
            train_anchor_count=len(train_set),
            val_anchor_count=len(val_set),
            train_singleton_ratio=round(train_sing_ratio, 4),
            val_singleton_ratio=round(val_sing_ratio, 4),
            train_country_dist=dict(train_country_dist),
            val_country_dist=dict(val_country_dist),
            anchor_overlap_count=len(anchor_overlap),
            target_overlap_count=len(target_overlap),
            is_leak_free=is_leak_free,
        )

        logger.info(
            f"Split created: {len(train_set)} train, {len(val_set)} val (is_leak_free={is_leak_free})",
            extra={"payload": manifest.to_dict()},
        )

        return DatasetSplit(
            train_anchors=tuple(sorted(train_set)),
            val_anchors=tuple(sorted(val_set)),
            manifest=manifest,
        )

    @staticmethod
    def save_split(split: DatasetSplit, output_dir: Path) -> Path:
        """Persist split manifests and anchor ID lists to disk."""
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)

        # Save manifest
        manifest_file = out / "split_manifest.json"
        with open(manifest_file, "w", encoding="utf-8") as f:
            json.dump(split.manifest.to_dict(), f, indent=2)

        # Save train anchors
        train_file = out / "train_anchors.txt"
        with open(train_file, "w", encoding="utf-8") as f:
            for aid in split.train_anchors:
                f.write(f"{aid}\n")

        # Save val anchors
        val_file = out / "val_anchors.txt"
        with open(val_file, "w", encoding="utf-8") as f:
            for aid in split.val_anchors:
                f.write(f"{aid}\n")

        return manifest_file

    @staticmethod
    def load_split(split_dir: Path) -> DatasetSplit:
        """Load a persisted split from disk."""
        sdir = Path(split_dir)
        manifest_file = sdir / "split_manifest.json"
        if not manifest_file.exists():
            raise FileNotFoundError(f"Split manifest not found at: {manifest_file}")

        with open(manifest_file, "r", encoding="utf-8") as f:
            m_dict = json.load(f)
        manifest = SplitManifest(**m_dict)

        train_file = sdir / "train_anchors.txt"
        with open(train_file, "r", encoding="utf-8") as f:
            train_anchors = tuple(line.strip() for line in f if line.strip())

        val_file = sdir / "val_anchors.txt"
        with open(val_file, "r", encoding="utf-8") as f:
            val_anchors = tuple(line.strip() for line in f if line.strip())

        return DatasetSplit(
            train_anchors=train_anchors,
            val_anchors=val_anchors,
            manifest=manifest,
        )
