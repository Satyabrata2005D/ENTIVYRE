"""
Central Feature Registry for ENTIVYRE.
Phase 16: Immutable feature schemas, stable column names, missing-value contracts,
provenance tracking, and typed feature vector serialization.

Guarantees:
- Every feature has a unique stable column name, documented description, and fallback default.
- Strict ordering preservation for feature vectors passed to ML models.
- Graceful imputation of missing or NaN feature values via explicit missing_value contracts.
- Exportable schema manifest for traceability and clean-room reproducibility.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple, Any

from entivyre.utils.logger import get_logger

logger = get_logger("ber.features.registry", stage="16_feature_registry")


@dataclass(frozen=True)
class FeatureDefinition:
    """Immutable specification for a single machine learning feature."""
    name: str
    group: str  # "name", "address", "country", "cross_field", "retrieval"
    dtype: str  # "float32", "int32"
    description: str
    missing_value: float
    provenance: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class FeatureRegistry:
    """
    Central registry governing all feature definitions across ENTIVYRE.
    Ensures stable feature indices, schema validation, and missing-value guarantees.
    """

    def __init__(self):
        self._features: Dict[str, FeatureDefinition] = {}
        self._ordered_names: List[str] = []

    def __len__(self) -> int:
        return len(self._features)

    def __contains__(self, name: str) -> bool:
        return name in self._features

    @property
    def feature_names(self) -> List[str]:
        """Ordered list of registered feature names."""
        return list(self._ordered_names)

    @property
    def total_features(self) -> int:
        return len(self._features)

    def register(self, feature: FeatureDefinition) -> None:
        """Register a new feature definition."""
        if feature.name in self._features:
            raise ValueError(f"Feature '{feature.name}' is already registered in FeatureRegistry")
        self._features[feature.name] = feature
        self._ordered_names.append(feature.name)

    def register_many(self, features: Iterable[FeatureDefinition]) -> None:
        """Batch registration of feature definitions."""
        for f in features:
            self.register(f)

    def get(self, name: str) -> FeatureDefinition:
        """Retrieve a registered feature definition."""
        feat = self._features.get(name)
        if feat is None:
            raise KeyError(f"Feature '{name}' not found in FeatureRegistry")
        return feat

    def get_features_by_group(self, group: str) -> List[FeatureDefinition]:
        """Retrieve all features belonging to a specific group."""
        return [f for f in self._features.values() if f.group == group]

    def vectorize(self, feature_dict: Dict[str, Any]) -> List[float]:
        """
        Convert a feature dictionary into a strictly ordered float vector.
        Missing or non-numeric keys are replaced by the feature's defined missing_value.
        """
        vector: List[float] = []
        for name in self._ordered_names:
            feat_def = self._features[name]
            val = feature_dict.get(name)
            if val is None:
                vector.append(feat_def.missing_value)
            else:
                try:
                    f_val = float(val)
                    # Check for float NaN
                    if f_val != f_val:  # NaN check
                        vector.append(feat_def.missing_value)
                    else:
                        vector.append(f_val)
                except (ValueError, TypeError):
                    vector.append(feat_def.missing_value)
        return vector

    def to_schema_dict(self) -> Dict[str, Any]:
        """Serializes the registry schema to a dictionary."""
        return {
            "total_features": len(self._features),
            "feature_names": self._ordered_names,
            "features": [self._features[name].to_dict() for name in self._ordered_names],
        }

    def save_schema(self, output_path: Path) -> Path:
        """Persist registry schema to JSON."""
        p = Path(output_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(self.to_schema_dict(), f, indent=2)
        logger.info(
            f"Saved FeatureRegistry schema with {len(self)} features to {p}",
            extra={"payload": {"total_features": len(self), "path": str(p)}},
        )
        return p

    @classmethod
    def from_schema_file(cls, schema_path: Path) -> FeatureRegistry:
        """Load registry from a persisted JSON schema file."""
        p = Path(schema_path)
        if not p.exists():
            raise FileNotFoundError(f"Schema file not found: {p}")
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
        registry = cls()
        for f_data in data.get("features", []):
            feat = FeatureDefinition(**f_data)
            registry.register(feat)
        return registry


def build_default_feature_registry() -> FeatureRegistry:
    """
    Constructs the canonical ENTIVYRE FeatureRegistry containing all 33 production
    features spanning Name, Address, Country, Cross-Field, and Retrieval evidence.
    """
    reg = FeatureRegistry()

    # 1. NAME FEATURES (Phase 17, 18)
    name_feats = [
        FeatureDefinition(
            name="name_exact_match",
            group="name",
            dtype="float32",
            description="Binary indicator if raw business names are strictly identical.",
            missing_value=0.0,
            provenance="ber.normalization.name_normalizer",
        ),
        FeatureDefinition(
            name="name_clean_exact_match",
            group="name",
            dtype="float32",
            description="Binary indicator if cleaned business names are identical.",
            missing_value=0.0,
            provenance="ber.normalization.name_normalizer",
        ),
        FeatureDefinition(
            name="name_canonical_exact_match",
            group="name",
            dtype="float32",
            description="Binary indicator if canonicalized business roots are identical.",
            missing_value=0.0,
            provenance="ber.normalization.name_normalizer",
        ),
        FeatureDefinition(
            name="name_token_jaccard",
            group="name",
            dtype="float32",
            description="Jaccard similarity between unique business name token sets.",
            missing_value=0.0,
            provenance="ber.features.similarity",
        ),
        FeatureDefinition(
            name="name_token_overlap_count",
            group="name",
            dtype="float32",
            description="Count of shared distinct tokens between business names.",
            missing_value=0.0,
            provenance="ber.features.similarity",
        ),
        FeatureDefinition(
            name="name_token_containment",
            group="name",
            dtype="float32",
            description="Fraction of shorter name tokens contained in longer name.",
            missing_value=0.0,
            provenance="ber.features.similarity",
        ),
        FeatureDefinition(
            name="name_char_ngram_cosine",
            group="name",
            dtype="float32",
            description="Character 3-gram TF-IDF cosine similarity between names.",
            missing_value=0.0,
            provenance="ber.retrieval.tfidf_retriever",
        ),
        FeatureDefinition(
            name="name_levenshtein_sim",
            group="name",
            dtype="float32",
            description="Normalized Levenshtein edit similarity between canonical names.",
            missing_value=0.0,
            provenance="ber.features.similarity",
        ),
        FeatureDefinition(
            name="name_length_ratio",
            group="name",
            dtype="float32",
            description="Ratio of shorter canonical name length to longer name length.",
            missing_value=0.0,
            provenance="ber.features.similarity",
        ),
        FeatureDefinition(
            name="name_numeric_overlap",
            group="name",
            dtype="float32",
            description="Jaccard overlap of numbers occurring inside business names.",
            missing_value=0.0,
            provenance="ber.features.similarity",
        ),
    ]

    # 2. ADDRESS FEATURES (Phase 19)
    addr_feats = [
        FeatureDefinition(
            name="address_exact_match",
            group="address",
            dtype="float32",
            description="Binary indicator if raw addresses are strictly identical.",
            missing_value=0.0,
            provenance="ber.normalization.address_normalizer",
        ),
        FeatureDefinition(
            name="address_clean_exact_match",
            group="address",
            dtype="float32",
            description="Binary indicator if cleaned addresses are identical.",
            missing_value=0.0,
            provenance="ber.normalization.address_normalizer",
        ),
        FeatureDefinition(
            name="address_canonical_exact_match",
            group="address",
            dtype="float32",
            description="Binary indicator if standardized canonical addresses are identical.",
            missing_value=0.0,
            provenance="ber.normalization.address_normalizer",
        ),
        FeatureDefinition(
            name="address_token_jaccard",
            group="address",
            dtype="float32",
            description="Jaccard similarity between address token sets.",
            missing_value=0.0,
            provenance="ber.features.similarity",
        ),
        FeatureDefinition(
            name="address_token_overlap_count",
            group="address",
            dtype="float32",
            description="Count of shared distinct tokens between addresses.",
            missing_value=0.0,
            provenance="ber.features.similarity",
        ),
        FeatureDefinition(
            name="address_char_ngram_cosine",
            group="address",
            dtype="float32",
            description="Character 3-gram TF-IDF cosine similarity between addresses.",
            missing_value=0.0,
            provenance="ber.retrieval.tfidf_retriever",
        ),
        FeatureDefinition(
            name="address_levenshtein_sim",
            group="address",
            dtype="float32",
            description="Normalized Levenshtein edit similarity between canonical addresses.",
            missing_value=0.0,
            provenance="ber.features.similarity",
        ),
        FeatureDefinition(
            name="address_numeric_jaccard",
            group="address",
            dtype="float32",
            description="Jaccard similarity between numeric tokens in addresses (house/plot numbers).",
            missing_value=0.0,
            provenance="ber.normalization.address_normalizer",
        ),
        FeatureDefinition(
            name="address_numeric_contradiction",
            group="address",
            dtype="float32",
            description="Binary indicator: 1.0 if both addresses specify numbers but share 0 overlap.",
            missing_value=0.0,
            provenance="ber.normalization.address_normalizer",
        ),
        FeatureDefinition(
            name="address_postal_code_match",
            group="address",
            dtype="float32",
            description="Binary indicator: 1.0 if both postal/PIN codes match, 0.0 otherwise.",
            missing_value=0.0,
            provenance="ber.normalization.address_normalizer",
        ),
        FeatureDefinition(
            name="address_is_missing",
            group="address",
            dtype="float32",
            description="Binary indicator: 1.0 if either anchor or candidate address is missing.",
            missing_value=1.0,
            provenance="ber.normalization.address_normalizer",
        ),
    ]

    # 3. COUNTRY FEATURES (Phase 09 / Phase 20)
    ctry_feats = [
        FeatureDefinition(
            name="country_exact_match",
            group="country",
            dtype="float32",
            description="Binary indicator: 1.0 if canonical country matches.",
            missing_value=0.0,
            provenance="ber.normalization.country_handler",
        ),
        FeatureDefinition(
            name="country_compatible",
            group="country",
            dtype="float32",
            description="Binary indicator: 1.0 if countries match or either is missing.",
            missing_value=1.0,
            provenance="ber.normalization.country_handler",
        ),
        FeatureDefinition(
            name="country_contradiction",
            group="country",
            dtype="float32",
            description="Binary indicator: 1.0 if both countries present but non-matching.",
            missing_value=0.0,
            provenance="ber.normalization.country_handler",
        ),
        FeatureDefinition(
            name="has_unseen_country",
            group="country",
            dtype="float32",
            description="Binary indicator: 1.0 if either country was not observed in training.",
            missing_value=0.0,
            provenance="ber.normalization.country_handler",
        ),
    ]

    # 4. CROSS-FIELD FEATURES (Phase 20)
    cross_feats = [
        FeatureDefinition(
            name="name_and_address_high_sim",
            group="cross_field",
            dtype="float32",
            description="Binary composite: name_jaccard >= 0.70 AND address_jaccard >= 0.50.",
            missing_value=0.0,
            provenance="ber.features.cross_field",
        ),
        FeatureDefinition(
            name="name_high_address_contradiction",
            group="cross_field",
            dtype="float32",
            description="Binary composite: high name match with address numeric contradiction.",
            missing_value=0.0,
            provenance="ber.features.cross_field",
        ),
        FeatureDefinition(
            name="name_exact_diff_country",
            group="cross_field",
            dtype="float32",
            description="Binary contradiction: exact name match across conflicting countries.",
            missing_value=0.0,
            provenance="ber.features.cross_field",
        ),
        FeatureDefinition(
            name="overall_composite_similarity",
            group="cross_field",
            dtype="float32",
            description="Weighted linear harmonic mean of name, address, and country scores.",
            missing_value=0.0,
            provenance="ber.features.cross_field",
        ),
    ]

    # 5. RETRIEVAL PROVENANCE FEATURES (Phase 14)
    retrieval_feats = [
        FeatureDefinition(
            name="in_standard_blocker",
            group="retrieval",
            dtype="float32",
            description="Binary indicator if pair was retrieved by standard inverted index.",
            missing_value=0.0,
            provenance="ber.blocking.candidate_generator",
        ),
        FeatureDefinition(
            name="in_tfidf_retriever",
            group="retrieval",
            dtype="float32",
            description="Binary indicator if pair was retrieved by TF-IDF retriever.",
            missing_value=0.0,
            provenance="ber.blocking.candidate_generator",
        ),
        FeatureDefinition(
            name="in_both_retrieval_passes",
            group="retrieval",
            dtype="float32",
            description="Binary indicator if pair was captured in both retrieval passes.",
            missing_value=0.0,
            provenance="ber.blocking.candidate_generator",
        ),
        FeatureDefinition(
            name="tfidf_retrieval_score",
            group="retrieval",
            dtype="float32",
            description="Cosine similarity score from TF-IDF retrieval (0.0 if not in pass).",
            missing_value=0.0,
            provenance="ber.retrieval.tfidf_retriever",
        ),
    ]

    reg.register_many(name_feats)
    reg.register_many(addr_feats)
    reg.register_many(ctry_feats)
    reg.register_many(cross_feats)
    reg.register_many(retrieval_feats)

    return reg

