"""
Unit, integration, and adversarial tests for Phase 03: Dataset Manifest & Discovery.
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

from ber.io.manifest import (
    profile_single_file,
    generate_dataset_manifest,
    verify_dataset_integrity,
    EXPECTED_FILES,
    FileManifest,
    DatasetManifest,
)


class TestDatasetManifest(unittest.TestCase):
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

    def test_profile_single_file_normal(self):
        """Test profiling a valid TSV file."""
        spec = EXPECTED_FILES["train_source1"]
        fm = profile_single_file("train_source1", self.root / "train" / "train_source1.tsv", spec)
        self.assertEqual(fm.file_key, "train_source1")
        self.assertEqual(fm.data_rows, 2)
        self.assertEqual(fm.total_lines, 3)
        self.assertTrue(fm.is_tab_delimited)
        self.assertTrue(fm.schema_valid)
        self.assertTrue(fm.id_prefix_valid)
        self.assertIn("S1-101", fm.sample_ids)
        self.assertEqual(len(fm.sha256), 64)
        self.assertEqual(len(fm.md5), 32)

    def test_generate_complete_manifest(self):
        """Test generating manifest for all 7 files."""
        manifest = generate_dataset_manifest(self.root)
        self.assertEqual(manifest.total_files, 7)
        self.assertEqual(manifest.total_records, 9)
        self.assertTrue(manifest.all_files_present)
        self.assertTrue(manifest.all_schemas_valid)
        self.assertTrue(manifest.all_prefixes_valid)

        # Check serialization
        d = manifest.to_dict()
        self.assertIn("files", d)
        self.assertEqual(len(d["files"]), 7)

    def test_missing_file_detection(self):
        """Test manifest handles missing files gracefully."""
        (self.root / "test" / "test_source3.tsv").unlink()
        manifest = generate_dataset_manifest(self.root)
        self.assertFalse(manifest.all_files_present)
        self.assertEqual(manifest.total_files, 6)

    def test_adversarial_malformed_header(self):
        """Test detection of comma-separated or malformed column header."""
        self._write_tsv(
            self.root / "train" / "train_source2.tsv",
            "entity_id,business_name,business_address,country\n"
            "S2-201,Acme,123 Main,US\n"
        )
        manifest = generate_dataset_manifest(self.root)
        self.assertFalse(manifest.all_schemas_valid)
        self.assertFalse(manifest.files["train_source2"].schema_valid)

    def test_adversarial_invalid_prefix(self):
        """Test detection of illegal entity ID prefix."""
        self._write_tsv(
            self.root / "train" / "train_source1.tsv",
            "entity_id\tbusiness_name\tbusiness_address\tcountry\n"
            "INVALID-101\tAcme Corp\t123 Main St\tUS\n"
        )
        manifest = generate_dataset_manifest(self.root)
        self.assertFalse(manifest.all_prefixes_valid)
        self.assertFalse(manifest.files["train_source1"].id_prefix_valid)

    def test_verify_dataset_integrity(self):
        """Test verifying manifest integrity and catching corruption."""
        manifest = generate_dataset_manifest(self.root)
        manifest_path = self.root / "manifest.json"
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest.to_dict(), f)

        # 1. Unmodified should pass
        valid, errors = verify_dataset_integrity(manifest_path, self.root, verify_hashes=True)
        self.assertTrue(valid)
        self.assertEqual(len(errors), 0)

        # 2. Corrupt file by appending data
        with open(self.root / "train" / "train_source1.tsv", "a") as f:
            f.write("S1-999\tCorrupt\tAddr\tUS\n")

        valid_corrupt, errors_corrupt = verify_dataset_integrity(manifest_path, self.root, verify_hashes=True)
        self.assertFalse(valid_corrupt)
        self.assertTrue(any("File size mismatch" in e or "corruption" in e for e in errors_corrupt))


if __name__ == "__main__":
    unittest.main()
