#!/usr/bin/env python3
"""
Full Dataset Audit and Comprehensive Profiling Script.
Generates:
1. artifacts/data_authorization_audit.csv
2. data_profile/file_inventory.csv
3. data_profile/schema_report.csv
4. data_profile/missingness.csv
5. data_profile/duplicate_report.csv
6. data_profile/country_report.csv
7. data_profile/name_profile.csv
8. data_profile/address_profile.csv
9. data_profile/source_profile.csv
10. data_profile/label_profile.csv
"""

import os
import sys
import csv
import json
import hashlib
from pathlib import Path
from collections import Counter, defaultdict

proj_root = Path(__file__).resolve().parents[1]
data_profile_dir = proj_root / "data_profile"
artifacts_dir = proj_root / "artifacts"
data_profile_dir.mkdir(parents=True, exist_ok=True)
artifacts_dir.mkdir(parents=True, exist_ok=True)

def compute_sha256(path, max_bytes=100*1024*1024):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(65536):
            h.update(chunk)
            if f.tell() > max_bytes:
                break
    return h.hexdigest()

def main():
    print("==================================================")
    print("GENERATING DATA AUTHORIZATION AUDIT & PROFILES")
    print("==================================================")

    # 1. DATA AUTHORIZATION AUDIT
    audit_rows = [
        {
            "file": "student_resource/dataset/train/train_source1.tsv",
            "source": "Source 1 (Train Query)",
            "provenance": "Amazon ML Challenge 2026 Official Resource",
            "official_challenge_data": "YES",
            "derived_from_official_data": "NO",
            "external_identity_data": "NO",
            "allowed_for_matching": "YES (Training)",
            "reason": "Official anchor records for offline training, tuning, and validation."
        },
        {
            "file": "student_resource/dataset/train/train_source2.tsv",
            "source": "Source 2 (Train Target)",
            "provenance": "Amazon ML Challenge 2026 Official Resource",
            "official_challenge_data": "YES",
            "derived_from_official_data": "NO",
            "external_identity_data": "NO",
            "allowed_for_matching": "YES (Training)",
            "reason": "Official target database 1 for offline candidate retrieval and blocking calibration."
        },
        {
            "file": "student_resource/dataset/train/train_source3.tsv",
            "source": "Source 3 (Train Target)",
            "provenance": "Amazon ML Challenge 2026 Official Resource",
            "official_challenge_data": "YES",
            "derived_from_official_data": "NO",
            "external_identity_data": "NO",
            "allowed_for_matching": "YES (Training)",
            "reason": "Official target database 2 for offline candidate retrieval and blocking calibration."
        },
        {
            "file": "student_resource/dataset/train/train_ground_truth.tsv",
            "source": "Ground Truth (Train Labels)",
            "provenance": "Amazon ML Challenge 2026 Official Resource",
            "official_challenge_data": "YES",
            "derived_from_official_data": "NO",
            "external_identity_data": "NO",
            "allowed_for_matching": "NO (Labels Only)",
            "reason": "Official labels strictly quarantined for supervised training and offline validation; never input to test matcher."
        },
        {
            "file": "student_resource/dataset/test/test_source1.tsv",
            "source": "Source 1 (Test Anchor Query)",
            "provenance": "Amazon ML Challenge 2026 Official Resource",
            "official_challenge_data": "YES",
            "derived_from_official_data": "NO",
            "external_identity_data": "NO",
            "allowed_for_matching": "YES (Test Query)",
            "reason": "Official test anchor queries for leaderboard inference."
        },
        {
            "file": "student_resource/dataset/test/test_source2.tsv",
            "source": "Source 2 (Test Target)",
            "provenance": "Amazon ML Challenge 2026 Official Resource",
            "official_challenge_data": "YES",
            "derived_from_official_data": "NO",
            "external_identity_data": "NO",
            "allowed_for_matching": "YES (Test Target)",
            "reason": "Official test target database 1 for leaderboard candidate retrieval."
        },
        {
            "file": "student_resource/dataset/test/test_source3.tsv",
            "source": "Source 3 (Test Target)",
            "provenance": "Amazon ML Challenge 2026 Official Resource",
            "official_challenge_data": "YES",
            "derived_from_official_data": "NO",
            "external_identity_data": "NO",
            "allowed_for_matching": "YES (Test Target)",
            "reason": "Official test target database 2 for leaderboard candidate retrieval."
        },
        {
            "file": "output/candidate_pairs.tsv",
            "source": "Candidate Retrieval Output",
            "provenance": "Derived Artifact from Official Test Sources",
            "official_challenge_data": "NO (Derived)",
            "derived_from_official_data": "YES",
            "external_identity_data": "NO",
            "allowed_for_matching": "YES (Submission Contract)",
            "reason": "Official challenge submission artifact; strictly derived via offline multi-pass blocking."
        },
        {
            "file": "output/matching_results.tsv",
            "source": "Final Match Output",
            "provenance": "Derived Artifact from Official Test Sources",
            "official_challenge_data": "NO (Derived)",
            "derived_from_official_data": "YES",
            "external_identity_data": "NO",
            "allowed_for_matching": "YES (Submission Contract)",
            "reason": "Official challenge submission artifact; strictly derived via calibrated decision engine."
        }
    ]

    audit_path = artifacts_dir / "data_authorization_audit.csv"
    with open(audit_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "file", "source", "provenance", "official_challenge_data",
            "derived_from_official_data", "external_identity_data",
            "allowed_for_matching", "reason"
        ])
        writer.writeheader()
        writer.writerows(audit_rows)
    print(f"Created: {audit_path}")

    # 2. PROFILING TARGET FILES
    files_to_profile = [
        ("train_source1", proj_root / "student_resource/dataset/train/train_source1.tsv", "Train", "S1"),
        ("train_source2", proj_root / "student_resource/dataset/train/train_source2.tsv", "Train", "S2"),
        ("train_source3", proj_root / "student_resource/dataset/train/train_source3.tsv", "Train", "S3"),
        ("train_ground_truth", proj_root / "student_resource/dataset/train/train_ground_truth.tsv", "Train", "GT"),
        ("test_source1", proj_root / "student_resource/dataset/test/test_source1.tsv", "Test", "S1"),
        ("test_source2", proj_root / "student_resource/dataset/test/test_source2.tsv", "Test", "S2"),
        ("test_source3", proj_root / "student_resource/dataset/test/test_source3.tsv", "Test", "S3"),
    ]

    inventory_rows = []
    schema_rows = []
    missing_rows = []
    dup_rows = []
    country_rows = []
    name_rows = []
    addr_rows = []
    source_rows = []

    for name_key, fpath, split, src in files_to_profile:
        print(f"Profiling {name_key}...")
        fsize = fpath.stat().st_size
        fsize_mb = fsize / (1024 * 1024)
        
        # Fast sampling for statistics
        total_lines = 0
        missing_name = 0
        missing_addr = 0
        missing_country = 0
        country_counter = Counter()
        id_set = set()
        dup_ids = 0
        
        name_lens = []
        name_tok_lens = []
        addr_lens = []
        addr_tok_lens = []
        addr_has_num = 0
        addr_has_postal = 0

        sample_limit = 100000
        cols = []

        with open(fpath, "r", encoding="utf-8") as f:
            header = f.readline().rstrip("\r\n").split("\t")
            cols = header
            for idx, col in enumerate(cols):
                schema_rows.append({
                    "file": fpath.name,
                    "column_name": col,
                    "ordinal_position": idx + 1,
                    "data_type": "string",
                    "sample_values": ""
                })
            
            for line in f:
                total_lines += 1
                if total_lines <= sample_limit:
                    parts = line.rstrip("\r\n").split("\t")
                    if name_key == "train_ground_truth":
                        eid = parts[0] if len(parts) > 0 else ""
                        matches = parts[1] if len(parts) > 1 else ""
                        if eid in id_set:
                            dup_ids += 1
                        else:
                            id_set.add(eid)
                    else:
                        eid = parts[0] if len(parts) > 0 else ""
                        b_name = parts[1] if len(parts) > 1 else ""
                        b_addr = parts[2] if len(parts) > 2 else ""
                        b_country = parts[3] if len(parts) > 3 else ""
                        
                        if eid in id_set:
                            dup_ids += 1
                        else:
                            id_set.add(eid)
                        
                        if not b_name: missing_name += 1
                        if not b_addr: missing_addr += 1
                        if not b_country: missing_country += 1
                        
                        country_counter[b_country] += 1
                        
                        nl = len(b_name)
                        nt = len(b_name.split())
                        name_lens.append(nl)
                        name_tok_lens.append(nt)
                        
                        al = len(b_addr)
                        at = len(b_addr.split())
                        addr_lens.append(al)
                        addr_tok_lens.append(at)
                        
                        if any(c.isdigit() for c in b_addr):
                            addr_has_num += 1
                        if any(t.isdigit() and len(t) in (5, 6) for t in b_addr.split()):
                            addr_has_postal += 1
                else:
                    # Just count lines for remaining
                    pass

        # Estimate full line count based on bytes/average line length if huge
        avg_line_bytes = fsize / max(total_lines, 1) if total_lines > sample_limit else fsize / max(total_lines, 1)
        full_est_lines = total_lines

        inventory_rows.append({
            "file": fpath.name,
            "path": str(fpath.relative_to(proj_root)),
            "file_type": "TSV",
            "size_bytes": fsize,
            "size_mb": f"{fsize_mb:.2f}",
            "sampled_rows": min(total_lines, sample_limit),
            "estimated_total_rows": full_est_lines
        })

        if name_key != "train_ground_truth":
            N = len(name_lens)
            missing_rows.extend([
                {"file": fpath.name, "column": "entity_id", "total_sampled": N, "missing_count": 0, "missing_pct": 0.0},
                {"file": fpath.name, "column": "business_name", "total_sampled": N, "missing_count": missing_name, "missing_pct": round(missing_name/N*100, 3)},
                {"file": fpath.name, "column": "business_address", "total_sampled": N, "missing_count": missing_addr, "missing_pct": round(missing_addr/N*100, 3)},
                {"file": fpath.name, "column": "country", "total_sampled": N, "missing_count": missing_country, "missing_pct": round(missing_country/N*100, 3)},
            ])

            dup_rows.append({
                "file": fpath.name,
                "sampled_records": N,
                "unique_ids": len(id_set),
                "duplicate_ids": dup_ids,
                "duplicate_rate_pct": round(dup_ids / max(N, 1) * 100, 4)
            })

            for cty, count in country_counter.most_common():
                country_rows.append({
                    "file": fpath.name,
                    "country": cty or "(BLANK)",
                    "count": count,
                    "percentage": round(count / N * 100, 2)
                })

            name_rows.append({
                "file": fpath.name,
                "avg_char_length": round(sum(name_lens) / max(N, 1), 2),
                "min_char_length": min(name_lens) if name_lens else 0,
                "max_char_length": max(name_lens) if name_lens else 0,
                "avg_token_count": round(sum(name_tok_lens) / max(N, 1), 2),
                "min_tokens": min(name_tok_lens) if name_tok_lens else 0,
                "max_tokens": max(name_tok_lens) if name_tok_lens else 0
            })

            addr_rows.append({
                "file": fpath.name,
                "avg_char_length": round(sum(addr_lens) / max(N, 1), 2),
                "min_char_length": min(addr_lens) if addr_lens else 0,
                "max_char_length": max(addr_lens) if addr_lens else 0,
                "avg_tokens": round(sum(addr_tok_lens) / max(N, 1), 2),
                "has_number_pct": round(addr_has_num / max(N, 1) * 100, 2),
                "has_postal_pct": round(addr_has_postal / max(N, 1) * 100, 2)
            })

            source_rows.append({
                "source": src,
                "split": split,
                "file": fpath.name,
                "sampled_records": N,
                "size_mb": f"{fsize_mb:.2f}"
            })

    # Write profiling CSVs
    def write_csv(p, rows, fieldnames):
        with open(p, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Created: {p}")

    write_csv(data_profile_dir / "file_inventory.csv", inventory_rows, list(inventory_rows[0].keys()))
    write_csv(data_profile_dir / "schema_report.csv", schema_rows, list(schema_rows[0].keys()))
    write_csv(data_profile_dir / "missingness.csv", missing_rows, list(missing_rows[0].keys()))
    write_csv(data_profile_dir / "duplicate_report.csv", dup_rows, list(dup_rows[0].keys()))
    write_csv(data_profile_dir / "country_report.csv", country_rows, list(country_rows[0].keys()))
    write_csv(data_profile_dir / "name_profile.csv", name_rows, list(name_rows[0].keys()))
    write_csv(data_profile_dir / "address_profile.csv", addr_rows, list(addr_rows[0].keys()))
    write_csv(data_profile_dir / "source_profile.csv", source_rows, list(source_rows[0].keys()))

    # 3. LABEL PROFILE (Ground Truth)
    gt_file = proj_root / "student_resource/dataset/train/train_ground_truth.tsv"
    gt_total = 0
    gt_with_matches = 0
    gt_singletons = 0
    gt_total_pairs = 0
    gt_match_counts = Counter()
    s2_matches = 0
    s3_matches = 0

    with open(gt_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)
        for row in reader:
            gt_total += 1
            matched_str = row[1].strip() if len(row) > 1 else ""
            if not matched_str:
                gt_singletons += 1
                gt_match_counts[0] += 1
            else:
                gt_with_matches += 1
                matches = matched_str.split(",")
                m_count = len(matches)
                gt_match_counts[m_count] += 1
                gt_total_pairs += m_count
                for m in matches:
                    if m.startswith("S2-"): s2_matches += 1
                    elif m.startswith("S3-"): s3_matches += 1

    label_rows = [
        {"metric": "total_source1_anchors", "value": str(gt_total)},
        {"metric": "anchors_with_matches", "value": str(gt_with_matches)},
        {"metric": "true_singletons", "value": str(gt_singletons)},
        {"metric": "singleton_ratio_pct", "value": f"{gt_singletons / max(gt_total, 1) * 100:.2f}%"},
        {"metric": "total_true_pairs", "value": str(gt_total_pairs)},
        {"metric": "mean_matches_per_anchor_overall", "value": f"{gt_total_pairs / max(gt_total, 1):.3f}"},
        {"metric": "mean_matches_per_matched_anchor", "value": f"{gt_total_pairs / max(gt_with_matches, 1):.3f}"},
        {"metric": "max_matches_per_anchor", "value": str(max(gt_match_counts.keys()))},
        {"metric": "total_source2_matches", "value": str(s2_matches)},
        {"metric": "total_source3_matches", "value": str(s3_matches)},
        {"metric": "ratio_s2_to_s3_matches", "value": f"{s2_matches / max(s3_matches, 1):.2f}"}
    ]
    write_csv(data_profile_dir / "label_profile.csv", label_rows, ["metric", "value"])

    print("\nALL DATA AUDITS AND PROFILES SUCCESSFULLY GENERATED!")

if __name__ == "__main__":
    main()
