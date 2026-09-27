"""
Unit and Integration Tests for Phase 32: Output Serializer & Format Validator.
"""
import unittest
import tempfile
from pathlib import Path

from ber.outputs.serializer import (
    OutputSerializer,
    OutputValidationReport,
    MATCHING_HEADER,
    CANDIDATE_HEADER,
)


class TestOutputSerializer(unittest.TestCase):
    def test_serialization_and_validation_roundtrip(self):
        candidates = {
            "S1-100": ["S2-001", "S3-002", "S2-003"],
            "S1-200": ["S2-004"],
            "S1-300": [], # zero candidates
        }
        predictions = {
            "S1-100": ["S2-001", "S3-002"],
            "S1-200": ["S2-004"],
            "S1-300": [], # singleton
        }

        with tempfile.TemporaryDirectory() as tmpdir:
            m_path = Path(tmpdir) / "matching_results.tsv"
            c_path = Path(tmpdir) / "candidate_pairs.tsv"

            OutputSerializer.serialize_matching_results(predictions, m_path)
            OutputSerializer.serialize_candidate_pairs(candidates, c_path)

            self.assertTrue(m_path.exists())
            self.assertTrue(c_path.exists())

            # Validate files
            report = OutputSerializer.validate_submission_files(
                m_path,
                c_path,
                expected_s1_ids={"S1-100", "S1-200", "S1-300"},
            )
            self.assertTrue(report.is_valid)
            self.assertEqual(report.total_matching_rows, 3)
            self.assertEqual(report.singleton_matching_rows, 1)
            self.assertEqual(report.matched_rows, 2)
            self.assertEqual(report.candidate_subset_violations, 0)
            self.assertEqual(len(report.format_errors), 0)

    def test_candidate_subset_violation_detection(self):
        candidates = {
            "S1-100": ["S2-001"],
        }
        # Model predicted S3-999 which was NOT in candidates
        predictions = {
            "S1-100": ["S2-001", "S3-999"],
        }

        with tempfile.TemporaryDirectory() as tmpdir:
            m_path = Path(tmpdir) / "matching_results.tsv"
            c_path = Path(tmpdir) / "candidate_pairs.tsv"

            # Bypass auto-clean by writing manually to test validator
            with open(c_path, "w", encoding="utf-8") as f:
                f.write(CANDIDATE_HEADER)
                f.write("S1-100\tS2-001\n")

            with open(m_path, "w", encoding="utf-8") as f:
                f.write(MATCHING_HEADER)
                f.write("S1-100\tS2-001 S3-999\n")

            report = OutputSerializer.validate_submission_files(m_path, c_path)
            self.assertFalse(report.is_valid)
            self.assertGreaterEqual(report.candidate_subset_violations, 1)

    def test_illegal_self_match_and_prefix_detection(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            m_path = Path(tmpdir) / "matching_results.tsv"
            c_path = Path(tmpdir) / "candidate_pairs.tsv"

            with open(c_path, "w", encoding="utf-8") as f:
                f.write(CANDIDATE_HEADER)
                f.write("S1-100\tS1-100\n")  # Self-match in candidates

            with open(m_path, "w", encoding="utf-8") as f:
                f.write(MATCHING_HEADER)
                f.write("S1-100\tS1-100\n")  # Self-match in matches

            report = OutputSerializer.validate_submission_files(m_path, c_path)
            self.assertFalse(report.is_valid)
            self.assertTrue(any("Self-match" in err or "prefix" in err for err in report.format_errors))


if __name__ == "__main__":
    unittest.main()
