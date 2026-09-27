#!/usr/bin/env python3
"""
Test engine.py directly against validation cache without monkeypatching.
"""
import sys
import json
import pickle
import random
from pathlib import Path

proj_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(proj_root / "code" / "business_entity_resolution" / "src"))
from ber.inference.engine import InferenceEngine, InferenceConfig

VAL_DIR = proj_root / "artifacts" / "challengers" / "CHALLENGER_007" / "val_cache"

with open(VAL_DIR / "norm_anchors.pkl", "rb") as f:
    anchors = pickle.load(f)
with open(VAL_DIR / "norm_targets.pkl", "rb") as f:
    targets = pickle.load(f)
with open(VAL_DIR / "candidates_s2.json", "r", encoding="utf-8") as f:
    c2 = json.load(f)
with open(VAL_DIR / "candidates_s3.json", "r", encoding="utf-8") as f:
    c3 = json.load(f)
with open(VAL_DIR / "ground_truth.json", "r", encoding="utf-8") as f:
    ground_truth = json.load(f)

all_ids = list(ground_truth.keys())
random.seed(42)
shuffled_ids = list(all_ids)
random.shuffle(shuffled_ids)
dev_ids = set(shuffled_ids[:4000])
hold_ids = set(shuffled_ids[4000:])

def evaluate_metrics(tp, fp, fn):
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f05 = 1.25 * prec * rec / (0.25 * prec + rec) if (0.25 * prec + rec) > 0 else 0.0
    return prec, rec, f05

engine = InferenceEngine(InferenceConfig())

tp_all, fp_all, fn_all = 0, 0, 0
tp_hold, fp_hold, fn_hold = 0, 0, 0
total_matches = 0

for aid in all_ids:
    a = anchors[aid]
    gt_set = set(ground_truth[aid])
    cands = c2.get(aid, []) + c3.get(aid, [])
    scored = []
    for cid in cands:
        t = targets.get(cid)
        if not t: continue
        s = engine._score_pair(
            a['canon'], a['toks'], a['concat'],
            a['addr_toks'], a['num_toks'], a['country'],
            t[0], t[1], t[2], t[3], t[4], t[5], a.get('postal', '')
        )
        if s >= engine.config.decision_threshold:
            scored.append((cid, s))
    scored.sort(key=lambda x: x[1], reverse=True)
    preds = set(x[0] for x in scored[:engine.config.max_matches_per_anchor])
    total_matches += len(preds)

    cur_tp = len(preds & gt_set)
    cur_fp = len(preds - gt_set)
    cur_fn = len(gt_set - preds)

    tp_all += cur_tp
    fp_all += cur_fp
    fn_all += cur_fn

    if aid in hold_ids:
        tp_hold += cur_tp
        fp_hold += cur_fp
        fn_hold += cur_fn

p_all, r_all, f_all = evaluate_metrics(tp_all, fp_all, fn_all)
p_hold, r_hold, f_hold = evaluate_metrics(tp_hold, fp_hold, fn_hold)

print(f"OFFICIAL InferenceEngine WITH CHALLENGER_008:")
print(f"  Total Matches: {total_matches:,}")
print(f"  OVERALL:  F0.5={f_all:.5f} | Precision={p_all*100:.2f}% | Recall={r_all*100:.2f}%")
print(f"  HOLDOUT:  F0.5={f_hold:.5f} | Precision={p_hold*100:.2f}% | Recall={r_hold*100:.2f}%")
