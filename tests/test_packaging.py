"""
Unit tests for Phase 38: Official Submission Packaging.
"""
import os
import shutil
import zipfile
import tempfile
import unittest
from pathlib import Path

from scripts.package_submission import package_submission


class TestSubmissionPackaging(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.output_dir = Path(self.temp_dir) / "output"
        self.code_dir = Path(self.temp_dir) / "code" / "business_entity_resolution"
        self.dest_dir = Path(self.temp_dir) / "submission"
        self.doc_path = Path(self.temp_dir) / "Documentation_template.md"

        self.output_dir.mkdir(parents=True)
        (self.code_dir / "src" / "ber").mkdir(parents=True)
        self.dest_dir.mkdir(parents=True)

        # Mock output files
        with open(self.output_dir / "matching_results.tsv", "w", encoding="utf-8") as f:
            f.write("source1_entity_id\tmatched_entity_ids\nS1-001\tS2-002\n")
        with open(self.output_dir / "candidate_pairs.tsv", "w", encoding="utf-8") as f:
            f.write("source1_entity_id\tcandidate_entity_ids\nS1-001\tS2-002\n")

        # Mock code files
        with open(self.code_dir / "src" / "ber" / "dummy.py", "w") as f:
            f.write("# dummy code\n")
        with open(self.code_dir / "README.md", "w") as f:
            f.write("# README\n")
        with open(self.code_dir / "requirements.txt", "w") as f:
            f.write("pytest\n")

        # Mock documentation
        with open(self.doc_path, "w") as f:
            f.write("# Documentation\n")

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_package_creation_and_contents(self):
        """Verify ZIP archive is correctly structured according to official specifications."""
        zip_path = package_submission(
            team_name="ENTIVYRE_TEST",
            output_dir=self.output_dir,
            code_dir=self.code_dir,
            doc_path=self.doc_path,
            target_zip_dir=self.dest_dir,
        )

        self.assertTrue(zip_path.is_file())
        self.assertEqual(zip_path.name, "ENTIVYRE_TEST_submission.zip")

        # Inspect zip contents
        with zipfile.ZipFile(zip_path, "r") as zf:
            namelist = set(zf.namelist())

            # Expected essential files
            self.assertIn("output/matching_results.tsv", namelist)
            self.assertIn("output/candidate_pairs.tsv", namelist)
            self.assertIn("code/business_entity_resolution/src/ber/dummy.py", namelist)
            self.assertIn("code/business_entity_resolution/README.md", namelist)
            self.assertIn("code/business_entity_resolution/requirements.txt", namelist)
            self.assertIn("Documentation_template.md", namelist)

            # Ensure zero pycache or pyc leaked
            for name in namelist:
                self.assertNotIn("__pycache__", name)
                self.assertFalse(name.endswith(".pyc"))


if __name__ == "__main__":
    unittest.main()
