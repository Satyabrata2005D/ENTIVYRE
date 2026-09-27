"""
Address Normalization and Address Intelligence Engine for ENTIVYRE.
Phase 08: Numbers, Abbreviations, Landmarks, Postal Codes, and Component Isolation.

Guarantees:
- Multi-tier representations: RAW, CLEAN, CANONICAL, TOKENS, and NUMERICS.
- Zero mutation of raw text.
- Standardized road/street/building abbreviations (US, India, France).
- Extraction of numeric evidence (house/plot/building numbers, ZIP/PIN codes).
- Postal code isolation (5-digit US/FR, 6-digit Indian PIN).
- Landmark extraction ('near', 'opposite', 'behind').
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Tuple, Set, Any

from ber.normalization.transliteration import transliterate_devanagari

NON_ALPHANUM_REGEX = re.compile(r"[^a-z0-9\s]")
WHITESPACE_REGEX = re.compile(r"\s+")
ORDINAL_REGEX = re.compile(r"\b(\d+)(?:st|nd|rd|th)\b")
DIGIT_TOKEN_REGEX = re.compile(r"\b\d+\b")

# Regex for postal codes: 5-digit (US / France) or 6-digit (India PIN)
POSTAL_CODE_REGEX = re.compile(r"\b([1-9][0-9]{5}|[0-9]{5}(?:-[0-9]{4})?)\b")

# Standard address keyword mappings
ADDRESS_KEYWORD_MAP: Dict[str, str] = {
    # Thoroughfare
    "road": "rd", "rd": "rd",
    "street": "st", "st": "st", "str": "st",
    "avenue": "ave", "ave": "ave", "av": "ave",
    "boulevard": "blvd", "blvd": "blvd", "bd": "blvd",
    "lane": "ln", "ln": "ln",
    "drive": "dr", "dr": "dr",
    "court": "ct", "ct": "ct",
    "place": "pl", "pl": "pl",
    "square": "sq", "sq": "sq",
    "highway": "hwy", "hwy": "hwy",
    "expressway": "expy", "expy": "expy",
    "parkway": "pkwy", "pkwy": "pkwy",
    "route": "rt", "rt": "rt",
    "circle": "cir", "cir": "cir",
    # French thoroughfare
    "rue": "rue", "chemin": "ch", "ch": "ch", "allee": "all", "all": "all", "avenue": "ave",
    "impasse": "imp", "imp": "imp", "passage": "pas", "pas": "pas",
    "cours": "crs", "crs": "crs", "quai": "quai", "zi": "zi",
    # Sub-units & Municipal
    "suite": "ste", "ste": "ste",
    "apartment": "apt", "apt": "apt",
    "floor": "fl", "fl": "fl", "flr": "fl",
    "building": "bldg", "bldg": "bldg",
    "room": "rm", "rm": "rm",
    "department": "dept", "dept": "dept",
    # Indian municipal & landmarks
    "nagar": "nagar", "ngr": "nagar",
    "marg": "marg", "mrg": "marg",
    "sector": "sector", "sec": "sector",
    "colony": "colony",
    "chowk": "chowk",
    "bazaar": "bazar", "bazar": "bazar",
    "opposite": "opp", "opp": "opp",
    "near": "nr", "nr": "nr",
    "behind": "behind",
    "beside": "beside",
    "cross": "cross",
    # Cardinals
    "north": "n", "south": "s", "east": "e", "west": "w",
}

# Sorted keyword substitution regex
KW_PATTERNS = sorted(ADDRESS_KEYWORD_MAP.keys(), key=len, reverse=True)
ADDRESS_KW_REGEX = re.compile(r"\b(" + "|".join(re.escape(k) for k in KW_PATTERNS) + r")\b", re.IGNORECASE)


@dataclass(frozen=True)
class NormalizedAddress:
    """Structured representation of an address."""
    raw: str
    clean: str
    canonical: str
    tokens: Tuple[str, ...]
    tokens_sorted: Tuple[str, ...]
    numeric_tokens: Tuple[str, ...]
    postal_code: Optional[str]
    is_empty: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @property
    def token_set(self) -> Set[str]:
        return set(self.tokens)

    @property
    def numeric_set(self) -> Set[str]:
        return set(self.numeric_tokens)


class AddressNormalizer:
    """Production address normalization and intelligence engine."""

    def __init__(self, strip_accents: bool = True, transliterate: bool = True):
        self.strip_accents = strip_accents
        self.transliterate = transliterate

    def normalize(self, raw_address: Optional[str]) -> NormalizedAddress:
        if raw_address is None:
            raw_str = ""
        else:
            raw_str = str(raw_address).strip()

        if not raw_str or raw_str.lower() in {"nan", "null", "none", "n/a", "undefined"}:
            return NormalizedAddress(
                raw=raw_str,
                clean="",
                canonical="",
                tokens=(),
                tokens_sorted=(),
                numeric_tokens=(),
                postal_code=None,
                is_empty=True,
            )

        text = raw_str

        # 1. Transliterate Devanagari if present
        if self.transliterate:
            text, _ = transliterate_devanagari(text)

        # 2. Unicode NFKD & accent stripping
        if self.strip_accents:
            decomposed = unicodedata.normalize("NFKD", text)
            text = "".join(c for c in decomposed if not unicodedata.combining(c))

        text_lower = text.lower()

        # 3. Extract postal code before removing punctuation
        postal_match = POSTAL_CODE_REGEX.search(text_lower)
        postal_code: Optional[str] = postal_match.group(1) if postal_match else None

        # 4. Clean punctuation and standardize ordinals (e.g. 2nd -> 2)
        clean_text = NON_ALPHANUM_REGEX.sub(" ", text_lower)
        clean_text = ORDINAL_REGEX.sub(r"\1", clean_text)
        clean_text = WHITESPACE_REGEX.sub(" ", clean_text).strip()

        # 5. Standardize address keywords
        def replace_kw(match: re.Match) -> str:
            kw = match.group(1).lower()
            return ADDRESS_KEYWORD_MAP.get(kw, kw)

        canonical_text = ADDRESS_KW_REGEX.sub(replace_kw, clean_text)
        canonical_text = WHITESPACE_REGEX.sub(" ", canonical_text).strip()

        # 6. Extract tokens and numeric evidence (with leading zeros stripped on numbers)
        raw_toks = tuple(t for t in canonical_text.split() if t)
        all_tokens = tuple(t.lstrip('0') or '0' if t.isdigit() and len(t) <= 6 else t for t in raw_toks)
        sorted_tokens = tuple(sorted(set(all_tokens)))
        numeric_tokens = tuple(sorted(set(t.lstrip('0') or '0' for t in DIGIT_TOKEN_REGEX.findall(canonical_text) if len(t) <= 6)))

        return NormalizedAddress(
            raw=raw_str,
            clean=clean_text,
            canonical=canonical_text,
            tokens=all_tokens,
            tokens_sorted=sorted_tokens,
            numeric_tokens=numeric_tokens,
            postal_code=postal_code,
            is_empty=False,
        )


def compare_numeric_evidence(addr1: NormalizedAddress, addr2: NormalizedAddress) -> Tuple[float, bool]:
    """
    Compares numeric tokens between two addresses.
    Returns (numeric_jaccard_similarity, has_numeric_contradiction).
    
    If both have numbers but disjoint numbers (e.g. 101 vs 105), contradiction is True.
    """
    if addr1.is_empty or addr2.is_empty:
        return 0.0, False

    nums1 = addr1.numeric_set
    nums2 = addr2.numeric_set

    if not nums1 or not nums2:
        return 0.0, False

    intersection = nums1 & nums2
    union = nums1 | nums2
    jaccard = len(intersection) / len(union) if union else 0.0

    # Isolate street/building numbers by excluding postal codes if present
    street_nums1 = nums1 - ({addr1.postal_code} if addr1.postal_code else set())
    street_nums2 = nums2 - ({addr2.postal_code} if addr2.postal_code else set())

    if street_nums1 and street_nums2:
        contradiction = (len(street_nums1 & street_nums2) == 0)
    else:
        contradiction = (len(intersection) == 0) and (len(nums1) > 0 and len(nums2) > 0)

    return jaccard, contradiction
