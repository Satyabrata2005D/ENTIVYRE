"""
Business Name Normalization Engine for ENTIVYRE.
Phase 07: Raw / Canonical / Token / Character Representations.

Guarantees:
- Multi-tier representations: RAW, CLEAN, CANONICAL, TOKENS, and N-GRAMS.
- Zero mutation of raw text.
- Devanagari-to-Latin transliteration.
- URL, domain, and web noise stripping.
- Legal suffix detection and canonical root extraction.
- Word-order invariant tokenization.
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Tuple, Set, Any

from ber.normalization.transliteration import transliterate_devanagari

# Compiled Regexes
URL_PROTOCOL_REGEX = re.compile(r"https?://(?:www\.)?|www\.", re.IGNORECASE)
TLD_SUFFIX_REGEX = re.compile(r"\.(?:com|org|net|in|fr|co|io|biz|info|gov|edu)(?:/[^\s]*)?\b", re.IGNORECASE)
HONORIFIC_PREFIX_REGEX = re.compile(r"^(?:m\s*/?\s*s\.?|shri|sri|smt|dr\.?|er\.?|late)\s+", re.IGNORECASE)
PHONE_REGEX = re.compile(r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b|\b\d{10}\b")
NON_ALPHANUM_REGEX = re.compile(r"[^a-z0-9\s]")
WHITESPACE_REGEX = re.compile(r"\s+")

# Legal suffix normalization map (standardized replacement)
LEGAL_SUFFIX_MAP: Dict[str, str] = {
    "private limited": "pvt ltd",
    "pvt limited": "pvt ltd",
    "pvt ltd": "pvt ltd",
    "pvtltd": "pvt ltd",
    "p limited": "pvt ltd",
    "limited": "ltd",
    "ltd": "ltd",
    "incorporated": "inc",
    "inc": "inc",
    "corporation": "corp",
    "corp": "corp",
    "limited liability company": "llc",
    "llc": "llc",
    "l l c": "llc",
    "company": "co",
    "co": "co",
    "sarl": "sarl",
    "s a r l": "sarl",
    "sa": "sa",
    "s a": "sa",
    "gmbh": "gmbh",
    "enterprise": "enterprises",
    "enterprises": "enterprises",
    "associates": "associates",
    "industries": "industries",
    "solutions": "solutions",
    "services": "services",
    "technologies": "technologies",
    "private": "pvt",
    "pvt": "pvt",
    "llp": "llp",
    "l l p": "llp",
    "public limited": "ltd",
    "plc": "ltd",
    "p l c": "ltd",
    "proprietorship": "prop",
    "prop": "prop",
}

# Regex for matching legal suffixes at word boundaries
SUFFIX_PATTERNS = sorted(LEGAL_SUFFIX_MAP.keys(), key=len, reverse=True)
LEGAL_SUFFIX_REGEX = re.compile(
    r"\b(" + "|".join(re.escape(k) for k in SUFFIX_PATTERNS) + r")\b",
    re.IGNORECASE
)


@dataclass(frozen=True)
class NormalizedName:
    """Multi-tier representation of a business name."""
    raw: str
    clean: str
    canonical: str
    tokens: Tuple[str, ...]
    tokens_sorted: Tuple[str, ...]
    legal_suffix: Optional[str]
    has_transliteration: bool
    has_url_stripped: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @property
    def token_set(self) -> Set[str]:
        return set(self.tokens)


class NameNormalizer:
    """Production-grade conservative business name normalizer."""

    def __init__(
        self,
        strip_noise: bool = True,
        transliterate: bool = True,
        strip_accents: bool = True,
    ):
        self.strip_noise = strip_noise
        self.transliterate = transliterate
        self.strip_accents = strip_accents

    def normalize(self, raw_name: Optional[str]) -> NormalizedName:
        """
        Normalizes raw business name into structured representation.
        Always preserves raw input verbatim.
        """
        if raw_name is None:
            raw_str = ""
        else:
            raw_str = str(raw_name).strip()

        if not raw_str:
            return NormalizedName(
                raw=raw_str,
                clean="",
                canonical="",
                tokens=(),
                tokens_sorted=(),
                legal_suffix=None,
                has_transliteration=False,
                has_url_stripped=False,
            )

        text = raw_str

        # 1. Devanagari transliteration if present
        has_trans = False
        if self.transliterate:
            text, has_trans = transliterate_devanagari(text)

        # 2. Unicode normalization (NFKD) and accent stripping
        if self.strip_accents:
            decomposed = unicodedata.normalize("NFKD", text)
            text = "".join(c for c in decomposed if not unicodedata.combining(c))

        text_lower = text.lower()

        # 3. URL and phone noise stripping with domain unmasking
        has_url = False
        if self.strip_noise:
            if URL_PROTOCOL_REGEX.search(text_lower) or TLD_SUFFIX_REGEX.search(text_lower):
                has_url = True
                text_lower = URL_PROTOCOL_REGEX.sub(" ", text_lower)
                text_lower = TLD_SUFFIX_REGEX.sub(" ", text_lower)
                text_lower = text_lower.replace(".", " ").replace("-", " ").replace("/", " ").replace("_", " ")
            text_lower = PHONE_REGEX.sub(" ", text_lower)

        # 4. Clean punctuation to whitespace
        clean_text = NON_ALPHANUM_REGEX.sub(" ", text_lower)
        clean_text = WHITESPACE_REGEX.sub(" ", clean_text).strip()

        # 4b. Strip leading honorific prefix (e.g. M/s, Shri, Sri, Smt, Dr)
        if HONORIFIC_PREFIX_REGEX.search(clean_text):
            sub_h = HONORIFIC_PREFIX_REGEX.sub("", clean_text).strip()
            if sub_h and len(sub_h.split()) >= 1:
                clean_text = sub_h

        # 5. Extract legal suffix and build canonical root
        detected_suffix: Optional[str] = None
        canonical_text = clean_text

        # Find suffix tokens
        suffix_matches = LEGAL_SUFFIX_REGEX.findall(clean_text)
        if suffix_matches:
            # Pick longest matched suffix
            raw_suf = max(suffix_matches, key=len).lower()
            detected_suffix = LEGAL_SUFFIX_MAP.get(raw_suf, raw_suf)
            # Remove suffix from canonical representation
            sub_canonical = LEGAL_SUFFIX_REGEX.sub(" ", clean_text)
            sub_canonical = WHITESPACE_REGEX.sub(" ", sub_canonical).strip()
            # Guard against completely removing the name if name is only a suffix
            if sub_canonical:
                canonical_text = sub_canonical

        # 6. Tokenize canonical root
        raw_tokens = tuple(t for t in canonical_text.split() if t)
        sorted_tokens = tuple(sorted(set(raw_tokens)))

        return NormalizedName(
            raw=raw_str,
            clean=clean_text,
            canonical=canonical_text,
            tokens=raw_tokens,
            tokens_sorted=sorted_tokens,
            legal_suffix=detected_suffix,
            has_transliteration=has_trans,
            has_url_stripped=has_url,
        )


def compute_char_ngrams(text: str, n: int = 3) -> Tuple[str, ...]:
    """Generates character n-grams from normalized text."""
    if not text:
        return ()
    padded = f"#{text}#"
    if len(padded) < n:
        return (padded,)
    return tuple(padded[i : i + n] for i in range(len(padded) - n + 1))
