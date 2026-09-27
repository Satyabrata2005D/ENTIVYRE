"""
Unit, integration, and adversarial tests for Phase 05: Data and Identifier Validation.
"""
import os
import sys
import unittest
import tempfile
import json
from pathlib import Path

_project_root = Path(__file__).resolve().parent.parent
_ber_src = _project_root / "code" / "business_entity_resolution" / "src"
if str(_ber_src) not in sys.path:
    sys.path.insert(0, str(_ber_src))

from ber.validation.data_validator import (
    validate_source_file,
    validate_ground_truth_file,
    run_full_dataset_validation,
    FileValidationResult,
    DatasetValidationReport,
)


class TestDataValidation(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "train").mkdir(parents=True, exist_ok=True)
        (self.root / "test").mkdir(parents=True, exist_ok=True)

        # Create valid mock files for train and test
        self._write_tsv(
            self.root / "train" / "train_source1.tsv",
            "entity_id\tbusiness_name\tbusiness_address\tcountry\n"
            "S1-101\tAcme Corp\t123 Main St\tUS\n"
            "S1-102\tGlobex Inc\t456 Market St\tIndia\n"
        )
        self._write_tsv(
            self.root / "train" / "train_source2.tsv",
            "entity_id\tbusiness_name\tbusiness_address\tcountry\n"
            "S2-201\tAcme Corporation\t123 Main Street\tUS\n"
        )
        self._write_tsv(
            self.root / "train" / "train_source3.tsv",
            "entity_id\tbusiness_name\tbusiness_address\tcountry\n"
            "S3-301\tGlobex\t456 Market Road\tIndia\n"
        )
        self._write_tsv(
            self.root / "train" / "train_ground_truth.tsv",
            "source1_entity_id\tmatched_entity_ids\n"
            "S1-101\tS2-201\n"
            "S1-102\tS3-301\n"
        )
        self._write_tsv(
            self.root / "test" / "test_source1.tsv",
            "entity_id\tbusiness_name\tbusiness_address\tcountry\n"
            "S1-501\tFrench Entity\t10 Rue de Paris\tFrance\n"
        )
        self._write_tsv(
            self.root / "test" / "test_source2.tsv",
            "entity_id\tbusiness_name\tbusiness_address\tcountry\n"
            "S2-601\tFrench Entity SARL\t10 Rue Paris\tFrance\n"
        )
        self._write_tsv(
            self.root / "test" / "test_source3.tsv",
            "entity_id\tbusiness_name\tbusiness_address\tcountry\n"
            "S3-701\tFrench Entity Co\t10 Rue de Paris\tFrance\n"
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def _write_tsv(self, path: Path, content: str):
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    def test_validate_source_file_normal(self):
        """Test validating a normal valid source file."""
        res, ids = validate_source_file(
            self.root / "train" / "train_source1.tsv", "train_source1", "S1-"
        )
        self.assertTrue(res.is_valid)
        self.assertEqual(res.total_records, 2)
        self.assertEqual(res.duplicate_id_count, 0)
        self.assertEqual(res.missingness.missing_names, 0)
        self.assertEqual(res.missingness.missing_addresses, 0)
        self.assertEqual(ids, {"S1-101", "S1-102"})

    def test_detect_duplicate_ids(self):
        """Test catching duplicate IDs inside a source file."""
        self._write_tsv(
            self.root / "train" / "train_source1.tsv",
            "entity_id\tbusiness_name\tbusiness_address\tcountry\n"
            "S1-101\tAcme\t123 St\tUS\n"
            "S1-101\tAcme Dupe\t456 Rd\tUS\n"
        )
        res, ids = validate_source_file(
            self.root / "train" / "train_source1.tsv", "train_source1", "S1-"
        )
        self.assertFalse(res.is_valid)
        self.assertEqual(res.duplicate_id_count, 1)
        self.assertIn("S1-101", res.sample_duplicate_ids)

    def test_missing_address_percentage(self):
        """Test calculating missing address metrics."""
        self._write_tsv(
            self.root / "train" / "train_source2.tsv",
            "entity_id\tbusiness_name\tbusiness_address\tcountry\n"
            "S2-1\tAcme\t123 St\tUS\n"
            "S2-2\tBeta\tnan\tUS\n"
            "S2-3\tGamma\t\tUS\n"
            "S2-4\tDelta\t456 Ave\tUS\n"
        )
        res, ids = validate_source_file(
            self.root / "train" / "train_source2.tsv", "train_source2", "S2-"
        )
        self.assertEqual(res.missingness.missing_addresses, 2)
        self.assertEqual(res.missingness.missing_address_pct, 50.0)

    def test_full_dataset_validation_normal(self):
        """Test complete full dataset validation report on clean data."""
        report = run_full_dataset_validation(self.root)
        self.assertTrue(report.all_files_valid)
        self.assertEqual(report.train_test_overlap_count, 0)
        self.assertEqual(report.ground_truth_orphan_targets_count, 0)
        self.assertAlmostEqual(report.ground_truth_s1_coverage_pct, 100.0)

    def test_adversarial_train_test_overlap(self):
        """Test catching ID leakage between train and test."""
        self._write_tsv(
            self.root / "test" / "test_source1.tsv",
            "entity_id\tbusiness_name\tbusiness_address\tcountry\n"
            "S1-101\tLeaked From Train\t123 St\tUS\n"
        )
        report = run_full_dataset_validation(self.root)
        self.assertFalse(report.all_files_valid)
        self.assertEqual(report.train_test_overlap_count, 1)

    def test_adversarial_orphan_ground_truth_target(self):
        """Test catching ground truth targets that don't exist in S2 or S3."""
        self._write_tsv(
            self.root / "train" / "train_ground_truth.tsv",
            "source1_entity_id\tmatched_entity_ids\n"
            "S1-101\tS2-99999\n"  # S2-99999 does not exist in train_source2
        )
        report = run_full_dataset_validation(self.root)
        self.assertFalse(report.all_files_valid)
        self.assertEqual(report.ground_truth_orphan_targets_count, 1)


if __name__ == "__main__":
    unittest.main()
