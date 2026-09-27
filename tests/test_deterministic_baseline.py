"""
Unit and Integration Tests for Phase 21: Deterministic Baseline Model.
"""
import unittest

from ber.models.deterministic_baseline import DeterministicBaseline, DecisionResult
from entivyre.contracts.metrics import compute_macro_f05


class TestDeterministicBaseline(unittest.TestCase):
    def setUp(self):
        self.model = DeterministicBaseline(high_sim_threshold=0.85)

    def test_exact_canonical_compatible_address(self):
        feats = {
            "name_canonical_exact_match": 1.0,
            "country_contradiction": 0.0,
            "address_numeric_contradiction": 0.0,
            "address_token_jaccard": 0.65,
            "address_is_missing": 0.0,
            "overall_composite_similarity": 0.94,
        }
        res = self.model.classify_pair(feats, target_id="S2-101")
        self.assertTrue(res.is_match)
        self.assertEqual(res.rule_name, "RULE_EXACT_CANONICAL_WITH_COMPATIBLE_ADDRESS")
        self.assertGreater(res.confidence, 0.90)

    def test_rejection_on_country_contradiction(self):
        feats = {
            "name_canonical_exact_match": 1.0,
            "name_exact_match": 1.0,
            "country_contradiction": 1.0,
            "address_numeric_contradiction": 0.0,
            "overall_composite_similarity": 0.20,
        }
        res = self.model.classify_pair(feats, target_id="S3-202")
        self.assertFalse(res.is_match)
        self.assertEqual(res.rule_name, "REJECT_COUNTRY_CONTRADICTION")
        self.assertEqual(res.confidence, 0.0)

    def test_rejection_on_address_numeric_contradiction(self):
        feats = {
            "name_canonical_exact_match": 1.0,
            "country_contradiction": 0.0,
            "address_numeric_contradiction": 1.0,
            "name_high_address_contradiction": 1.0,
            "overall_composite_similarity": 0.35,
        }
        res = self.model.classify_pair(feats, target_id="S2-303")
        self.assertFalse(res.is_match)
        self.assertEqual(res.rule_name, "REJECT_ADDRESS_NUMERIC_CONTRADICTION")
        self.assertEqual(res.confidence, 0.0)

    def test_predict_anchor_candidates_multi_match(self):
        # Anchor has 3 candidates: 2 valid matches, 1 contradiction
        candidates = [
            ("S2-001", {
                "name_canonical_exact_match": 1.0,
                "country_contradiction": 0.0,
                "address_numeric_contradiction": 0.0,
                "address_token_jaccard": 0.80,
                "address_is_missing": 0.0,
                "overall_composite_similarity": 0.95,
            }),
            ("S3-002", {
                "name_and_address_high_sim": 1.0,
                "country_contradiction": 0.0,
                "address_numeric_contradiction": 0.0,
                "overall_composite_similarity": 0.91,
            }),
            ("S2-999", {
                "name_canonical_exact_match": 1.0,
                "country_contradiction": 1.0,  # Contradiction
                "address_numeric_contradiction": 0.0,
            }),
        ]
        matched_ids = self.model.predict_anchor_candidates("S1-100", candidates)
        self.assertEqual(matched_ids, ["S2-001", "S3-002"])
        self.assertNotIn("S2-999", matched_ids)

    def test_singleton_handling_and_official_metric_credit(self):
        # Anchor S1-SNG is a true singleton (empty target list in GT)
        # S1-MTC has 1 true target (S2-111)
        gt = {
            "S1-SNG": (),
            "S1-MTC": ("S2-111",),
        }

        # Case A: Correct singleton prediction ([]) -> 1.0 credit
        pred_perfect = {
            "S1-SNG": (),
            "S1-MTC": ("S2-111",),
        }
        summary_perfect, _ = self.model.evaluate(gt, pred_perfect)
        self.assertEqual(summary_perfect.macro_f05, 1.0)
        self.assertEqual(summary_perfect.singleton_f05, 1.0)
        self.assertEqual(summary_perfect.matched_f05, 1.0)

        # Case B: False merge on singleton (predicted S2-999) -> 0.0 penalty
        pred_false_merge = {
            "S1-SNG": ("S2-999",),
            "S1-MTC": ("S2-111",),
        }
        summary_fm, _ = self.model.evaluate(gt, pred_false_merge)
        self.assertEqual(summary_fm.singleton_f05, 0.0)
        self.assertEqual(summary_fm.matched_f05, 1.0)
        self.assertEqual(summary_fm.macro_f05, 0.5)


if __name__ == "__main__":
    unittest.main()
