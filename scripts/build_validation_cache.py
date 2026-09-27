#!/usr/bin/env python3
"""
Builds an immutable validation evaluation cache for the 5,000 validation anchors.
Saves:
- validation_ground_truth.json (anchor_id -> true_target_ids)
- validation_anchors.json (anchor_id -> (name, address, country))
- validation_candidates_s2.json (anchor_id -> [s2_cand_ids])
- validation_candidates_s3.json (anchor_id -> [s3_cand_ids])
- validation_target_records.json (cand_id -> (raw_name, raw_address, country))
This allows running ablations, threshold sweeps, and error analyses in seconds!
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
    print("BUILDING IMMUTABLE VALIDATION CACHE (5,000 ANCHORS)")
    print("=" * 70)

    # 1. Load Ground Truth
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

    # 2. Load Anchor Records
    s1_records = {}
    with open(S1_PATH, "r", encoding="utf-8") as f:
        f.readline()
        for line in f:
            parts = line.rstrip("\r\n").split("\t")
            if len(parts) < 4: continue
            eid = parts[0].strip()
            if eid in gt:
                s1_records[eid] = {
                    "name": parts[1],
                    "address": parts[2] if len(parts) > 2 else "",
                    "country": parts[3] if len(parts) > 3 else ""
                }

    print(f"Loaded {len(s1_records)} S1 anchor records")

    engine = InferenceEngine(InferenceConfig())

    # 3. Retrieve Candidates from Source 2
    print("\nRetrieving candidates from Source 2...")
    engine.index_target_file(S2_PATH)
    s2_cands = defaultdict(list)
    needed_s2_ids = set()

    for s1_id, rec in s1_records.items():
        keys = engine.extract_blocking_keys(rec["name"], rec["address"], rec["country"])
        seen = set()
        cands = []
        for k in keys:
            p = engine.index.get(k)
            if p:
                for tid in p:
                    if tid not in seen and tid != s1_id:
                        seen.add(tid)
                        cands.append(tid)
                        if len(cands) >= engine.config.max_candidates_per_anchor:
                            break
            if len(cands) >= engine.config.max_candidates_per_anchor:
                break
        s2_cands[s1_id] = cands
        needed_s2_ids.update(cands)

    # Also add true matches to needed set
    for s1_id, matches in gt.items():
        for m in matches:
            if m.startswith("S2-"):
                needed_s2_ids.add(m)

    print(f"  Source 2: {len(needed_s2_ids):,} distinct targets needed")

    # Load raw records for needed S2 targets
    target_records = {}
    with open(S2_PATH, "r", encoding="utf-8") as f:
        f.readline()
        for line in f:
            parts = line.rstrip("\r\n").split("\t")
            if len(parts) < 4: continue
            eid = parts[0].strip()
            if eid in needed_s2_ids:
                target_records[eid] = {
                    "name": parts[1],
                    "address": parts[2] if len(parts) > 2 else "",
                    "country": parts[3] if len(parts) > 3 else ""
                }

    engine.index.clear()
    engine.target_records.clear()
    gc.collect()

    # 4. Retrieve Candidates from Source 3
    print("\nRetrieving candidates from Source 3...")
    engine.index_target_file(S3_PATH)
    s3_cands = defaultdict(list)
    needed_s3_ids = set()

    for s1_id, rec in s1_records.items():
        keys = engine.extract_blocking_keys(rec["name"], rec["address"], rec["country"])
        seen = set()
        cands = []
        for k in keys:
            p = engine.index.get(k)
            if p:
                for tid in p:
                    if tid not in seen and tid != s1_id:
                        seen.add(tid)
                        cands.append(tid)
                        if len(cands) >= engine.config.max_candidates_per_anchor:
                            break
            if len(cands) >= engine.config.max_candidates_per_anchor:
                break
        s3_cands[s1_id] = cands
        needed_s3_ids.update(cands)

    for s1_id, matches in gt.items():
        for m in matches:
            if m.startswith("S3-"):
                needed_s3_ids.add(m)

    print(f"  Source 3: {len(needed_s3_ids):,} distinct targets needed")

    with open(S3_PATH, "r", encoding="utf-8") as f:
        f.readline()
        for line in f:
            parts = line.rstrip("\r\n").split("\t")
            if len(parts) < 4: continue
            eid = parts[0].strip()
            if eid in needed_s3_ids:
                target_records[eid] = {
                    "name": parts[1],
                    "address": parts[2] if len(parts) > 2 else "",
                    "country": parts[3] if len(parts) > 3 else ""
                }

    # Save Cache Files
    print("\nSaving cache files to disk...")
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

    print(f"Validation cache successfully created at {CACHE_DIR}!")

if __name__ == "__main__":
    main()
