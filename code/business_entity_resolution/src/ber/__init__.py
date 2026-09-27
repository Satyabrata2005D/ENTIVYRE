"""
BER: Business Entity Resolution Core Package
Official package layout for Amazon ML Challenge submission.
"""
from __future__ import annotations
import sys
from pathlib import Path

# Ensure root package (entivyre) is resolvable
_project_root = Path(__file__).resolve().parent.parent.parent.parent.parent
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from entivyre.config import AppConfig, load_config
from entivyre.contracts.schema import (
    Source1Record,
    Source2Record,
    Source3Record,
    GroundTruthRecord,
    MatchingRecord,
    CandidateRecord,
    ContractValidationReport,
    parse_entity_id
)
from entivyre.contracts.metrics import MacroF05Evaluator, compute_macro_f05
from entivyre.contracts.verifier import SubmissionVerifier, validate_submission_files
from entivyre.utils.logger import get_logger, configure_logging

__all__ = [
    "AppConfig",
    "load_config",
    "Source1Record",
    "Source2Record",
    "Source3Record",
    "GroundTruthRecord",
    "MatchingRecord",
    "CandidateRecord",
    "ContractValidationReport",
    "parse_entity_id",
    "MacroF05Evaluator",
    "compute_macro_f05",
    "SubmissionVerifier",
    "validate_submission_files",
    "get_logger",
    "configure_logging",
]
