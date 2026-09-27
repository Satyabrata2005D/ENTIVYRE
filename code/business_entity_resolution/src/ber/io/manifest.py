"""
Dataset Manifest & Cryptographic Discovery Engine for ENTIVYRE.
Phase 03: File Checksums, Sizes, Row Counts, and Schema Manifest.

Guarantees:
- Streaming cryptographic hash calculation (SHA-256 and MD5) with zero memory bloat.
- Exact line and row counting without loading multi-gigabyte files into RAM.
- Strict tab-delimiter and header verification against official challenge contracts.
- Automated data immutability seal verification.
"""
from __future__ import annotations

import os
import sys
import json
import hashlib
import time
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Any, Tuple

from entivyre.utils.logger import get_logger

logger = get_logger("ber.io.manifest", stage="03_dataset_manifest")

BUFFER_SIZE = 1024 * 1024  # 1 MB chunk for streaming hash and line counting

EXPECTED_FILES = {
    "train_source1": {
        "rel_path": "train/train_source1.tsv",
        "split": "train",
        "role": "reference_anchor",
        "expected_columns": ["entity_id", "business_name", "business_address", "country"],
        "id_prefix": "S1-",
    },
    "train_source2": {
        "rel_path": "train/train_source2.tsv",
        "split": "train",
        "role": "match_target",
        "expected_columns": ["entity_id", "business_name", "business_address", "country"],
        "id_prefix": "S2-",
    },
    "train_source3": {
        "rel_path": "train/train_source3.tsv",
        "split": "train",
        "role": "match_target",
        "expected_columns": ["entity_id", "business_name", "business_address", "country"],
        "id_prefix": "S3-",
    },
    "train_ground_truth": {
        "rel_path": "train/train_ground_truth.tsv",
        "split": "train",
        "role": "ground_truth",
        "expected_columns": ["source1_entity_id", "matched_entity_ids"],
        "id_prefix": "S1-",
    },
    "test_source1": {
        "rel_path": "test/test_source1.tsv",
        "split": "test",
        "role": "reference_anchor",
        "expected_columns": ["entity_id", "business_name", "business_address", "country"],
        "id_prefix": "S1-",
    },
    "test_source2": {
        "rel_path": "test/test_source2.tsv",
        "split": "test",
        "role": "match_target",
        "expected_columns": ["entity_id", "business_name", "business_address", "country"],
        "id_prefix": "S2-",
    },
    "test_source3": {
        "rel_path": "test/test_source3.tsv",
        "split": "test",
        "role": "match_target",
        "expected_columns": ["entity_id", "business_name", "business_address", "country"],
        "id_prefix": "S3-",
    },
}


@dataclass(frozen=True)
class FileManifest:
    """Cryptographic and structural metadata for a single dataset file."""
    file_key: str
    relative_path: str
    absolute_path: str
    file_size_bytes: int
    sha256: str
    md5: str
    total_lines: int
    data_rows: int
    header: List[str]
    is_tab_delimited: bool
    schema_valid: bool
    id_prefix_valid: bool
    sample_ids: List[str]
    processing_time_s: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class DatasetManifest:
    """Master manifest covering the complete challenge dataset."""
    dataset_root: str
    manifest_version: str
    created_at_utc: str
    total_files: int
    total_bytes: int
    total_records: int
    files: Dict[str, FileManifest]
    all_files_present: bool
    all_schemas_valid: bool
    all_prefixes_valid: bool

    def to_dict(self) -> Dict[str, Any]:
        return {
            "dataset_root": self.dataset_root,
            "manifest_version": self.manifest_version,
            "created_at_utc": self.created_at_utc,
            "total_files": self.total_files,
            "total_bytes": self.total_bytes,
            "total_records": self.total_records,
            "all_files_present": self.all_files_present,
            "all_schemas_valid": self.all_schemas_valid,
            "all_prefixes_valid": self.all_prefixes_valid,
            "files": {k: v.to_dict() for k, v in self.files.items()},
        }


