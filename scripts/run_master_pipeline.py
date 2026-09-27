#!/usr/bin/env python3
"""
ENTIVYRE — Master End-to-End Pipeline Execution Engine.
Orchestrates and executes all stages of the project in sequence:
  Stage 1: Pre-Flight Readiness Verification
  Stage 2: Dataset Discovery & Cryptographic Hashing
  Stage 3: Dataset Ingestion & Cross-Split Integrity Validation
  Stage 4: Exploratory Data Profiling (EDA)
  Stage 5: Complete Unit, Integration & Adversarial Test Suite
  Stage 6: Fair-Play & Air-Gap Security Audit
  Stage 7: Submission Package Assembly & Verification
  Stage 8: Official Challenge Validator Verification
  Stage 9: Clean-Room Sandbox Reproducibility Verification
  Stage 10: 17-Point Master Release Certification
"""
import os
import sys
import time
import argparse
import subprocess
from pathlib import Path

# Add project root and source directory to path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "code" / "business_entity_resolution" / "src"))

from ber.security.fair_play import FairPlayAuditor
from ber.outputs.serializer import OutputSerializer
from ber.validation.official_validator import OfficialValidatorBridge
from ber.utils.profiler import get_peak_memory_mb


def print_banner(text: str, ch: str = "="):
    line = ch * 65
    print(f"\n{line}")
    print(f" {text}")
    print(f"{line}")


def run_stage(stage_num: int, title: str, cmd: list, cwd: Path = PROJECT_ROOT) -> bool:
    print_banner(f"STAGE {stage_num:02d}: {title}", "-")
    start = time.time()
    proc = subprocess.run(cmd, cwd=cwd, text=True)
    elapsed = time.time() - start
    success = (proc.returncode == 0)
    status_str = "SUCCESS" if success else "FAILED"
    print(f"\n>> Stage {stage_num:02d} [{status_str}] in {elapsed:.2f}s (Peak RSS: {get_peak_memory_mb():.1f} MB)")
    return success


