"""Data schema contracts and invariants for ENTIVYRE.

Enforces strict structural, typing, and semantic validation across:
- Source records (S1, S2, S3)
- Ground truth records
- Candidate generation outputs (candidate_pairs.tsv)
- Final matching outputs (matching_results.tsv)
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Set, Tuple

# Official entity ID regex pattern: S1-00001, S2-00047, S3-00812
ENTITY_ID_PATTERN = re.compile(r"^(S[123])-(\d+)$")
ISO_COUNTRY_PATTERN = re.compile(r"^[A-Z]{2}$")

# Official TSV column constants
MATCHING_HEADER = ("source1_entity_id", "matched_entity_ids")
CANDIDATE_HEADER = ("source1_entity_id", "candidate_entity_ids")
SOURCE_HEADER = ("entity_id", "name", "address", "country")
GROUND_TRUTH_HEADER = ("entity_id", "matched_entity_ids")

FORBIDDEN_NAN_STRINGS = frozenset({"nan", "none", "null", "n/a", "undefined"})


class SourcePrefix(str, Enum):
    SOURCE1 = "S1"
    SOURCE2 = "S2"
    SOURCE3 = "S3"


def parse_entity_id(entity_id: str) -> Tuple[SourcePrefix, int]:
    """Parse and validate an entity ID into prefix and numeric sequence.

    Raises:
        ValueError: if entity_id does not strictly conform to 'S[1-3]-[0-9]+'.
    """
    if not isinstance(entity_id, str):
        raise ValueError(f"Entity ID must be str, got {type(entity_id).__name__}: {entity_id!r}")
    
    clean_id = entity_id.strip()
    match = ENTITY_ID_PATTERN.match(clean_id)
    if not match:
        raise ValueError(
            f"Invalid entity ID format: {entity_id!r}. "
            f"Expected pattern 'S1-XXXXX', 'S2-XXXXX', or 'S3-XXXXX'."
        )
    return SourcePrefix(match.group(1)), int(match.group(2))


@dataclass(frozen=True)
class SourceRecord:
    """Canonical representation of an ingested raw source entity record."""

    entity_id: str
    name: str
    address: str
    country: str

    @property
    def business_name(self) -> str:
        return self.name

    @property
    def business_address(self) -> str:
        return self.address

    def __post_init__(self) -> None:
        prefix, _ = parse_entity_id(self.entity_id)
        if not isinstance(self.country, str) or not self.country.strip():
            raise ValueError(f"Country must be non-empty string, got: {self.country!r}")
        # Detect accidental 'nan' literal string corruption
        if self.country.strip().lower() in FORBIDDEN_NAN_STRINGS:
            raise ValueError(f"Literal NaN string detected in country field for {self.entity_id}: {self.country!r}")
        if self.name.strip().lower() in FORBIDDEN_NAN_STRINGS:
            raise ValueError(f"Literal NaN string detected in name field for {self.entity_id}: {self.name!r}")


@dataclass(frozen=True)
class Source1Record(SourceRecord):
    """Source 1 entity record (clean reference anchor)."""

    def __post_init__(self) -> None:
        super().__post_init__()
        prefix, _ = parse_entity_id(self.entity_id)
        if prefix != SourcePrefix.SOURCE1:
            raise ValueError(f"Source1Record entity_id must start with S1-, got: {self.entity_id}")


@dataclass(frozen=True)
class Source2Record(SourceRecord):
    """Source 2 entity record (noisy secondary source)."""

    def __post_init__(self) -> None:
        super().__post_init__()
        prefix, _ = parse_entity_id(self.entity_id)
        if prefix != SourcePrefix.SOURCE2:
            raise ValueError(f"Source2Record entity_id must start with S2-, got: {self.entity_id}")


@dataclass(frozen=True)
class Source3Record(SourceRecord):
    """Source 3 entity record (noisy tertiary source)."""

    def __post_init__(self) -> None:
        super().__post_init__()
        prefix, _ = parse_entity_id(self.entity_id)
        if prefix != SourcePrefix.SOURCE3:
            raise ValueError(f"Source3Record entity_id must start with S3-, got: {self.entity_id}")


@dataclass(frozen=True)
class GroundTruthRecord:
    """Ground truth mapping linking one Source 1 entity to zero or more S2/S3 entities."""

    entity_id: str
    matched_entity_ids: Tuple[str, ...]

    @property
    def source1_entity_id(self) -> str:
        return self.entity_id

    def __post_init__(self) -> None:
        prefix, _ = parse_entity_id(self.entity_id)
        if prefix != SourcePrefix.SOURCE1:
            raise ValueError(f"GroundTruthRecord anchor must be S1 entity, got: {self.entity_id}")
        
        # Verify no self-matches and valid prefixes for matched IDs
        seen: Set[str] = set()
        for mid in self.matched_entity_ids:
            mid_clean = mid.strip()
            if not mid_clean:
                raise ValueError("Empty entity ID in matched list")
            if mid_clean in seen:
                raise ValueError(f"Duplicate entity ID in ground truth list: {mid_clean}")
            seen.add(mid_clean)

            m_prefix, _ = parse_entity_id(mid_clean)
            if m_prefix == SourcePrefix.SOURCE1:
                raise ValueError(f"Forbidden self-match in ground truth: {mid_clean}")

    @property
    def is_singleton(self) -> bool:
        """True if Source 1 entity has no true matches (empty match list)."""
        return len(self.matched_entity_ids) == 0



@dataclass(frozen=True)
class CandidateRecord:
    """Row contract for candidate_pairs.tsv."""

    source1_entity_id: str
    candidate_entity_ids: Tuple[str, ...]

    def __post_init__(self) -> None:
        prefix, _ = parse_entity_id(self.source1_entity_id)
        if prefix != SourcePrefix.SOURCE1:
            raise ValueError(f"source1_entity_id must start with S1-, got: {self.source1_entity_id}")

        seen: Set[str] = set()
        for cid in self.candidate_entity_ids:
            cid_clean = cid.strip()
            if not cid_clean:
                raise ValueError("Empty candidate entity ID encountered")
            if cid_clean in seen:
                raise ValueError(f"Duplicate candidate ID in list: {cid_clean}")
            seen.add(cid_clean)
            c_prefix, _ = parse_entity_id(cid_clean)
            if c_prefix == SourcePrefix.SOURCE1:
                raise ValueError(f"Forbidden self-match in candidate list: {cid_clean}")

    def to_tsv_row(self) -> str:
        """Render deterministic TSV formatted row."""
        return f"{self.source1_entity_id}\t{','.join(self.candidate_entity_ids)}\n"


@dataclass(frozen=True)
class MatchingRecord:
    """Row contract for matching_results.tsv."""

    source1_entity_id: str
    matched_entity_ids: Tuple[str, ...]

    def __post_init__(self) -> None:
        prefix, _ = parse_entity_id(self.source1_entity_id)
        if prefix != SourcePrefix.SOURCE1:
            raise ValueError(f"source1_entity_id must start with S1-, got: {self.source1_entity_id}")

        seen: Set[str] = set()
        for mid in self.matched_entity_ids:
            mid_clean = mid.strip()
            if not mid_clean:
                raise ValueError("Empty matched entity ID encountered")
            if mid_clean in seen:
                raise ValueError(f"Duplicate matched ID in list: {mid_clean}")
            seen.add(mid_clean)
            m_prefix, _ = parse_entity_id(mid_clean)
            if m_prefix == SourcePrefix.SOURCE1:
                raise ValueError(f"Forbidden self-match in matched list: {mid_clean}")

    def to_tsv_row(self) -> str:
        """Render deterministic TSV formatted row."""
        return f"{self.source1_entity_id}\t{','.join(self.matched_entity_ids)}\n"


@dataclass
class ValidationIssue:
    """Structured description of an individual contract violation or warning."""

    severity: str  # "ERROR" or "WARNING"
    rule_id: str
    message: str
    sample_offenders: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "severity": self.severity,
            "rule_id": self.rule_id,
            "message": self.message,
            "sample_offenders": self.sample_offenders,
        }


@dataclass
class ContractValidationReport:
    """Comprehensive validation report produced when auditing submission outputs."""

    is_valid: bool
    total_source1_entities: int
    total_empty_rows: int
    total_non_empty_rows: int
    total_predicted_matches: int
    errors: List[ValidationIssue] = field(default_factory=list)
    warnings: List[ValidationIssue] = field(default_factory=list)
    execution_time_seconds: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "is_valid": self.is_valid,
            "total_source1_entities": self.total_source1_entities,
            "total_empty_rows": self.total_empty_rows,
            "total_non_empty_rows": self.total_non_empty_rows,
            "total_predicted_matches": self.total_predicted_matches,
            "error_count": len(self.errors),
            "warning_count": len(self.warnings),
            "errors": [e.to_dict() for e in self.errors],
            "warnings": [w.to_dict() for w in self.warnings],
            "execution_time_seconds": round(self.execution_time_seconds, 4),
        }