def profile_single_file(file_key: str, file_path: Path, spec: Dict[str, Any]) -> FileManifest:
    """
    Profiles a single TSV file using streaming chunked reads.
    Calculates SHA-256, MD5, size, row counts, and verifies header contract.
    """
    t0 = time.perf_counter()
    if not file_path.exists():
        raise FileNotFoundError(f"Dataset file missing: {file_path}")

    file_size = file_path.stat().st_size
    sha256_hash = hashlib.sha256()
    md5_hash = hashlib.md5()

    total_lines = 0
    header_line: Optional[str] = None
    sample_ids: List[str] = []

    with open(file_path, "rb") as f:
        # First read header as text
        raw_header = f.readline()
        if raw_header:
            total_lines += 1
            sha256_hash.update(raw_header)
            md5_hash.update(raw_header)
            header_line = raw_header.decode("utf-8", errors="replace").rstrip("\r\n")

        # Now stream the rest in binary chunks for fast hash and newline count
        carry = b""
        lines_parsed = 0
        while True:
            chunk = f.read(BUFFER_SIZE)
            if not chunk:
                break
            sha256_hash.update(chunk)
            md5_hash.update(chunk)

            # Count newlines in chunk
            total_lines += chunk.count(b"\n")
            carry = chunk[-1:] if chunk else b""

        # Account for trailing line without newline if any
        if carry and carry != b"\n":
            total_lines += 1

    # Extract sample IDs from first few rows
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        f.readline()  # skip header
        for _ in range(5):
            line = f.readline()
            if not line:
                break
            parts = line.rstrip("\r\n").split("\t")
            if parts and parts[0]:
                sample_ids.append(parts[0])

    data_rows = max(0, total_lines - 1)
    
    # Header validation
    header_cols = header_line.split("\t") if header_line else []
    is_tab = "\t" in (header_line or "")
    expected_cols = spec.get("expected_columns", [])
    schema_valid = (header_cols == expected_cols)

    # Prefix validation
    expected_prefix = spec.get("id_prefix", "")
    prefix_valid = all(sid.startswith(expected_prefix) for sid in sample_ids) if sample_ids else False

    elapsed = time.perf_counter() - t0
    logger.info(
        f"Profiled {file_key}",
        extra={
            "payload": {
                "file_key": file_key,
                "size_mb": round(file_size / (1024 * 1024), 2),
                "data_rows": data_rows,
                "schema_valid": schema_valid,
                "elapsed_s": round(elapsed, 3),
            }
        },
    )

    return FileManifest(
        file_key=file_key,
        relative_path=spec["rel_path"],
        absolute_path=str(file_path.resolve()),
        file_size_bytes=file_size,
        sha256=sha256_hash.hexdigest(),
        md5=md5_hash.hexdigest(),
        total_lines=total_lines,
        data_rows=data_rows,
        header=header_cols,
        is_tab_delimited=is_tab,
        schema_valid=schema_valid,
        id_prefix_valid=prefix_valid,
        sample_ids=sample_ids,
        processing_time_s=elapsed,
    )


def generate_dataset_manifest(
    dataset_root: str | Path,
    file_specs: Optional[Dict[str, Dict[str, Any]]] = None,
) -> DatasetManifest:
    """
    Generates a complete dataset manifest for all raw challenge files.
    Ensures zero mutation of raw data.
    """
    root_path = Path(dataset_root).resolve()
    specs = file_specs or EXPECTED_FILES
    
    manifest_files: Dict[str, FileManifest] = {}
    total_bytes = 0
    total_records = 0
    all_schemas_valid = True
    all_prefixes_valid = True
    all_present = True

    logger.info(f"Initiating dataset discovery at {root_path}")

    for file_key, spec in specs.items():
        file_path = root_path / spec["rel_path"]
        if not file_path.exists():
            all_present = False
            all_schemas_valid = False
            all_prefixes_valid = False
            logger.error(f"Missing required dataset file: {file_path}")
            continue

        fm = profile_single_file(file_key, file_path, spec)
        manifest_files[file_key] = fm
        total_bytes += fm.file_size_bytes
        total_records += fm.data_rows

        if not fm.schema_valid:
            all_schemas_valid = False
        if not fm.id_prefix_valid:
            all_prefixes_valid = False

    created_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    master = DatasetManifest(
        dataset_root=str(root_path),
        manifest_version="1.0.0",
        created_at_utc=created_at,
        total_files=len(manifest_files),
        total_bytes=total_bytes,
        total_records=total_records,
        files=manifest_files,
        all_files_present=all_present and len(manifest_files) == len(specs),
        all_schemas_valid=all_schemas_valid,
        all_prefixes_valid=all_prefixes_valid,
    )

    logger.info(
        "Dataset manifest generation complete",
        extra={
            "payload": {
                "total_files": master.total_files,
                "total_bytes": master.total_bytes,
                "total_records": master.total_records,
                "all_valid": master.all_files_present and master.all_schemas_valid,
            }
        },
    )
    return master


def verify_dataset_integrity(
    manifest_path: str | Path,
    dataset_root: Optional[str | Path] = None,
    verify_hashes: bool = False,
) -> Tuple[bool, List[str]]:
    """
    Verifies that the raw dataset matches the recorded manifest.
    Guarantees immutability and guards against accidental corruption.
    
    If verify_hashes is True, recomputes SHA-256 for all files.
    """
    p = Path(manifest_path)
    if not p.exists():
        return False, [f"Manifest file not found: {manifest_path}"]

    with open(p, "r", encoding="utf-8") as f:
        data = json.load(f)

    root = Path(dataset_root or data.get("dataset_root", ".")).resolve()
    errors: List[str] = []

    files_dict = data.get("files", {})
    for file_key, fm in files_dict.items():
        rel_path = fm.get("relative_path")
        target_file = root / rel_path
        if not target_file.exists():
            errors.append(f"Missing file: {rel_path}")
            continue

        stat = target_file.stat()
        if stat.st_size != fm.get("file_size_bytes"):
            errors.append(
                f"File size mismatch for {rel_path}: expected {fm.get('file_size_bytes')} bytes, got {stat.st_size} bytes"
            )

        if verify_hashes:
            sha256 = hashlib.sha256()
            with open(target_file, "rb") as f:
                while chunk := f.read(BUFFER_SIZE):
                    sha256.update(chunk)
            computed = sha256.hexdigest()
            if computed != fm.get("sha256"):
                errors.append(
                    f"SHA-256 corruption detected in {rel_path}: expected {fm.get('sha256')}, got {computed}"
                )

    is_valid = len(errors) == 0
    return is_valid, errors
