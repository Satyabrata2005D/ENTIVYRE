"""ENTIVYRE Contracts and Specifications Module.

Exposes typed data models, validation invariants, challenge metric calculations,
and the non-negotiable requirements matrix for the Amazon ML Challenge 2026.
"""

from entivyre.contracts.metrics import (
    EntityMetricResult,
    MacroEvaluationSummary,
    compute_entity_f05,
    compute_macro_f05,
)
from entivyre.contracts.rules import (
    REQUIREMENTS_MATRIX,
    EnforcementType,
    RequirementCategory,
    RequirementDefinition,
    export_requirements_matrix_dict,
    get_requirements_by_category,
    get_requirements_by_enforcement,
)
from entivyre.contracts.schema import (
    CANDIDATE_HEADER,
    MATCHING_HEADER,
    CandidateRecord,
    ContractValidationReport,
    GroundTruthRecord,
    MatchingRecord,
    Source1Record,
    Source2Record,
    Source3Record,
    SourcePrefix,
    SourceRecord,
    ValidationIssue,
    parse_entity_id,
)
from entivyre.contracts.verifier import (
    validate_file_contract,
    validate_submission_pipeline,
)

__all__ = [
    # Schema
    "SourcePrefix",
    "SourceRecord",
    "Source1Record",
    "Source2Record",
    "Source3Record",
    "GroundTruthRecord",
    "CandidateRecord",
    "MatchingRecord",
    "ValidationIssue",
    "ContractValidationReport",
    "MATCHING_HEADER",
    "CANDIDATE_HEADER",
    "parse_entity_id",
    # Metrics
    "EntityMetricResult",
    "MacroEvaluationSummary",
    "compute_entity_f05",
    "compute_macro_f05",
    # Rules
    "REQUIREMENTS_MATRIX",
    "RequirementCategory",
    "EnforcementType",
    "RequirementDefinition",
    "get_requirements_by_category",
    "get_requirements_by_enforcement",
    "export_requirements_matrix_dict",
    # Verifier
    "validate_file_contract",
    "validate_submission_pipeline",
]
