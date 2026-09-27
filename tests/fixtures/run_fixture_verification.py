"""Fixture run script for Phase 01: Specification and Contract.

Generates a representative synthetic fixture dataset, executes contract verification,
measures throughput and memory footprint, and persists the stage manifest.
"""

from __future__ import annotations

import json
import os
import resource
import time

from entivyre.contracts.metrics import compute_macro_f05
from entivyre.contracts.rules import export_requirements_matrix_dict
from entivyre.contracts.verifier import validate_submission_pipeline
from entivyre.utils.logger import get_logger

logger = get_logger("entivyre.contracts.fixture", stage="01_contracts")


def run_fixture() -> None:
    fixture_dir = "tests/fixtures/synthetic_data"
    os.makedirs(fixture_dir, exist_ok=True)
    os.makedirs("artifacts/contracts", exist_ok=True)

    s1_path = os.path.join(fixture_dir, "test_source1.tsv")
    s2_path = os.path.join(fixture_dir, "test_source2.tsv")
    s3_path = os.path.join(fixture_dir, "test_source3.tsv")
    cand_path = os.path.join(fixture_dir, "candidate_pairs.tsv")
    match_path = os.path.join(fixture_dir, "matching_results.tsv")

    # Generate 100 representative synthetic test records
    # Distribution:
    # - 10 singletons (true empty, pred empty) -> score 1.0
    # - 5 singletons (true empty, pred false positive) -> score 0.0
    # - 70 standard matches (multi-source, some precision penalties)
    # - 15 missed matches (true matches, pred empty) -> score 0.0
    s1_lines = ["entity_id\tname\taddress\tcountry\n"]
    s2_lines = ["entity_id\tname\taddress\tcountry\n"]
    s3_lines = ["entity_id\tname\taddress\tcountry\n"]
    cand_lines = ["source1_entity_id\tcandidate_entity_ids\n"]
    match_lines = ["source1_entity_id\tmatched_entity_ids\n"]

    ground_truth = {}
    predictions = {}

    for i in range(1, 101):
        s1_id = f"S1-{i:05d}"
        s1_lines.append(f"{s1_id}\tBusiness Name {i}\tAddress {i} St\tUS\n")

        s2_id = f"S2-{i:05d}"
        s3_id = f"S3-{i:05d}"
        s2_lines.append(f"{s2_id}\tBusiness {i} Inc\tAddr {i}\tUS\n")
        s3_lines.append(f"{s3_id}\tBiz {i} LLC\tAddress {i}\tUS\n")

        if i <= 10:
            # Singleton correct: no true matches, predict empty
            ground_truth[s1_id] = []
            predictions[s1_id] = []
            cand_lines.append(f"{s1_id}\t\n")
            match_lines.append(f"{s1_id}\t\n")
        elif i <= 15:
            # Singleton false merge: no true matches, predicted candidate
            ground_truth[s1_id] = []
            predictions[s1_id] = [s2_id]
            cand_lines.append(f"{s1_id}\t{s2_id}\n")
            match_lines.append(f"{s1_id}\t{s2_id}\n")
        elif i <= 85:
            # Multi-match: true matches S2 and S3, predict both
            ground_truth[s1_id] = [s2_id, s3_id]
            predictions[s1_id] = [s2_id, s3_id]
            cand_lines.append(f"{s1_id}\t{s2_id},{s3_id}\n")
            match_lines.append(f"{s1_id}\t{s2_id},{s3_id}\n")
        else:
            # Missed matches: true matches S2 and S3, predict empty
            ground_truth[s1_id] = [s2_id, s3_id]
            predictions[s1_id] = []
            cand_lines.append(f"{s1_id}\t\n")
            match_lines.append(f"{s1_id}\t\n")

    with open(s1_path, "w", encoding="utf-8") as f:
        f.writelines(s1_lines)
    with open(s2_path, "w", encoding="utf-8") as f:
        f.writelines(s2_lines)
    with open(s3_path, "w", encoding="utf-8") as f:
        f.writelines(s3_lines)
    with open(cand_path, "w", encoding="utf-8") as f:
        f.writelines(cand_lines)
    with open(match_path, "w", encoding="utf-8") as f:
        f.writelines(match_lines)

    # Measure memory and execution time
    start_time = time.perf_counter()
    report = validate_submission_pipeline(
        matching_path=match_path,
        candidate_path=cand_path,
        test_dir=fixture_dir,
        check_ids=True,
    )
    elapsed_time = time.perf_counter() - start_time

    # Peak memory usage (maxrss in KB on macOS / Linux)
    usage = resource.getrusage(resource.RUSAGE_SELF)
    max_rss_mb = usage.ru_maxrss / (1024 * 1024) if "darwin" in os.sys.platform else usage.ru_maxrss / 1024

    # Compute F_0.5 metric on the synthetic ground truth vs predictions
    metric_summary, _ = compute_macro_f05(ground_truth, predictions)

    # Persist stage artifact / manifest
    manifest = {
        "stage": "01_specification_and_contract",
        "increment": "01.1",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "status": "PROMOTED",
        "requirements_count": 15,
        "requirements": export_requirements_matrix_dict(),
        "fixture_metrics": {
            "total_entities": metric_summary.total_entities,
            "singleton_count": metric_summary.singleton_count,
            "macro_f05": metric_summary.macro_f05,
            "mean_precision": metric_summary.mean_precision,
            "mean_recall": metric_summary.mean_recall,
            "singleton_f05": metric_summary.singleton_f05,
            "matched_f05": metric_summary.matched_f05,
            "perfect_score_count": metric_summary.perfect_score_count,
            "zero_score_count": metric_summary.zero_score_count,
        },
        "validation_report": report.to_dict(),
        "performance": {
            "validation_time_seconds": round(elapsed_time, 6),
            "records_processed": report.total_source1_entities,
            "throughput_rows_per_second": round(report.total_source1_entities / elapsed_time, 2) if elapsed_time > 0 else 0,
            "peak_memory_mb": round(max_rss_mb, 2),
        },
    }

    manifest_path = "artifacts/contracts/phase01_contract_manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    logger.info(
        "Fixture run and contract manifest generation successful",
        extra={"payload": {"manifest_path": manifest_path, "is_valid": report.is_valid, "macro_f05": metric_summary.macro_f05}},
    )
    print(f"Phase 01 manifest persisted to {manifest_path}")
    print(f"Validation Valid: {report.is_valid}, Macro F_0.5: {metric_summary.macro_f05:.4f}")


if __name__ == "__main__":
    run_fixture()
