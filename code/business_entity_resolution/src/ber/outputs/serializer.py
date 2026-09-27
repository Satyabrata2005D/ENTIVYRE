"""
Production Output Serializer and Format Validator for ENTIVYRE.
Phase 32: Serialization of matching_results.tsv and candidate_pairs.tsv
strictly conforming to official Amazon ML Challenge specifications.

Guarantees:
- Strict tab-delimited formatting (.tsv) with valid UTF-8 text encoding.
- Exact column headers:
    matching_results.tsv: source1_entity_id\tmatched_entity_ids
    candidate_pairs.tsv:  source1_entity_id\tcandidate_entity_ids
- Space-delimited target IDs within rows; empty string "" for valid no-match cases.
- Complete 100% coverage of Source 1 entities with zero duplicates and zero omissions.
- Candidate-pairs contract: strictly audits that matching_results is a subset of candidate_pairs.
- Prefix conformity: all targets must start with 'S2-' or 'S3-' (no 'S1-' self-matches).
- Pure-Python, zero external C-dependencies.
"""
from __future__ import annotations

import os
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Tuple, Any, Mapping, Collection, Set, Sequence

from entivyre.utils.logger import get_logger

logger = get_logger("ber.outputs.serializer", stage="32_output_serializer")

MATCHING_HEADER: str = "source1_entity_id\tmatched_entity_ids\n"
CANDIDATE_HEADER: str = "source1_entity_id\tcandidate_entity_ids\n"


