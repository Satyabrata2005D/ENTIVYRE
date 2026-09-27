"""
Unit and adversarial tests for Phase 17: Similarity Features.
"""
import unittest
from pathlib import Path
import sys

_project_root = Path(__file__).resolve().parent.parent
_ber_src = _project_root / "code" / "business_entity_resolution" / "src"
if str(_ber_src) not in sys.path:
    sys.path.insert(0, str(_ber_src))

from ber.features.similarity import (
    token_jaccard,
    token_overlap_count,
    token_containment,
    levenshtein_distance,
    normalized_levenshtein_similarity,
    length_ratio,
    extract_name_similarity_features,
)
from ber.normalization.name_normalizer import NameNormalizer


class TestSimilarityFeatures(unittest.TestCase):
    def setUp(self):
        self.normalizer = NameNormalizer()

    def test_token_jaccard_and_overlap(self):
        """Test token Jaccard similarity and overlap count."""
        t1 = ["apex", "logistics", "hub"]
        t2 = ["hub", "apex", "services"]

        jaccard = token_jaccard(t1, t2)
        overlap = token_overlap_count(t1, t2)

        # 2 shared tokens out of 4 distinct ("apex", "hub") / ("apex", "hub", "logistics", "services")
        self.assertAlmostEqual(jaccard, 0.5, places=4)
        self.assertEqual(overlap, 2.0)

        # Disjoint
        self.assertEqual(token_jaccard(["apple"], ["banana"]), 0.0)
        self.assertEqual(token_overlap_count(["apple"], ["banana"]), 0.0)

        # Empty
        self.assertEqual(token_jaccard([], ["test"]), 0.0)
        self.assertEqual(token_jaccard([], []), 0.0)

    def test_token_containment(self):
        """Test asymmetric token containment."""
        t1 = ["apex"]
        t2 = ["apex", "logistics", "international"]
        self.assertEqual(token_containment(t1, t2), 1.0)
        self.assertEqual(token_containment(t2, t1), 1.0)
        self.assertEqual(token_containment(["apple"], ["banana"]), 0.0)
        self.assertEqual(token_containment([], []), 0.0)

    def test_levenshtein_distance_and_similarity(self):
        """Test Levenshtein distance and normalized similarity."""
        # Identical
        self.assertEqual(levenshtein_distance("walmart", "walmart"), 0)
        self.assertEqual(normalized_levenshtein_similarity("walmart", "walmart"), 1.0)

        # 1 substitution
        self.assertEqual(levenshtein_distance("starbucks", "starbuckz"), 1)
        self.assertAlmostEqual(normalized_levenshtein_similarity("starbucks", "starbuckz"), 8 / 9, places=3)

        # 1 insertion / deletion
        self.assertEqual(levenshtein_distance("amazon", "amazons"), 1)
        self.assertAlmostEqual(normalized_levenshtein_similarity("amazon", "amazons"), 6 / 7, places=3)

        # Completely disjoint
        self.assertEqual(levenshtein_distance("abc", "xyz"), 3)
        self.assertEqual(normalized_levenshtein_similarity("abc", "xyz"), 0.0)

        # Empty strings
        self.assertEqual(levenshtein_distance("", "test"), 4)
        self.assertEqual(normalized_levenshtein_similarity("", "test"), 0.0)
        self.assertEqual(normalized_levenshtein_similarity("", ""), 1.0)

    def test_length_ratio(self):
        """Test length ratio calculation."""
        self.assertEqual(length_ratio("cat", "cats"), 0.75)
        self.assertEqual(length_ratio("same", "same"), 1.0)
        self.assertEqual(length_ratio("", "test"), 0.0)
        self.assertEqual(length_ratio("", ""), 1.0)

    def test_extract_name_similarity_features(self):
        """Test full name similarity feature extraction against FeatureRegistry schema."""
        n1 = self.normalizer.normalize("Acme 77 Logistics Inc")
        n2 = self.normalizer.normalize("Acme 77 Logistics Corp")
        n3 = self.normalizer.normalize("Beta 88 Transport")

        feats12 = extract_name_similarity_features(n1, n2)

        # Raw names differ ("Inc" vs "Corp")
        self.assertEqual(feats12["name_exact_match"], 0.0)
        # Canonical roots match ("acme 77 logistics")
        self.assertEqual(feats12["name_canonical_exact_match"], 1.0)
        self.assertEqual(feats12["name_token_jaccard"], 1.0)
        self.assertEqual(feats12["name_levenshtein_sim"], 1.0)
        self.assertEqual(feats12["name_length_ratio"], 1.0)
        self.assertEqual(feats12["name_numeric_overlap"], 1.0)  # "77" matches

        feats13 = extract_name_similarity_features(n1, n3)
        self.assertEqual(feats13["name_exact_match"], 0.0)
        self.assertEqual(feats13["name_canonical_exact_match"], 0.0)
        self.assertEqual(feats13["name_token_jaccard"], 0.0)
        self.assertEqual(feats13["name_numeric_overlap"], 0.0)  # "77" vs "88"


if __name__ == "__main__":
    unittest.main()
