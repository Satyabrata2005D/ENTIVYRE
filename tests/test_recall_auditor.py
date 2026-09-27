"""
Unit and adversarial tests for Phase 15: Candidate Recall Audit.
"""
import tempfile
import unittest
from pathlib import Path
import sys

_project_root = Path(__file__).resolve().parent.parent
_ber_src = _project_root / "code" / "business_entity_resolution" / "src"
if str(_ber_src) not in sys.path:
    sys.path.insert(0, str(_ber_src))

from ber.blocking.recall_auditor import CandidateRecallAuditor, RecallAuditReport
from ber.labels.ground_truth import GroundTruthStore


class TestCandidateRecallAuditor(unittest.TestCase):
    def setUp(self):
        self.auditor = CandidateRecallAuditor()
        # Mock ground truth:
        # S1-1: 2 targets (S2-10, S3-20)
        # S1-2: 2 targets (S2-30, S3-40)
        # S1-3: 1 target  (S2-50)
        # S1-4: singleton (0 targets)
        self.gt_store = GroundTruthStore.from_dict({
            "S1-1": ["S2-10", "S3-20"],
            "S1-2": ["S2-30", "S3-40"],
            "S1-3": ["S2-50"],
            "S1-4": [],
        })
        self.countries = {
            "S1-1": "US",
            "S1-2": "US",
            "S1-3": "INDIA",
            "S1-4": "US",
        }

    def test_perfect_candidate_recall(self):
        """Test metrics when candidate generator finds 100% of targets."""
        cands_map = {
            "S1-1": ["S2-10", "S3-20", "S2-999"],
            "S1-2": ["S2-30", "S3-40"],
            "S1-3": ["S2-50"],
            "S1-4": ["S2-888"],  # singleton with some false candidates
        }
        report = self.auditor.audit(cands_map, self.gt_store, self.countries)

        self.assertEqual(report.total_anchors, 4)
        self.assertEqual(report.matched_anchors, 3)
        self.assertEqual(report.singleton_anchors, 1)
        self.assertEqual(report.total_true_targets, 5)
        self.assertEqual(report.total_found_targets, 5)
        self.assertEqual(report.global_target_recall, 1.0)
        self.assertEqual(report.anchor_full_recall_rate, 1.0)
        self.assertEqual(report.anchor_partial_recall_rate, 0.0)
        self.assertEqual(report.anchor_zero_recall_rate, 0.0)
        self.assertEqual(report.source2_target_recall, 1.0)
        self.assertEqual(report.source3_target_recall, 1.0)
        self.assertEqual(len(report.missed_matches_sample), 0)

    def test_partial_and_zero_recall_scenarios(self):
        """Test recall breakdown across full, partial, and zero recall anchors."""
        cands_map = {
            "S1-1": ["S2-10", "S3-20"],  # Full: 2/2 found
            "S1-2": ["S2-30"],           # Partial: 1/2 found (missed S3-40)
            "S1-3": ["S2-999"],          # Zero: 0/1 found (missed S2-50)
            "S1-4": [],                  # Singleton: 0 candidates
        }
        report = self.auditor.audit(cands_map, self.gt_store, self.countries)

        self.assertEqual(report.matched_anchors, 3)
        # Total true targets = 5, total found = 3 (60% recall)
        self.assertEqual(report.total_true_targets, 5)
        self.assertEqual(report.total_found_targets, 3)
        self.assertEqual(report.global_target_recall, 0.6)

        # Anchor rates: 1 full, 1 partial, 1 zero out of 3 matched anchors
        self.assertAlmostEqual(report.anchor_full_recall_rate, 1 / 3, places=3)
        self.assertAlmostEqual(report.anchor_partial_recall_rate, 1 / 3, places=3)
        self.assertAlmostEqual(report.anchor_zero_recall_rate, 1 / 3, places=3)

        # Source breakdowns:
        # S2: S2-10 found, S2-30 found, S2-50 missed -> 2/3 found
        self.assertAlmostEqual(report.source2_target_recall, 2 / 3, places=3)
        # S3: S3-20 found, S3-40 missed -> 1/2 found
        self.assertEqual(report.source3_target_recall, 0.5)

        # Country breakdowns:
        # US: S1-1 (2/2) + S1-2 (1/2) = 3/4 found (0.75)
        self.assertEqual(report.country_recall["US"], 0.75)
        # INDIA: S1-3 (0/1) = 0.0
        self.assertEqual(report.country_recall["INDIA"], 0.0)

        # Forensic missed matches sample
        self.assertGreaterEqual(len(report.missed_matches_sample), 2)
        missed_aids = [m["anchor_id"] for m in report.missed_matches_sample]
        self.assertIn("S1-2", missed_aids)
        self.assertIn("S1-3", missed_aids)

    def test_reduction_ratio_and_volume_stats(self):
        """Test candidate volume percentiles and reduction ratio calculation."""
        cands_map = {
            f"S1-{i}": [f"S2-{j}" for j in range(10)]
            for i in range(100)
        }
        report = self.auditor.audit(cands_map, self.gt_store, total_target_population=1_000_000)
        self.assertEqual(report.candidate_volume["mean"], 10.0)
        self.assertEqual(report.candidate_volume["median"], 10.0)
        self.assertEqual(report.candidate_volume["max"], 10.0)
        self.assertGreater(report.reduction_ratio, 0.999)

    def test_save_report(self):
        """Test persisting audit report to JSON."""
        cands_map = {"S1-1": ["S2-10"]}
        report = self.auditor.audit(cands_map, self.gt_store)

        with tempfile.TemporaryDirectory() as tmpdir:
            out_file = Path(tmpdir) / "audit_report.json"
            saved_path = CandidateRecallAuditor.save_report(report, out_file)
            self.assertTrue(saved_path.exists())


if __name__ == "__main__":
    unittest.main()
