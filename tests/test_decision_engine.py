"""
Unit and Integration Tests for Phases 25, 26, & 27: Threshold Optimization, Singleton Handling, & Multi-Match Resolution.
"""
import unittest
import tempfile
from pathlib import Path

from ber.decision.threshold_optimizer import ThresholdOptimizer
from ber.decision.matcher import EntityMatcher


class TestDecisionEngine(unittest.TestCase):
    def test_threshold_optimizer(self):
        # 2 anchors: 1 singleton, 1 multi-match
        gt = {
            "S1-001": (),                  # Singleton
            "S1-002": ("S2-10", "S3-20"),  # Multi-match
        }
        # Scored candidates:
        # S1-001 has 1 weak candidate score 0.40
        # S1-002 has true matches at 0.85 and 0.90, and false positive at 0.60
        scored_candidates = {
            "S1-001": [("S2-99", 0.40)],
            "S1-002": [("S2-10", 0.85), ("S3-20", 0.90), ("S2-50", 0.60)],
        }

        optimizer = ThresholdOptimizer(candidate_thresholds=[0.30, 0.50, 0.70, 0.80])
        res = optimizer.optimize_scored_candidates(scored_candidates, gt)

        # Threshold >= 0.70 avoids the false positive on S1-001 (score 0.40) and S1-002 (score 0.60)
        # Yielding perfect F0.5 = 1.0!
        self.assertGreaterEqual(res.best_threshold, 0.70)
        self.assertEqual(res.best_macro_f05, 1.0)
        self.assertGreater(len(res.curve), 0)

        # Test persistence
        with tempfile.TemporaryDirectory() as tmpdir:
            out_file = Path(tmpdir) / "threshold_res.json"
            res.save(out_file)
            self.assertTrue(out_file.exists())

    def test_singleton_handling_phase26(self):
        matcher = EntityMatcher(decision_threshold=0.70)

        # Case 1: Zero candidates -> Empty match
        self.assertEqual(matcher.resolve_anchor("S1-SNG1", []), [])

        # Case 2: Low confidence candidate -> Empty match
        low_conf = [("S2-01", 0.45, {"overall_composite_similarity": 0.45})]
        self.assertEqual(matcher.resolve_anchor("S1-SNG2", low_conf), [])

        # Case 3: Country contradiction candidate -> Filtered out -> Empty match
        contra_cand = [("S2-02", 0.88, {"country_contradiction": 1.0})]
        self.assertEqual(matcher.resolve_anchor("S1-SNG3", contra_cand), [])

        # Case 4: Address numeric contradiction candidate -> Filtered out -> Empty match
        contra_addr = [("S2-03", 0.85, {"address_numeric_contradiction": 1.0})]
        self.assertEqual(matcher.resolve_anchor("S1-SNG4", contra_addr), [])

    def test_multi_match_resolution_phase27(self):
        matcher = EntityMatcher(decision_threshold=0.70, max_matches_per_anchor=2)

        scored_candidates = [
            ("S2-01", 0.95, {}),
            ("S3-02", 0.85, {}),
            ("S2-03", 0.75, {}),  # Will be excluded due to max_matches_per_anchor=2
            ("S1-100", 0.99, {}), # Self-match must be excluded
            ("S2-01", 0.95, {}),  # Duplicate must be deduplicated
        ]

        matches = matcher.resolve_anchor("S1-100", scored_candidates)
        # Should contain top 2 distinct non-self matches in descending score order
        self.assertEqual(matches, ["S2-01", "S3-02"])

    def test_candidate_subset_invariant_validator(self):
        candidate_pairs = {
            "S1-1": ["S2-A", "S3-B", "S2-C"],
            "S1-2": ["S2-D"],
        }

        # Valid predictions (subset of candidates)
        valid_preds = {
            "S1-1": ["S2-A", "S3-B"],
            "S1-2": [],
        }
        is_valid, violations = EntityMatcher.validate_candidate_subset_invariant(valid_preds, candidate_pairs)
        self.assertTrue(is_valid)
        self.assertEqual(len(violations), 0)

        # Invalid prediction (predicted target not in candidates)
        invalid_preds = {
            "S1-1": ["S2-A", "S2-ILLEGAL"],
            "S1-2": [],
        }
        is_valid, violations = EntityMatcher.validate_candidate_subset_invariant(invalid_preds, candidate_pairs)
        self.assertFalse(is_valid)
        self.assertEqual(len(violations), 1)


if __name__ == "__main__":
    unittest.main()