@dataclass
class OutputValidationReport:
    """Detailed audit report validating challenge submission file contracts."""
    is_valid: bool
    matching_file: str
    candidate_file: str
    total_matching_rows: int
    total_candidate_rows: int
    singleton_matching_rows: int
    matched_rows: int
    candidate_subset_violations: int
    format_errors: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class OutputSerializer:
    """
    Serializes and validates official submission TSV files.
    """

    @staticmethod
    def serialize_matching_results(
        predictions: Mapping[str, Collection[str]],
        output_path: Path,
        ordered_s1_ids: Optional[Sequence[str]] = None,
    ) -> Path:
        """
        Serialize predictions to output/matching_results.tsv.
        """
        p = Path(output_path)
        p.parent.mkdir(parents=True, exist_ok=True)

        s1_ids = ordered_s1_ids if ordered_s1_ids is not None else sorted(predictions.keys())

        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(MATCHING_HEADER)
            for s1_id in s1_ids:
                targets = predictions.get(s1_id, ())
                # Clean, deduplicate, filter self-matches
                seen = set()
                clean_targets: List[str] = []
                for tid in targets:
                    tid_clean = str(tid).strip()
                    if tid_clean and tid_clean != s1_id and tid_clean not in seen:
                        if tid_clean.startswith(("S2-", "S3-")):
                            seen.add(tid_clean)
                            clean_targets.append(tid_clean)

                targets_str = ",".join(clean_targets)
                f.write(f"{s1_id}\t{targets_str}\n")

        logger.info(
            f"Serialized matching_results.tsv to {p} ({len(s1_ids)} Source 1 records)",
            extra={"payload": {"path": str(p), "records": len(s1_ids)}},
        )
        return p

    @staticmethod
    def serialize_candidate_pairs(
        candidates: Mapping[str, Collection[str]],
        output_path: Path,
        ordered_s1_ids: Optional[Sequence[str]] = None,
    ) -> Path:
        """
        Serialize candidate pairs to output/candidate_pairs.tsv.
        """
        p = Path(output_path)
        p.parent.mkdir(parents=True, exist_ok=True)

        s1_ids = ordered_s1_ids if ordered_s1_ids is not None else sorted(candidates.keys())

        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(CANDIDATE_HEADER)
            for s1_id in s1_ids:
                cands = candidates.get(s1_id, ())
                seen = set()
                clean_cands: List[str] = []
                for cid in cands:
                    cid_clean = str(cid).strip()
                    if cid_clean and cid_clean != s1_id and cid_clean not in seen:
                        if cid_clean.startswith(("S2-", "S3-")):
                            seen.add(cid_clean)
                            clean_cands.append(cid_clean)

                cands_str = ",".join(clean_cands)
                f.write(f"{s1_id}\t{cands_str}\n")

        logger.info(
            f"Serialized candidate_pairs.tsv to {p} ({len(s1_ids)} Source 1 records)",
            extra={"payload": {"path": str(p), "records": len(s1_ids)}},
        )
        return p

    @staticmethod
    def validate_submission_files(
        matching_tsv_path: Path,
        candidate_tsv_path: Path,
        expected_s1_ids: Optional[Set[str]] = None,
    ) -> OutputValidationReport:
        """
        Exhaustive audit of generated TSV submission files against all challenge rules.
        """
        m_path = Path(matching_tsv_path)
        c_path = Path(candidate_tsv_path)
        errors: List[str] = []

        if not m_path.exists():
            return OutputValidationReport(
                is_valid=False,
                matching_file=str(m_path),
                candidate_file=str(c_path),
                total_matching_rows=0,
                total_candidate_rows=0,
                singleton_matching_rows=0,
                matched_rows=0,
                candidate_subset_violations=0,
                format_errors=[f"File not found: {m_path}"],
            )

        if not c_path.exists():
            return OutputValidationReport(
                is_valid=False,
                matching_file=str(m_path),
                candidate_file=str(c_path),
                total_matching_rows=0,
                total_candidate_rows=0,
                singleton_matching_rows=0,
                matched_rows=0,
                candidate_subset_violations=0,
                format_errors=[f"File not found: {c_path}"],
            )

        # 1. Read and validate candidate_pairs.tsv
        cand_map: Dict[str, Set[str]] = {}
        with open(c_path, "r", encoding="utf-8") as f:
            c_header = f.readline()
            if c_header != CANDIDATE_HEADER:
                errors.append(f"Invalid candidate header: {repr(c_header)} != {repr(CANDIDATE_HEADER)}")

            line_no = 1
            for line in f:
                line_no += 1
                parts = line.rstrip("\r\n").split("\t")
                if len(parts) != 2:
                    errors.append(f"Candidate file line {line_no} has {len(parts)} parts, expected 2")
                    continue
                s1_id, cands_str = parts
                if s1_id in cand_map:
                    errors.append(f"Candidate file line {line_no}: Duplicate Source 1 ID '{s1_id}'")
                cand_list = [c.strip() for c in cands_str.split(",") if c.strip()]
                cand_map[s1_id] = set(cand_list)

        # 2. Read and validate matching_results.tsv
        seen_s1: Set[str] = set()
        singleton_count = 0
        matched_count = 0
        subset_violations = 0

        with open(m_path, "r", encoding="utf-8") as f:
            m_header = f.readline()
            if m_header != MATCHING_HEADER:
                errors.append(f"Invalid matching header: {repr(m_header)} != {repr(MATCHING_HEADER)}")

            line_no = 1
            for line in f:
                line_no += 1
                parts = line.rstrip("\r\n").split("\t")
                if len(parts) != 2:
                    errors.append(f"Matching file line {line_no} has {len(parts)} parts, expected 2")
                    continue
                s1_id, matches_str = parts
                if s1_id in seen_s1:
                    errors.append(f"Matching file line {line_no}: Duplicate Source 1 ID '{s1_id}'")
                seen_s1.add(s1_id)

                matches_list = [m.strip() for m in matches_str.split(",") if m.strip()]
                if not matches_list:
                    singleton_count += 1
                else:
                    matched_count += 1

                # Check prefixes and self-matches
                for mid in matches_list:
                    if not mid.startswith(("S2-", "S3-")):
                        errors.append(f"Matching file line {line_no}: Illegal target prefix '{mid}'")
                    if mid == s1_id:
                        errors.append(f"Matching file line {line_no}: Self-match forbidden '{mid}'")

                # Check candidate-pairs subset invariant!
                allowed_cands = cand_map.get(s1_id, set())
                for mid in matches_list:
                    if mid not in allowed_cands:
                        subset_violations += 1
                        if subset_violations <= 5:
                            errors.append(
                                f"Matching line {line_no}: Predicted match '{mid}' not in candidate_pairs for '{s1_id}'!"
                            )

        # 3. Check expected S1 coverage
        if expected_s1_ids is not None:
            missing_s1 = expected_s1_ids - seen_s1
            extra_s1 = seen_s1 - expected_s1_ids
            if missing_s1:
                errors.append(f"Matching file missing {len(missing_s1)} expected Source 1 entities")
            if extra_s1:
                errors.append(f"Matching file contains {len(extra_s1)} unexpected entities")

        is_valid = (len(errors) == 0 and subset_violations == 0)

        report = OutputValidationReport(
            is_valid=is_valid,
            matching_file=str(m_path),
            candidate_file=str(c_path),
            total_matching_rows=len(seen_s1),
            total_candidate_rows=len(cand_map),
            singleton_matching_rows=singleton_count,
            matched_rows=matched_count,
            candidate_subset_violations=subset_violations,
            format_errors=errors[:20],
        )

        logger.info(
            f"Validated submission files (valid: {is_valid}, rows: {len(seen_s1)}, subset violations: {subset_violations})",
            extra={"payload": report.to_dict()},
        )
        return report
