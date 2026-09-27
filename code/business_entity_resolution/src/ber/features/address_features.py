"""
Address-Specific Feature Extraction Engine for ENTIVYRE.
Phase 19: Address token overlap, Levenshtein distance, postal code matching,
numeric token evidence, and numeric contradiction indicators.

Guarantees:
- Extracts all 10 address features defined in FeatureRegistry.
- Accurately detects numeric building/plot contradictions (hard negative indicator).
- Resilient to missing/NaN addresses (sets address_is_missing=1.0 and zeros similarities).
- Pure-Python, zero external C-dependencies.
"""
from __future__ import annotations

from typing import Dict, Iterable, Optional, Set, Tuple, Any

from ber.normalization.address_normalizer import (
    NormalizedAddress,
    compare_numeric_evidence,
)
from ber.features.similarity import (
    token_jaccard,
    token_overlap_count,
    normalized_levenshtein_similarity,
)


def extract_address_features(
    anchor: NormalizedAddress,
    candidate: NormalizedAddress,
) -> Dict[str, float]:
    """
    Extract all Address features defined in the FeatureRegistry.
    """
    # 1. Missingness handling
    if anchor.is_empty or candidate.is_empty:
        return {
            "address_exact_match": 0.0,
            "address_clean_exact_match": 0.0,
            "address_canonical_exact_match": 0.0,
            "address_token_jaccard": 0.0,
            "address_token_overlap_count": 0.0,
            "address_levenshtein_sim": 0.0,
            "address_numeric_jaccard": 0.0,
            "address_numeric_contradiction": 0.0,
            "address_postal_code_match": 0.0,
            "address_is_missing": 1.0,
        }

    # 2. Exact match indicators
    exact_raw = 1.0 if (anchor.raw and candidate.raw and anchor.raw == candidate.raw) else 0.0
    exact_clean = 1.0 if (anchor.clean and candidate.clean and anchor.clean == candidate.clean) else 0.0
    exact_canon = 1.0 if (anchor.canonical and candidate.canonical and anchor.canonical == candidate.canonical) else 0.0

    # 3. Token similarity
    jaccard = token_jaccard(anchor.tokens, candidate.tokens)
    overlap = token_overlap_count(anchor.tokens, candidate.tokens)

    # 4. Levenshtein edit similarity on canonical addresses
    lev_sim = normalized_levenshtein_similarity(anchor.canonical, candidate.canonical)

    # 5. Numeric evidence and contradiction
    num_jaccard, has_contra = compare_numeric_evidence(anchor, candidate)

    # 6. Postal code match
    postal_match = 0.0
    if anchor.postal_code and candidate.postal_code:
        if anchor.postal_code == candidate.postal_code:
            postal_match = 1.0

    return {
        "address_exact_match": exact_raw,
        "address_clean_exact_match": exact_clean,
        "address_canonical_exact_match": exact_canon,
        "address_token_jaccard": round(jaccard, 4),
        "address_token_overlap_count": overlap,
        "address_levenshtein_sim": round(lev_sim, 4),
        "address_numeric_jaccard": round(num_jaccard, 4),
        "address_numeric_contradiction": 1.0 if has_contra else 0.0,
        "address_postal_code_match": postal_match,
        "address_is_missing": 0.0,
    }
