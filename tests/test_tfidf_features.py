"""
Unit and adversarial tests for Phase 18: TF-IDF Features.
"""
import unittest
from pathlib import Path
import sys

_project_root = Path(__file__).resolve().parent.parent
_ber_src = _project_root / "code" / "business_entity_resolution" / "src"
if str(_ber_src) not in sys.path:
    sys.path.insert(0, str(_ber_src))

from ber.features.tfidf_features import TfidfFeatureExtractor
from ber.normalization.name_normalizer import NameNormalizer
from ber.normalization.address_normalizer import AddressNormalizer


class TestTfidfFeatures(unittest.TestCase):
    def setUp(self):
        self.name_norm = NameNormalizer()
        self.addr_norm = AddressNormalizer()
        self.extractor = TfidfFeatureExtractor()

    def test_identical_name_and_address(self):
        """Test that identical names and addresses achieve 1.0 cosine similarity."""
        n1 = self.name_norm.normalize("Apex Logistics Solutions")
        n2 = self.name_norm.normalize("Apex Logistics Solutions")
        a1 = self.addr_norm.normalize("123 Main St, New York, NY 10001")
        a2 = self.addr_norm.normalize("123 Main St, New York, NY 10001")

        feats = self.extractor.extract_features(n1, n2, a1, a2, tfidf_retrieval_score=0.95)

        self.assertAlmostEqual(feats["name_char_ngram_cosine"], 1.0, places=2)
        self.assertAlmostEqual(feats["address_char_ngram_cosine"], 1.0, places=2)
        self.assertEqual(feats["tfidf_retrieval_score"], 0.95)

    def test_typo_name_and_abbreviated_address(self):
        """Test character n-gram cosine tolerance on typos and address abbreviations."""
        n1 = self.name_norm.normalize("Walmart Supercenter")
        n2 = self.name_norm.normalize("Wal-Mart Supercntr")
        a1 = self.addr_norm.normalize("100 Main Street")
        a2 = self.addr_norm.normalize("100 Main St")

        feats = self.extractor.extract_features(n1, n2, a1, a2)

        self.assertGreater(feats["name_char_ngram_cosine"], 0.55)
        self.assertGreater(feats["address_char_ngram_cosine"], 0.85)

    def test_missing_address_handling(self):
        """Test that missing or nan addresses produce 0.0 without errors."""
        n1 = self.name_norm.normalize("Acme Supplies")
        n2 = self.name_norm.normalize("Acme Supplies")
        a1 = self.addr_norm.normalize("100 Main St")
        a2_missing = self.addr_norm.normalize("nan")

        feats = self.extractor.extract_features(n1, n2, a1, a2_missing)

        self.assertAlmostEqual(feats["name_char_ngram_cosine"], 1.0, places=2)
        self.assertEqual(feats["address_char_ngram_cosine"], 0.0)


if __name__ == "__main__":
    unittest.main()
