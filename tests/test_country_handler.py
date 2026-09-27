"""
Unit and adversarial tests for Phase 09: Country / Open-Set Handling.
"""
import unittest
from pathlib import Path
import sys

_project_root = Path(__file__).resolve().parent.parent
_ber_src = _project_root / "code" / "business_entity_resolution" / "src"
if str(_ber_src) not in sys.path:
    sys.path.insert(0, str(_ber_src))

from ber.normalization.country_handler import (
    CountryHandler,
    NormalizedCountry,
    CountryComparison,
)


class TestCountryHandler(unittest.TestCase):
    def setUp(self):
        self.handler = CountryHandler()

    def test_observed_train_countries(self):
        """Test normalization and observation status of training countries (US, India)."""
        # US aliases
        for variant in ["US", "USA", "United States", "united states of america", "U.S.A."]:
            norm = self.handler.normalize(variant)
            self.assertEqual(norm.canonical, "US")
            self.assertFalse(norm.is_missing)
            self.assertTrue(norm.is_observed_in_train)

        # India aliases
        for variant in ["India", "IN", "IND", "Bharat", "hindustan"]:
            norm = self.handler.normalize(variant)
            self.assertEqual(norm.canonical, "INDIA")
            self.assertFalse(norm.is_missing)
            self.assertTrue(norm.is_observed_in_train)

    def test_test_set_country_france(self):
        """Test that France (present in test set) is canonicalized and recognized as unobserved in train."""
        for variant in ["France", "FR", "fra", "République Française"]:
            norm = self.handler.normalize(variant)
            self.assertEqual(norm.canonical, "FRANCE")
            self.assertFalse(norm.is_missing)
            self.assertFalse(norm.is_observed_in_train)

    def test_novel_open_set_countries(self):
        """Test open-set guarantee: completely arbitrary country never crashes."""
        novel = self.handler.normalize("Brazil")
        self.assertEqual(novel.canonical, "BRAZIL")
        self.assertFalse(novel.is_observed_in_train)
        self.assertFalse(novel.is_missing)

        japan = self.handler.normalize("Japan")
        self.assertEqual(japan.canonical, "JAPAN")
        self.assertFalse(japan.is_observed_in_train)

    def test_empty_and_nan_countries(self):
        """Test handling of None, empty, whitespace, and literal NaN values."""
        for val in [None, "", "   ", "nan", "null", "None", "N/A"]:
            norm = self.handler.normalize(val)
            self.assertTrue(norm.is_missing)
            self.assertEqual(norm.canonical, "")
            self.assertFalse(norm.is_observed_in_train)

    def test_country_comparison_and_contradiction(self):
        """Test matching, contradiction, and unseen indicator logic."""
        us = self.handler.normalize("US")
        usa = self.handler.normalize("United States")
        india = self.handler.normalize("India")
        france = self.handler.normalize("France")
        missing = self.handler.normalize("nan")

        # 1. Exact match (both in train)
        cmp_us = self.handler.compare(us, usa)
        self.assertTrue(cmp_us.exact_match)
        self.assertTrue(cmp_us.compatible)
        self.assertFalse(cmp_us.contradiction)
        self.assertFalse(cmp_us.has_unseen_country)

        # 2. Hard contradiction (different countries)
        cmp_us_in = self.handler.compare(us, india)
        self.assertFalse(cmp_us_in.exact_match)
        self.assertFalse(cmp_us_in.compatible)
        self.assertTrue(cmp_us_in.contradiction)
        self.assertFalse(cmp_us_in.has_unseen_country)

        # 3. Exact match on open-set country (France)
        cmp_fr = self.handler.compare(france, france)
        self.assertTrue(cmp_fr.exact_match)
        self.assertTrue(cmp_fr.compatible)
        self.assertFalse(cmp_fr.contradiction)
        self.assertTrue(cmp_fr.has_unseen_country)

        # 4. Missing value compatibility
        cmp_missing = self.handler.compare(us, missing)
        self.assertFalse(cmp_missing.exact_match)
        self.assertTrue(cmp_missing.compatible)
        self.assertFalse(cmp_missing.contradiction)
        self.assertTrue(cmp_missing.candidate_missing)

    def test_features_dict(self):
        """Test ML feature vector generation."""
        us = self.handler.normalize("US")
        india = self.handler.normalize("India")
        cmp_obj = self.handler.compare(us, india)
        feats = cmp_obj.to_feature_dict()

        self.assertEqual(feats["country_exact_match"], 0.0)
        self.assertEqual(feats["country_compatible"], 0.0)
        self.assertEqual(feats["country_contradiction"], 1.0)
        self.assertEqual(feats["has_unseen_country"], 0.0)


if __name__ == "__main__":
    unittest.main()
