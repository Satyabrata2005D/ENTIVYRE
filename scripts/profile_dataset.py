#!/usr/bin/env python3
"""
CLI script to execute Phase 06: Data Profiling and EDA.
Profiles name lengths, scripts, legal suffixes, address keywords, missingness,
and ground truth multiplicity statistics.
Outputs artifacts/profiles/eda_profile_report.json and eda_summary.md.
"""
import sys
import json
import time
import argparse
from pathlib import Path

_root = Path(__file__).resolve().parent.parent
_ber_src = _root / "code" / "business_entity_resolution" / "src"
if str(_ber_src) not in sys.path:
    sys.path.insert(0, str(_ber_src))

from ber.profiling.profiler import DatasetProfiler
from entivyre.config import load_config

def main():
    parser = argparse.ArgumentParser(description="ENTIVYRE EDA & Profiling CLI")
    parser.add_argument("--dataset-dir", type=str, default=None, help="Optional dataset root override")
    parser.add_argument("--sample-limit", type=int, default=None, help="Optional record limit per file for fast profiling")
    args = parser.parse_args()

    cfg = load_config()
    dataset_root = Path(args.dataset_dir) if args.dataset_dir else (_root / cfg.paths.dataset_root)
    out_dir = _root / cfg.paths.artifacts_dir / "profiles"
    out_dir.mkdir(parents=True, exist_ok=True)
    report_path = out_dir / "eda_profile_report.json"
    summary_path = out_dir / "eda_summary.md"

    print("=== ENTIVYRE: Phase 06 Data Profiling & EDA Engine ===")
    print(f"Dataset root: {dataset_root}")
    if args.sample_limit:
        print(f"Sampling limit: {args.sample_limit:,} records per file")

    profiler = DatasetProfiler(sample_limit=args.sample_limit)
    t0 = time.perf_counter()

    profiles = {}
    # Profile Sources
    for split in ["train", "test"]:
        for s_idx in [1, 2, 3]:
            fkey = f"{split}_source{s_idx}"
            fpath = dataset_root / split / f"{fkey}.tsv"
            if fpath.exists():
                print(f"Profiling {fkey}...")
                sp = profiler.profile_source(fpath, fkey, chunk_size=cfg.runtime.chunk_size)
                profiles[fkey] = sp.to_dict()

    # Profile Ground Truth
    gt_path = dataset_root / "train" / "train_ground_truth.tsv"
    if gt_path.exists():
        print("Profiling train_ground_truth...")
        gt_prof = profiler.profile_ground_truth(gt_path, chunk_size=cfg.runtime.chunk_size)
        profiles["train_ground_truth"] = gt_prof.to_dict()

    elapsed = time.perf_counter() - t0
    report_data = {
        "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "sample_limit": args.sample_limit,
        "elapsed_seconds": round(elapsed, 2),
        "profiles": profiles,
    }

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=2)

    # Generate Markdown Summary
    md = [
        "# ENTIVYRE Exploratory Data Analysis & Profiling Summary",
        f"**Date:** {report_data['timestamp_utc']} | **Runtime:** {elapsed:.2f}s\n",
        "## 1. Ground Truth Multiplicity Distribution",
    ]
    if "train_ground_truth" in profiles:
        gt = profiles["train_ground_truth"]
        md.extend([
            f"- **Total S1 Anchors:** {gt['total_s1_anchors']:,}",
            f"- **Total Matches:** {gt['total_matches']:,}",
            f"- **Singletons (0 matches):** {gt['singleton_count']:,} ({gt['singleton_pct']}%)",
            f"- **Single Matches (1 match):** {gt['single_match_count']:,} ({gt['single_match_pct']}%)",
            f"- **Multi Matches (>=2 matches):** {gt['multi_match_count']:,} ({gt['multi_match_pct']}%)",
            f"- **Max Matches for Single S1:** {gt['max_matches_per_s1']}",
            f"- **Mean Matches per S1:** {gt['mean_matches_per_s1']:.2f}",
            f"- **Matches S2 only:** {gt['s2_matches_count']:,}",
            f"- **Matches S3 only:** {gt['s3_matches_count']:,}",
            f"- **Matches BOTH S2 and S3:** {gt['both_s2_s3_count']:,}\n",
        ])

    md.append("## 2. Source Missingness & Text Distributions\n")
    md.append("| File | Total Records | Missing Addr % | Mean Name Chars | Devanagari Names | URL Names |")
    md.append("|---|---|---|---|---|---|")
    for k in sorted(profiles.keys()):
        if k == "train_ground_truth":
            continue
        p = profiles[k]
        md.append(
            f"| `{k}` | {p['total_records']:,} | {p['missing_address_pct']:.2f}% | "
            f"{p['name_stats']['mean_char_len']} | {p['name_stats']['has_devanagari_count']:,} | "
            f"{p['name_stats']['has_urls_count']:,} |"
        )

    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")

    print(f"\nProfiling successfully completed in {elapsed:.2f}s!")
    print(f"Report JSON: {report_path}")
    print(f"Summary Markdown: {summary_path}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
