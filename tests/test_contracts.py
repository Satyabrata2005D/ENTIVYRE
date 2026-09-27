"""Unit and adversarial test suite for ENTIVYRE contracts, schemas, and metrics."""

import os
import tempfile
import unittest

from entivyre.contracts.metrics import (
    compute_entity_f05,
    compute_macro_f05,
)
from entivyre.contracts.rules import (
    REQUIREMENTS_MATRIX,
    EnforcementType,
    RequirementCategory,
)
from entivyre.contracts.schema import (
    CandidateRecord,
    GroundTruthRecord,
    MatchingRecord,
    Source1Record,
    Source2Record,
    Source3Record,
    SourcePrefix,
    parse_entity_id,
)
from entivyre.contracts.verifier import (
    validate_file_contract,
    validate_submission_pipeline,
)


class TestEntityIDParsing(unittest.TestCase):
    """Tests for entity ID structural parsing and invariants."""

    def test_valid_entity_ids(self):
        prefix, num = parse_entity_id("S1-00042")
        self.assertEqual(prefix, SourcePrefix.SOURCE1)
        self.assertEqual(num, 42)

        prefix, num = parse_entity_id("S2-1234567")
        self.assertEqual(prefix, SourcePrefix.SOURCE2)
        self.assertEqual(num, 1234567)

        prefix, num = parse_entity_id("S3-0")
        self.assertEqual(prefix, SourcePrefix.SOURCE3)
        self.assertEqual(num, 0)

    def test_invalid_entity_ids(self):
        invalid_ids = ["S4-001", "s1-001", "S1001", "12345", "S2-", "-100", "", None]
        for bad_id in invalid_ids:
            with self.subTest(bad_id=bad_id):
                with self.assertRaises(ValueError):
                    parse_entity_id(bad_id)  # type: ignore


class TestRecordContracts(unittest.TestCase):
    """Tests for SourceRecord and GroundTruthRecord dataclass invariants."""

    def test_valid_source_records(self):
        s1 = Source1Record("S1-001", "Amazon Corp", "410 Terry Ave N, Seattle", "US")
        self.assertEqual(s1.entity_id, "S1-001")
        self.assertEqual(s1.country, "US")

        # Source 2/3 can have empty address
        s2 = Source2Record("S2-002", "Amazon UK", "", "GB")
        self.assertEqual(s2.address, "")

        s3 = Source3Record("S3-003", "Amazon DE GmbH", "Marcel-Breuer-Str 12", "DE")
        self.assertEqual(s3.name, "Amazon DE GmbH")

    def test_adversarial_source_records(self):
        # Mismatched source prefix
        with self.assertRaises(ValueError):
            Source1Record("S2-001", "Invalid S1", "Street", "US")

        # Invalid country code (empty or NaN)
        with self.assertRaises(ValueError):
            Source1Record("S1-001", "Valid Name", "Street", "")  # Empty country invalid
        with self.assertRaises(ValueError):
            Source1Record("S1-001", "Valid Name", "Street", "nan")  # NaN country invalid

        # Literal 'nan' string in name
        with self.assertRaises(ValueError):
            Source1Record("S1-001", "NaN", "Street", "US")

    def test_ground_truth_records(self):
        # Normal multi-match
        gt = GroundTruthRecord("S1-001", ("S2-100", "S3-200"))
        self.assertFalse(gt.is_singleton)
        self.assertEqual(len(gt.matched_entity_ids), 2)

        # Normal singleton
        gt_singleton = GroundTruthRecord("S1-002", ())
        self.assertTrue(gt_singleton.is_singleton)

        # Adversarial: self-match
        with self.assertRaises(ValueError):
            GroundTruthRecord("S1-001", ("S1-001",))

        # Adversarial: duplicate in match list
        with self.assertRaises(ValueError):
            GroundTruthRecord("S1-001", ("S2-100", "S2-100"))

    def test_candidate_and_matching_records(self):
        cand = CandidateRecord("S1-001", ("S2-10", "S3-20"))
        self.assertEqual(cand.to_tsv_row(), "S1-001\tS2-10,S3-20\n")

        match = MatchingRecord("S1-001", ("S2-10",))
        self.assertEqual(match.to_tsv_row(), "S1-001\tS2-10\n")

        # Empty match serialization
        empty_match = MatchingRecord("S1-002", ())
        self.assertEqual(empty_match.to_tsv_row(), "S1-002\t\n")


