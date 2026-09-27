"""
Unit and adversarial tests for Phase 12: Blocking Baseline.
"""
import unittest
from pathlib import Path
import sys

_project_root = Path(__file__).resolve().parent.parent
_ber_src = _project_root / "code" / "business_entity_resolution" / "src"
if str(_ber_src) not in sys.path:
    sys.path.insert(0, str(_ber_src))

from ber.blocking.standard_blocker import StandardBlocker, BlockingRecord, BlockingAuditMetrics
from ber.normalization.name_normalizer import NameNormalizer
from ber.normalization.address_normalizer import AddressNormalizer
from ber.normalization.country_handler import CountryHandler
from ber.labels.ground_truth import GroundTruthStore


class TestStandardBlocker(unittest.TestCase):
    def setUp(self):
        self.name_norm = NameNormalizer()
        self.addr_norm = AddressNormalizer()
        self.ctry_norm = CountryHandler()

        self.blocker = StandardBlocker(max_candidates_per_anchor=10, max_key_frequency=5)

    def _make_record(self, eid: str, name: str, addr: str, ctry: str) -> BlockingRecord:
        return BlockingRecord.from_raw(
            entity_id=eid,
            business_name=name,
            business_address=addr,
            country=ctry,
            name_normalizer=self.name_norm,
            addr_normalizer=self.addr_norm,
            country_handler=self.ctry_norm,
        )

    def test_key_extraction_and_order_invariance(self):
        """Test that reordered business names produce overlapping blocking keys."""
        rec1 = self._make_record("S1-1", "Apex Omega Logistics", "123 Main St 10001", "US")
        rec2 = self._make_record("S2-10", "Logistics Apex Omega", "123 Main St 10001", "US")

        keys1 = self.blocker.extract_keys(rec1)
        keys2 = self.blocker.extract_keys(rec2)

        # Sorted tokens key must be identical
        self.assertIn("NAME_SORTED:apex logistics omega", keys1)
        self.assertIn("NAME_SORTED:apex logistics omega", keys2)
        # Shared sorted key
        self.assertTrue(len(keys1 & keys2) > 0)

    def test_postal_code_blocking_key(self):
        """Test postal code + name token key generation."""
        rec = self._make_record("S1-2", "Starbucks Coffee", "500 5th Ave, New York, NY 10018", "US")
        keys = self.blocker.extract_keys(rec)
        self.assertIn("POSTAL_NAME:10018:starbucks", keys)

    def test_indexing_and_candidate_retrieval(self):
        """Test indexing target records and retrieving candidates for an anchor."""
        t1 = self._make_record("S2-101", "Acme Corporation", "100 Broadway", "US")
        t2 = self._make_record("S3-201", "Acme Corp Ltd", "100 Broadway", "US")
        t3 = self._make_record("S2-102", "Totally Different Cafe", "99 1st Ave", "US")

        self.blocker.index_targets_batch([t1, t2, t3])
        self.assertEqual(len(self.blocker), 3)

        anchor = self._make_record("S1-1", "Acme Corporation", "100 Broadway", "US")
        candidates = self.blocker.retrieve_candidates(anchor)

        # Both Acme targets should be retrieved, unrelated cafe should not
        self.assertIn("S2-101", candidates)
        self.assertIn("S3-201", candidates)
        self.assertNotIn("S2-102", candidates)

        # Ensure no self match
        anchor_same_id = self._make_record("S2-101", "Acme Corporation", "100 Broadway", "US")
        candidates_self = self.blocker.retrieve_candidates(anchor_same_id)
        self.assertNotIn("S2-101", candidates_self)

    def test_candidate_cap(self):
        """Test capping candidates at max_candidates_per_anchor."""
        blocker_cap = StandardBlocker(max_candidates_per_anchor=2)
        targets = [
            self._make_record(f"S2-{i}", "Common Business Name", "Address", "US")
            for i in range(10)
        ]
        blocker_cap.index_targets_batch(targets)

        anchor = self._make_record("S1-100", "Common Business Name", "Address", "US")
        candidates = blocker_cap.retrieve_candidates(anchor)
        self.assertEqual(len(candidates), 2)

    def test_blocking_audit_metrics(self):
        """Test blocking audit and candidate recall against ground truth."""
        t1 = self._make_record("S2-101", "Acme Supplies", "100 Broadway", "US")
        t2 = self._make_record("S3-201", "Acme Supplies Inc", "100 Broadway", "US")
        self.blocker.index_targets_batch([t1, t2])

        anchor = self._make_record("S1-1", "Acme Supplies", "100 Broadway", "US")
        gt = GroundTruthStore.from_dict({
            "S1-1": ["S2-101", "S3-201"]
        })

        audit = self.blocker.audit_blocking([anchor], gt)
        self.assertEqual(audit.total_anchors_queried, 1)
        self.assertEqual(audit.total_candidate_pairs, 2)
        self.assertEqual(audit.candidate_recall, 1.0)
        self.assertEqual(audit.zero_candidate_anchor_count, 0)


if __name__ == "__main__":
    unittest.main()
