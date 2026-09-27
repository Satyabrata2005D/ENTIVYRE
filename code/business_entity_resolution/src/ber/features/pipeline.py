"""
End-to-End Feature Extraction Pipeline for ENTIVYRE.
Phase 20: Unified feature extraction orchestrator extracting all 33 registered
features across Name, Address, Country, Cross-Field, and Retrieval evidence.

Guarantees:
- Produces complete, strongly-typed feature dictionaries matching FeatureRegistry schema.
- Vectorizes dictionaries into deterministic, strictly ordered float vectors.
- Handles raw entity records, normalized objects, or individual field strings.
- Gracefully manages missing fields, NaN values, and open-set countries.
- High-throughput pure-Python implementation with zero external C-dependencies.
"""
from __future__ import annotations

from typing import Dict, List, Optional, Any, Union

from ber.normalization.name_normalizer import NameNormalizer, NormalizedName
from ber.normalization.address_normalizer import AddressNormalizer, NormalizedAddress
from ber.normalization.country_handler import CountryHandler, NormalizedCountry, CountryComparison
from ber.features.registry import FeatureRegistry, build_default_feature_registry
from ber.features.similarity import extract_name_similarity_features
from ber.features.address_features import extract_address_features
from ber.features.tfidf_features import TfidfFeatureExtractor
from ber.features.cross_field import extract_cross_field_features


class FeatureExtractionPipeline:
    """
    Unified production feature extractor coordinating all 5 feature groups:
    Name (10), Address (11), Country (4), Cross-Field (4), Retrieval (4) = 33 features.
    """

    def __init__(
        self,
        registry: Optional[FeatureRegistry] = None,
        name_normalizer: Optional[NameNormalizer] = None,
        address_normalizer: Optional[AddressNormalizer] = None,
        country_handler: Optional[CountryHandler] = None,
        tfidf_extractor: Optional[TfidfFeatureExtractor] = None,
    ):
        self.registry = registry or build_default_feature_registry()
        self.name_normalizer = name_normalizer or NameNormalizer()
        self.address_normalizer = address_normalizer or AddressNormalizer()
        self.country_handler = country_handler or CountryHandler()
        self.tfidf_extractor = tfidf_extractor or TfidfFeatureExtractor()

    def _ensure_normalized_components(
        self,
        entity: Any,
    ) -> tuple[NormalizedName, NormalizedAddress, NormalizedCountry]:
        """
        Extract or normalize (NormalizedName, NormalizedAddress, NormalizedCountry)
        from either an object with .name, .address, .country or a dict or tuple.
        """
        if isinstance(entity, tuple) and len(entity) == 3:
            name_val, addr_val, ctry_val = entity
        elif isinstance(entity, dict):
            name_val = entity.get("name", "")
            addr_val = entity.get("address", "")
            ctry_val = entity.get("country", "")
        else:
            name_val = getattr(entity, "name", "")
            addr_val = getattr(entity, "address", "")
            ctry_val = getattr(entity, "country", "")

        # Normalize if not already normalized
        norm_name = (
            name_val if isinstance(name_val, NormalizedName)
            else self.name_normalizer.normalize(name_val)
        )
        norm_addr = (
            addr_val if isinstance(addr_val, NormalizedAddress)
            else self.address_normalizer.normalize(addr_val)
        )
        norm_ctry = (
            ctry_val if isinstance(ctry_val, NormalizedCountry)
            else self.country_handler.normalize(ctry_val)
        )

        return norm_name, norm_addr, norm_ctry

    def extract_features(
        self,
        anchor: Any,
        candidate: Any,
        retrieval_meta: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, float]:
        """
        Extract all 33 features for a single (anchor, candidate) pair.
        """
        meta = retrieval_meta or {}

        # 1. Normalize representations
        a_name, a_addr, a_ctry = self._ensure_normalized_components(anchor)
        c_name, c_addr, c_ctry = self._ensure_normalized_components(candidate)

        # 2. Name similarity features (Phase 17)
        name_feats = extract_name_similarity_features(a_name, c_name)

        # 3. Address similarity features (Phase 19)
        addr_feats = extract_address_features(a_addr, c_addr)

        # 4. Country features (Phase 09)
        ctry_comp = self.country_handler.compare(a_ctry, c_ctry)
        ctry_feats = {
            "country_exact_match": 1.0 if ctry_comp.exact_match else 0.0,
            "country_compatible": 1.0 if ctry_comp.compatible else 0.0,
            "country_contradiction": 1.0 if ctry_comp.contradiction else 0.0,
            "has_unseen_country": 1.0 if ctry_comp.has_unseen_country else 0.0,
        }

        # 5. TF-IDF character n-gram features (Phase 18)
        retrieval_tfidf_score = float(meta.get("tfidf_retrieval_score", 0.0))
        tfidf_feats = self.tfidf_extractor.extract_features(
            anchor_name=a_name,
            candidate_name=c_name,
            anchor_addr=a_addr,
            candidate_addr=c_addr,
            tfidf_retrieval_score=retrieval_tfidf_score,
        )

        # 6. Cross-field interaction features (Phase 20)
        cross_feats = extract_cross_field_features(
            name_features=name_feats,
            address_features=addr_feats,
            country_features=ctry_feats,
            tfidf_features=tfidf_feats,
        )

        # 7. Retrieval provenance features (Phase 14)
        in_std = 1.0 if meta.get("in_standard_blocker", False) else 0.0
        in_tfidf = 1.0 if meta.get("in_tfidf_retriever", False) else 0.0
        in_both = 1.0 if (meta.get("in_both_retrieval_passes", False) or (in_std == 1.0 and in_tfidf == 1.0)) else 0.0

        retrieval_feats = {
            "in_standard_blocker": in_std,
            "in_tfidf_retriever": in_tfidf,
            "in_both_retrieval_passes": in_both,
            "tfidf_retrieval_score": retrieval_tfidf_score,
        }

        # Combine all groups
        all_features: Dict[str, float] = {}
        all_features.update(name_feats)
        all_features.update(addr_feats)
        all_features.update(ctry_feats)
        all_features.update(cross_feats)
        all_features.update(retrieval_feats)

        # Ensure name_char_ngram_cosine and address_char_ngram_cosine are passed through
        all_features["name_char_ngram_cosine"] = tfidf_feats["name_char_ngram_cosine"]
        all_features["address_char_ngram_cosine"] = tfidf_feats["address_char_ngram_cosine"]

        return all_features

    def extract_vector(
        self,
        anchor: Any,
        candidate: Any,
        retrieval_meta: Optional[Dict[str, Any]] = None,
    ) -> List[float]:
        """
        Extract all 33 features and vectorize to ordered float vector strictly matching
        the FeatureRegistry schema.
        """
        feat_dict = self.extract_features(anchor, candidate, retrieval_meta)
        return self.registry.vectorize(feat_dict)