class TestMetricContract(unittest.TestCase):
    """Tests for official F_0.5 evaluation metric fidelity."""

    def test_official_readme_example(self):
        """Verify exact calculation from README.md example:

        - Model predicts: S2-00047, S2-00193, S3-00812
        - Ground truth:   S2-00047, S3-00812
        - Precision = 2/3 = 0.6667
        - Recall = 2/2 = 1.0
        - F_0.5 = (1.25 * 0.6667 * 1.0) / (0.25 * 0.6667 + 1.0) = 5/7 ≈ 0.7142857
        """
        true_matches = ["S2-00047", "S3-00812"]
        pred_matches = ["S2-00047", "S2-00193", "S3-00812"]

        res = compute_entity_f05("S1-00001", true_matches, pred_matches)

        self.assertAlmostEqual(res.precision, 2.0 / 3.0, places=5)
        self.assertAlmostEqual(res.recall, 1.0, places=5)
        self.assertAlmostEqual(res.f05, 5.0 / 7.0, places=5)
        self.assertEqual(round(res.f05, 3), 0.714)

    def test_singleton_metric_contract(self):
        """Singletons:

        - Correctly predicting empty list -> 1.0
        - Predicting false positive matches -> 0.0
        """
        # Correct singleton
        res_correct = compute_entity_f05("S1-001", [], [])
        self.assertEqual(res_correct.f05, 1.0)
        self.assertEqual(res_correct.precision, 1.0)
        self.assertEqual(res_correct.recall, 1.0)
        self.assertTrue(res_correct.is_singleton)

        # Incorrect singleton (false merge)
        res_incorrect = compute_entity_f05("S1-001", [], ["S2-001"])
        self.assertEqual(res_incorrect.f05, 0.0)
        self.assertEqual(res_incorrect.precision, 0.0)
        self.assertEqual(res_incorrect.recall, 0.0)

    def test_non_singleton_empty_prediction(self):
        """Entity with true matches but model predicts empty -> 0.0."""
        res = compute_entity_f05("S1-001", ["S2-100"], [])
        self.assertEqual(res.f05, 0.0)
        self.assertEqual(res.recall, 0.0)

    def test_macro_f05_aggregation(self):
        """Macro F_0.5 is unweighted average across all S1 entities."""
        gt = {
            "S1-1": ["S2-1"],        # Perfect: 1.0
            "S1-2": [],              # Singleton correct: 1.0
            "S1-3": ["S2-2"],        # Completely missed: 0.0
            "S1-4": [],              # Singleton false positive: 0.0
        }
        pred = {
            "S1-1": ["S2-1"],
            "S1-2": [],
            "S1-3": [],
            "S1-4": ["S2-99"],
        }

        summary, per_entity = compute_macro_f05(gt, pred)

        self.assertEqual(summary.total_entities, 4)
        self.assertEqual(summary.singleton_count, 2)
        self.assertEqual(summary.matched_count, 2)
        # 1.0 + 1.0 + 0.0 + 0.0 = 2.0 / 4 = 0.50
        self.assertAlmostEqual(summary.macro_f05, 0.50, places=5)
        self.assertAlmostEqual(summary.singleton_f05, 0.50, places=5)
        self.assertAlmostEqual(summary.matched_f05, 0.50, places=5)


