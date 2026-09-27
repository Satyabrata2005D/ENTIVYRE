"""
Unit and adversarial tests for Phase 14: Multi-Pass Candidate Generation.
"""
import unittest
from pathlib import Path
import sys

_project_root = Path(__file__).resolve().parent.parent
_ber_src = _project_root / "code" / "business_entity_resolution" / "src"
if str(_ber_src) not in sys.path:
    sys.path.insert(0, str(_ber_src))

from ber.blocking.candidate_generator import (
    MultiPassCandidateGenerator,
    EnrichedCandidate,
    CandidateGenerationAuditMetrics,
)
from ber.blocking.standard_blocker import BlockingRecord
from ber.normalization.name_normalizer import NameNormalizer
from ber.normalization.address_normalizer import AddressNormalizer
from ber.normalization.country_handler import CountryHandler
from ber.labels.ground_truth import GroundTruthStore


class TestMultiPassCandidateGenerator(unittest.TestCase):
    def setUp(self):
        self.name_norm = NameNormalizer()
        self.addr_norm = AddressNormalizer()
        self.ctry_norm = CountryHandler()

        self.generator = MultiPassCandidateGenerator(
            max_candidates=10,
            standard_blocker_top_k=5,
            tfidf_top_k=5,
            tfidf_min_similarity=0.35,
        )

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

    def test_multi_pass_union_and_provenance(self):
        """Test that candidate generator unions passes and records provenance accurately."""
        # Target 1: Exact match with anchor
        t1 = self._make_record("S2-101", "Walmart Supercenter", "100 Main St", "US")
        # Target 2: Typo variant - won't match exact blocking key, but WILL match TF-IDF n-grams!
        t2 = self._make_record("S3-201", "Wal-Mrt Supercntr", "100 Main St", "US")
        # Target 3: Disjoint target
        t3 = self._make_record("S2-103", "Burger King", "55 5th Ave", "US")

        self.generator.index_targets([t1, t2, t3])

        anchor = self._make_record("S1-1", "Walmart Supercenter", "100 Main St", "US")
        cands = self.generator.generate_candidates(anchor)
        cand_map = {c.target_id: c for c in cands}

        # T1 should be found by both passes
        self.assertIn("S2-101", cand_map)
        self.assertIn("standard_blocker", cand_map["S2-101"].retrieval_sources)
        self.assertIn("tfidf_retriever", cand_map["S2-101"].retrieval_sources)

        # T2 (typo variant) should be rescued by TF-IDF!
        self.assertIn("S3-201", cand_map)
        self.assertIn("tfidf_retriever", cand_map["S3-201"].retrieval_sources)

        # T3 should NOT be present
        self.assertNotIn("S2-103", cand_map)

        # T1 (both passes) should rank higher than T2 (single pass)
        self.assertEqual(cands[0].target_id, "S2-101")

    def test_strict_candidate_invariants(self):
        """Verify no duplicate candidates, no self-matches, and strict cap."""
        generator_cap = MultiPassCandidateGenerator(max_candidates=3)
        targets = [
            self._make_record(f"S2-{i}", "Acme Supply Hub", "Address", "US")
            for i in range(15)
        ]
        generator_cap.index_targets(targets)

        anchor = self._make_record("S2-0", "Acme Supply Hub", "Address", "US")
        cands = generator_cap.generate_candidates(anchor)

        # Strict cap
        self.assertLessEqual(len(cands), 3)

        # No self match
        cand_ids = [c.target_id for c in cands]
        self.assertNotIn("S2-0", cand_ids)

        # No duplicate IDs
        self.assertEqual(len(cand_ids), len(set(cand_ids)))

    def test_candidate_pairs_map_and_audit(self):
        """Test dictionary generation and full recall audit."""
        t1 = self._make_record("S2-101", "Apex Logistics", "10 Road", "US")
        t2 = self._make_record("S3-201", "Apex Logistics International", "10 Road", "US")
        self.generator.index_targets([t1, t2])

        anchor = self._make_record("S1-1", "Apex Logistics", "10 Road", "US")
        gt = GroundTruthStore.from_dict({
            "S1-1": ["S2-101", "S3-201"]
        })

        pair_map = self.generator.generate_candidate_pairs_map([anchor])
        self.assertIn("S1-1", pair_map)
        self.assertEqual(set(pair_map["S1-1"]), {"S2-101", "S3-201"})

        audit = self.generator.audit_candidate_generation([anchor], gt)
        self.assertEqual(audit.total_anchors, 1)
        self.assertEqual(audit.total_candidate_pairs, 2)
        self.assertEqual(audit.candidate_recall, 1.0)


if __name__ == "__main__":
    unittest.main()
