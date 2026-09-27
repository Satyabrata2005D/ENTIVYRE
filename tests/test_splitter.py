"""
Unit and adversarial tests for Phase 11: Entity-Grouped Stratified Validation Splitter.
"""
import tempfile
import unittest
from pathlib import Path
import sys

_project_root = Path(__file__).resolve().parent.parent
_ber_src = _project_root / "code" / "business_entity_resolution" / "src"
if str(_ber_src) not in sys.path:
    sys.path.insert(0, str(_ber_src))

from ber.evaluation.splitter import EntityGroupedSplitter, DatasetSplit
from ber.labels.ground_truth import GroundTruthStore


class TestEntityGroupedSplitter(unittest.TestCase):
    def setUp(self):
        # Create a synthetic dataset of 100 anchors with varied countries and match multiplicities
        self.metadata = []
        self.gt_mapping = {}

        for i in range(100):
            aid = f"S1-{i:03d}"
            # Country: 60 US, 40 India
            country = "US" if i < 60 else "INDIA"
            self.metadata.append({"entity_id": aid, "country": country})

            # Multiplicity:
            # 0-9: singleton (0 targets)
            # 10-49: single match (1 target)
            # 50-79: 2-3 matches
            # 80-99: 4 matches
            if i < 10:
                self.gt_mapping[aid] = []
            elif i < 50:
                self.gt_mapping[aid] = [f"S2-{i * 10}"]
            elif i < 80:
                self.gt_mapping[aid] = [f"S2-{i * 10}", f"S3-{i * 10 + 1}"]
            else:
                self.gt_mapping[aid] = [
                    f"S2-{i * 10}", f"S2-{i * 10 + 1}", f"S3-{i * 10 + 2}", f"S3-{i * 10 + 3}"
                ]

        self.gt_store = GroundTruthStore.from_dict(self.gt_mapping)
        self.splitter = EntityGroupedSplitter(val_ratio=0.20, seed=42)

    def test_zero_leakage_invariants(self):
        """Verify strict disjointness of anchors and targets."""
        split = self.splitter.create_split(self.metadata, self.gt_store)
        self.assertTrue(split.manifest.is_leak_free)
        self.assertEqual(split.manifest.anchor_overlap_count, 0)
        self.assertEqual(split.manifest.target_overlap_count, 0)

        # In-memory sets check
        train_anchors = split.train_anchor_set
        val_anchors = split.val_anchor_set
        self.assertEqual(len(train_anchors & val_anchors), 0)
        self.assertEqual(len(train_anchors) + len(val_anchors), 100)

        # Check total targets disjointness
        train_targets = {t for aid in train_anchors for t in self.gt_store.get_targets(aid)}
        val_targets = {t for aid in val_anchors for t in self.gt_store.get_targets(aid)}
        self.assertEqual(len(train_targets & val_targets), 0)

    def test_stratification_balance(self):
        """Test country and singleton proportions in train vs val."""
        split = self.splitter.create_split(self.metadata, self.gt_store)
        manifest = split.manifest

        # Both train and val should have roughly 10% singletons
        self.assertAlmostEqual(manifest.train_singleton_ratio, 0.10, delta=0.05)
        self.assertAlmostEqual(manifest.val_singleton_ratio, 0.10, delta=0.05)

        # Country ratio: ~60% US in both
        train_us_ratio = manifest.train_country_dist.get("US", 0) / manifest.train_anchor_count
        val_us_ratio = manifest.val_country_dist.get("US", 0) / manifest.val_anchor_count
        self.assertAlmostEqual(train_us_ratio, 0.60, delta=0.08)
        self.assertAlmostEqual(val_us_ratio, 0.60, delta=0.08)

    def test_reproducibility_and_seed(self):
        """Verify identical splits with same seed, different with different seed."""
        split1 = self.splitter.create_split(self.metadata, self.gt_store)
        split2 = self.splitter.create_split(self.metadata, self.gt_store)
        self.assertEqual(split1.train_anchors, split2.train_anchors)
        self.assertEqual(split1.val_anchors, split2.val_anchors)

        splitter_diff = EntityGroupedSplitter(val_ratio=0.20, seed=999)
        split3 = splitter_diff.create_split(self.metadata, self.gt_store)
        self.assertNotEqual(split1.val_anchors, split3.val_anchors)

    def test_persistence_roundtrip(self):
        """Test saving and loading split manifest and ID files."""
        split = self.splitter.create_split(self.metadata, self.gt_store)

        with tempfile.TemporaryDirectory() as tmpdir:
            out_dir = Path(tmpdir) / "test_split"
            manifest_path = EntityGroupedSplitter.save_split(split, out_dir)
            self.assertTrue(manifest_path.exists())

            loaded = EntityGroupedSplitter.load_split(out_dir)
            self.assertEqual(loaded.train_anchors, split.train_anchors)
            self.assertEqual(loaded.val_anchors, split.val_anchors)
            self.assertEqual(loaded.manifest.is_leak_free, True)
            self.assertEqual(loaded.manifest.total_anchors, 100)

    def test_invalid_val_ratio(self):
        """Test that invalid split ratios raise ValueError."""
        with self.assertRaises(ValueError):
            EntityGroupedSplitter(val_ratio=0.0)
        with self.assertRaises(ValueError):
            EntityGroupedSplitter(val_ratio=1.0)
        with self.assertRaises(ValueError):
            EntityGroupedSplitter(val_ratio=-0.1)


if __name__ == "__main__":
    unittest.main()
