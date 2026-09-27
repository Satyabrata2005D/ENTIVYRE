"""
Comprehensive Data and Identifier Validation Engine for ENTIVYRE.
Phase 05: Schema, IDs, Source Prefixes, Missingness, and Referential Integrity.

Guarantees:
- Streaming validation of all 7 challenge files with bounded memory.
- Intra-file duplicate ID detection.
- Missingness profiling (null/empty/NaN counts and percentages).
- Cross-split ID disjointness verification (train vs test overlap = 0).
- Ground truth referential integrity verification (all targets in S2/S3).
"""
from __future__ import annotations

import os
import sys
import json
import time
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Set, Tuple, Any

from ber.io.ingestion import stream_source_chunks, stream_ground_truth_chunks, clean_field_text
from entivyre.contracts.schema import ENTITY_ID_PATTERN, parse_entity_id
from entivyre.utils.logger import get_logger

logger = get_logger("ber.validation.data_validator", stage="05_data_validation")


@dataclass(frozen=True)
class MissingnessStats:
    """Missingness statistics for columns in a source file."""
    total_records: int
    missing_names: int
    missing_addresses: int
    missing_countries: int
    missing_name_pct: float
    missing_address_pct: float
    missing_country_pct: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class FileValidationResult:
    """Validation report for an individual dataset file."""
    file_key: str
    file_path: str
    total_records: int
    duplicate_id_count: int
    invalid_id_count: int
    prefix_mismatch_count: int
    sample_duplicate_ids: List[str]
    sample_invalid_ids: List[str]
    missingness: MissingnessStats
    country_distribution: Dict[str, int]
    is_valid: bool
    execution_time_s: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class DatasetValidationReport:
    """Master validation report across the full dataset."""
    timestamp_utc: str
    all_files_valid: bool
    files: Dict[str, FileValidationResult]
    train_test_overlap_count: int
    ground_truth_orphan_targets_count: int
    ground_truth_s1_coverage_pct: float
    total_records_evaluated: int
    total_execution_time_s: float

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp_utc": self.timestamp_utc,
            "all_files_valid": self.all_files_valid,
            "train_test_overlap_count": self.train_test_overlap_count,
            "ground_truth_orphan_targets_count": self.ground_truth_orphan_targets_count,
            "ground_truth_s1_coverage_pct": self.ground_truth_s1_coverage_pct,
            "total_records_evaluated": self.total_records_evaluated,
            "total_execution_time_s": self.total_execution_time_s,
            "files": {k: v.to_dict() for k, v in self.files.items()},
        }


def validate_source_file(
    file_path: str | Path,
    file_key: str,
    expected_prefix: str,
    chunk_size: int = 50000,
) -> Tuple[FileValidationResult, Set[str]]:
    """
    Validates schema, IDs, prefixes, and missingness for a source file.
    Returns (FileValidationResult, set_of_all_entity_ids).
    """
    t0 = time.perf_counter()
    p = Path(file_path).resolve()
    seen_ids: Set[str] = set()
    dup_ids: Set[str] = set()
    invalid_ids: Set[str] = set()
    prefix_mismatches: Set[str] = set()
    countries: Dict[str, int] = {}

    missing_names = 0
    missing_addrs = 0
    missing_countries = 0
    total_records = 0

    for chunk, _ in stream_source_chunks(p, chunk_size=chunk_size, expected_prefix=expected_prefix):
        for rec in chunk:
            total_records += 1
            eid = rec.entity_id

            # Check duplicate ID
            if eid in seen_ids:
                dup_ids.add(eid)
            else:
                seen_ids.add(eid)

            # Check ID pattern
            if not ENTITY_ID_PATTERN.match(eid):
                invalid_ids.add(eid)

            # Check prefix
            if not eid.startswith(expected_prefix):
                prefix_mismatches.add(eid)

            # Missingness checks
            if not rec.name:
                missing_names += 1
            if not rec.address:
                missing_addrs += 1
            if not rec.country:
                missing_countries += 1
            else:
                countries[rec.country] = countries.get(rec.country, 0) + 1

    elapsed = time.perf_counter() - t0
    missingness = MissingnessStats(
        total_records=total_records,
        missing_names=missing_names,
        missing_addresses=missing_addrs,
        missing_countries=missing_countries,
        missing_name_pct=round(missing_names / total_records * 100, 4) if total_records else 0.0,
        missing_address_pct=round(missing_addrs / total_records * 100, 4) if total_records else 0.0,
        missing_country_pct=round(missing_countries / total_records * 100, 4) if total_records else 0.0,
    )

    # Source 1 requires complete names; noisy targets (S2, S3) tolerate rare missing names
    name_check = (missing_names == 0) if expected_prefix == "S1-" else (missing_names <= 500)

    is_valid = (
        len(dup_ids) == 0
        and len(invalid_ids) == 0
        and len(prefix_mismatches) == 0
        and name_check
    )

    result = FileValidationResult(
        file_key=file_key,
        file_path=str(p),
        total_records=total_records,
        duplicate_id_count=len(dup_ids),
        invalid_id_count=len(invalid_ids),
        prefix_mismatch_count=len(prefix_mismatches),
        sample_duplicate_ids=sorted(dup_ids)[:5],
        sample_invalid_ids=sorted(invalid_ids)[:5],
        missingness=missingness,
        country_distribution=countries,
        is_valid=is_valid,
        execution_time_s=elapsed,
    )
    return result, seen_ids


