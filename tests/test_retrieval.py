"""
Unit and adversarial tests for Phase 13: Character n-gram / TF-IDF Retrieval.
"""
import unittest
from pathlib import Path
import sys

_project_root = Path(__file__).resolve().parent.parent
_ber_src = _project_root / "code" / "business_entity_resolution" / "src"
if str(_ber_src) not in sys.path:
    sys.path.insert(0, str(_ber_src))

from ber.retrieval.tfidf_retriever import SparseCharTfidfRetriever, RetrievalCandidate


class TestSparseCharTfidfRetriever(unittest.TestCase):
    def setUp(self):
        self.retriever = SparseCharTfidfRetriever(ngram_size=3, min_df=1)
        self.corpus = [
            ("S2-1", "walmart supercenter"),
            ("S3-1", "target store"),
            ("S2-2", "mcdonalds restaurant"),
            ("S3-2", "starbucks coffee company"),
            ("S2-3", "baskin robbins ice cream"),
        ]
        self.retriever.fit_and_index(self.corpus)

    def test_exact_match_retrieval(self):
        """Test that exact query returns top similarity close to 1.0."""
        cands = self.retriever.retrieve_top_k("walmart supercenter", k=5, min_similarity=0.5)
        self.assertGreater(len(cands), 0)
        self.assertEqual(cands[0].target_id, "S2-1")
        self.assertAlmostEqual(cands[0].similarity_score, 1.0, places=2)

    def test_typo_and_subword_tolerance(self):
        """Test retrieval under typos, spelling variations, and missing characters."""
        # 1. Punctuation/hyphen variant: "wal mart" vs "walmart"
        cands_wal = self.retriever.retrieve_top_k("wal mart supercenter", k=5, min_similarity=0.4)
        self.assertGreater(len(cands_wal), 0)
        self.assertEqual(cands_wal[0].target_id, "S2-1")
        self.assertGreater(cands_wal[0].similarity_score, 0.65)

        # 2. Vowel typo: "basken robins" vs "baskin robbins"
        cands_br = self.retriever.retrieve_top_k("basken robins", k=5, min_similarity=0.4)
        self.assertGreater(len(cands_br), 0)
        self.assertEqual(cands_br[0].target_id, "S2-3")
        self.assertGreater(cands_br[0].similarity_score, 0.55)

        # 3. Space variation: "mc donalds" vs "mcdonalds"
        cands_mc = self.retriever.retrieve_top_k("mc donalds", k=5, min_similarity=0.4)
        self.assertGreater(len(cands_mc), 0)
        self.assertEqual(cands_mc[0].target_id, "S2-2")

    def test_top_k_bounding(self):
        """Test that result count never exceeds k."""
        cands = self.retriever.retrieve_top_k("coffee ice cream restaurant", k=2, min_similarity=0.1)
        self.assertLessEqual(len(cands), 2)

    def test_min_similarity_threshold(self):
        """Test that weak similarities are properly filtered out."""
        # Query with virtually no overlap with any target
        cands = self.retriever.retrieve_top_k("quantum computing laboratory", k=5, min_similarity=0.4)
        self.assertEqual(len(cands), 0)

    def test_pairwise_cosine_similarity(self):
        """Test compute_cosine_similarity method."""
        # Self similarity
        self.assertAlmostEqual(
            self.retriever.compute_cosine_similarity("starbucks", "starbucks"), 1.0
        )
        # High similarity for minor typo
        sim_typo = self.retriever.compute_cosine_similarity("starbucks", "starbuck")
        self.assertGreater(sim_typo, 0.70)

        # Disjoint similarity
        sim_disjoint = self.retriever.compute_cosine_similarity("apple", "zebra")
        self.assertLess(sim_disjoint, 0.10)

        # Empty string
        self.assertEqual(self.retriever.compute_cosine_similarity("", "starbucks"), 0.0)

    def test_empty_query(self):
        """Test handling of empty or blank queries."""
        self.assertEqual(self.retriever.retrieve_top_k("", k=5), [])
        self.assertEqual(self.retriever.retrieve_top_k("   ", k=5), [])


if __name__ == "__main__":
    unittest.main()
