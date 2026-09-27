"""
Open-Set Country Normalization and Compatibility Handler for ENTIVYRE.
Phase 09: Open-set country standardization, alias resolution, compatibility,
and unseen-country feature engineering.

Guarantees:
- Never crashes or errors on unseen/novel countries.
- Handles train set ("US", "India") and test set ("France" + any open-set country).
- Multi-tier representations: RAW, CANONICAL, IS_MISSING, IS_UNSEEN.
- Deterministic compatibility and contradiction detection.
- Produces numerical features for downstream matching models.
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, asdict
from typing import Dict, Optional, Set, Tuple, Any

NON_ALPHANUM_REGEX = re.compile(r"[^a-z0-9\s]")
WHITESPACE_REGEX = re.compile(r"\s+")

# Standard country aliases mapping to canonical uppercase identifiers
COUNTRY_ALIAS_MAP: Dict[str, str] = {
    # United States
    "us": "US",
    "usa": "US",
    "united states": "US",
    "united states of america": "US",
    "u s": "US",
    "u s a": "US",
    # India
    "india": "INDIA",
    "in": "INDIA",
    "ind": "INDIA",
    "bharat": "INDIA",
    "hindustan": "INDIA",
    # France (explicitly present in challenge test set: 14.98% of test S1)
    "france": "FRANCE",
    "fr": "FRANCE",
    "fra": "FRANCE",
    "republique francaise": "FRANCE",
    # United Kingdom
    "uk": "UK",
    "united kingdom": "UK",
    "gb": "UK",
    "gbr": "UK",
    "great britain": "UK",
    "england": "UK",
    # Canada
    "canada": "CANADA",
    "ca": "CANADA",
    "can": "CANADA",
    # Germany
    "germany": "GERMANY",
    "de": "GERMANY",
    "deu": "GERMANY",
    "deutschland": "GERMANY",
    # Australia
    "australia": "AUSTRALIA",
    "au": "AUSTRALIA",
    "aus": "AUSTRALIA",
    # Singapore
    "singapore": "SINGAPORE",
    "sg": "SINGAPORE",
    "sgp": "SINGAPORE",
    # Japan
    "japan": "JAPAN",
    "jp": "JAPAN",
    "jpn": "JAPAN",
}

# The set of countries observed in training data
DEFAULT_TRAIN_OBSERVED_COUNTRIES: Set[str] = {"US", "INDIA"}


@dataclass(frozen=True)
class NormalizedCountry:
    """Structured representation of a country."""
    raw: str
    canonical: str
    is_missing: bool
    is_observed_in_train: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class CountryComparison:
    """Detailed country compatibility and contradiction analysis."""
    exact_match: bool
    compatible: bool
    contradiction: bool
    has_unseen_country: bool
    anchor_missing: bool
    candidate_missing: bool

    def to_feature_dict(self) -> Dict[str, float]:
        """Numeric features for machine learning models."""
        return {
            "country_exact_match": 1.0 if self.exact_match else 0.0,
            "country_compatible": 1.0 if self.compatible else 0.0,
            "country_contradiction": 1.0 if self.contradiction else 0.0,
            "has_unseen_country": 1.0 if self.has_unseen_country else 0.0,
            "anchor_country_missing": 1.0 if self.anchor_missing else 0.0,
            "candidate_country_missing": 1.0 if self.candidate_missing else 0.0,
        }


class CountryHandler:
    """
    Production open-set country normalization and compatibility engine.
    Fully open-set: handles any novel country in test data gracefully.
    """

    def __init__(
        self,
        train_countries: Optional[Set[str]] = None,
        custom_alias_map: Optional[Dict[str, str]] = None,
    ):
        self.train_countries = (
            set(train_countries) if train_countries is not None
            else set(DEFAULT_TRAIN_OBSERVED_COUNTRIES)
        )
        self.alias_map = dict(COUNTRY_ALIAS_MAP)
        if custom_alias_map:
            self.alias_map.update(custom_alias_map)

    def normalize(self, raw_country: Optional[str]) -> NormalizedCountry:
        """
        Normalize a raw country string into canonical form with open-set support.
        Preserves original raw string unchanged.
        """
        if raw_country is None:
            raw_str = ""
        else:
            raw_str = str(raw_country).strip()

        if not raw_str or raw_str.lower() in {"nan", "null", "none", "n/a", "undefined"}:
            return NormalizedCountry(
                raw=raw_str,
                canonical="",
                is_missing=True,
                is_observed_in_train=False,
            )

        # 1. Unicode decomposition & accent stripping
        decomposed = unicodedata.normalize("NFKD", raw_str)
        text = "".join(c for c in decomposed if not unicodedata.combining(c))

        # 2. Punctuation and whitespace normalization
        clean_text = NON_ALPHANUM_REGEX.sub(" ", text.lower())
        clean_text = WHITESPACE_REGEX.sub(" ", clean_text).strip()

        # 3. Canonical lookup or fallback to uppercase cleaned string (open-set guarantee)
        canonical = self.alias_map.get(clean_text, clean_text.upper())

        is_observed = canonical in self.train_countries

        return NormalizedCountry(
            raw=raw_str,
            canonical=canonical,
            is_missing=False,
            is_observed_in_train=is_observed,
        )

    def compare(
        self,
        anchor: NormalizedCountry,
        candidate: NormalizedCountry,
    ) -> CountryComparison:
        """
        Compare anchor and candidate countries.
        Determines exact match, compatibility, contradiction, and open-set status.
        """
        # Missing values
        if anchor.is_missing or candidate.is_missing:
            # Compatible if either is missing, but not exact match and not contradiction
            return CountryComparison(
                exact_match=False,
                compatible=True,
                contradiction=False,
                has_unseen_country=not (anchor.is_observed_in_train and candidate.is_observed_in_train),
                anchor_missing=anchor.is_missing,
                candidate_missing=candidate.is_missing,
            )

        # Both present
        exact = (anchor.canonical == candidate.canonical)
        contradiction = not exact
        compatible = exact
        has_unseen = (not anchor.is_observed_in_train) or (not candidate.is_observed_in_train)

        return CountryComparison(
            exact_match=exact,
            compatible=compatible,
            contradiction=contradiction,
            has_unseen_country=has_unseen,
            anchor_missing=False,
            candidate_missing=False,
        )
