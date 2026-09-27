"""Requirements Matrix and Fair-Play Policy Contracts for ENTIVYRE.

Defines the non-negotiable rules from the Amazon ML Challenge 2026 specification,
providing programmatic audit checks and metadata schemas.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional


class RequirementCategory(str, Enum):
    INPUT_SCHEMA = "INPUT_SCHEMA"
    OUTPUT_FORMAT = "OUTPUT_FORMAT"
    INTEGRITY = "INTEGRITY"
    METRIC = "METRIC"
    FAIR_PLAY = "FAIR_PLAY"
    MODEL_LICENSE = "MODEL_LICENSE"


class EnforcementType(str, Enum):
    AUTOMATED_GATE = "AUTOMATED_GATE"      # Hard gate: rejects submission if failed
    DIAGNOSTIC_AUDIT = "DIAGNOSTIC_AUDIT"  # Diagnostic/warning: flags pipeline issue
    CODE_AUDIT = "CODE_AUDIT"              # Verified during manual/code audit


@dataclass(frozen=True)
class RequirementDefinition:
    """Formal entry in the ENTIVYRE Requirements Matrix."""

    req_id: str
    category: RequirementCategory
    enforcement: EnforcementType
    rule_statement: str
    official_source: str
    validation_logic: str


# Comprehensive Requirements Matrix
REQUIREMENTS_MATRIX: List[RequirementDefinition] = [
    RequirementDefinition(
        req_id="REQ-01",
        category=RequirementCategory.OUTPUT_FORMAT,
        enforcement=EnforcementType.AUTOMATED_GATE,
        rule_statement="Output file matching_results.tsv is required; candidate_pairs.tsv is required for final submission.",
        official_source="README.md lines 10-18, 143-160",
        validation_logic="os.path.isfile(matching_path) and os.path.isfile(candidate_path)",
    ),
    RequirementDefinition(
        req_id="REQ-02",
        category=RequirementCategory.OUTPUT_FORMAT,
        enforcement=EnforcementType.AUTOMATED_GATE,
        rule_statement="Files must be strictly Tab-Separated (.tsv) and valid UTF-8 text.",
        official_source="README.md lines 116-121, 323-328",
        validation_logic="Check encoding utf-8 and presence of '\\t' delimiter without raw comma delimitation.",
    ),
    RequirementDefinition(
        req_id="REQ-03",
        category=RequirementCategory.OUTPUT_FORMAT,
        enforcement=EnforcementType.AUTOMATED_GATE,
        rule_statement="Header rows must match exact expected column names: source1_entity_id\\tmatched_entity_ids and source1_entity_id\\tcandidate_entity_ids.",
        official_source="README.md lines 48-49, 123-129",
        validation_logic="First line must equal exact tab-separated list.",
    ),
    RequirementDefinition(
        req_id="REQ-04",
        category=RequirementCategory.INTEGRITY,
        enforcement=EnforcementType.AUTOMATED_GATE,
        rule_statement="Every Source 1 entity in test_source1.tsv must appear in submission outputs exactly once.",
        official_source="README.md lines 191-198",
        validation_logic="set(seen_s1_ids) == set(required_test_s1_ids)",
    ),
    RequirementDefinition(
        req_id="REQ-05",
        category=RequirementCategory.INTEGRITY,
        enforcement=EnforcementType.AUTOMATED_GATE,
        rule_statement="Duplicate source1_entity_id rows are strictly forbidden.",
        official_source="README.md lines 166-170",
        validation_logic="len(seen_s1_ids) == len(unique_s1_ids)",
    ),
    RequirementDefinition(
        req_id="REQ-06",
        category=RequirementCategory.OUTPUT_FORMAT,
        enforcement=EnforcementType.AUTOMATED_GATE,
        rule_statement="Matched and candidate IDs must only have S2- or S3- prefixes.",
        official_source="README.md lines 182-185",
        validation_logic="all(id.startswith(('S2-', 'S3-')) for id in list)",
    ),
    RequirementDefinition(
        req_id="REQ-07",
        category=RequirementCategory.INTEGRITY,
        enforcement=EnforcementType.AUTOMATED_GATE,
        rule_statement="Self-matches (S1- IDs in matched or candidate lists) are strictly forbidden.",
        official_source="README.md lines 177-180",
        validation_logic="not any(id.startswith('S1-') for id in list)",
    ),
    RequirementDefinition(
        req_id="REQ-08",
        category=RequirementCategory.OUTPUT_FORMAT,
        enforcement=EnforcementType.AUTOMATED_GATE,
        rule_statement="Repeated entity IDs inside a single matched or candidate list are forbidden.",
        official_source="README.md lines 172-175",
        validation_logic="len(ids) == len(set(ids))",
    ),
    RequirementDefinition(
        req_id="REQ-09",
        category=RequirementCategory.OUTPUT_FORMAT,
        enforcement=EnforcementType.AUTOMATED_GATE,
        rule_statement="Singletons / empty predictions must be an empty string following tab, never 'nan', 'null', 'None'.",
        official_source="README.md lines 147-150",
        validation_logic="rest.strip() != 'nan' and rest.strip() != 'null'",
    ),
    RequirementDefinition(
        req_id="REQ-10",
        category=RequirementCategory.INTEGRITY,
        enforcement=EnforcementType.DIAGNOSTIC_AUDIT,
        rule_statement="Final matches must be a subset of candidate blocking pairs for each Source 1 entity.",
        official_source="README.md lines 258-270",
        validation_logic="matched_ids.issubset(candidate_ids)",
    ),
    RequirementDefinition(
        req_id="REQ-11",
        category=RequirementCategory.INTEGRITY,
        enforcement=EnforcementType.DIAGNOSTIC_AUDIT,
        rule_statement="Matched entity IDs should exist in test_source2.tsv or test_source3.tsv.",
        official_source="README.md lines 30-39, 186-189",
        validation_logic="matched_id in (test_s2_ids | test_s3_ids)",
    ),
    RequirementDefinition(
        req_id="REQ-12",
        category=RequirementCategory.METRIC,
        enforcement=EnforcementType.AUTOMATED_GATE,
        rule_statement="Evaluation metric is Macro-averaged F_0.5 with explicit singleton credit (1.0 for true empty & pred empty, 0.0 for true empty & pred non-empty).",
        official_source="README.md lines 180-210",
        validation_logic="compute_macro_f05() implementation",
    ),
    RequirementDefinition(
        req_id="REQ-13",
        category=RequirementCategory.MODEL_LICENSE,
        enforcement=EnforcementType.CODE_AUDIT,
        rule_statement="Model parameter count must not exceed 8 Billion parameters.",
        official_source="README.md lines 175-178",
        validation_logic="Audit model parameter size <= 8,000,000,000",
    ),
    RequirementDefinition(
        req_id="REQ-14",
        category=RequirementCategory.MODEL_LICENSE,
        enforcement=EnforcementType.CODE_AUDIT,
        rule_statement="Pretrained models must be licensed under MIT or Apache 2.0.",
        official_source="README.md lines 175-178",
        validation_logic="Verify model license in ['MIT', 'Apache-2.0']",
    ),
    RequirementDefinition(
        req_id="REQ-15",
        category=RequirementCategory.FAIR_PLAY,
        enforcement=EnforcementType.CODE_AUDIT,
        rule_statement="Zero external business databases, entity resolution APIs, government registries, or geocoding APIs allowed.",
        official_source="README.md lines 230-245",
        validation_logic="Audit code for zero outbound network calls and zero external lookup artifacts",
    ),
]


def get_requirements_by_category(category: RequirementCategory) -> List[RequirementDefinition]:
    """Filter requirements matrix by category."""
    return [req for req in REQUIREMENTS_MATRIX if req.category == category]


def get_requirements_by_enforcement(enforcement: EnforcementType) -> List[RequirementDefinition]:
    """Filter requirements matrix by enforcement mechanism."""
    return [req for req in REQUIREMENTS_MATRIX if req.enforcement == enforcement]


def export_requirements_matrix_dict() -> List[Dict[str, Any]]:
    """Export complete requirements matrix as serializable dictionary list."""
    return [
        {
            "req_id": r.req_id,
            "category": r.category.value,
            "enforcement": r.enforcement.value,
            "rule_statement": r.rule_statement,
            "official_source": r.official_source,
            "validation_logic": r.validation_logic,
        }
        for r in REQUIREMENTS_MATRIX
    ]
