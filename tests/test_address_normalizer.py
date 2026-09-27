"""
Unit and adversarial tests for Phase 08: Address Normalization & Intelligence.
"""
import unittest
from pathlib import Path
import sys

_project_root = Path(__file__).resolve().parent.parent
_ber_src = _project_root / "code" / "business_entity_resolution" / "src"
if str(_ber_src) not in sys.path:
    sys.path.insert(0, str(_ber_src))

from ber.normalization.address_normalizer import (
    AddressNormalizer,
    NormalizedAddress,
    compare_numeric_evidence,
)


class TestAddressNormalizer(unittest.TestCase):
    def setUp(self):
        self.normalizer = AddressNormalizer()

    def test_abbreviation_standardization(self):
        """Test unifying street, suite, floor, road abbreviations."""
        addr = "123 Main Street, Suite 400, 2nd Floor"
        norm = self.normalizer.normalize(addr)
        self.assertEqual(norm.raw, addr)
        self.assertIn("st", norm.tokens)
        self.assertIn("ste", norm.tokens)
        self.assertIn("fl", norm.tokens)
        self.assertEqual(norm.numeric_tokens, ("123", "2", "400"))

    def test_indian_address_landmarks(self):
        """Test Indian address landmark and municipal terms."""
        addr = "Opposite City Hospital, Near Sector 14, Gandhi Nagar"
        norm = self.normalizer.normalize(addr)
        self.assertIn("opp", norm.tokens)
        self.assertIn("nr", norm.tokens)
        self.assertIn("sector", norm.tokens)
        self.assertIn("nagar", norm.tokens)
        self.assertEqual(norm.numeric_tokens, ("14",))

    def test_postal_code_extraction(self):
        """Test extraction of US, Indian, and French postal codes."""
        # US ZIP
        us_norm = self.normalizer.normalize("123 Main St, New York, NY 10001")
        self.assertEqual(us_norm.postal_code, "10001")

        # Indian PIN
        in_norm = self.normalizer.normalize("Plot 5, Whitefield, Bengaluru 560066")
        self.assertEqual(in_norm.postal_code, "560066")

        # French Postal Code
        fr_norm = self.normalizer.normalize("10 Rue de la Paix, 75002 Paris")
        self.assertEqual(fr_norm.postal_code, "75002")

    def test_numeric_evidence_comparison(self):
        """Test numeric token comparison and contradiction logic."""
        addr1 = self.normalizer.normalize("101 Main Street")
        addr2 = self.normalizer.normalize("101 Main St, Ste 5")
        addr3 = self.normalizer.normalize("105 Main Street")
        addr_no_num = self.normalizer.normalize("Main Street")

        # Same building number: match
        jaccard12, contra12 = compare_numeric_evidence(addr1, addr2)
        self.assertGreater(jaccard12, 0.0)
        self.assertFalse(contra12)

        # Different building number: contradiction!
        jaccard13, contra13 = compare_numeric_evidence(addr1, addr3)
        self.assertEqual(jaccard13, 0.0)
        self.assertTrue(contra13)

        # Missing number in one address: neutral, no contradiction
        jaccard_none, contra_none = compare_numeric_evidence(addr1, addr_no_num)
        self.assertEqual(jaccard_none, 0.0)
        self.assertFalse(contra_none)

    def test_empty_and_nan_address(self):
        """Test handling of empty, whitespace, and literal NaN addresses."""
        norm_none = self.normalizer.normalize(None)
        self.assertTrue(norm_none.is_empty)

        norm_nan = self.normalizer.normalize("nan")
        self.assertTrue(norm_nan.is_empty)

        norm_blank = self.normalizer.normalize("   ")
        self.assertTrue(norm_blank.is_empty)


if __name__ == "__main__":
    unittest.main()
