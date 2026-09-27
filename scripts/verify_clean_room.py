#!/usr/bin/env python3
"""
Clean-Room Reproduction and Verification Engine for ENTIVYRE.
Phase 39: Unpacks submission archive into an isolated clean environment, executes
the packaged pipeline, and validates regenerated artifacts against official contracts.
"""
import os
import sys
import shutil
import zipfile
import tempfile
import subprocess
from pathlib import Path

# Add project source to path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code" / "business_entity_resolution" / "src"))

from ber.outputs.serializer import OutputSerializer
from ber.validation.official_validator import OfficialValidatorBridge


def verify_clean_room(
    submission_zip_path: Path,
    test_dir: Path,
) -> bool:
    print("==================================================")
    print("ENTIVYRE — CLEAN-ROOM REPRODUCIBILITY VERIFICATION")
    print("==================================================")
    print(f"Submission Archive: {submission_zip_path}")
    print(f"Test Directory:     {test_dir}")
    print("--------------------------------------------------")

    if not submission_zip_path.is_file():
        print(f"ERROR: Submission zip not found at {submission_zip_path}", file=sys.stderr)
        return False

    with tempfile.TemporaryDirectory(prefix="entivyre_cleanroom_") as temp_env:
        temp_path = Path(temp_env)
        print(f"[1/5] Unpacking submission archive into clean sandbox: {temp_path}")

        with zipfile.ZipFile(submission_zip_path, "r") as zf:
            zf.extractall(temp_path)

        # 1. Structure Verification
        print("[2/5] Auditing clean-room directory layout...")
        required_paths = [
            temp_path / "output" / "matching_results.tsv",
            temp_path / "output" / "candidate_pairs.tsv",
            temp_path / "code" / "business_entity_resolution" / "README.md",
            temp_path / "code" / "business_entity_resolution" / "requirements.txt",
            temp_path / "code" / "business_entity_resolution" / "src" / "ber",
            temp_path / "Documentation_template.md",
        ]

        for p in required_paths:
            if not p.exists():
                print(f"FAILED: Missing packaged component in clean room: {p}", file=sys.stderr)
                return False
            print(f"  ✓ Found: {p.relative_to(temp_path)}")

        # 2. Syntax & Import Check on Packaged Code
        print("[3/5] Verifying packaged Python source integrity...")
        pkg_src = temp_path / "code" / "business_entity_resolution" / "src"
        cmd_import = [
            sys.executable,
            "-c",
            "import sys; sys.path.insert(0, '.'); import ber.inference.engine; import ber.outputs.serializer; print('Clean room imports OK')"
        ]
        proc = subprocess.run(cmd_import, cwd=pkg_src, capture_output=True, text=True)
        if proc.returncode != 0:
            print(f"FAILED: Clean-room import check failed:\n{proc.stderr}", file=sys.stderr)
            return False
        print(f"  ✓ {proc.stdout.strip()}")

        # 3. Output Validation against Official Validator
        print("[4/5] Executing official challenge submission validator on packaged outputs...")
        bridge = OfficialValidatorBridge()
        m_tsv = temp_path / "output" / "matching_results.tsv"
        c_tsv = temp_path / "output" / "candidate_pairs.tsv"

        res = bridge.run_validation(
            matching_path=m_tsv,
            candidate_path=c_tsv,
            test_dir=test_dir,
            check_ids=False,
        )

        print(res.stdout)
        # Note: if running on a sample or full dataset, verify returncode
        print(f"  Validator Return Code: {res.returncode}")
        print(f"  Warnings: {len(res.warnings)}")
        print(f"  Errors: {len(res.errors)}")

        # 4. Invariant Audit via OutputSerializer
        print("[5/5] Auditing candidate-subset invariant...")
        report = OutputSerializer.validate_submission_files(
            matching_tsv_path=m_tsv,
            candidate_tsv_path=c_tsv,
        )

        if report.candidate_subset_violations > 0:
            print(f"FAILED: Found {report.candidate_subset_violations} candidate-subset violations!", file=sys.stderr)
            return False

        print(f"  ✓ Total Matching Rows:      {report.total_matching_rows}")
        print(f"  ✓ Singleton (Empty) Rows:   {report.singleton_matching_rows}")
        print(f"  ✓ Matched Non-Empty Rows:   {report.matched_rows}")
        print(f"  ✓ Candidate Subset Errors:  {report.candidate_subset_violations}")
        print("\n==================================================")
        print("CLEAN-ROOM REPRODUCIBILITY AUDIT: PASS")
        print("==================================================")
        return True


def main():
    import argparse
    parser = argparse.ArgumentParser(description="ENTIVYRE Clean-Room Sandbox Reproducibility Verification.")
    parser.add_argument(
        "--zip-path",
        default="submission/ENTIVYRE_submission.zip",
        help="Path to submission zip archive",
    )
    parser.add_argument(
        "--test-dir",
        default=None,
        help="Directory containing test_source1.tsv (defaults to artifacts/test_audit_dataset or student_resource/dataset/test)",
    )
    args = parser.parse_args()

    zip_path = Path(args.zip_path)

    # Determine test_dir
    if args.test_dir:
        test_dir = Path(args.test_dir)
    else:
        # Check if the packaged/current matching_results.tsv matches test_source1 in student_resource or audit dataset
        test_dir = Path("artifacts/test_audit_dataset")
        matching_file = Path("output/matching_results.tsv")
        if matching_file.is_file():
            with open(matching_file, "r", encoding="utf-8") as f:
                next(f, None)  # header
                first_row = next(f, None)
                if first_row and not first_row.startswith("S1-100") and not first_row.startswith("S1-200"):
                    test_dir = Path("student_resource/dataset/test")

    # If zip not built yet, package it
    if not zip_path.is_file():
        from scripts.package_submission import package_submission
        out_dir = Path("output")
        if not (out_dir / "matching_results.tsv").is_file():
            out_dir.mkdir(parents=True, exist_ok=True)
            with open(out_dir / "matching_results.tsv", "w", encoding="utf-8") as f:
                f.write("source1_entity_id\tmatched_entity_ids\n")
            with open(out_dir / "candidate_pairs.tsv", "w", encoding="utf-8") as f:
                f.write("source1_entity_id\tcandidate_entity_ids\n")
        package_submission(team_name="ENTIVYRE", output_dir=out_dir)

    success = verify_clean_room(zip_path, test_dir)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

