"""
Unit and Integration Tests for Phase 28: Forensic Error Analyzer.
"""
import unittest
import tempfile
from pathlib import Path

from ber.evaluation.error_analyzer import ErrorAnalyzer


class TestErrorAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = ErrorAnalyzer(sample_limit_per_category=3)

    def test_error_taxonomies_categorization(self):
        # Ground truth:
        # S1-EXACT: matches S2-1
        # S1-BMISS: matches S2-2 (candidate generator never retrieved S2-2)
        # S1-MODFN: matches S2-3 (retrieved in candidates, but model rejected it)
        # S1-MODFP: matches S2-4, but model ALSO predicted S3-5
        # S1-SNGFM: singleton (empty), but model predicted S2-6
        # S1-SNGFD: matches S2-7, but model predicted empty []
        gt = {
            "S1-EXACT": ("S2-1",),
            "S1-BMISS": ("S2-2",),
            "S1-MODFN": ("S2-3", "S3-3"),
            "S1-MODFP": ("S2-4",),
            "S1-SNGFM": (),
            "S1-SNGFD": ("S2-7",),
        }
        candidates = {
            "S1-EXACT": ["S2-1"],
            "S1-BMISS": ["S2-99"],  # True target S2-2 missing!
            "S1-MODFN": ["S2-3", "S3-3"],   # True targets present in candidates
            "S1-MODFP": ["S2-4", "S3-5"],
            "S1-SNGFM": ["S2-6"],
            "S1-SNGFD": ["S2-7"],
        }
        predictions = {
            "S1-EXACT": ["S2-1"],
            "S1-BMISS": [],
            "S1-MODFN": ["S3-3"],          # Predicted S3-3, missed S2-3
            "S1-MODFP": ["S2-4", "S3-5"],  # False positive S3-5
            "S1-SNGFM": ["S2-6"],    # False merge on singleton
            "S1-SNGFD": [],          # False dismissal
        }

        report = self.analyzer.analyze(gt, predictions, candidates)

        self.assertEqual(report.total_anchors, 6)
        self.assertEqual(report.exact_match_anchors, 1)
        self.assertEqual(report.blocking_miss_count, 1)
        self.assertEqual(report.model_false_negative_count, 1)
        self.assertEqual(report.model_false_positive_count, 1)
        self.assertEqual(report.singleton_false_merge_count, 1)
        self.assertEqual(report.singleton_false_dismissal_count, 1)

        # Check sample diagnostics
        self.assertEqual(len(report.sample_diagnostics["BLOCKING_MISS"]), 1)
        self.assertEqual(report.sample_diagnostics["BLOCKING_MISS"][0]["anchor_id"], "S1-BMISS")

        self.assertEqual(len(report.sample_diagnostics["SINGLETON_FALSE_MERGE"]), 1)
        self.assertEqual(report.sample_diagnostics["SINGLETON_FALSE_MERGE"][0]["anchor_id"], "S1-SNGFM")

        # Test reports export
        with tempfile.TemporaryDirectory() as tmpdir:
            json_file = Path(tmpdir) / "error_report.json"
            md_file = Path(tmpdir) / "error_report.md"

            report.save_json(json_file)
            report.save_markdown(md_file)

            self.assertTrue(json_file.exists())
            self.assertTrue(md_file.exists())

            with open(md_file, "r") as f:
                content = f.read()
                self.assertIn("ENTIVYRE Forensic Error Analysis Report", content)
                self.assertIn("BLOCKING_MISS", content)


if __name__ == "__main__":
    unittest.main()
