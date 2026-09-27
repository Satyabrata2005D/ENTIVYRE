"""
Unit and adversarial tests for Phase 16: Feature Registry.
"""
import tempfile
import unittest
from pathlib import Path
import sys

_project_root = Path(__file__).resolve().parent.parent
_ber_src = _project_root / "code" / "business_entity_resolution" / "src"
if str(_ber_src) not in sys.path:
    sys.path.insert(0, str(_ber_src))

from ber.features.registry import (
    FeatureDefinition,
    FeatureRegistry,
    build_default_feature_registry,
)


class TestFeatureRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = build_default_feature_registry()

    def test_default_registry_features(self):
        """Test that default registry contains all 33 production features across 5 groups."""
        self.assertEqual(len(self.registry), 33)
        self.assertEqual(len(self.registry.feature_names), 33)

        name_feats = self.registry.get_features_by_group("name")
        self.assertEqual(len(name_feats), 10)

        addr_feats = self.registry.get_features_by_group("address")
        self.assertEqual(len(addr_feats), 11)

        ctry_feats = self.registry.get_features_by_group("country")
        self.assertEqual(len(ctry_feats), 4)

        cross_feats = self.registry.get_features_by_group("cross_field")
        self.assertEqual(len(cross_feats), 4)

        retrieval_feats = self.registry.get_features_by_group("retrieval")
        self.assertEqual(len(retrieval_feats), 4)

    def test_unique_name_constraint(self):
        """Test that registering duplicate feature name raises ValueError."""
        dup = FeatureDefinition(
            name="name_exact_match",
            group="name",
            dtype="float32",
            description="Duplicate definition",
            missing_value=0.0,
            provenance="test",
        )
        with self.assertRaises(ValueError):
            self.registry.register(dup)

    def test_unknown_feature_lookup(self):
        """Test lookup of unregistered feature raises KeyError."""
        with self.assertRaises(KeyError):
            self.registry.get("non_existent_feature_123")

    def test_vectorize_with_missing_and_nan(self):
        """Test vectorization contract and graceful imputation of missing/NaN values."""
        # Partial dictionary missing several keys and containing NaN
        partial_dict = {
            "name_exact_match": 1.0,
            "name_token_jaccard": 0.85,
            "country_compatible": 1.0,
            "address_token_jaccard": float("nan"),  # NaN should be imputed
            "address_is_missing": "invalid_string", # Invalid string should be imputed
        }

        vec = self.registry.vectorize(partial_dict)
        self.assertEqual(len(vec), 33)

        # Verified values
        name_exact_idx = self.registry.feature_names.index("name_exact_match")
        self.assertEqual(vec[name_exact_idx], 1.0)

        name_jaccard_idx = self.registry.feature_names.index("name_token_jaccard")
        self.assertEqual(vec[name_jaccard_idx], 0.85)

        # Imputed NaN
        addr_jaccard_idx = self.registry.feature_names.index("address_token_jaccard")
        self.assertEqual(vec[addr_jaccard_idx], 0.0)  # default missing_value for address_token_jaccard

        # Imputed missing key
        ngram_cosine_idx = self.registry.feature_names.index("name_char_ngram_cosine")
        self.assertEqual(vec[ngram_cosine_idx], 0.0)  # default missing_value

    def test_schema_save_and_load(self):
        """Test JSON persistence and reconstruction roundtrip."""
        with tempfile.TemporaryDirectory() as tmpdir:
            out_file = Path(tmpdir) / "test_feature_schema.json"
            saved_path = self.registry.save_schema(out_file)
            self.assertTrue(saved_path.exists())

            loaded = FeatureRegistry.from_schema_file(out_file)
            self.assertEqual(len(loaded), len(self.registry))
            self.assertEqual(loaded.feature_names, self.registry.feature_names)


if __name__ == "__main__":
    unittest.main()
