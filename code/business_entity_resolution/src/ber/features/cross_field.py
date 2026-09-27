"""
Cross-Field Feature Extraction Engine for ENTIVYRE.
Phase 20: Cross-field interaction indicators, joint name-address evidence,
country-name conflict detection, and composite similarity scoring.

Guarantees:
- Emits all 4 cross-field features defined in FeatureRegistry.
- Accurately captures high-confidence joint matches (name_and_address_high_sim).
- Flags subtle hard negatives: high name similarity with address numeric contradiction.
- Flags cross-border name collisions: exact name across contradictory countries.
- Computes unified overall_composite_similarity incorporating missingness adaptations.
- Pure-Python, zero external C-dependencies.
"""
from __future__ import annotations

from typing import Dict, Any


def extract_cross_field_features(
    name_features: Dict[str, float],
    address_features: Dict[str, float],
    country_features: Dict[str, float],
    tfidf_features: Dict[str, float],
) -> Dict[str, float]:
    """
    Compute cross-field interaction features from precomputed sub-feature dicts.
    """
    # 1. High Name & Address Joint Evidence
    # High name similarity: token jaccard >= 0.70 or canonical exact match
    name_jaccard = name_features.get("name_token_jaccard", 0.0)
    name_canon_exact = name_features.get("name_canonical_exact_match", 0.0)
    name_lev = name_features.get("name_levenshtein_sim", 0.0)
    is_name_high = (name_jaccard >= 0.70) or (name_canon_exact == 1.0) or (name_lev >= 0.85)

    addr_jaccard = address_features.get("address_token_jaccard", 0.0)
    addr_canon_exact = address_features.get("address_canonical_exact_match", 0.0)
    addr_lev = address_features.get("address_levenshtein_sim", 0.0)
    addr_missing = address_features.get("address_is_missing", 0.0)
    is_addr_high = (addr_missing == 0.0) and ((addr_jaccard >= 0.50) or (addr_canon_exact == 1.0) or (addr_lev >= 0.75))

    name_and_address_high_sim = 1.0 if (is_name_high and is_addr_high) else 0.0

    # 2. High Name match with Address Numeric Contradiction
    # (e.g., Same chain "Starbucks", different building/street number "101" vs "105")
    addr_contra = address_features.get("address_numeric_contradiction", 0.0)
    name_high_address_contradiction = 1.0 if (is_name_high and addr_contra == 1.0) else 0.0

    # 3. Exact Name across Conflicting Countries
    # (e.g., "Apple Inc" in US vs "Apple Inc" in India - distinct corporate entities)
    country_contra = country_features.get("country_contradiction", 0.0)
    name_exact = (
        name_features.get("name_exact_match", 0.0) == 1.0
        or name_features.get("name_clean_exact_match", 0.0) == 1.0
        or name_canon_exact == 1.0
    )
    name_exact_diff_country = 1.0 if (name_exact and country_contra == 1.0) else 0.0

    # 4. Overall Composite Similarity
    # Compute representative name score
    name_cosine = tfidf_features.get("name_char_ngram_cosine", 0.0)
    name_score = max(name_jaccard, name_lev, name_cosine)
    if name_canon_exact == 1.0:
        name_score = max(name_score, 0.95)
    if name_features.get("name_exact_match", 0.0) == 1.0:
        name_score = 1.0

    # Compute representative address score
    addr_cosine = tfidf_features.get("address_char_ngram_cosine", 0.0)
    addr_score = max(addr_jaccard, addr_lev, addr_cosine)
    if addr_canon_exact == 1.0:
        addr_score = max(addr_score, 0.95)
    if address_features.get("address_exact_match", 0.0) == 1.0:
        addr_score = 1.0

    # Compute country score
    if country_features.get("country_exact_match", 0.0) == 1.0:
        ctry_score = 1.0
    elif country_features.get("country_compatible", 0.0) == 1.0:
        ctry_score = 0.8  # Compatible due to missingness or open-set
    else:
        ctry_score = 0.0

    # Weighted combination depending on address presence
    if addr_missing == 1.0:
        # Address missing: weight shifts primarily to name
        raw_composite = (0.85 * name_score) + (0.15 * ctry_score)
    else:
        raw_composite = (0.55 * name_score) + (0.35 * addr_score) + (0.10 * ctry_score)

    # Penalties for contradictions
    if country_contra == 1.0:
        raw_composite *= 0.15  # Severe penalty for cross-country contradiction
    if addr_contra == 1.0:
        raw_composite *= 0.30  # Substantial penalty for numeric address contradiction

    overall_composite_similarity = max(0.0, min(1.0, round(raw_composite, 4)))

    return {
        "name_and_address_high_sim": name_and_address_high_sim,
        "name_high_address_contradiction": name_high_address_contradiction,
        "name_exact_diff_country": name_exact_diff_country,
        "overall_composite_similarity": overall_composite_similarity,
    }