def main():
    parser = argparse.ArgumentParser(description="ENTIVYRE Master End-to-End Pipeline Runner.")
    parser.add_argument("--test-dir", default="student_resource/dataset/test", help="Test dataset directory")
    parser.add_argument("--train-dir", default="student_resource/dataset/train", help="Train dataset directory")
    parser.add_argument("--re-run-inference", action="store_true", help="Re-execute full 1.73M test inference before validation")
    args = parser.parse_args()

    overall_start = time.time()
    print_banner("ENTIVYRE — MASTER END-TO-END EXECUTION PIPELINE")
    print(f"Project Root:    {PROJECT_ROOT}")
    print(f"Test Directory:  {args.test_dir}")
    print(f"Train Directory: {args.train_dir}")
    print(f"Start Time:      {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}")
    print("=" * 65)

    results = {}

    # Stage 1: Pre-flight Readiness Check
    results["01_readiness"] = run_stage(
        1, "Pre-Flight Readiness Check",
        [sys.executable, "scripts/check_readiness.py"]
    )
    if not results["01_readiness"]:
        print("Readiness check failed. Aborting pipeline.", file=sys.stderr)
        sys.exit(1)

    # Stage 2: Dataset Discovery & Manifest
    results["02_manifest"] = run_stage(
        2, "Dataset Discovery & Cryptographic Manifest Generation",
        [sys.executable, "scripts/generate_manifest.py", "--dataset-dir", "student_resource/dataset"]
    )

    # Stage 3: Dataset Ingestion & Validation
    results["03_validation"] = run_stage(
        3, "Dataset Ingestion & Cross-Split Integrity Validation",
        [sys.executable, "scripts/validate_dataset.py", "--dataset-dir", "student_resource/dataset"]
    )

    # Stage 4: Dataset Profiling & EDA
    results["04_profiling"] = run_stage(
        4, "Dataset Statistical Profiling & Entity Distribution Analysis",
        [sys.executable, "scripts/profile_dataset.py", "--dataset-dir", "student_resource/dataset", "--sample-limit", "50000"]
    )

    # Stage 5: Comprehensive Unit & Adversarial Test Suite
    env = os.environ.copy()
    env["PYTHONPATH"] = str((PROJECT_ROOT / "code" / "business_entity_resolution" / "src").resolve()) + ":" + env.get("PYTHONPATH", "")
    print_banner("STAGE 05: Complete Unit, Integration & Adversarial Test Suite", "-")
    t0 = time.time()
    test_proc = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "tests"],
        cwd=PROJECT_ROOT, env=env, text=True
    )
    results["05_tests"] = (test_proc.returncode == 0)
    print(f"\n>> Stage 05 [{'SUCCESS' if results['05_tests'] else 'FAILED'}] in {time.time() - t0:.2f}s")

    # Optional Re-run Inference
    if args.re_run_inference:
        results["05b_inference"] = run_stage(
            5, "Full-Scale Test Inference (1.73M S1 records)",
            [sys.executable, "scripts/run_test_inference.py", "--test-dir", args.test_dir, "--partitioned", "--validate"]
        )

    # Stage 6: Fair-Play & License Audit
    print_banner("STAGE 06: Fair-Play, Air-Gap & Open-Source License Audit", "-")
    src_dir = PROJECT_ROOT / "code" / "business_entity_resolution" / "src"
    fp_report = FairPlayAuditor.audit_source_directory(src_dir)
    print(f"  Source Tree Inspected:    {src_dir}")
    print(f"  Files Scanned:            {fp_report.audited_files_count}")
    print(f"  Banned Imports Found:     {len(fp_report.banned_imports_found)}")
    print(f"  Banned Domains Found:     {len(fp_report.banned_urls_found)}")
    print(f"  Permissive License Audit: {'PASS' if fp_report.license_audit_passed else 'FAIL'}")
    print(f"  Fair-Play Compliance:     {'PASS' if fp_report.is_compliant else 'FAIL'}")
    results["06_fair_play"] = fp_report.is_compliant and fp_report.license_audit_passed

    # Stage 7: Submission Packaging
    results["07_package"] = run_stage(
        7, "Submission Package Assembly (<team_name>_submission.zip)",
        [sys.executable, "scripts/package_submission.py"]
    )

    # Stage 8: Official Challenge Submission Validator
    results["08_official_validator"] = run_stage(
        8, "Official Challenge Submission Validator Verification",
        [
            sys.executable, "scripts/run_official_validator.py",
            "--matching", "output/matching_results.tsv",
            "--candidate", "output/candidate_pairs.tsv",
            "--test-dir", args.test_dir,
        ]
    )

    # Stage 9: Clean-Room Sandbox Reproducibility Verification
    results["09_clean_room"] = run_stage(
        9, "Clean-Room Sandbox Extraction & Execution Verification",
        [sys.executable, "scripts/verify_clean_room.py", "--test-dir", args.test_dir]
    )

    # Stage 10: 17-Point Final Release Audit Certification
    results["10_release_audit"] = run_stage(
        10, "17-Point Master Release Certification & Report Generation",
        [sys.executable, "scripts/run_release_audit.py"]
    )

    # Final Summary Dashboard
    total_elapsed = time.time() - overall_start
    all_passed = all(results.values())

    print_banner("ENTIVYRE — MASTER EXECUTION SUMMARY", "=")
    print(f"Overall Status:    {'ALL STAGES PASSED (CERTIFIED FOR RELEASE)' if all_passed else 'FAILED'}")
    print(f"Total Time:        {total_elapsed:.2f}s (~{total_elapsed/60:.1f} minutes)")
    print(f"Peak Memory:       {get_peak_memory_mb():.1f} MB")
    print("\nStage Breakdown:")
    for k, v in results.items():
        status_icon = "✓ PASS" if v else "✗ FAIL"
        print(f"  {k:22s} : {status_icon}")
    print("=" * 65)

    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
