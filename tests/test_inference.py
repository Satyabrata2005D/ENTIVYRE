"""
Unit tests for Phase 34: High-Throughput Streaming Inference Engine.
"""
import os
import shutil
import tempfile
import unittest
from pathlib import Path

from ber.inference.engine import InferenceEngine, InferenceConfig, InferenceStats
from ber.outputs.serializer import OutputSerializer


class TestInferenceEngine(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_dir = Path(self.temp_dir) / "dataset" / "test"
        self.output_dir = Path(self.temp_dir) / "output"
        self.test_dir.mkdir(parents=True)
        self.output_dir.mkdir(parents=True)

        # Create test_source1.tsv
        self.s1_file = self.test_dir / "test_source1.tsv"
        with open(self.s1_file, "w", encoding="utf-8") as f:
            f.write("entity_id\tbusiness_name\tbusiness_address\tcountry\n")
            f.write("S1-001\tStarbucks Coffee Co\t123 Market St\tUS\n")
            f.write("S1-002\tApex Supermarket\t456 Commercial Rd\tIndia\n")
            f.write("S1-003\tLe Bistrot Parisien\t10 Rue de la Paix\tFrance\n")  # Open set country
            f.write("S1-004\tUnique Hermit Solo Enterprise\t999 Isolated Way\tUS\n")  # Singleton

        # Create test_source2.tsv
        self.s2_file = self.test_dir / "test_source2.tsv"
        with open(self.s2_file, "w", encoding="utf-8") as f:
            f.write("entity_id\tbusiness_name\tbusiness_address\tcountry\n")
            f.write("S2-101\tStarbucks Coffee\t123 Market Street\tUS\n")
            f.write("S2-102\tApex Supermarket Private Ltd\t456 Commercial Road\tIndia\n")
            f.write("S2-103\tLe Bistrot Parisien SARL\t10 Rue de la Paix\tFrance\n")

        # Create test_source3.tsv
        self.s3_file = self.test_dir / "test_source3.tsv"
        with open(self.s3_file, "w", encoding="utf-8") as f:
            f.write("entity_id\tbusiness_name\tbusiness_address\tcountry\n")
            f.write("S3-201\tStarbucks\t123 Market St, Suite 4\tUS\n")
            f.write("S3-202\tApex Retail\t456 Commercial Rd\tIndia\n")

        self.engine = InferenceEngine(InferenceConfig(log_interval=10))

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_indexing_targets(self):
        """Verify target sources are indexed properly into memory."""
        s2_count = self.engine.index_target_file(self.s2_file)
        s3_count = self.engine.index_target_file(self.s3_file)

        self.assertEqual(s2_count, 3)
        self.assertEqual(s3_count, 2)
        self.assertEqual(len(self.engine.target_records), 5)
        self.assertGreater(len(self.engine.index), 0)

    def test_streaming_inference_execution(self):
        """Verify end-to-end streaming inference execution and output generation."""
        self.engine.index_target_file(self.s2_file)
        self.engine.index_target_file(self.s3_file)

        matching_path = self.output_dir / "matching_results.tsv"
        candidate_path = self.output_dir / "candidate_pairs.tsv"

        stats = self.engine.run_streaming_inference(
            source1_tsv_path=self.s1_file,
            matching_output_path=matching_path,
            candidate_output_path=candidate_path,
        )

        self.assertEqual(stats.total_anchors, 4)
        self.assertEqual(stats.matched_count, 3)
        self.assertEqual(stats.singleton_count, 1)
        self.assertGreater(stats.total_candidate_pairs, 0)

        # Verify files exist and validate against OutputSerializer
        report = OutputSerializer.validate_submission_files(
            matching_tsv_path=matching_path,
            candidate_tsv_path=candidate_path,
            expected_s1_ids={"S1-001", "S1-002", "S1-003", "S1-004"},
        )

        self.assertTrue(report.is_valid, f"Validation errors: {report.format_errors}")
        self.assertEqual(report.candidate_subset_violations, 0)
        self.assertEqual(report.total_matching_rows, 4)
        self.assertEqual(report.singleton_matching_rows, 1)
        self.assertEqual(report.matched_rows, 3)


if __name__ == "__main__":
    unittest.main()
