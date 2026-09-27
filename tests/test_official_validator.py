"""
Unit tests for Phase 33: Official Challenge Validator Integration.
"""
import os
import shutil
import tempfile
import unittest
from pathlib import Path

from ber.outputs.serializer import OutputSerializer
from ber.validation.official_validator import OfficialValidatorBridge, OfficialValidationResult


class TestOfficialValidatorIntegration(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.output_dir = Path(self.temp_dir) / "output"
        self.test_dir = Path(self.temp_dir) / "dataset" / "test"
        self.output_dir.mkdir(parents=True)
        self.test_dir.mkdir(parents=True)

        # Create synthetic test_source1.tsv
        self.s1_file = self.test_dir / "test_source1.tsv"
        with open(self.s1_file, "w", encoding="utf-8") as f:
            f.write("entity_id\tname\taddress\tcountry\n")
            f.write("S1-00001\tAcme Inc\t100 Main St\tUS\n")
            f.write("S1-00002\tApex Store\t200 Oak Rd\tIndia\n")
            f.write("S1-00003\tSolo Enterprise\t300 Pine Ave\tFrance\n")

        # Create synthetic test_source2.tsv & test_source3.tsv
        with open(self.test_dir / "test_source2.tsv", "w", encoding="utf-8") as f:
            f.write("entity_id\tname\taddress\tcountry\n")
            f.write("S2-00010\tAcme Corporation\t100 Main St\tUS\n")
            f.write("S2-00020\tApex Superstore\t200 Oak Rd\tIndia\n")

        with open(self.test_dir / "test_source3.tsv", "w", encoding="utf-8") as f:
            f.write("entity_id\tname\taddress\tcountry\n")
            f.write("S3-00011\tAcme LLC\t100 Main St\tUS\n")

        # Find official validator script
        self.official_script = Path.cwd() / "student_resource" / "utils" / "validate_submission.py"
        self.assertTrue(self.official_script.is_file(), f"Missing {self.official_script}")

        self.bridge = OfficialValidatorBridge(script_path=self.official_script)

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_valid_submission_passes_official_validator(self):
        """Verify compliant matching and candidate files pass official validator with exit code 0."""
        matching_path = self.output_dir / "matching_results.tsv"
        candidate_path = self.output_dir / "candidate_pairs.tsv"

        predictions = {
            "S1-00001": ["S2-00010", "S3-00011"],
            "S1-00002": ["S2-00020"],
            "S1-00003": [],  # Singleton
        }
        candidates = {
            "S1-00001": ["S2-00010", "S3-00011"],
            "S1-00002": ["S2-00020"],
            "S1-00003": [],  # Singleton
        }

        OutputSerializer.serialize_matching_results(predictions, matching_path)
        OutputSerializer.serialize_candidate_pairs(candidates, candidate_path)

        res = self.bridge.run_validation(
            matching_path=matching_path,
            candidate_path=candidate_path,
            test_dir=self.test_dir,
            check_ids=True,
        )

        self.assertTrue(res.success)
        self.assertEqual(res.returncode, 0)
        self.assertEqual(len(res.errors), 0)
        self.assertIn("PASS — no blocking issues found", res.stdout)

    def test_missing_s1_row_fails_official_validator(self):
        """Verify omission of required S1 record fails with exit code 1."""
        matching_path = self.output_dir / "matching_results.tsv"
        candidate_path = self.output_dir / "candidate_pairs.tsv"

        # Missing S1-00003!
        predictions = {
            "S1-00001": ["S2-00010"],
            "S1-00002": ["S2-00020"],
        }
        candidates = predictions.copy()

        OutputSerializer.serialize_matching_results(predictions, matching_path)
        OutputSerializer.serialize_candidate_pairs(candidates, candidate_path)

        res = self.bridge.run_validation(
            matching_path=matching_path,
            candidate_path=candidate_path,
            test_dir=self.test_dir,
            check_ids=False,
        )

        self.assertFalse(res.success)
        self.assertEqual(res.returncode, 1)
        self.assertTrue(any("required S1 entity(ies) missing" in e for e in res.errors))

    def test_candidate_subset_discrepancy_generates_warning(self):
        """Verify that prediction not in candidate set emits official warning."""
        matching_path = self.output_dir / "matching_results.tsv"
        candidate_path = self.output_dir / "candidate_pairs.tsv"

        predictions = {
            "S1-00001": ["S2-00010", "S3-00011"],
            "S1-00002": ["S2-00020"],
            "S1-00003": [],
        }
        # candidate file omits S3-00011
        candidates = {
            "S1-00001": ["S2-00010"],
            "S1-00002": ["S2-00020"],
            "S1-00003": [],
        }

        OutputSerializer.serialize_matching_results(predictions, matching_path)
        OutputSerializer.serialize_candidate_pairs(candidates, candidate_path)

        res = self.bridge.run_validation(
            matching_path=matching_path,
            candidate_path=candidate_path,
            test_dir=self.test_dir,
            check_ids=False,
        )

        # Official validator treats subset difference as warning, exit code 0
        self.assertTrue(res.success)
        self.assertEqual(res.returncode, 0)
        self.assertTrue(any("not present in candidate_pairs.tsv" in w for w in res.warnings))


if __name__ == "__main__":
    unittest.main()