def validate_ground_truth_file(
    file_path: str | Path,
    file_key: str = "train_ground_truth",
    chunk_size: int = 50000,
) -> Tuple[FileValidationResult, Set[str], Set[str]]:
    """
    Validates schema and IDs for the ground truth file.
    Returns (FileValidationResult, set_of_s1_ids, set_of_matched_ids).
    """
    t0 = time.perf_counter()
    p = Path(file_path).resolve()
    seen_s1: Set[str] = set()
    dup_s1: Set[str] = set()
    all_matched: Set[str] = set()
    invalid_ids: Set[str] = set()
    prefix_mismatches: Set[str] = set()
    total_records = 0
    empty_matches = 0

    for chunk, _ in stream_ground_truth_chunks(p, chunk_size=chunk_size):
        for rec in chunk:
            total_records += 1
            s1_id = rec.source1_entity_id

            if s1_id in seen_s1:
                dup_s1.add(s1_id)
            else:
                seen_s1.add(s1_id)

            if not s1_id.startswith("S1-") or not ENTITY_ID_PATTERN.match(s1_id):
                invalid_ids.add(s1_id)

            if rec.is_singleton:
                empty_matches += 1
            else:
                for mid in rec.matched_entity_ids:
                    all_matched.add(mid)
                    if not (mid.startswith("S2-") or mid.startswith("S3-")):
                        prefix_mismatches.add(mid)

    elapsed = time.perf_counter() - t0
    missingness = MissingnessStats(
        total_records=total_records,
        missing_names=0,
        missing_addresses=0,
        missing_countries=0,
        missing_name_pct=0.0,
        missing_address_pct=0.0,
        missing_country_pct=0.0,
    )

    is_valid = len(dup_s1) == 0 and len(invalid_ids) == 0 and len(prefix_mismatches) == 0
    res = FileValidationResult(
        file_key=file_key,
        file_path=str(p),
        total_records=total_records,
        duplicate_id_count=len(dup_s1),
        invalid_id_count=len(invalid_ids),
        prefix_mismatch_count=len(prefix_mismatches),
        sample_duplicate_ids=sorted(dup_s1)[:5],
        sample_invalid_ids=sorted(invalid_ids)[:5],
        missingness=missingness,
        country_distribution={"singletons": empty_matches, "matched_entities": total_records - empty_matches},
        is_valid=is_valid,
        execution_time_s=elapsed,
    )
    return res, seen_s1, all_matched


def run_full_dataset_validation(
    dataset_root: str | Path,
    chunk_size: int = 50000,
) -> DatasetValidationReport:
    """
    Executes complete Phase 05 validation across all 7 challenge files:
    - Intra-file ID uniqueness and prefix integrity
    - Missingness across all fields
    - Train vs Test ID disjointness
    - Ground truth referential integrity against train S1, S2, and S3
    """
    t0 = time.perf_counter()
    root = Path(dataset_root).resolve()
    logger.info(f"Initiating full data validation at {root}")

    file_results: Dict[str, FileValidationResult] = {}
    train_ids: Dict[str, Set[str]] = {}
    test_ids: Dict[str, Set[str]] = {}

    # 1. Validate Train Sources
    for key, prefix in [("train_source1", "S1-"), ("train_source2", "S2-"), ("train_source3", "S3-")]:
        fpath = root / "train" / f"{key}.tsv"
        res, ids = validate_source_file(fpath, key, prefix, chunk_size=chunk_size)
        file_results[key] = res
        train_ids[key] = ids

    # 2. Validate Train Ground Truth
    gt_path = root / "train" / "train_ground_truth.tsv"
    gt_res, gt_s1_ids, gt_target_ids = validate_ground_truth_file(gt_path, chunk_size=chunk_size)
    file_results["train_ground_truth"] = gt_res

    # 3. Validate Test Sources
    for key, prefix in [("test_source1", "S1-"), ("test_source2", "S2-"), ("test_source3", "S3-")]:
        fpath = root / "test" / f"{key}.tsv"
        res, ids = validate_source_file(fpath, key, prefix, chunk_size=chunk_size)
        file_results[key] = res
        test_ids[key] = ids

    # 4. Referential Integrity Checks
    # Ground truth S1 coverage
    s1_train = train_ids.get("train_source1", set())
    s1_cov = (len(gt_s1_ids & s1_train) / len(s1_train) * 100) if s1_train else 0.0

    # Ground truth targets exist in S2 or S3
    valid_targets = train_ids.get("train_source2", set()) | train_ids.get("train_source3", set())
    orphan_targets = gt_target_ids - valid_targets

    # Train vs Test ID disjointness
    all_train_ids = set().union(*train_ids.values())
    all_test_ids = set().union(*test_ids.values())
    overlap = all_train_ids & all_test_ids

    total_records = sum(r.total_records for r in file_results.values())
    all_valid = (
        all(r.is_valid for r in file_results.values())
        and len(overlap) == 0
        and len(orphan_targets) == 0
        and s1_cov >= 99.999
    )

    elapsed = time.perf_counter() - t0
    report = DatasetValidationReport(
        timestamp_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        all_files_valid=all_valid,
        files=file_results,
        train_test_overlap_count=len(overlap),
        ground_truth_orphan_targets_count=len(orphan_targets),
        ground_truth_s1_coverage_pct=s1_cov,
        total_records_evaluated=total_records,
        total_execution_time_s=elapsed,
    )

    logger.info(
        "Data validation complete",
        extra={
            "payload": {
                "all_valid": report.all_files_valid,
                "total_records": report.total_records_evaluated,
                "train_test_overlap": report.train_test_overlap_count,
                "orphan_targets": report.ground_truth_orphan_targets_count,
                "elapsed_s": round(report.total_execution_time_s, 2),
            }
        },
    )
    return report
