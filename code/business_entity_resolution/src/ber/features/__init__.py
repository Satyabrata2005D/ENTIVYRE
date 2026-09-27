"""
BER Features subpackage.
"""
from ber.features.registry import (
    FeatureDefinition,
    FeatureRegistry,
    build_default_feature_registry,
)
from ber.features.similarity import (
    token_jaccard,
    token_overlap_count,
    token_containment,
    levenshtein_distance,
    normalized_levenshtein_similarity,
    length_ratio,
    extract_name_similarity_features,
)
from ber.features.tfidf_features import TfidfFeatureExtractor
from ber.features.address_features import extract_address_features
from ber.features.cross_field import extract_cross_field_features
from ber.features.pipeline import FeatureExtractionPipeline

__all__ = [
    "FeatureDefinition",
    "FeatureRegistry",
    "build_default_feature_registry",
    "token_jaccard",
    "token_overlap_count",
    "token_containment",
    "levenshtein_distance",
    "normalized_levenshtein_similarity",
    "length_ratio",
    "extract_name_similarity_features",
    "TfidfFeatureExtractor",
    "extract_address_features",
    "extract_cross_field_features",
    "FeatureExtractionPipeline",
]
