"""
Unit tests for Phase 39: Clean-Room Reproducibility Verification.
"""
import os
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.package_submission import package_submission
from scripts.verify_clean_room import verify_clean_room


class TestCleanRoomVerification(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.output_dir = Path(self.temp_dir) / "output"
        self.test_dir = Path(self.temp_dir) / "dataset" / "test"
        self.submission_dir = Path(self.temp_dir) / "submission"
        self.code_dir = Path(self.temp_dir) / "code" / "business_entity_resolution"
        self.doc_path = Path(self.temp_dir) / "Documentation_template.md"

        self.output_dir.mkdir(parents=True)
        self.test_dir.mkdir(parents=True)
        self.submission_dir.mkdir(parents=True)
        (self.code_dir / "src" / "ber").mkdir(parents=True)

        # Create synthetic test_source1.tsv
        with open(self.test_dir / "test_source1.tsv", "w", encoding="utf-8") as f:
            f.write("entity_id\tbusiness_name\tbusiness_address\tcountry\n")
            f.write("S1-100\tOmega Corp\t500 Fifth Ave\tUS\n")
            f.write("S1-200\tBeta Store\t600 Sixth Ave\tIndia\n")

        # Create valid output files
        with open(self.output_dir / "matching_results.tsv", "w", encoding="utf-8") as f:
            f.write("source1_entity_id\tmatched_entity_ids\n")
            f.write("S1-100\tS2-101\n")
            f.write("S1-200\t\n")

        with open(self.output_dir / "candidate_pairs.tsv", "w", encoding="utf-8") as f:
            f.write("source1_entity_id\tcandidate_entity_ids\n")
            f.write("S1-100\tS2-101,S3-102\n")
            f.write("S1-200\t\n")

        # Copy actual packages from src to simulate clean room
        src_real = Path.cwd() / "code" / "business_entity_resolution" / "src"
        dest_mock = self.code_dir / "src"
        for pkg_name in ("ber", "entivyre"):
            pkg_src = src_real / pkg_name
            pkg_dest = dest_mock / pkg_name
            if pkg_src.is_dir():
                for item in pkg_src.iterdir():
                    if item.is_dir() and item.name not in {"__pycache__"}:
                        shutil.copytree(item, pkg_dest / item.name)
                    elif item.is_file() and not item.name.endswith(".pyc"):
                        pkg_dest.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(item, pkg_dest / item.name)

        with open(self.code_dir / "README.md", "w") as f:
            f.write("# README\n")
        with open(self.code_dir / "requirements.txt", "w") as f:
            f.write("numpy\n")
        with open(self.doc_path, "w") as f:
            f.write("# Documentation\n")

        # Package submission zip
        self.zip_path = package_submission(
            team_name="ENTIVYRE_CLEANROOM",
            output_dir=self.output_dir,
            code_dir=self.code_dir,
            doc_path=self.doc_path,
            target_zip_dir=self.submission_dir,
        )

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_clean_room_reproducibility(self):
        """Verify that packaged archive can be successfully validated in isolated sandbox."""
        success = verify_clean_room(
            submission_zip_path=self.zip_path,
            test_dir=self.test_dir,
        )
        self.assertTrue(success)


if __name__ == "__main__":
    unittest.main()
