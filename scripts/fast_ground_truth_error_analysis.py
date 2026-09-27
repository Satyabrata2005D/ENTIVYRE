#!/usr/bin/env python3
"""
Fast Ground Truth Error Analysis
Loads 5,000 validation anchors and ONLY their true targets.
Executes in ~3 seconds.
Dissects:
1. Exact Blocking Recall (do anchor & true target share >=1 blocking key?)
2. Exact Scoring Recall (does score >= threshold for retrieved true pairs?)
3. Distribution of missed scores (vetoed vs borderline vs low score)
4. Concrete failure examples and missing patterns.
"""
import sys
import os
import csv
import time
import random
from pathlib import Path
from collections import Counter, defaultdict
from difflib import SequenceMatcher

proj_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(proj_root / "code" / "business_entity_resolution" / "src"))
sys.path.insert(0, str(proj_root))

from ber.inference.engine import InferenceEngine, InferenceConfig
from ber.normalization.name_normalizer import NameNormalizer
from ber.normalization.address_normalizer import AddressNormalizer
from ber.normalization.country_handler import CountryHandler

DATA_DIR = proj_root / "student_resource" / "dataset" / "train"

def main():
    print("=" * 80)
    print("FAST GROUND TRUTH ERROR ANALYSIS (5,000 Anchors)")
    print("=" * 80)
    t0 = time.time()
    
    # 1. Load ground truth
    print("[1/4] Loading ground truth...", flush=True)
    gt = {}
    with open(DATA_DIR / "train_ground_truth.tsv", "r", encoding="utf-8") as f:
        next(f)
        for line in f:
            parts = line.rstrip("\r\n").split("\t")
            s1 = parts[0].strip()
            tgts = set(parts[1].strip().split(",")) if len(parts) > 1 and parts[1].strip() else set()
            gt[s1] = tgts

    random.seed(42)
    # Filter for non-singletons for FN analysis
    non_singletons = [k for k, v in gt.items() if v]
    sample_ids = set(random.sample(non_singletons, 5000))
    needed_targets = set()
    for sid in sample_ids:
        needed_targets.update(gt[sid])
    print(f"  Sampled 5,000 anchors with {len(needed_targets):,} true targets in {time.time()-t0:.2f}s", flush=True)

    # 2. Load S1 records
    print("[2/4] Loading S1 records...", flush=True)
    s1_records = {}
    with open(DATA_DIR / "train_source1.tsv", "r", encoding="utf-8") as f:
        hdr = [c.lower() for c in f.readline().rstrip("\r\n").split("\t")]
        i_idx, n_idx, a_idx, c_idx = hdr.index("entity_id"), hdr.index("business_name"), hdr.index("business_address"), hdr.index("country")
        for line in f:
            p = line.rstrip("\r\n").split("\t")
            eid = p[i_idx].strip()
            if eid in sample_ids:
                s1_records[eid] = (p[n_idx], p[a_idx] if a_idx < len(p) else "", p[c_idx])

    # 3. Stream S2 & S3 for ONLY needed targets
    print("[3/4] Streaming S2 & S3 for true target records...", flush=True)
    target_records = {}
    def load_needed(path):
        with open(path, "r", encoding="utf-8") as f:
            hdr = [c.lower() for c in f.readline().rstrip("\r\n").split("\t")]
            i_idx, n_idx, a_idx, c_idx = hdr.index("entity_id"), hdr.index("business_name"), hdr.index("business_address"), hdr.index("country")
            for line in f:
                p = line.rstrip("\r\n").split("\t")
                eid = p[i_idx].strip()
                if eid in needed_targets:
                    target_records[eid] = (p[n_idx], p[a_idx] if a_idx < len(p) else "", p[c_idx])
                    if len(target_records) == len(needed_targets):
                        break

    load_needed(DATA_DIR / "train_source2.tsv")
    load_needed(DATA_DIR / "train_source3.tsv")
    print(f"  Loaded {len(target_records):,} target records in {time.time()-t0:.2f}s", flush=True)

    # 4. Engine evaluation
    print("[4/4] Evaluating Blocking and Scoring coverage...", flush=True)
    config = InferenceConfig()
    engine = InferenceEngine(config)
    nn = engine.name_normalizer
    an = engine.address_normalizer
    ch = engine.country_handler

    total_pairs = 0
    blocking_hits = 0
    blocking_misses = 0
    scoring_hits = 0
    scoring_misses = 0

    blocking_miss_examples = []
    scoring_miss_examples = []
    scoring_distribution = Counter()

    for s1_id in sample_ids:
        s1_name, s1_addr, s1_ctry = s1_records[s1_id]
        s1_keys = set(engine.extract_blocking_keys(s1_name, s1_addr, s1_ctry))
        
        norm_s1_name = nn.normalize(s1_name)
        norm_s1_addr = an.normalize(s1_addr) if s1_addr else None
        s1_canon = norm_s1_name.canonical
        s1_toks = set(t for t in norm_s1_name.tokens if len(t) >= config.min_name_token_length)
        s1_addr_toks = set(t for t in norm_s1_addr.tokens if len(t) >= config.min_addr_token_length) if norm_s1_addr else set()
        s1_num_toks = set(norm_s1_addr.numeric_tokens) if norm_s1_addr else set()
        s1_country = ch.normalize(s1_ctry).canonical or "UNKNOWN"
        s1_concat = "".join(norm_s1_name.tokens)

        for tid in gt[s1_id]:
            if tid not in target_records:
                continue
            total_pairs += 1
            t_name, t_addr, t_ctry = target_records[tid]
            t_keys = set(engine.extract_blocking_keys(t_name, t_addr, t_ctry))

            shared_keys = s1_keys & t_keys
            norm_t_name = nn.normalize(t_name)
            norm_t_addr = an.normalize(t_addr) if t_addr else None
            t_canon = norm_t_name.canonical
            t_toks = set(t for t in norm_t_name.tokens if len(t) >= config.min_name_token_length)
            t_addr_toks = set(t for t in norm_t_addr.tokens if len(t) >= config.min_addr_token_length) if norm_t_addr else set()
            t_num_toks = set(norm_t_addr.numeric_tokens) if norm_t_addr else set()
            t_country = ch.normalize(t_ctry).canonical or "UNKNOWN"
            t_postal = norm_t_addr.postal_code if norm_t_addr else ""
            t_concat = "".join(norm_t_name.tokens)

            # Score pair
            score = engine._score_pair(
                s1_canon, s1_toks, s1_concat,
                s1_addr_toks, s1_num_toks, s1_country,
                t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_concat
            )

            if shared_keys:
                blocking_hits += 1
                if score >= config.decision_threshold:
                    scoring_hits += 1
                else:
                    scoring_misses += 1
                    if len(scoring_miss_examples) < 50:
                        scoring_miss_examples.append({
                            "s1_name": s1_name, "s1_addr": s1_addr, "s1_ctry": s1_ctry,
                            "t_name": t_name, "t_addr": t_addr, "t_ctry": t_ctry,
                            "score": score, "shared_keys": list(shared_keys)[:3],
                            "s1_canon": s1_canon, "t_canon": t_canon
                        })
            else:
                blocking_misses += 1
                if len(blocking_miss_examples) < 50:
                    blocking_miss_examples.append({
                        "s1_name": s1_name, "s1_addr": s1_addr, "s1_ctry": s1_ctry,
                        "t_name": t_name, "t_addr": t_addr, "t_ctry": t_ctry,
                        "score_if_retrieved": score,
                        "s1_keys": list(s1_keys)[:4], "t_keys": list(t_keys)[:4],
                        "s1_canon": s1_canon, "t_canon": t_canon
                    })

            # Track score distribution across all true pairs
            if score == 0.0:
                scoring_distribution["0.00 (vetoed/zero)"] += 1
            elif score < 0.30:
                scoring_distribution["0.01 - 0.29"] += 1
            elif score < 0.50:
                scoring_distribution["0.30 - 0.49"] += 1
            elif score < config.decision_threshold:
                scoring_distribution[f"0.50 - {config.decision_threshold:.2f} (near miss)"] += 1
            else:
                scoring_distribution[f"{config.decision_threshold:.2f} - 1.00 (match)"] += 1

    print("\n" + "=" * 80)
    print("ANALYSIS RESULTS ACROSS TRUE PAIRS")
    print("=" * 80)
    print(f"Total True Pairs Analyzed: {total_pairs:,}")
    print(f"Blocking Hits:   {blocking_hits:,} ({blocking_hits/total_pairs*100:.2f}%)")
    print(f"Blocking Misses: {blocking_misses:,} ({blocking_misses/total_pairs*100:.2f}%)")
    print(f"Scoring Hits (Retrieved & >= {config.decision_threshold}): {scoring_hits:,} ({scoring_hits/total_pairs*100:.2f}%)")
    print(f"Scoring Misses (Retrieved but < {config.decision_threshold}): {scoring_misses:,} ({scoring_misses/total_pairs*100:.2f}%)")
    
    print("\nScore Distribution Across ALL True Pairs:")
    for k, v in scoring_distribution.most_common():
        print(f"  {k:30s}: {v:6,d} ({v/total_pairs*100:.2f}%)")

    print("\n" + "=" * 80)
    print("TOP 15 BLOCKING MISS EXAMPLES (Anchor & Target have 0 shared keys)")
    print("=" * 80)
    for i, ex in enumerate(blocking_miss_examples[:15]):
        print(f"\n[{i+1}] S1: {ex['s1_name']}")
        print(f"     Addr: {ex['s1_addr']} | Ctry: {ex['s1_ctry']}")
        print(f"     Canon: '{ex['s1_canon']}' | S1 Keys: {ex['s1_keys']}")
        print(f"     TGT: {ex['t_name']}")
        print(f"     Addr: {ex['t_addr']} | Ctry: {ex['t_ctry']}")
        print(f"     Canon: '{ex['t_canon']}' | Tgt Keys: {ex['t_keys']}")
        print(f"     Score if retrieved: {ex['score_if_retrieved']:.4f}")

    print("\n" + "=" * 80)
    print("TOP 15 SCORING MISS EXAMPLES (Shared key exists, but score < threshold)")
    print("=" * 80)
    for i, ex in enumerate(scoring_miss_examples[:15]):
        print(f"\n[{i+1}] S1: {ex['s1_name']}")
        print(f"     Addr: {ex['s1_addr']}")
        print(f"     TGT: {ex['t_name']}")
        print(f"     Addr: {ex['t_addr']}")
        print(f"     Score: {ex['score']:.4f} (Threshold: {config.decision_threshold})")
        print(f"     Shared keys: {ex['shared_keys']}")
        print(f"     S1 Canon: '{ex['s1_canon']}' vs TGT Canon: '{ex['t_canon']}'")

    print(f"\nCompleted in {time.time()-t0:.2f} seconds.")

if __name__ == "__main__":
    main()
