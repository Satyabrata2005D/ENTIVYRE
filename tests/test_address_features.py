"""
Unit and adversarial tests for Phase 19: Address-Specific Features.
"""
import unittest
from pathlib import Path
import sys

_project_root = Path(__file__).resolve().parent.parent
_ber_src = _project_root / "code" / "business_entity_resolution" / "src"
if str(_ber_src) not in sys.path:
    sys.path.insert(0, str(_ber_src))

from ber.features.address_features import extract_address_features
from ber.normalization.address_normalizer import AddressNormalizer


class TestAddressFeatures(unittest.TestCase):
    def setUp(self):
        self.normalizer = AddressNormalizer()

    def test_canonical_address_match(self):
        """Test abbreviation canonicalization and token matching."""
        a1 = self.normalizer.normalize("123 Main Street, Suite 400")
        a2 = self.normalizer.normalize("123 Main St, Ste 400")

        feats = extract_address_features(a1, a2)

        self.assertEqual(feats["address_exact_match"], 0.0)
        self.assertEqual(feats["address_canonical_exact_match"], 1.0)
        self.assertEqual(feats["address_token_jaccard"], 1.0)
        self.assertEqual(feats["address_numeric_contradiction"], 0.0)
        self.assertEqual(feats["address_is_missing"], 0.0)

    def test_numeric_building_contradiction(self):
        """Test hard contradiction when house/building numbers diverge."""
        a1 = self.normalizer.normalize("101 Main Street")
        a2 = self.normalizer.normalize("105 Main Street")

        feats = extract_address_features(a1, a2)

        self.assertEqual(feats["address_numeric_contradiction"], 1.0)
        self.assertEqual(feats["address_numeric_jaccard"], 0.0)
        self.assertGreater(feats["address_token_jaccard"], 0.4)  # Shared street tokens

    def test_postal_code_matching(self):
        """Test postal code match feature across matching and non-matching PINs."""
        a1 = self.normalizer.normalize("Plot 5, Whitefield, Bengaluru 560066")
        a2 = self.normalizer.normalize("Plot 5, Whitefield 560066")
        a3 = self.normalizer.normalize("Plot 5, Whitefield 560001")

        feats_match = extract_address_features(a1, a2)
        self.assertEqual(feats_match["address_postal_code_match"], 1.0)

        feats_mismatch = extract_address_features(a1, a3)
        self.assertEqual(feats_mismatch["address_postal_code_match"], 0.0)

    def test_missing_and_nan_address(self):
        """Test missingness flag and neutral contradiction on missing addresses."""
        a1 = self.normalizer.normalize("123 Main St")
        a_none = self.normalizer.normalize(None)
        a_nan = self.normalizer.normalize("nan")

        feats_none = extract_address_features(a1, a_none)
        self.assertEqual(feats_none["address_is_missing"], 1.0)
        self.assertEqual(feats_none["address_numeric_contradiction"], 0.0)
        self.assertEqual(feats_none["address_token_jaccard"], 0.0)

        feats_nan = extract_address_features(a1, a_nan)
        self.assertEqual(feats_nan["address_is_missing"], 1.0)


if __name__ == "__main__":
    unittest.main()
