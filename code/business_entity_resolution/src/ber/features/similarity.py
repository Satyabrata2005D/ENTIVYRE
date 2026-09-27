"""
Core String Similarity and Distance Computation Engine for ENTIVYRE.
Phase 17: Token Jaccard, Token Containment, Levenshtein Edit Distance,
Length Ratios, and Name Similarity Feature Extraction.

Guarantees:
- Pure-Python, zero C-extension dependencies.
- Memory-bounded Levenshtein implementation with O(min(M, N)) space.
- Exact arithmetic: outputs bounded in [0.0, 1.0].
- Safe handling of empty, whitespace, and single-character strings.
- Direct alignment with FeatureRegistry column contracts.
"""
from __future__ import annotations

from typing import Dict, Iterable, Optional, Set, Tuple, Any
from ber.normalization.name_normalizer import NormalizedName


def token_jaccard(tokens1: Iterable[str], tokens2: Iterable[str]) -> float:
    """Compute Jaccard similarity between two token collections."""
    set1 = set(tokens1)
    set2 = set(tokens2)
    if not set1 or not set2:
        return 0.0
    intersection = set1 & set2
    union = set1 | set2
    return len(intersection) / len(union) if union else 0.0


def token_overlap_count(tokens1: Iterable[str], tokens2: Iterable[str]) -> float:
    """Compute count of shared distinct tokens."""
    set1 = set(tokens1)
    set2 = set(tokens2)
    return float(len(set1 & set2))


def token_containment(tokens1: Iterable[str], tokens2: Iterable[str]) -> float:
    """
    Compute fraction of tokens from the shorter token set contained in the longer token set.
    """
    set1 = set(tokens1)
    set2 = set(tokens2)
    if not set1 or not set2:
        return 0.0
    min_len = min(len(set1), len(set2))
    if min_len == 0:
        return 0.0
    intersection = set1 & set2
    return len(intersection) / min_len


def levenshtein_distance(s1: str, s2: str, max_dist: Optional[int] = None) -> int:
    """
    Compute Levenshtein edit distance with O(min(M, N)) space complexity.
    """
    if s1 == s2:
        return 0
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)

    # Ensure s1 is the shorter string to minimize row allocation
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    len1 = len(s1)
    len2 = len(s2)

    # Early exit if length difference already exceeds max_dist
    if max_dist is not None and abs(len1 - len2) > max_dist:
        return max_dist + 1

    previous_row = list(range(len1 + 1))
    current_row = [0] * (len1 + 1)

    for j, c2 in enumerate(s2, 1):
        current_row[0] = j
        min_in_row = current_row[0]

        for i, c1 in enumerate(s1, 1):
            cost = 0 if c1 == c2 else 1
            current_row[i] = min(
                previous_row[i] + 1,      # deletion
                current_row[i - 1] + 1,   # insertion
                previous_row[i - 1] + cost # substitution
            )
            if current_row[i] < min_in_row:
                min_in_row = current_row[i]

        if max_dist is not None and min_in_row > max_dist:
            return max_dist + 1

        previous_row, current_row = current_row, previous_row

    return previous_row[len1]


def normalized_levenshtein_similarity(s1: str, s2: str) -> float:
    """
    Compute normalized Levenshtein similarity in [0.0, 1.0].
    similarity = 1.0 - (levenshtein_distance / max_len)
    """
    if not s1 and not s2:
        return 1.0
    if not s1 or not s2:
        return 0.0
    if s1 == s2:
        return 1.0

    max_len = max(len(s1), len(s2))
    if max_len == 0:
        return 1.0

    dist = levenshtein_distance(s1, s2)
    return max(0.0, min(1.0, 1.0 - (dist / max_len)))


def length_ratio(s1: str, s2: str) -> float:
    """Compute ratio of shorter string length to longer string length in [0.0, 1.0]."""
    if not s1 and not s2:
        return 1.0
    if not s1 or not s2:
        return 0.0
    len1 = len(s1)
    len2 = len(s2)
    max_len = max(len1, len2)
    min_len = min(len1, len2)
    return min_len / max_len if max_len > 0 else 0.0


def extract_name_similarity_features(
    anchor: NormalizedName,
    candidate: NormalizedName,
) -> Dict[str, float]:
    """
    Extract all Name Similarity features defined in the FeatureRegistry.
    """
    # Exact match flags
    raw_exact = 1.0 if (anchor.raw and candidate.raw and anchor.raw == candidate.raw) else 0.0
    clean_exact = 1.0 if (anchor.clean and candidate.clean and anchor.clean == candidate.clean) else 0.0
    canon_exact = 1.0 if (anchor.canonical and candidate.canonical and anchor.canonical == candidate.canonical) else 0.0

    # Token overlap metrics
    jaccard = token_jaccard(anchor.tokens, candidate.tokens)
    overlap = token_overlap_count(anchor.tokens, candidate.tokens)
    containment = token_containment(anchor.tokens, candidate.tokens)

    # Edit distance and length ratio on canonical name roots
    lev_sim = normalized_levenshtein_similarity(anchor.canonical, candidate.canonical)
    len_rat = length_ratio(anchor.canonical, candidate.canonical)

    # Numbers in names
    nums_anchor = {t for t in anchor.tokens if t.isdigit()}
    nums_cand = {t for t in candidate.tokens if t.isdigit()}
    if nums_anchor and nums_cand:
        num_overlap = len(nums_anchor & nums_cand) / len(nums_anchor | nums_cand)
    elif not nums_anchor and not nums_cand:
        num_overlap = 0.0
    else:
        num_overlap = 0.0

    return {
        "name_exact_match": raw_exact,
        "name_clean_exact_match": clean_exact,
        "name_canonical_exact_match": canon_exact,
        "name_token_jaccard": round(jaccard, 4),
        "name_token_overlap_count": overlap,
        "name_token_containment": round(containment, 4),
        "name_levenshtein_sim": round(lev_sim, 4),
        "name_length_ratio": round(len_rat, 4),
        "name_numeric_overlap": round(num_overlap, 4),
    }
