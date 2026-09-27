"""
Unit and adversarial tests for Phase 07: Business Name Normalization.
"""
import unittest
from pathlib import Path
import sys

_project_root = Path(__file__).resolve().parent.parent
_ber_src = _project_root / "code" / "business_entity_resolution" / "src"
if str(_ber_src) not in sys.path:
    sys.path.insert(0, str(_ber_src))

from ber.normalization.name_normalizer import (
    NameNormalizer,
    NormalizedName,
    compute_char_ngrams,
)


class TestNameNormalizer(unittest.TestCase):
    def setUp(self):
        self.normalizer = NameNormalizer()

    def test_standard_legal_suffix_removal(self):
        """Test stripping legal suffixes and extracting canonical root."""
        res = self.normalizer.normalize("Acme Corporation")
        self.assertEqual(res.raw, "Acme Corporation")
        self.assertEqual(res.clean, "acme corporation")
        self.assertEqual(res.canonical, "acme")
        self.assertEqual(res.legal_suffix, "corp")
        self.assertEqual(res.tokens, ("acme",))

    def test_indian_pvt_ltd_variations(self):
        """Test variations of Private Limited."""
        names = [
            "Reliance Industries Private Limited",
            "Reliance Industries Pvt. Ltd.",
            "Reliance Industries Pvt Ltd",
            "Reliance Industries Limited",
        ]
        canonicals = [self.normalizer.normalize(n).canonical for n in names]
        # All should resolve to 'reliance industries'
        for c in canonicals:
            self.assertEqual(c, "reliance")

    def test_word_order_invariance(self):
        """Test word-order invariant token sorting."""
        res1 = self.normalizer.normalize("Tata Motors Global")
        res2 = self.normalizer.normalize("Global Motors Tata")
        self.assertEqual(res1.tokens_sorted, res2.tokens_sorted)
        self.assertEqual(res1.tokens_sorted, ("global", "motors", "tata"))

    def test_devanagari_transliteration(self):
        """Test transliteration of Hindi business names."""
        res = self.normalizer.normalize("श्री गणेश एंटरप्राइजेज")
        self.assertTrue(res.has_transliteration)
        self.assertIn("shri", res.clean)
        self.assertIn("ganesh", res.clean)

    def test_url_and_noise_stripping(self):
        """Test stripping embedded web URLs and phone numbers."""
        res = self.normalizer.normalize("Acme Corp http://www.acme-corp.com +1-800-555-1234")
        self.assertTrue(res.has_url_stripped)
        self.assertEqual(res.canonical, "acme")
        self.assertNotIn("http", res.clean)
        self.assertNotIn("1234", res.clean)

    def test_accent_stripping(self):
        """Test French diacritic decomposition."""
        res = self.normalizer.normalize("Café Société SARL")
        self.assertEqual(res.clean, "cafe societe sarl")
        self.assertEqual(res.canonical, "cafe societe")
        self.assertEqual(res.legal_suffix, "sarl")

    def test_adversarial_empty_and_whitespace(self):
        """Test handling of None, empty strings, and whitespace."""
        res_none = self.normalizer.normalize(None)
        self.assertEqual(res_none.canonical, "")
        self.assertEqual(res_none.tokens, ())

        res_empty = self.normalizer.normalize("   ")
        self.assertEqual(res_empty.canonical, "")

    def test_compute_char_ngrams(self):
        """Test generating character n-grams."""
        ngrams = compute_char_ngrams("acme", n=3)
        self.assertIn("#ac", ngrams)
        self.assertIn("acm", ngrams)
        self.assertIn("cme", ngrams)
        self.assertIn("me#", ngrams)


if __name__ == "__main__":
    unittest.main()
