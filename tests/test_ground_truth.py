"""
Unit and adversarial tests for Phase 10: Ground-Truth Engineering.
"""
import tempfile
import unittest
from pathlib import Path
import sys

_project_root = Path(__file__).resolve().parent.parent
_ber_src = _project_root / "code" / "business_entity_resolution" / "src"
if str(_ber_src) not in sys.path:
    sys.path.insert(0, str(_ber_src))

from ber.labels.ground_truth import GroundTruthStore, GroundTruthStats


class TestGroundTruthStore(unittest.TestCase):
    def setUp(self):
        self.mock_data = {
            "S1-1": ["S2-101", "S3-201"],          # multi-match (2 targets)
            "S1-2": ["S2-102"],                     # 1 target
            "S1-3": [],                             # singleton (0 targets)
            "S1-4": ["S2-104", "S2-105", "S3-204"], # multi-match (3 targets)
        }
        self.store = GroundTruthStore.from_dict(self.mock_data)

    def test_store_indexing_and_targets(self):
        """Test forward and reverse lookups."""
        self.assertEqual(len(self.store), 4)
        self.assertTrue(self.store.contains_anchor("S1-1"))
        self.assertFalse(self.store.contains_anchor("S1-999"))

        # Targets
        t1 = self.store.get_targets("S1-1")
        self.assertEqual(t1, ("S2-101", "S3-201"))

        # Reverse lookup
        self.assertEqual(self.store.get_anchor_for_target("S2-101"), "S1-1")
        self.assertEqual(self.store.get_anchor_for_target("S3-204"), "S1-4")
        self.assertIsNone(self.store.get_anchor_for_target("S2-999"))

    def test_singleton_detection(self):
        """Test identification of singletons."""
        self.assertTrue(self.store.is_singleton("S1-3"))
        self.assertFalse(self.store.is_singleton("S1-1"))
        self.assertFalse(self.store.is_singleton("S1-2"))

    def test_pairwise_label_computation(self):
        """Test compute_pair_label logic."""
        # True positives
        self.assertEqual(self.store.compute_pair_label("S1-1", "S2-101"), 1)
        self.assertEqual(self.store.compute_pair_label("S1-1", "S3-201"), 1)
        self.assertEqual(self.store.compute_pair_label("S1-2", "S2-102"), 1)

        # True negatives
        self.assertEqual(self.store.compute_pair_label("S1-1", "S2-102"), 0)
        self.assertEqual(self.store.compute_pair_label("S1-3", "S2-101"), 0)
        self.assertEqual(self.store.compute_pair_label("S1-999", "S2-101"), 0)

    def test_candidate_recall_evaluation(self):
        """Test candidate recall calculations."""
        # Anchor with 2 true targets
        found, total, recall = self.store.evaluate_candidate_recall(
            "S1-1", ["S2-101", "S2-999"]
        )
        self.assertEqual(found, 1)
        self.assertEqual(total, 2)
        self.assertEqual(recall, 0.5)

        # Anchor with 100% recall
        found, total, recall = self.store.evaluate_candidate_recall(
            "S1-1", ["S2-101", "S3-201", "S2-999"]
        )
        self.assertEqual(found, 2)
        self.assertEqual(total, 2)
        self.assertEqual(recall, 1.0)

        # Singleton recall: defined as 1.0 (no true targets were missed)
        found_s, total_s, recall_s = self.store.evaluate_candidate_recall(
            "S1-3", ["S2-999"]
        )
        self.assertEqual(found_s, 0)
        self.assertEqual(total_s, 0)
        self.assertEqual(recall_s, 1.0)

    def test_stats_calculation(self):
        """Test summary statistics calculation."""
        stats = self.store.stats
        self.assertEqual(stats.total_anchors, 4)
        self.assertEqual(stats.total_targets, 6)
        self.assertEqual(stats.singleton_count, 1)
        self.assertEqual(stats.multi_match_count, 2)
        self.assertEqual(stats.s2_target_count, 4)
        self.assertEqual(stats.s3_target_count, 2)
        self.assertEqual(stats.max_targets_per_anchor, 3)

    def test_from_file_streaming(self):
        """Test streaming from a TSV file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            gt_file = Path(tmpdir) / "train_ground_truth.tsv"
            with open(gt_file, "w", encoding="utf-8") as f:
                f.write("source1_entity_id\tmatched_entity_ids\n")
                f.write("S1-10\tS2-100 S3-101\n")
                f.write("S1-20\t\n")  # singleton
                f.write("S1-30\tS2-200\n")

            loaded = GroundTruthStore.from_file(gt_file)
            self.assertEqual(len(loaded), 3)
            self.assertTrue(loaded.is_singleton("S1-20"))
            self.assertEqual(loaded.get_targets("S1-10"), ("S2-100", "S3-101"))
            self.assertEqual(loaded.stats.singleton_count, 1)
            self.assertEqual(loaded.stats.total_targets, 3)


if __name__ == "__main__":
    unittest.main()
