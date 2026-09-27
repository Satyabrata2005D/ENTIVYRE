#!/usr/bin/env python3
"""
CHALLENGER_003 Validation — Quick 5000-anchor test on training data.
Measures TP/FP/FN/Precision/Recall/F0.5 to validate improvements before full inference.
"""

import os
import sys
import time
import csv
from pathlib import Path
from collections import defaultdict

proj_root = Path(__file__).parent.parent
sys.path.insert(0, str(proj_root / "code" / "business_entity_resolution" / "src"))
sys.path.insert(0, str(proj_root / "entivyre"))

from ber.inference.engine import InferenceEngine, InferenceConfig

DATASET_DIR = proj_root / "student_resource" / "dataset" / "train"
S1_PATH = DATASET_DIR / "train_source1.tsv"
S2_PATH = DATASET_DIR / "train_source2.tsv"
S3_PATH = DATASET_DIR / "train_source3.tsv"
GT_PATH = DATASET_DIR / "train_ground_truth.tsv"

SAMPLE_SIZE = 5000


def load_ground_truth(gt_path, limit):
    gt = {}
    with open(gt_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)
        count = 0
        for row in reader:
            if count >= limit:
                break
            s1_id = row[0].strip()
            matched_str = row[1].strip() if len(row) > 1 else ""
            gt[s1_id] = set(matched_str.split(",")) if matched_str else set()
            count += 1
    return gt


def load_source_records(path, id_set=None):
    records = {}
    with open(path, 'r', encoding='utf-8') as f:
        f.readline()
        for line in f:
            parts = line.rstrip('\r\n').split('\t')
            if len(parts) < 4:
                continue
            eid = parts[0].strip()
            if id_set is not None and eid not in id_set:
                continue
            records[eid] = (parts[1], parts[2] if len(parts) > 2 else "", parts[3] if len(parts) > 3 else "")
    return records


def main():
    print("=" * 80)
    print("CHALLENGER_003 VALIDATION — 5000-Anchor Training Sample")
    print("=" * 80)
    
    t0 = time.time()
    
    print(f"\n[1] Loading ground truth...")
    gt = load_ground_truth(GT_PATH, SAMPLE_SIZE)
    total_true = sum(len(v) for v in gt.values())
    has_matches = sum(1 for v in gt.values() if v)
    print(f"  {len(gt)} anchors, {has_matches} with matches, {total_true} total true pairs")
    
    print(f"\n[2] Loading S1 records...")
    s1_records = load_source_records(S1_PATH, set(gt.keys()))
    
    print(f"\n[3] Indexing targets...")
    engine = InferenceEngine(InferenceConfig())
    n2 = engine.index_target_file(S2_PATH)
    n3 = engine.index_target_file(S3_PATH)
    print(f"  Indexed {n2+n3} targets, {len(engine.index)} index keys")
    
    print(f"\n[4] Running inference...")
    from ber.normalization.name_normalizer import NameNormalizer
    from ber.normalization.address_normalizer import AddressNormalizer
    from ber.normalization.country_handler import CountryHandler
    
    nn = NameNormalizer()
    an = AddressNormalizer()
    ch = CountryHandler()
    
    tp = fp = fn = 0
    fn_blocking = fn_score = 0
    
    for i, (s1_id, true_matches) in enumerate(gt.items()):
        if s1_id not in s1_records:
            fn += len(true_matches)
            continue
        
        name, address, country = s1_records[s1_id]
        
        # Blocking
        keys = engine.extract_blocking_keys(name, address, country)
        seen = set()
        cands = []
        for k in keys:
            posting = engine.index.get(k)
            if posting:
                for tid in posting:
                    if tid not in seen and tid != s1_id:
                        seen.add(tid)
                        cands.append(tid)
                        if len(cands) >= engine.config.max_candidates_per_anchor:
                            break
            if len(cands) >= engine.config.max_candidates_per_anchor:
                break
        
        cand_set = set(cands)
        
        # Scoring
        norm_name = nn.normalize(name)
        norm_addr = an.normalize(address) if address else None
        anchor_canon = norm_name.canonical
        anchor_toks = set(t for t in norm_name.tokens if len(t) >= 2)
        anchor_addr_toks = set(t for t in norm_addr.tokens if len(t) >= 2) if norm_addr else set()
        anchor_num_toks = set(norm_addr.numeric_tokens) if norm_addr else set()
        anchor_country = ch.normalize(country).canonical or "UNKNOWN"
        anchor_concat = "".join(norm_name.tokens)
        
        matched = set()
        for cid in cands:
            rec = engine.target_records.get(cid)
            if not rec:
                continue
            t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat = rec
            
            score = engine._score_pair(
                anchor_canon, anchor_toks, anchor_concat,
                anchor_addr_toks, anchor_num_toks, anchor_country,
                t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat,
            )
            
            if score >= engine.config.decision_threshold:
                matched.add(cid)
        
        # Cap matches
        if len(matched) > engine.config.max_matches_per_anchor:
            matched = set(list(matched)[:engine.config.max_matches_per_anchor])
        
        tp += len(matched & true_matches)
        fp += len(matched - true_matches)
        
        missed = true_matches - matched
        fn += len(missed)
        for m in missed:
            if m not in cand_set:
                fn_blocking += 1
            else:
                fn_score += 1
        
        if (i+1) % 1000 == 0:
            elapsed = time.time() - t0
            prec = tp / (tp + fp) if (tp + fp) > 0 else 0
            rec = tp / (tp + fn) if (tp + fn) > 0 else 0
            f05 = (1.25 * prec * rec) / (0.25 * prec + rec) if (0.25 * prec + rec) > 0 else 0
            print(f"  [{i+1}/{SAMPLE_SIZE}] TP={tp} FP={fp} FN={fn} P={prec:.4f} R={rec:.4f} F0.5={f05:.4f} [{elapsed:.0f}s]")
    
    # Final metrics
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    f05 = 1.25 * precision * recall / (0.25 * precision + recall) if (0.25 * precision + recall) > 0 else 0
    
    elapsed = time.time() - t0
    
    print("\n" + "=" * 80)
    print("CHALLENGER_003 VALIDATION RESULTS")
    print("=" * 80)
    print(f"  TP:  {tp}")
    print(f"  FP:  {fp}")
    print(f"  FN:  {fn}")
    print(f"  Precision: {precision:.4f}")
    print(f"  Recall:    {recall:.4f}")
    print(f"  F1:        {f1:.4f}")
    print(f"  F0.5:      {f05:.4f}")
    print(f"\n  FN Breakdown:")
    print(f"    Blocking miss: {fn_blocking} ({100*fn_blocking/max(fn,1):.1f}%)")
    print(f"    Score miss:    {fn_score} ({100*fn_score/max(fn,1):.1f}%)")
    print(f"\n  Elapsed: {elapsed:.1f}s")
    
    print("\n  COMPARISON vs CHALLENGER_002:")
    print(f"    CHALLENGER_002: P=0.9091 R=0.5435 F0.5=0.8013")
    print(f"    CHALLENGER_003: P={precision:.4f} R={recall:.4f} F0.5={f05:.4f}")
    improvement = f05 - 0.8013
    print(f"    F0.5 Change: {'+' if improvement >= 0 else ''}{improvement:.4f}")
    print("=" * 80)


if __name__ == "__main__":
    main()
