"""
Unit and adversarial tests for Phase 04: Safe Ingestion Engine.
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

from ber.io.ingestion import (
    stream_source_chunks,
    stream_ground_truth_chunks,
    load_ground_truth_map,
    clean_field_text,
    QuarantineManager,
    Source1Record,
    Source2Record,
    Source3Record,
    GroundTruthRecord,
)


class TestSafeIngestionEngine(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def _write_file(self, filename: str, content: str) -> Path:
        p = self.root / filename
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(content)
        return p

    def test_clean_field_text(self):
        """Test cleaning of missing, whitespace, and literal nan strings."""
        self.assertEqual(clean_field_text(None), "")
        self.assertEqual(clean_field_text("   "), "")
        self.assertEqual(clean_field_text("nan"), "")
        self.assertEqual(clean_field_text("NAN"), "")
        self.assertEqual(clean_field_text("null"), "")
        self.assertEqual(clean_field_text("None"), "")
        self.assertEqual(clean_field_text("N/A"), "")
        self.assertEqual(clean_field_text("  Valid Business  "), "Valid Business")

    def test_stream_source_normal_chunks(self):
        """Test streaming valid source records in small chunks."""
        content = (
            "entity_id\tbusiness_name\tbusiness_address\tcountry\n"
            "S1-1\tAcme\t123 Main St\tUS\n"
            "S1-2\tBeta LLC\tnan\tIndia\n"
            "S1-3\tGamma Inc\t789 Broad Rd\tFrance\n"
        )
        tsv_path = self._write_file("test_s1.tsv", content)
        
        chunks = []
        for chunk, stats in stream_source_chunks(tsv_path, chunk_size=2):
            chunks.append(chunk)

        self.assertEqual(len(chunks), 2)
        self.assertEqual(len(chunks[0]), 2)
        self.assertEqual(len(chunks[1]), 1)

        rec1 = chunks[0][0]
        self.assertIsInstance(rec1, Source1Record)
        self.assertEqual(rec1.entity_id, "S1-1")
        self.assertEqual(rec1.business_name, "Acme")
        self.assertEqual(rec1.business_address, "123 Main St")
        self.assertEqual(rec1.country, "US")

        # Verify nan was cleaned to empty string
        rec2 = chunks[0][1]
        self.assertEqual(rec2.entity_id, "S1-2")
        self.assertEqual(rec2.business_address, "")

    def test_stream_ground_truth_singletons_and_multimatch(self):
        """Test streaming ground truth records including singletons."""
        content = (
            "source1_entity_id\tmatched_entity_ids\n"
            "S1-100\t\n"  # Singleton with empty match
            "S1-101\tS2-201\n"  # Single match
            "S1-102\tS2-202,S3-301 S3-302\n"  # Multi-match with mixed delimiters
            "S1-103\tnan\n"  # Literal nan singleton
        )
        gt_path = self._write_file("gt.tsv", content)

        gt_records = []
        for chunk, _ in stream_ground_truth_chunks(gt_path, chunk_size=10):
            gt_records.extend(chunk)

        self.assertEqual(len(gt_records), 4)
        self.assertEqual(gt_records[0].source1_entity_id, "S1-100")
        self.assertEqual(gt_records[0].matched_entity_ids, ())
        self.assertTrue(gt_records[0].is_singleton)

        self.assertEqual(gt_records[1].source1_entity_id, "S1-101")
        self.assertEqual(gt_records[1].matched_entity_ids, ("S2-201",))
        self.assertFalse(gt_records[1].is_singleton)

        self.assertEqual(gt_records[2].source1_entity_id, "S1-102")
        self.assertEqual(set(gt_records[2].matched_entity_ids), {"S2-202", "S3-301", "S3-302"})

        self.assertEqual(gt_records[3].source1_entity_id, "S1-103")
        self.assertEqual(gt_records[3].matched_entity_ids, ())

    def test_quarantine_malformed_rows(self):
        """Test that malformed, corrupted, or prefix-mismatched rows are quarantined."""
        content = (
            "entity_id\tbusiness_name\tbusiness_address\tcountry\n"
            "S1-1\tValid One\t123 St\tUS\n"
            "MALFORMED_ROW_FEWER_COLS\tOnly Two\n"
            "S1-2\tValid Two\t456 Rd\tIndia\n"
            "S2-999\tWrong Prefix in S1\t789 Ave\tUS\n"
            "S1-INVALID_ID_CHARS\tBad ID\t000 St\tUS\n"
            "S1-3\tValid Three\t111 Blvd\tUS\n"
        )
        tsv_path = self._write_file("corrupt.tsv", content)
        qm = QuarantineManager(output_dir=self.root / "reports")

        valid_records = []
        for chunk, stats in stream_source_chunks(tsv_path, chunk_size=10, expected_prefix="S1-", quarantine=qm):
            valid_records.extend(chunk)

        # Only S1-1, S1-2, S1-3 should be emitted
        self.assertEqual(len(valid_records), 3)
        self.assertEqual([r.entity_id for r in valid_records], ["S1-1", "S1-2", "S1-3"])

        # 3 rows quarantined: fewer cols, wrong prefix, bad id chars
        self.assertEqual(len(qm.quarantined), 3)
        report_path = qm.persist_report("corrupt_test")
        self.assertTrue(report_path.exists())

        with open(report_path) as f:
            data = json.load(f)
            self.assertEqual(data["total_quarantined"], 3)

    def test_load_ground_truth_map(self):
        """Test fast loading of ground truth map."""
        content = (
            "source1_entity_id\tmatched_entity_ids\n"
            "S1-1\tS2-10 S3-20\n"
            "S1-2\t\n"
        )
        gt_path = self._write_file("gt_map.tsv", content)
        mapping = load_ground_truth_map(gt_path)

        self.assertEqual(len(mapping), 2)
        self.assertEqual(mapping["S1-1"], ("S2-10", "S3-20"))
        self.assertEqual(mapping["S1-2"], ())


if __name__ == "__main__":
    unittest.main()
