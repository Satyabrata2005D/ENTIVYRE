#!/usr/bin/env python3
"""
Post-inference verification, comparison, validation, and packaging script for ENTIVYRE.
Implements Phases 7, 8, and 9 of the mandate.
"""
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile
from datetime import datetime
from pathlib import Path


def sha256_file(path: Path, chunk_size: int = 1048576) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()


def main():
    print("==================================================")
    print("PHASE 7 — VERIFY THAT OUTPUT HAS CHANGED")
    print("==================================================")

    old_match_path = Path("output/backup_challenger_005_old/matching_results.tsv")
    old_cand_path = Path("output/backup_challenger_005_old/candidate_pairs.tsv")
    new_match_path = Path("output/matching_results.tsv")
    new_cand_path = Path("output/candidate_pairs.tsv")

    if not new_match_path.exists():
        print(f"ERROR: {new_match_path} does not exist! Inference did not produce output.", file=sys.stderr)
        sys.exit(1)
    if not new_cand_path.exists():
        print(f"ERROR: {new_cand_path} does not exist!", file=sys.stderr)
        sys.exit(1)

    # 1. Stat & Timestamps
    stat_new_m = new_match_path.stat()
    stat_new_c = new_cand_path.stat()
    print(f"New matching_results.tsv:")
    print(f"  Size: {stat_new_m.st_size:,} bytes")
    print(f"  Modified: {datetime.fromtimestamp(stat_new_m.st_mtime).isoformat()}")

    print(f"New candidate_pairs.tsv:")
    print(f"  Size: {stat_new_c.st_size:,} bytes")
    print(f"  Modified: {datetime.fromtimestamp(stat_new_c.st_mtime).isoformat()}")

    # 2. SHA-256 calculation
    print("\nCalculating SHA-256 for newly generated matching_results.tsv...")
    new_match_sha256 = sha256_file(new_match_path)
    print(f"NEW MATCHING SHA256:  {new_match_sha256}")

    old_match_sha256 = "0aedd76d1ca9d440f7950dd28acd8651a52a41fe6497353b7e324cc336a5f79e"
    print(f"OLD MATCHING SHA256:  {old_match_sha256}")

    is_identical = (new_match_sha256 == old_match_sha256)
    print(f"IDENTICAL:            {'YES' if is_identical else 'NO'}")

    print("\nCalculating SHA-256 for candidate_pairs.tsv...")
    new_cand_sha256 = sha256_file(new_cand_path)
    old_cand_sha256 = "547adefba6d643270d54b4ed3a778b230902bdbf0997d3d5189d3d02cd8ad0a4"
    print(f"NEW CANDIDATE SHA256: {new_cand_sha256}")
    print(f"OLD CANDIDATE SHA256: {old_cand_sha256}")

    # 3. Row-by-row comparison between old and new matching_results.tsv
    print("\nStreaming comparison of matching_results.tsv rows...")
    changed_rows = 0
    total_rows = 0
    old_matches_total = 0
    new_matches_total = 0

    sample_diffs = []

    with open(old_match_path, "r", encoding="utf-8") as f_old, \
         open(new_match_path, "r", encoding="utf-8") as f_new:
        
        header_old = f_old.readline()
        header_new = f_new.readline()

        for line_num, (l_old, l_new) in enumerate(zip(f_old, f_new), start=2):
            total_rows += 1
            p_old = l_old.rstrip("\r\n").split("\t")
            p_new = l_new.rstrip("\r\n").split("\t")

            m_old = p_old[1] if len(p_old) > 1 else ""
            m_new = p_new[1] if len(p_new) > 1 else ""

            if m_old:
                old_matches_total += len(m_old.split(","))
            if m_new:
                new_matches_total += len(m_new.split(","))

            if m_old != m_new:
                changed_rows += 1
                if len(sample_diffs) < 10:
                    sample_diffs.append((p_old[0], m_old, m_new))

    print(f"Total S1 Entity Rows:   {total_rows:,}")
    print(f"Changed Matching Rows: {changed_rows:,} ({changed_rows/total_rows*100:.3f}%)")
    print(f"Old Total Match Count: {old_matches_total:,}")
    print(f"New Total Match Count: {new_matches_total:,}")
    print(f"Net Match Difference:  {new_matches_total - old_matches_total:+,}")

    if sample_diffs:
        print("\nSample Changed Predictions:")
        for s1_id, old_m, new_m in sample_diffs[:5]:
            print(f"  Anchor: {s1_id}")
            print(f"    Old: {old_m}")
            print(f"    New: {new_m}")

    if is_identical:
        print("\n" + "="*50)
        print("CRITICAL STOP: NEW OUTPUT IS IDENTICAL TO OLD 0.784 RUN!")
        print("DO NOT PACKAGE. DO NOT SUBMIT.")
        print("="*50)
        sys.exit(2)

    # 4. Phase 8: Validation
    print("\n==================================================")
    print("PHASE 8 — OFFICIAL VALIDATION")
    print("==================================================")
    cmd_val = [
        "python3", "student_resource/utils/validate_submission.py",
        "--matching", str(new_match_path),
        "--candidate", str(new_cand_path),
        "--test-dir", "student_resource/dataset/test",
    ]
    print(f"Running validator: {' '.join(cmd_val)}")
    val_proc = subprocess.run(cmd_val, capture_output=True, text=True)
    print(val_proc.stdout)
    if val_proc.stderr:
        print(val_proc.stderr, file=sys.stderr)

    if val_proc.returncode != 0:
        print(f"VALIDATOR FAILED with code {val_proc.returncode}!", file=sys.stderr)
        sys.exit(3)

    print("VALIDATOR: PASS")

    # 5. Phase 9: Packaging
    print("\n==================================================")
    print("PHASE 9 — FRESH PACKAGING & ZIP AUDIT")
    print("==================================================")
    sub_dir = Path("submission")
    sub_dir.mkdir(parents=True, exist_ok=True)
    fresh_zip = sub_dir / "ENTIVYRE_submission_FRESH.zip"
    fresh_match_zip = sub_dir / "ENTIVYRE_matching_only_FRESH.zip"

    # Also update standard submission ZIPs
    std_zip = sub_dir / "ENTIVYRE_submission.zip"
    std_match_zip = sub_dir / "ENTIVYRE_matching_only.zip"

    print(f"Creating {fresh_match_zip}...")
    with zipfile.ZipFile(fresh_match_zip, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(new_match_path, arcname="matching_results.tsv")

    print(f"Creating {std_match_zip} (overwrite with fresh)...")
    shutil.copy2(fresh_match_zip, std_match_zip)

    # Verify extracted matching_results.tsv hash
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_p = Path(tmp_dir)
        with zipfile.ZipFile(fresh_match_zip, "r") as z:
            z.extract("matching_results.tsv", path=tmp_p)
        extracted_hash = sha256_file(tmp_p / "matching_results.tsv")
        print(f"Extracted matching_results.tsv SHA-256: {extracted_hash}")
        assert extracted_hash == new_match_sha256, "ZIP extract hash mismatch!"
        print("MATCHING ZIP VERIFIED: SHA-256 matches fresh output exactly.")

    print("\n==================================================")
    print("PHASE 10 READY — SUMMARY DATA PREPARED")
    print("==================================================")


if __name__ == "__main__":
    main()
