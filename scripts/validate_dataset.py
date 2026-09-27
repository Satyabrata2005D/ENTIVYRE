#!/usr/bin/env python3
"""
CLI script to execute Phase 05: Data and Identifier Validation.
Outputs artifacts/reports/data_validation_report.json.
"""
import sys
import json
import time
from pathlib import Path

_root = Path(__file__).resolve().parent.parent
_ber_src = _root / "code" / "business_entity_resolution" / "src"
if str(_ber_src) not in sys.path:
    sys.path.insert(0, str(_ber_src))

from ber.validation.data_validator import run_full_dataset_validation
from entivyre.config import load_config

def main():
    cfg = load_config()
    dataset_root = _root / cfg.paths.dataset_root
    out_dir = _root / cfg.paths.artifacts_dir / "reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    report_path = out_dir / "data_validation_report.json"

    print("=== ENTIVYRE: Phase 05 Data Validation Pipeline ===")
    print(f"Dataset root: {dataset_root}")
    t0 = time.perf_counter()

    report = run_full_dataset_validation(dataset_root, chunk_size=cfg.runtime.chunk_size)
    d = report.to_dict()

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2)

    elapsed = time.perf_counter() - t0
    print(f"\nValidation completed in {elapsed:.2f}s:")
    print(f"Overall Valid: {report.all_files_valid}")
    print(f"Total Records Evaluated: {report.total_records_evaluated:,}")
    print(f"Train/Test Overlap: {report.train_test_overlap_count}")
    print(f"Ground Truth S1 Coverage: {report.ground_truth_s1_coverage_pct:.4f}%")
    print(f"Ground Truth Orphan Targets: {report.ground_truth_orphan_targets_count}")
    print(f"Report saved to: {report_path}")

    for k, v in report.files.items():
        print(f"  - {k}: records={v.total_records:,}, missing_addr={v.missingness.missing_address_pct:.2f}%, valid={v.is_valid}")

    if not report.all_files_valid:
        print("\nERROR: Data validation found blocking contract violations!")
        sys.exit(1)

    print("\nSUCCESS: All datasets conform strictly to schema and integrity contracts.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
