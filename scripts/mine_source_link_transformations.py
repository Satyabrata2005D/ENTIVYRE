#!/usr/bin/env python3
"""
Phase 4 & Phase 5: Advanced Source-Link and Cross-Source Consistency Analysis.
Mines 10,000 true positive links from ground truth:
- S1 <-> S2 pairs
- S1 <-> S3 pairs
- S2 <-> S3 cross-source consistency (pairs sharing the same S1 parent)

Analyzes:
1. Token transformations & abbreviation mappings
2. Legal suffix transformations
3. Script / multilingual patterns (Devanagari, Dravidian, Bengali, etc.)
4. Address component alignment (building numbers, postal codes, locality)
5. Synthetic noise & corruption patterns
6. Cross-source agreement: How much do S2 and S3 agree when pointing to the same S1?
"""

import sys
import gc
import re
import csv
import json
import time
from pathlib import Path
from collections import Counter, defaultdict
from difflib import SequenceMatcher

proj_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(proj_root / "code" / "business_entity_resolution" / "src"))

from ber.normalization.name_normalizer import NameNormalizer
from ber.normalization.address_normalizer import AddressNormalizer
from ber.normalization.country_handler import CountryHandler

DATASET_DIR = proj_root / "student_resource" / "dataset" / "train"
S1_PATH = DATASET_DIR / "train_source1.tsv"
S2_PATH = DATASET_DIR / "train_source2.tsv"
S3_PATH = DATASET_DIR / "train_source3.tsv"
GT_PATH = DATASET_DIR / "train_ground_truth.tsv"

SAMPLE_ANCHORS = 10000

