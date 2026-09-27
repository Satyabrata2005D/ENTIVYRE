"""
Unit and Integration Tests for Phase 20: Cross-Field Features & Feature Extraction Pipeline.
"""
import unittest

from ber.normalization.name_normalizer import NameNormalizer
from ber.normalization.address_normalizer import AddressNormalizer
from ber.normalization.country_handler import CountryHandler
from ber.features.registry import build_default_feature_registry
from ber.features.cross_field import extract_cross_field_features
from ber.features.pipeline import FeatureExtractionPipeline


class TestCrossFieldFeatures(unittest.TestCase):
    def setUp(self):
        self.registry = build_default_feature_registry()
        self.pipeline = FeatureExtractionPipeline(registry=self.registry)

    def test_name_and_address_high_sim(self):
        anchor = {
            "name": "Acme Industrial Corporation",
            "address": "100 Innovation Way, Suite 400, Chicago, IL 60601",
            "country": "US",
        }
        candidate = {
            "name": "Acme Industrial Corp",
            "address": "100 Innovation Way, Ste 400, Chicago, IL 60601",
            "country": "US",
        }
        meta = {
            "in_standard_blocker": True,
            "in_tfidf_retriever": True,
            "tfidf_retrieval_score": 0.95,
        }

        features = self.pipeline.extract_features(anchor, candidate, meta)
        self.assertEqual(features["name_and_address_high_sim"], 1.0)
        self.assertEqual(features["name_high_address_contradiction"], 0.0)
        self.assertEqual(features["name_exact_diff_country"], 0.0)
        self.assertGreater(features["overall_composite_similarity"], 0.90)

    def test_name_high_address_contradiction_hard_negative(self):
        # Same chain name, but different house numbers -> Hard negative
        anchor = {
            "name": "Starbucks Coffee",
            "address": "101 Broadway Avenue, New York, NY 10001",
            "country": "US",
        }
        candidate = {
            "name": "Starbucks Coffee",
            "address": "105 Broadway Avenue, New York, NY 10001",
            "country": "US",
        }

        features = self.pipeline.extract_features(anchor, candidate)
        self.assertEqual(features["address_numeric_contradiction"], 1.0)
        self.assertEqual(features["name_high_address_contradiction"], 1.0)
        # Composite score must be heavily penalized
        self.assertLess(features["overall_composite_similarity"], 0.50)

    def test_name_exact_diff_country_collision(self):
        # Exact same name across conflicting countries
        anchor = {
            "name": "Reliance Retail Limited",
            "address": "Maker Chambers IV, Nariman Point, Mumbai 400021",
            "country": "India",
        }
        candidate = {
            "name": "Reliance Retail Limited",
            "address": "500 5th Avenue, New York, NY 10110",
            "country": "US",
        }

        features = self.pipeline.extract_features(anchor, candidate)
        self.assertEqual(features["country_contradiction"], 1.0)
        self.assertEqual(features["name_exact_diff_country"], 1.0)
        self.assertLess(features["overall_composite_similarity"], 0.30)

    def test_missing_address_adaptation(self):
        anchor = {
            "name": "Blue Dart Express",
            "address": "Plot 12, Andheri East, Mumbai 400069",
            "country": "India",
        }
        candidate = {
            "name": "Blue Dart Express Ltd",
            "address": "",  # Missing address in scraped source
            "country": "India",
        }

        features = self.pipeline.extract_features(anchor, candidate)
        self.assertEqual(features["address_is_missing"], 1.0)
        self.assertGreater(features["overall_composite_similarity"], 0.70)

    def test_full_pipeline_vectorization(self):
        anchor = {
            "name": "Baskin Robbins",
            "address": "123 Main Street",
            "country": "US",
        }
        candidate = {
            "name": "Baskin-Robbins Ice Cream",
            "address": "123 Main St",
            "country": "US",
        }
        meta = {
            "in_standard_blocker": True,
            "in_tfidf_retriever": False,
            "tfidf_retrieval_score": 0.0,
        }

        features = self.pipeline.extract_features(anchor, candidate, meta)
        # Check all 33 features exist
        self.assertEqual(len(features), 33)
        for name in self.registry.feature_names:
            self.assertIn(name, features)

        # Check vectorize produces strictly ordered vector of length 33
        vector = self.pipeline.extract_vector(anchor, candidate, meta)
        self.assertEqual(len(vector), 33)
        self.assertIsInstance(vector, list)
        for val in vector:
            self.assertIsInstance(val, float)
            self.assertFalse(val != val)  # No NaNs


if __name__ == "__main__":
    unittest.main()
