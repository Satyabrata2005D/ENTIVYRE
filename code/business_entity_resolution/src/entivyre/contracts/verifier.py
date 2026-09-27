"""Production-grade contract verification engine for ENTIVYRE.

Executes streaming pre-submission audits and enforces official challenge invariants
with structured diagnostics and machine-readable JSON reports.
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from typing import Dict, List, Optional, Set, Tuple

from entivyre.contracts.schema import (
    CANDIDATE_HEADER,
    MATCHING_HEADER,
    ContractValidationReport,
    ValidationIssue,
)
from entivyre.utils.logger import get_logger

logger = get_logger("entivyre.contracts.verifier", stage="01_contracts")

DELIM = "\t"
MAX_EXAMPLES = 5


def _format_examples(items: Set[str]) -> List[str]:
    """Format a deterministic sorted sample of offending IDs."""
    return sorted(items)[:MAX_EXAMPLES]


def read_entity_ids_streaming(path: str) -> Set[str]:
    """Read the first column (entity_id) from a TSV file in a streaming fashion."""
    ids: Set[str] = set()
    with open(path, "r", encoding="utf-8") as f:
        # Skip header
        f.readline()
        for line in f:
            line_str = line.strip()
            if not line_str:
                continue
            entity_id = line_str.split(DELIM, 1)[0].strip()
            if entity_id:
                ids.add(entity_id)
    return ids


def validate_file_contract(
    path: str,
    expected_header: Tuple[str, str],
    col_name: str,
    required_s1_ids: Optional[Set[str]] = None,
    valid_target_ids: Optional[Set[str]] = None,
) -> Tuple[Optional[Dict[str, Set[str]]], List[ValidationIssue], List[ValidationIssue], Dict[str, int]]:
    """Validate a results-style TSV file against structural and semantic rules.

    Returns:
        (mapping, errors, warnings, stats)
    """
    errors: List[ValidationIssue] = []
    warnings: List[ValidationIssue] = []
    stats: Dict[str, int] = {"total_rows": 0, "empty_rows": 0, "total_target_ids": 0}

    if not os.path.isfile(path):
        errors.append(
            ValidationIssue(
                severity="ERROR",
                rule_id="REQ-01",
                message=f"File not found: {path}",
            )
        )
        return None, errors, warnings, stats

    filename = os.path.basename(path)
    mapping: Dict[str, Set[str]] = {}
    seen_s1: Set[str] = set()
    dup_s1_rows: Set[str] = set()
    intra_dupes: Set[str] = set()
    self_matches: Set[str] = set()
    invalid_prefixes: Set[str] = set()
    unknown_ids: Set[str] = set()
    nan_string_rows: Set[str] = set()

    with open(path, "r", encoding="utf-8") as f:
        header_line = f.readline()
        if not header_line:
            errors.append(
                ValidationIssue(
                    severity="ERROR",
                    rule_id="REQ-02",
                    message=f"{filename} is completely empty.",
                )
            )
            return None, errors, warnings, stats

        if DELIM not in header_line and "," in header_line:
            errors.append(
                ValidationIssue(
                    severity="ERROR",
                    rule_id="REQ-02",
                    message=(
                        f"{filename} appears to be COMMA-separated instead of TAB-separated. "
                        "Submissions must be strictly tab-separated (.tsv)."
                    ),
                )
            )
            return None, errors, warnings, stats

        header_cols = tuple(c.strip().lower() for c in header_line.rstrip("\r\n").split(DELIM))
        if header_cols != expected_header:
            errors.append(
                ValidationIssue(
                    severity="ERROR",
                    rule_id="REQ-03",
                    message=(
                        f"{filename} has invalid header: {list(header_cols)}. "
                        f"Expected exactly {list(expected_header)} (tab-separated)."
                    ),
                )
            )
            return None, errors, warnings, stats

        for line_num, line in enumerate(f, start=2):
            s1, tab, rest = line.partition(DELIM)
            if not tab:
                if s1.strip():
                    errors.append(
                        ValidationIssue(
                            severity="ERROR",
                            rule_id="REQ-02",
                            message=f"{filename}: malformed row without tab at line {line_num}: {line.rstrip()!r}",
                        )
                    )
                continue

            s1 = s1.strip()
            stats["total_rows"] += 1

            if s1 in seen_s1:
                dup_s1_rows.add(s1)
            seen_s1.add(s1)

            rest_stripped = rest.rstrip("\r\n").strip()
            if not rest_stripped:
                stats["empty_rows"] += 1
                mapping[s1] = set()
                continue

            # Detect literal 'nan', 'null', 'None'
            if rest_stripped.lower() in ("nan", "null", "none"):
                nan_string_rows.add(s1)
                mapping[s1] = set()
                continue

            ids = [i.strip() for i in rest_stripped.split(",") if i.strip()]
            if len(ids) != len(set(ids)):
                intra_dupes.add(s1)

            id_set = set(ids)
            stats["total_target_ids"] += len(id_set)
            mapping[s1] = id_set

            for tid in id_set:
                if tid.startswith("S1-"):
                    self_matches.add(tid)
                elif not tid.startswith(("S2-", "S3-")):
                    invalid_prefixes.add(tid)
                elif valid_target_ids is not None and tid not in valid_target_ids:
                    unknown_ids.add(tid)

    # Check violations
    if dup_s1_rows:
        errors.append(
            ValidationIssue(
                severity="ERROR",
                rule_id="REQ-05",
                message=f"{filename}: duplicate source1_entity_id row(s) found.",
                sample_offenders=_format_examples(dup_s1_rows),
            )
        )

    if intra_dupes:
        errors.append(
            ValidationIssue(
                severity="ERROR",
                rule_id="REQ-08",
                message=f"{filename}: repeated entity ID inside {col_name} list.",
                sample_offenders=_format_examples(intra_dupes),
            )
        )

    if self_matches:
        errors.append(
            ValidationIssue(
                severity="ERROR",
                rule_id="REQ-07",
                message=f"{filename}: {col_name} contains forbidden Source-1 self-matches.",
                sample_offenders=_format_examples(self_matches),
            )
        )

    if invalid_prefixes:
        errors.append(
            ValidationIssue(
                severity="ERROR",
                rule_id="REQ-06",
                message=f"{filename}: {col_name} contains IDs without S2- or S3- prefix.",
                sample_offenders=_format_examples(invalid_prefixes),
            )
        )

    if nan_string_rows:
        errors.append(
            ValidationIssue(
                severity="ERROR",
                rule_id="REQ-09",
                message=f"{filename}: literal string 'nan'/'null'/'none' used instead of clean empty string.",
                sample_offenders=_format_examples(nan_string_rows),
            )
        )

    if required_s1_ids is not None:
        missing_s1 = required_s1_ids - seen_s1
        if missing_s1:
            errors.append(
                ValidationIssue(
                    severity="ERROR",
                    rule_id="REQ-04",
                    message=f"{filename}: {len(missing_s1)} required Source-1 entities are missing.",
                    sample_offenders=_format_examples(missing_s1),
                )
            )

        extra_s1 = seen_s1 - required_s1_ids
        if extra_s1:
            errors.append(
                ValidationIssue(
                    severity="ERROR",
                    rule_id="REQ-04",
                    message=f"{filename}: {len(extra_s1)} Source-1 IDs are not present in test_source1.tsv.",
                    sample_offenders=_format_examples(extra_s1),
                )
            )

    if unknown_ids:
        warnings.append(
            ValidationIssue(
                severity="WARNING",
                rule_id="REQ-11",
                message=f"{filename}: {len(unknown_ids)} {col_name} IDs do not exist in test Source 2/3 datasets.",
                sample_offenders=_format_examples(unknown_ids),
            )
        )

    return mapping, errors, warnings, stats


def validate_submission_pipeline(
    matching_path: str,
    candidate_path: Optional[str] = None,
    test_dir: Optional[str] = None,
    test_source1_path: Optional[str] = None,
    check_ids: bool = False,
) -> ContractValidationReport:
    """Execute complete end-to-end submission contract validation.

    Args:
        matching_path: Path to matching_results.tsv
        candidate_path: Optional path to candidate_pairs.tsv
        test_dir: Directory containing test_source1.tsv, test_source2.tsv, test_source3.tsv
        test_source1_path: Direct path to test_source1.tsv (if test_dir not given)
        check_ids: If True, load and verify target IDs against test_source2/3.tsv
    """
    start_time = time.perf_counter()
    errors: List[ValidationIssue] = []
    warnings: List[ValidationIssue] = []

    logger.info(
        "Starting submission contract validation",
        extra={"payload": {"matching_path": matching_path, "candidate_path": candidate_path}},
    )

    # 1. Resolve test Source 1 required IDs
    required_s1_ids: Optional[Set[str]] = None
    s1_file = test_source1_path or (os.path.join(test_dir, "test_source1.tsv") if test_dir else None)
    if s1_file and os.path.isfile(s1_file):
        required_s1_ids = read_entity_ids_streaming(s1_file)
        logger.info(f"Loaded {len(required_s1_ids)} required Source 1 entities from {s1_file}")
    elif s1_file:
        errors.append(
            ValidationIssue(
                severity="ERROR",
                rule_id="REQ-04",
                message=f"test_source1.tsv not found at {s1_file}",
            )
        )

    # 2. Optionally load valid S2/S3 target IDs
    valid_target_ids: Optional[Set[str]] = None
    if check_ids and test_dir:
        targets: Set[str] = set()
        for s_name in ("test_source2.tsv", "test_source3.tsv"):
            s_path = os.path.join(test_dir, s_name)
            if os.path.isfile(s_path):
                targets |= read_entity_ids_streaming(s_path)
            else:
                warnings.append(
                    ValidationIssue(
                        severity="WARNING",
                        rule_id="REQ-11",
                        message=f"{s_path} not found. Skipping ID existence check for {s_name}.",
                    )
                )
        if targets:
            valid_target_ids = targets
            logger.info(f"Loaded {len(valid_target_ids)} valid test target IDs (S2/S3)")

    # 3. Validate matching_results.tsv
    matched_mapping, m_errors, m_warnings, m_stats = validate_file_contract(
        matching_path,
        MATCHING_HEADER,
        "matched_entity_ids",
        required_s1_ids=required_s1_ids,
        valid_target_ids=valid_target_ids,
    )
    errors.extend(m_errors)
    warnings.extend(m_warnings)

    # 4. Validate candidate_pairs.tsv (if provided)
    candidate_mapping: Optional[Dict[str, Set[str]]] = None
    if candidate_path and os.path.isfile(candidate_path):
        candidate_mapping, c_errors, c_warnings, _ = validate_file_contract(
            candidate_path,
            CANDIDATE_HEADER,
            "candidate_entity_ids",
            required_s1_ids=required_s1_ids,
            valid_target_ids=valid_target_ids,
        )
        errors.extend(c_errors)
        warnings.extend(c_warnings)
    elif candidate_path:
        warnings.append(
            ValidationIssue(
                severity="WARNING",
                rule_id="REQ-01",
                message=f"Candidate file {candidate_path} not found. Final submission zip must contain it.",
            )
        )

    # 5. Check subset invariant: matches must be subset of candidates
    if matched_mapping is not None and candidate_mapping is not None:
        subset_offenders: Set[str] = set()
        for s1_id, matched_ids in matched_mapping.items():
            cand_ids = candidate_mapping.get(s1_id, set())
            unseen_matches = matched_ids - cand_ids
            if unseen_matches:
                subset_offenders.add(s1_id)

        if subset_offenders:
            warnings.append(
                ValidationIssue(
                    severity="WARNING",
                    rule_id="REQ-10",
                    message=(
                        f"{len(subset_offenders)} Source-1 entity(ies) have matched IDs not present "
                        "in candidate_pairs.tsv. Final matches should normally come from candidates."
                    ),
                    sample_offenders=_format_examples(subset_offenders),
                )
            )

    elapsed = time.perf_counter() - start_time
    is_valid = len(errors) == 0

    report = ContractValidationReport(
        is_valid=is_valid,
        total_source1_entities=m_stats.get("total_rows", 0),
        total_empty_rows=m_stats.get("empty_rows", 0),
        total_non_empty_rows=m_stats.get("total_rows", 0) - m_stats.get("empty_rows", 0),
        total_predicted_matches=m_stats.get("total_target_ids", 0),
        errors=errors,
        warnings=warnings,
        execution_time_seconds=elapsed,
    )

    logger.info(
        "Validation complete",
        extra={"payload": {"is_valid": is_valid, "errors": len(errors), "warnings": len(warnings), "elapsed_s": elapsed}},
    )
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="ENTIVYRE Submission Contract Validator CLI.")
    parser.add_argument("--matching", "-m", required=True, help="Path to matching_results.tsv")
    parser.add_argument("--candidate", "-c", default=None, help="Path to candidate_pairs.tsv")
    parser.add_argument("--test-dir", "-t", default=None, help="Folder with test_source1/2/3.tsv")
    parser.add_argument("--test-s1", default=None, help="Direct path to test_source1.tsv")
    parser.add_argument("--check-ids", action="store_true", help="Enable memory-heavy target ID existence check")
    parser.add_argument("--report-json", default=None, help="Output path for structured JSON report")
    args = parser.parse_args()

    report = validate_submission_pipeline(
        matching_path=args.matching,
        candidate_path=args.candidate,
        test_dir=args.test_dir,
        test_source1_path=args.test_s1,
        check_ids=args.check_ids,
    )

    import json
    if args.report_json:
        os.makedirs(os.path.dirname(os.path.abspath(args.report_json)), exist_ok=True)
        with open(args.report_json, "w", encoding="utf-8") as f:
            json.dump(report.to_dict(), f, indent=2)
        print(f"Wrote structured report to {args.report_json}")

    print("\n=== ENTIVYRE Contract Validation Summary ===")
    print(f"Valid: {report.is_valid}")
    print(f"Total Source-1 Entities: {report.total_source1_entities}")
    print(f"Total Predicted Matches: {report.total_predicted_matches}")
    print(f"Empty (Singleton) Predictions: {report.total_empty_rows}")
    print(f"Non-Empty Predictions: {report.total_non_empty_rows}")
    print(f"Elapsed Time: {report.execution_time_seconds:.4f}s")

    for w in report.warnings:
        print(f"\n[WARNING - {w.rule_id}]: {w.message}")
        if w.sample_offenders:
            print(f"  Samples: {', '.join(w.sample_offenders)}")

    if report.errors:
        print(f"\n[FAILED] - {len(report.errors)} blocking issue(s) detected:")
        for i, e in enumerate(report.errors, 1):
            print(f"  {i}. [{e.rule_id}] {e.message}")
            if e.sample_offenders:
                print(f"     Samples: {', '.join(e.sample_offenders)}")
        return 1

validate_submission_files = validate_submission_pipeline


class SubmissionVerifier:
    """Verifier class for validating submissions programmatically."""

    def __init__(self, check_ids: bool = False):
        self.check_ids = check_ids

    def verify(
        self,
        matching_path: str,
        candidate_path: Optional[str] = None,
        test_source1_path: Optional[str] = None,
        test_dir: Optional[str] = None,
    ) -> ContractValidationReport:
        return validate_submission_pipeline(
            matching_path=matching_path,
            candidate_path=candidate_path,
            test_source1_path=test_source1_path,
            test_dir=test_dir,
            check_ids=self.check_ids,
        )


if __name__ == "__main__":
    sys.exit(main())