class TestSubmissionVerifier(unittest.TestCase):
    """Tests for submission verifier invariants and adversarial failure modes."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.temp_dir.cleanup()

    def _create_tsv(self, filename: str, content: str) -> str:
        path = os.path.join(self.temp_dir.name, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return path

    def test_normal_valid_submission(self):
        test_s1 = self._create_tsv("test_source1.tsv", "entity_id\tname\taddress\tcountry\nS1-1\tA\tB\tUS\nS1-2\tC\tD\tUS\n")
        matching = self._create_tsv("matching_results.tsv", "source1_entity_id\tmatched_entity_ids\nS1-1\tS2-10,S3-20\nS1-2\t\n")
        candidate = self._create_tsv("candidate_pairs.tsv", "source1_entity_id\tcandidate_entity_ids\nS1-1\tS2-10,S3-20,S3-30\nS1-2\t\n")

        report = validate_submission_pipeline(
            matching_path=matching,
            candidate_path=candidate,
            test_source1_path=test_s1,
        )

        self.assertTrue(report.is_valid)
        self.assertEqual(len(report.errors), 0)
        self.assertEqual(report.total_source1_entities, 2)
        self.assertEqual(report.total_empty_rows, 1)
        self.assertEqual(report.total_non_empty_rows, 1)
        self.assertEqual(report.total_predicted_matches, 2)

    def test_adversarial_comma_separated_csv(self):
        """CSV comma-separated format must be caught and rejected (REQ-02)."""
        matching = self._create_tsv("matching_results.tsv", "source1_entity_id,matched_entity_ids\nS1-1,S2-10\n")
        report = validate_submission_pipeline(matching_path=matching)

        self.assertFalse(report.is_valid)
        rule_ids = [e.rule_id for e in report.errors]
        self.assertIn("REQ-02", rule_ids)

    def test_adversarial_self_match(self):
        """Self-matches (S1- in matched list) must be rejected (REQ-07)."""
        matching = self._create_tsv("matching_results.tsv", "source1_entity_id\tmatched_entity_ids\nS1-1\tS1-1\n")
        report = validate_submission_pipeline(matching_path=matching)

        self.assertFalse(report.is_valid)
        rule_ids = [e.rule_id for e in report.errors]
        self.assertIn("REQ-07", rule_ids)

    def test_adversarial_invalid_prefix(self):
        """IDs without S2- or S3- prefix must be rejected (REQ-06)."""
        matching = self._create_tsv("matching_results.tsv", "source1_entity_id\tmatched_entity_ids\nS1-1\tS4-999\n")
        report = validate_submission_pipeline(matching_path=matching)

        self.assertFalse(report.is_valid)
        rule_ids = [e.rule_id for e in report.errors]
        self.assertIn("REQ-06", rule_ids)

    def test_adversarial_duplicate_s1_rows(self):
        """Duplicate Source-1 entity rows must be rejected (REQ-05)."""
        matching = self._create_tsv("matching_results.tsv", "source1_entity_id\tmatched_entity_ids\nS1-1\tS2-1\nS1-1\tS2-2\n")
        report = validate_submission_pipeline(matching_path=matching)

        self.assertFalse(report.is_valid)
        rule_ids = [e.rule_id for e in report.errors]
        self.assertIn("REQ-05", rule_ids)

    def test_adversarial_intra_list_duplicates(self):
        """Repeated IDs within the same match list must be rejected (REQ-08)."""
        matching = self._create_tsv("matching_results.tsv", "source1_entity_id\tmatched_entity_ids\nS1-1\tS2-1,S2-1\n")
        report = validate_submission_pipeline(matching_path=matching)

        self.assertFalse(report.is_valid)
        rule_ids = [e.rule_id for e in report.errors]
        self.assertIn("REQ-08", rule_ids)

    def test_adversarial_literal_nan_string(self):
        """Literal string 'nan'/'null' must be rejected (REQ-09)."""
        matching = self._create_tsv("matching_results.tsv", "source1_entity_id\tmatched_entity_ids\nS1-1\tnan\n")
        report = validate_submission_pipeline(matching_path=matching)

        self.assertFalse(report.is_valid)
        rule_ids = [e.rule_id for e in report.errors]
        self.assertIn("REQ-09", rule_ids)

    def test_adversarial_missing_required_s1_entity(self):
        """Missing required test entities must be rejected (REQ-04)."""
        test_s1 = self._create_tsv("test_source1.tsv", "entity_id\tname\taddress\tcountry\nS1-1\tA\tB\tUS\nS1-2\tC\tD\tUS\n")
        # Missing S1-2
        matching = self._create_tsv("matching_results.tsv", "source1_entity_id\tmatched_entity_ids\nS1-1\tS2-10\n")

        report = validate_submission_pipeline(matching_path=matching, test_source1_path=test_s1)

        self.assertFalse(report.is_valid)
        rule_ids = [e.rule_id for e in report.errors]
        self.assertIn("REQ-04", rule_ids)

    def test_subset_invariant_warning(self):
        """Matched IDs not in candidate set produce a diagnostic warning (REQ-10)."""
        matching = self._create_tsv("matching_results.tsv", "source1_entity_id\tmatched_entity_ids\nS1-1\tS2-10,S3-99\n")
        candidate = self._create_tsv("candidate_pairs.tsv", "source1_entity_id\tcandidate_entity_ids\nS1-1\tS2-10\n")

        report = validate_submission_pipeline(matching_path=matching, candidate_path=candidate)

        # Warning, not fatal error
        self.assertTrue(report.is_valid)
        warning_rule_ids = [w.rule_id for w in report.warnings]
        self.assertIn("REQ-10", warning_rule_ids)


if __name__ == "__main__":
    unittest.main()