def main():
    print("=" * 80)
    print("PHASE 4 & 5: ADVANCED SOURCE-LINK & CROSS-SOURCE MINING")
    print("=" * 80)
    t0 = time.time()

    # 1. Sample 10,000 anchors with matches
    print("[1/5] Sampling ground truth anchors...", flush=True)
    gt_links = {}
    needed_s1 = set()
    needed_s2 = set()
    needed_s3 = set()

    with open(GT_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)
        for row in reader:
            if len(gt_links) >= SAMPLE_ANCHORS:
                break
            s1_id = row[0].strip()
            m_str = row[1].strip() if len(row) > 1 else ""
            if not m_str:
                continue
            matches = [x.strip() for x in m_str.split(",") if x.strip()]
            s2_m = [m for m in matches if m.startswith("S2-")]
            s3_m = [m for m in matches if m.startswith("S3-")]
            if s2_m and s3_m:
                gt_links[s1_id] = (s2_m, s3_m)
                needed_s1.add(s1_id)
                needed_s2.update(s2_m)
                needed_s3.update(s3_m)

    print(f"Sampled {len(gt_links):,} S1 anchors with both S2 and S3 matches.")
    print(f"Needed: {len(needed_s1):,} S1, {len(needed_s2):,} S2, {len(needed_s3):,} S3 records.")

    # 2. Load S1 records
    print("[2/5] Loading S1 records...", flush=True)
    s1_data = {}
    with open(S1_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)
        for row in reader:
            eid = row[0].strip()
            if eid in needed_s1:
                s1_data[eid] = (row[1], row[2] if len(row) > 2 else "", row[3] if len(row) > 3 else "")

    # 3. Stream S2
    print("[3/5] Streaming needed S2 records...", flush=True)
    s2_data = {}
    with open(S2_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)
        for row in reader:
            eid = row[0].strip()
            if eid in needed_s2:
                s2_data[eid] = (row[1], row[2] if len(row) > 2 else "", row[3] if len(row) > 3 else "")
                if len(s2_data) == len(needed_s2):
                    break

    # 4. Stream S3
    print("[4/5] Streaming needed S3 records...", flush=True)
    s3_data = {}
    with open(S3_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)
        for row in reader:
            eid = row[0].strip()
            if eid in needed_s3:
                s3_data[eid] = (row[1], row[2] if len(row) > 2 else "", row[3] if len(row) > 3 else "")
                if len(s3_data) == len(needed_s3):
                    break

    print(f"Loaded all records in {time.time()-t0:.1f}s.")

    # 5. Analyze S1 <-> S2, S1 <-> S3, and S2 <-> S3
    print("[5/5] Analyzing transformations and consistency...", flush=True)
    nn = NameNormalizer()
    an = AddressNormalizer()

    def analyze_pair(s_rec, t_rec):
        s_n, s_a, s_c = s_rec
        t_n, t_a, t_c = t_rec

        s_norm_n = nn.normalize(s_n)
        t_norm_n = nn.normalize(t_n)
        s_norm_a = an.normalize(s_a) if s_a else None
        t_norm_a = an.normalize(t_a) if t_a else None

        exact_raw_name = (s_n == t_n)
        exact_norm_name = (s_norm_n.canonical == t_norm_n.canonical)
        s_toks = set(s_norm_n.tokens)
        t_toks = set(t_norm_n.tokens)
        tok_jaccard = len(s_toks & t_toks) / len(s_toks | t_toks) if (s_toks | t_toks) else 0.0

        # Script detection
        has_non_ascii_s = any(ord(c) > 127 for c in s_n)
        has_non_ascii_t = any(ord(c) > 127 for c in t_n)

        # Address analysis
        s_bldgs = set(s_norm_a.numeric_tokens) if s_norm_a else set()
        t_bldgs = set(t_norm_a.numeric_tokens) if t_norm_a else set()
        bldg_overlap = bool(s_bldgs & t_bldgs) if (s_bldgs and t_bldgs) else None

        s_postal = s_norm_a.postal_code if s_norm_a else ""
        t_postal = t_norm_a.postal_code if t_norm_a else ""
        postal_match = (s_postal == t_postal) if (s_postal and t_postal) else None

        return {
            "exact_raw_name": exact_raw_name,
            "exact_norm_name": exact_norm_name,
            "tok_jaccard": tok_jaccard,
            "has_non_ascii_t": has_non_ascii_t,
            "bldg_overlap": bldg_overlap,
            "postal_match": postal_match,
            "s_toks": s_toks,
            "t_toks": t_toks
        }

    s1_s2_stats = {"total": 0, "exact_raw": 0, "exact_norm": 0, "jaccard_sum": 0.0, "non_ascii": 0, "bldg_match": 0, "bldg_conflict": 0, "bldg_na": 0}
    s1_s3_stats = {"total": 0, "exact_raw": 0, "exact_norm": 0, "jaccard_sum": 0.0, "non_ascii": 0, "bldg_match": 0, "bldg_conflict": 0, "bldg_na": 0}
    s2_s3_stats = {"total": 0, "exact_raw": 0, "exact_norm": 0, "jaccard_sum": 0.0, "both_non_ascii": 0, "bldg_match": 0, "bldg_conflict": 0}

    token_diff_counter_s2 = Counter()
    token_diff_counter_s3 = Counter()

    for s1_id, (s2_ids, s3_ids) in gt_links.items():
        s1_rec = s1_data.get(s1_id)
        if not s1_rec: continue

        # S1 <-> S2 pairs
        for s2_id in s2_ids:
            s2_rec = s2_data.get(s2_id)
            if not s2_rec: continue
            res = analyze_pair(s1_rec, s2_rec)
            s1_s2_stats["total"] += 1
            if res["exact_raw_name"]: s1_s2_stats["exact_raw"] += 1
            if res["exact_norm_name"]: s1_s2_stats["exact_norm"] += 1
            s1_s2_stats["jaccard_sum"] += res["tok_jaccard"]
            if res["has_non_ascii_t"]: s1_s2_stats["non_ascii"] += 1
            if res["bldg_overlap"] is True: s1_s2_stats["bldg_match"] += 1
            elif res["bldg_overlap"] is False: s1_s2_stats["bldg_conflict"] += 1
            else: s1_s2_stats["bldg_na"] += 1

            for diff_t in (res["t_toks"] - res["s_toks"]):
                if len(diff_t) >= 3: token_diff_counter_s2[diff_t] += 1

        # S1 <-> S3 pairs
        for s3_id in s3_ids:
            s3_rec = s3_data.get(s3_id)
            if not s3_rec: continue
            res = analyze_pair(s1_rec, s3_rec)
            s1_s3_stats["total"] += 1
            if res["exact_raw_name"]: s1_s3_stats["exact_raw"] += 1
            if res["exact_norm_name"]: s1_s3_stats["exact_norm"] += 1
            s1_s3_stats["jaccard_sum"] += res["tok_jaccard"]
            if res["has_non_ascii_t"]: s1_s3_stats["non_ascii"] += 1
            if res["bldg_overlap"] is True: s1_s3_stats["bldg_match"] += 1
            elif res["bldg_overlap"] is False: s1_s3_stats["bldg_conflict"] += 1
            else: s1_s3_stats["bldg_na"] += 1

            for diff_t in (res["t_toks"] - res["s_toks"]):
                if len(diff_t) >= 3: token_diff_counter_s3[diff_t] += 1

        # S2 <-> S3 consistency
        for s2_id in s2_ids[:2]:
            s2_rec = s2_data.get(s2_id)
            if not s2_rec: continue
            for s3_id in s3_ids[:2]:
                s3_rec = s3_data.get(s3_id)
                if not s3_rec: continue
                res = analyze_pair(s2_rec, s3_rec)
                s2_s3_stats["total"] += 1
                if res["exact_raw_name"]: s2_s3_stats["exact_raw"] += 1
                if res["exact_norm_name"]: s2_s3_stats["exact_norm"] += 1
                s2_s3_stats["jaccard_sum"] += res["tok_jaccard"]
                if res["bldg_overlap"] is True: s2_s3_stats["bldg_match"] += 1
                elif res["bldg_overlap"] is False: s2_s3_stats["bldg_conflict"] += 1

    print("\n--- S1 <-> S2 TRANSFORMATION STATS ---")
    n = s1_s2_stats["total"]
    print(f"Total Pairs: {n:,}")
    print(f"Exact Raw Name Match:        {s1_s2_stats['exact_raw']:,} ({s1_s2_stats['exact_raw']/n*100:.2f}%)")
    print(f"Exact Normalized Name Match: {s1_s2_stats['exact_norm']:,} ({s1_s2_stats['exact_norm']/n*100:.2f}%)")
    print(f"Mean Token Jaccard:          {s1_s2_stats['jaccard_sum']/n:.4f}")
    print(f"Non-ASCII Script Rate in S2: {s1_s2_stats['non_ascii']:,} ({s1_s2_stats['non_ascii']/n*100:.2f}%)")
    print(f"Building Number Match:       {s1_s2_stats['bldg_match']:,} ({s1_s2_stats['bldg_match']/n*100:.2f}%)")
    print(f"Building Number Conflict:    {s1_s2_stats['bldg_conflict']:,} ({s1_s2_stats['bldg_conflict']/n*100:.2f}%)")

    print("\n--- S1 <-> S3 TRANSFORMATION STATS ---")
    n = s1_s3_stats["total"]
    print(f"Total Pairs: {n:,}")
    print(f"Exact Raw Name Match:        {s1_s3_stats['exact_raw']:,} ({s1_s3_stats['exact_raw']/n*100:.2f}%)")
    print(f"Exact Normalized Name Match: {s1_s3_stats['exact_norm']:,} ({s1_s3_stats['exact_norm']/n*100:.2f}%)")
    print(f"Mean Token Jaccard:          {s1_s3_stats['jaccard_sum']/n:.4f}")
    print(f"Non-ASCII Script Rate in S3: {s1_s3_stats['non_ascii']:,} ({s1_s3_stats['non_ascii']/n*100:.2f}%)")
    print(f"Building Number Match:       {s1_s3_stats['bldg_match']:,} ({s1_s3_stats['bldg_match']/n*100:.2f}%)")
    print(f"Building Number Conflict:    {s1_s3_stats['bldg_conflict']:,} ({s1_s3_stats['bldg_conflict']/n*100:.2f}%)")

    print("\n--- S2 <-> S3 CROSS-SOURCE CONSISTENCY STATS ---")
    n = s2_s3_stats["total"]
    print(f"Total S2-S3 Pairs: {n:,}")
    print(f"Exact Raw Name Agreement:    {s2_s3_stats['exact_raw']:,} ({s2_s3_stats['exact_raw']/n*100:.2f}%)")
    print(f"Exact Normalized Agreement:  {s2_s3_stats['exact_norm']:,} ({s2_s3_stats['exact_norm']/n*100:.2f}%)")
    print(f"Mean S2-S3 Token Jaccard:    {s2_s3_stats['jaccard_sum']/n:.4f}")
    print(f"Building Number Match:       {s2_s3_stats['bldg_match']:,} ({s2_s3_stats['bldg_match']/n*100:.2f}%)")

    print("\nTop 15 Recurring Unaligned Tokens Added in S2 (relative to S1):")
    for t, cnt in token_diff_counter_s2.most_common(15):
        print(f"  {t:<15}: {cnt:>5,d}")

    print("\nTop 15 Recurring Unaligned Tokens Added in S3 (relative to S1):")
    for t, cnt in token_diff_counter_s3.most_common(15):
        print(f"  {t:<15}: {cnt:>5,d}")

if __name__ == "__main__":
    main()
