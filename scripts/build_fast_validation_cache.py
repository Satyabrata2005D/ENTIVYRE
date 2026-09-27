#!/usr/bin/env python3
"""
Fast Validation Cache Builder for 5,000 Anchors.
Uses key-filtered streaming over train_source2.tsv and train_source3.tsv.
Executes in under 60 seconds total.
"""

import sys
import gc
import json
import time
import csv
from pathlib import Path
from collections import defaultdict

proj_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(proj_root / "code" / "business_entity_resolution" / "src"))

from ber.inference.engine import InferenceEngine, InferenceConfig

DATASET_DIR = proj_root / "student_resource" / "dataset" / "train"
S1_PATH = DATASET_DIR / "train_source1.tsv"
S2_PATH = DATASET_DIR / "train_source2.tsv"
S3_PATH = DATASET_DIR / "train_source3.tsv"
GT_PATH = DATASET_DIR / "train_ground_truth.tsv"

CACHE_DIR = proj_root / "artifacts" / "challengers" / "CHALLENGER_007" / "val_cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

SAMPLE_SIZE = 5000

def main():
    print("=" * 70)
    print("FAST VALIDATION CACHE BUILDER (5,000 ANCHORS)")
    print("=" * 70)
    t0 = time.time()

    # 1. Load Ground Truth for first 5,000 anchors
    gt = {}
    with open(GT_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)
        for i, row in enumerate(reader):
            if i >= SAMPLE_SIZE:
                break
            s1_id = row[0].strip()
            m_str = row[1].strip() if len(row) > 1 else ""
            gt[s1_id] = [x.strip() for x in m_str.split(",") if x.strip()]

    print(f"Loaded {len(gt)} ground truth anchors ({sum(len(v) for v in gt.values())} true pairs)")

    # 2. Load Anchor Records & Collect Blocking Keys
    engine = InferenceEngine(InferenceConfig())
    s1_records = {}
    anchor_keys_map = {}
    all_anchor_keys = set()

    with open(S1_PATH, "r", encoding="utf-8") as f:
        f.readline()
        for line in f:
            parts = line.rstrip("\r\n").split("\t")
            if len(parts) < 4: continue
            eid = parts[0].strip()
            if eid in gt:
                rec = {
                    "name": parts[1],
                    "address": parts[2] if len(parts) > 2 else "",
                    "country": parts[3] if len(parts) > 3 else ""
                }
                s1_records[eid] = rec
                keys = engine.extract_blocking_keys(rec["name"], rec["address"], rec["country"])
                anchor_keys_map[eid] = keys
                all_anchor_keys.update(keys)

    print(f"Loaded {len(s1_records)} S1 anchors, generated {len(all_anchor_keys):,} unique blocking keys ({time.time()-t0:.1f}s)")

    # 3. Stream Source 2 with Key Filter
    print("\nStreaming Source 2 with key filtering...")
    t_s2 = time.time()
    s2_index = defaultdict(list)
    target_records = {}
    max_p = engine.config.max_postings_per_key

    with open(S2_PATH, "r", encoding="utf-8") as f:
        f.readline()
        for line in f:
            parts = line.rstrip("\r\n").split("\t")
            if len(parts) < 4: continue
            name = parts[1]
            address = parts[2] if len(parts) > 2 else ""
            country = parts[3] if len(parts) > 3 else ""
            
            # Quick check: extract keys
            keys = engine.extract_blocking_keys(name, address, country)
            matched_keys = [k for k in keys if k in all_anchor_keys]
            if matched_keys:
                eid = parts[0].strip()
                target_records[eid] = {"name": name, "address": address, "country": country}
                for k in matched_keys:
                    p = s2_index[k]
                    if len(p) < max_p:
                        p.append(eid)

    print(f"  Source 2 filtered: {len(target_records):,} records indexed in {time.time()-t_s2:.1f}s")

    # Retrieve S2 candidates per anchor
    s2_cands = {}
    max_c = engine.config.max_candidates_per_anchor
    for s1_id, keys in anchor_keys_map.items():
        seen = set()
        cands = []
        for k in keys:
            p = s2_index.get(k)
            if p:
                for tid in p:
                    if tid not in seen and tid != s1_id:
                        seen.add(tid)
                        cands.append(tid)
                        if len(cands) >= max_c:
                            break
            if len(cands) >= max_c:
                break
        s2_cands[s1_id] = cands

    del s2_index
    gc.collect()

    # 4. Stream Source 3 with Key Filter
    print("\nStreaming Source 3 with key filtering...")
    t_s3 = time.time()
    s3_index = defaultdict(list)

    with open(S3_PATH, "r", encoding="utf-8") as f:
        f.readline()
        for line in f:
            parts = line.rstrip("\r\n").split("\t")
            if len(parts) < 4: continue
            name = parts[1]
            address = parts[2] if len(parts) > 2 else ""
            country = parts[3] if len(parts) > 3 else ""
            
            keys = engine.extract_blocking_keys(name, address, country)
            matched_keys = [k for k in keys if k in all_anchor_keys]
            if matched_keys:
                eid = parts[0].strip()
                target_records[eid] = {"name": name, "address": address, "country": country}
                for k in matched_keys:
                    p = s3_index[k]
                    if len(p) < max_p:
                        p.append(eid)

    print(f"  Source 3 filtered: {len(target_records):,} total target records indexed in {time.time()-t_s3:.1f}s")

    s3_cands = {}
    for s1_id, keys in anchor_keys_map.items():
        seen = set()
        cands = []
        for k in keys:
            p = s3_index.get(k)
            if p:
                for tid in p:
                    if tid not in seen and tid != s1_id:
                        seen.add(tid)
                        cands.append(tid)
                        if len(cands) >= max_c:
                            break
            if len(cands) >= max_c:
                break
        s3_cands[s1_id] = cands

    del s3_index
    gc.collect()

    # Ensure all true targets are in target_records (load missing ones directly)
    missing_targets = set()
    for s1_id, matches in gt.items():
        for m in matches:
            if m not in target_records:
                missing_targets.add(m)

    if missing_targets:
        print(f"\nLoading {len(missing_targets)} true target records that had no blocking key match...")
        with open(S2_PATH, "r", encoding="utf-8") as f:
            f.readline()
            for line in f:
                p = line.rstrip("\r\n").split("\t")
                if len(p) >= 4 and p[0].strip() in missing_targets:
                    target_records[p[0].strip()] = {"name": p[1], "address": p[2] if len(p)>2 else "", "country": p[3]}
        with open(S3_PATH, "r", encoding="utf-8") as f:
            f.readline()
            for line in f:
                p = line.rstrip("\r\n").split("\t")
                if len(p) >= 4 and p[0].strip() in missing_targets:
                    target_records[p[0].strip()] = {"name": p[1], "address": p[2] if len(p)>2 else "", "country": p[3]}

    # Save Cache
    print("\nSaving cache to artifacts/challengers/CHALLENGER_007/val_cache/...")
    with open(CACHE_DIR / "ground_truth.json", "w", encoding="utf-8") as f:
        json.dump(gt, f)
    with open(CACHE_DIR / "anchors.json", "w", encoding="utf-8") as f:
        json.dump(s1_records, f)
    with open(CACHE_DIR / "candidates_s2.json", "w", encoding="utf-8") as f:
        json.dump(s2_cands, f)
    with open(CACHE_DIR / "candidates_s3.json", "w", encoding="utf-8") as f:
        json.dump(s3_cands, f)
    with open(CACHE_DIR / "target_records.json", "w", encoding="utf-8") as f:
        json.dump(target_records, f)

    total_time = time.time() - t0
    print(f"Fast Validation Cache successfully built in {total_time:.1f}s!")

if __name__ == "__main__":
    main()
