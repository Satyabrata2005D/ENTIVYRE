"""
Unit and Integration Tests for Phase 22: Supervised Pair Dataset Generator.
"""
import unittest

from ber.data.pair_dataset import PairDatasetGenerator, LabeledPair
from ber.features.registry import build_default_feature_registry


class TestPairDatasetGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = PairDatasetGenerator(max_negatives_per_positive=2, seed=42)
        self.registry = build_default_feature_registry()

    def test_anchor_pairs_generation_and_labeling(self):
        anchor = {
            "name": "Acme Widgets",
            "address": "100 Industrial Parkway, Austin, TX 78701",
            "country": "US",
        }
        candidates = {
            "S2-001": {  # True positive
                "name": "Acme Widgets Inc",
                "address": "100 Industrial Pkwy, Austin, TX 78701",
                "country": "US",
            },
            "S3-002": {  # True positive
                "name": "Acme Widgets",
                "address": "100 Industrial Parkway, Austin, TX",
                "country": "US",
            },
            "S2-991": {  # Hard negative
                "name": "Acme Tools & Hardware",
                "address": "200 Commercial Way, Dallas, TX 75201",
                "country": "US",
            },
            "S3-992": {  # Hard negative
                "name": "Beta Widgets",
                "address": "100 Industrial Parkway, Austin, TX 78701",
                "country": "US",
            },
            "S2-993": {  # Hard negative (will be capped by max_negatives_per_positive=2 -> max 4 negs)
                "name": "Gamma Widgets",
                "address": "300 Tech Blvd, Houston, TX 77001",
                "country": "US",
            },
        }
        gt_targets = {"S2-001", "S3-002"}

        pairs = self.generator.generate_anchor_pairs(
            anchor_id="S1-100",
            anchor_record=anchor,
            candidate_records=candidates,
            gt_target_ids=gt_targets,
            include_dict=True,
        )

        # 2 positives, 3 negatives <= 4 max negatives
        self.assertEqual(len(pairs), 5)
        pos_pairs = [p for p in pairs if p.label == 1.0]
        neg_pairs = [p for p in pairs if p.label == 0.0]
        self.assertEqual(len(pos_pairs), 2)
        self.assertEqual(len(neg_pairs), 3)

        # Verify positive labels
        pos_ids = {p.target_id for p in pos_pairs}
        self.assertEqual(pos_ids, {"S2-001", "S3-002"})

        # Verify feature vector length and no NaNs
        for p in pairs:
            self.assertEqual(len(p.features), 33)
            self.assertIsInstance(p.features, list)
            for val in p.features:
                self.assertFalse(val != val)

    def test_negative_capping(self):
        generator_cap1 = PairDatasetGenerator(max_negatives_per_positive=1, seed=42)
        anchor = {"name": "Target Store", "address": "123 Main St", "country": "US"}
        candidates = {
            "S2-POS": {"name": "Target Store", "address": "123 Main St", "country": "US"},
            "S2-NEG1": {"name": "Target Store", "address": "999 Oak St", "country": "US"},
            "S2-NEG2": {"name": "Target Pharmacy", "address": "456 Pine St", "country": "US"},
            "S2-NEG3": {"name": "Target Express", "address": "789 Elm St", "country": "US"},
        }
        gt_targets = {"S2-POS"}

        pairs = generator_cap1.generate_anchor_pairs(
            anchor_id="S1-200",
            anchor_record=anchor,
            candidate_records=candidates,
            gt_target_ids=gt_targets,
        )

        # 1 positive, exactly 1 negative sampled (max_negatives_per_positive=1)
        self.assertEqual(len(pairs), 2)
        self.assertEqual(sum(1 for p in pairs if p.label == 1.0), 1)
        self.assertEqual(sum(1 for p in pairs if p.label == 0.0), 1)

    def test_matrix_conversion_and_summary(self):
        pairs = [
            LabeledPair("S1-1", "S2-1", 1.0, [0.9] * 33),
            LabeledPair("S1-1", "S2-2", 0.0, [0.1] * 33),
            LabeledPair("S1-2", "S3-1", 1.0, [0.8] * 33),
        ]
        X, y, pair_ids = PairDatasetGenerator.to_matrices(pairs)
        self.assertEqual(len(X), 3)
        self.assertEqual(len(X[0]), 33)
        self.assertEqual(y, [1.0, 0.0, 1.0])
        self.assertEqual(pair_ids, [("S1-1", "S2-1"), ("S1-1", "S2-2"), ("S1-2", "S3-1")])

        summary = PairDatasetGenerator.summarize(pairs)
        self.assertEqual(summary.total_pairs, 3)
        self.assertEqual(summary.positive_count, 2)
        self.assertEqual(summary.negative_count, 1)
        self.assertEqual(summary.unique_anchors, 2)
        self.assertEqual(summary.unique_targets, 3)


if __name__ == "__main__":
    unittest.main()
