"""
Comprehensive Adversarial Stress and Robustness Test Suite for ENTIVYRE.
Phase 37: Edge cases, adversarial attacks, extreme lengths, Unicode, and malformed inputs.
"""
import unittest

from ber.normalization.name_normalizer import NameNormalizer
from ber.normalization.address_normalizer import AddressNormalizer
from ber.normalization.country_handler import CountryHandler
from ber.retrieval.tfidf_retriever import SparseCharTfidfRetriever
from ber.features.pipeline import FeatureExtractionPipeline
from ber.models.deterministic_baseline import DeterministicBaseline
from ber.decision.matcher import EntityMatcher


class TestRobustnessStress(unittest.TestCase):

    def setUp(self):
        self.name_norm = NameNormalizer()
        self.addr_norm = AddressNormalizer()
        self.country_handler = CountryHandler()
        self.pipeline = FeatureExtractionPipeline()
        self.baseline = DeterministicBaseline()
        self.matcher = EntityMatcher()

    def test_extreme_input_lengths(self):
        """Pipeline must handle massive string lengths without stack overflow or catastrophic slowdown."""
        massive_name = "Mega Corp " * 1000  # 10,000 characters
        massive_addr = "123 Long Infinite Highway Boulevard Suite 999 " * 500

        norm_name = self.name_norm.normalize(massive_name)
        norm_addr = self.addr_norm.normalize(massive_addr)

        self.assertGreater(len(norm_name.canonical), 0)
        self.assertGreater(len(norm_addr.canonical), 0)

        # Vectorization should complete safely and output finite numbers
        e1 = {"name": massive_name, "address": massive_addr, "country": "US"}
        e2 = {"name": massive_name, "address": massive_addr, "country": "US"}

        vec = self.pipeline.extract_vector(e1, e2)
        self.assertEqual(len(vec), 33)
        self.assertTrue(all(isinstance(v, float) and not (v != v) for v in vec))

    def test_bizarre_unicode_and_emojis(self):
        """Handle emojis, non-Latin scripts, zero-width joiners, and control characters gracefully."""
        bizarre_name = "☕ Café ✨ Parisien 🚀 & Sons \u200b\u200d (SARL)"
        bizarre_addr = "10 Rue de la Paix 🇫🇷 \t\r\n 75002 Paris"

        norm_name = self.name_norm.normalize(bizarre_name)
        norm_addr = self.addr_norm.normalize(bizarre_addr)

        self.assertIn("cafe", norm_name.canonical)
        self.assertIn("parisien", norm_name.canonical)
        self.assertIn("rue de la paix", norm_addr.canonical)
        self.assertEqual(norm_name.legal_suffix, "sarl")

    def test_empty_none_and_whitespace_inputs(self):
        """Pipeline must never crash on None, empty strings, or pure whitespace."""
        inputs = [None, "", "   ", "\t\t\n\n", "None", "null", "NaN", "undefined"]
        for inp in inputs:
            norm_name = self.name_norm.normalize(inp)
            norm_addr = self.addr_norm.normalize(inp)
            norm_ctry = self.country_handler.normalize(inp)

            self.assertIsInstance(norm_name.canonical, str)
            self.assertIsInstance(norm_addr.canonical, str)
            self.assertIsInstance(norm_ctry.canonical, str)

        e1 = {"name": "", "address": None, "country": None}
        e2 = {"name": "   ", "address": "", "country": "null"}

        vec = self.pipeline.extract_vector(e1, e2)
        self.assertEqual(len(vec), 33)
        # Check no NaNs
        for i, val in enumerate(vec):
            self.assertFalse(val != val, f"Feature index {i} produced NaN on empty entity")

    def test_severe_ocr_noise_and_punctuation_abuse(self):
        """Handle extreme punctuation and character substitutions."""
        name1 = "Wal-Mart #1021 -- Store & Pharmacy!!"
        name2 = "Walmart Store and Pharmacy Inc"

        norm1 = self.name_norm.normalize(name1)
        norm2 = self.name_norm.normalize(name2)

        self.assertIn("pharmacy", norm1.canonical)
        self.assertIn("pharmacy", norm2.canonical)

        retriever = SparseCharTfidfRetriever(ngram_size=3)
        retriever.fit_and_index([("S2-WMT", norm2.canonical)])
        results = retriever.retrieve_top_k(norm1.canonical, k=5, min_similarity=0.3)
        self.assertTrue(any(r.target_id == "S2-WMT" for r in results))

    def test_hard_negative_adjacent_store_contradiction(self):
        """Ensure adjacent stores on same street with different numbers are never merged."""
        store1 = {"name": "Target Store", "address": "101 North Main Street", "country": "US"}
        store2 = {"name": "Target Store", "address": "105 North Main Street", "country": "US"}

        feats = self.pipeline.extract_features(store1, store2)
        self.assertEqual(feats["address_numeric_contradiction"], 1.0)
        self.assertEqual(feats["name_high_address_contradiction"], 1.0)

        # Baseline must reject with contradiction
        decision = self.baseline.classify_pair(feats, target_id="S2-STORE2")
        self.assertFalse(decision.is_match)
        self.assertEqual(decision.rule_name, "REJECT_ADDRESS_NUMERIC_CONTRADICTION")

    def test_cross_country_brand_collision(self):
        """Ensure multinational brand with identical name in conflicting countries is rejected."""
        us_brand = {"name": "Himalaya Wellness", "address": "100 Technology Dr", "country": "US"}
        in_brand = {"name": "Himalaya Wellness", "address": "100 Technology Dr", "country": "India"}

        feats = self.pipeline.extract_features(us_brand, in_brand)
        self.assertEqual(feats["country_contradiction"], 1.0)
        self.assertEqual(feats["name_exact_diff_country"], 1.0)

        decision = self.baseline.classify_pair(feats, target_id="S2-BRAND")
        self.assertFalse(decision.is_match)
        self.assertEqual(decision.rule_name, "REJECT_COUNTRY_CONTRADICTION")

    def test_unseen_open_set_country_resilience(self):
        """Novel countries (e.g. France, Germany, Japan) must not trigger contradiction if identical."""
        e1 = {"name": "Boulangerie Paul", "address": "5 Place de la Bastille", "country": "France"}
        e2 = {"name": "Boulangerie Paul SARL", "address": "5 Pl. de la Bastille", "country": "FRANCE"}

        feats = self.pipeline.extract_features(e1, e2)
        self.assertEqual(feats["country_contradiction"], 0.0)
        self.assertEqual(feats["country_exact_match"], 1.0)
        self.assertEqual(feats["has_unseen_country"], 1.0)

        decision = self.baseline.classify_pair(feats, target_id="S2-FR2")
        self.assertTrue(decision.is_match)


if __name__ == "__main__":
    unittest.main()
