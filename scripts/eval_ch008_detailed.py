#!/usr/bin/env python3
"""
Detailed evaluation of the #1 Pareto-optimal CHALLENGER_008 configuration.
"""
import sys
import json
import time
import pickle
import random
from pathlib import Path
from difflib import SequenceMatcher

proj_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(proj_root / "code" / "business_entity_resolution" / "src"))

from ber.inference.engine import InferenceEngine, InferenceConfig, _char_similarity

VAL_DIR = proj_root / "artifacts" / "challengers" / "CHALLENGER_007" / "val_cache"

def evaluate_metrics(tp, fp, fn):
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f05 = 1.25 * prec * rec / (0.25 * prec + rec) if (0.25 * prec + rec) > 0 else 0.0
    return prec, rec, f05

def main():
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

    eng_ch007 = InferenceEngine(InferenceConfig(enable_challenger_007=True))

    tp_all, fp_all, fn_all = 0, 0, 0
    tp_dev, fp_dev, fn_dev = 0, 0, 0
    tp_hold, fp_hold, fn_hold = 0, 0, 0
    total_matches = 0

    p01_86_triggered = 0
    postal_080_triggered = 0

    for aid in all_ids:
        a = anchors[aid]
        gt_set = set(ground_truth[aid])
        cands = c2.get(aid, []) + c3.get(aid, [])
        scored = []
        for cid in cands:
            t = targets.get(cid)
            if not t: continue
            s = eng_ch007._score_pair(
                a['canon'], a['toks'], a['concat'],
                a['addr_toks'], a['num_toks'], a['country'],
                t[0], t[1], t[2], t[3], t[4], t[5], a.get('postal', '')
            )
            final_s = s
            if final_s < 0.58:
                # Contradiction check: country
                if a['country'] != "UNKNOWN" and t[3] != "UNKNOWN" and a['country'] != t[3]:
                    continue
                # Contradiction check: bldg number
                t_num_set = set(t[2])
                if a['num_toks'] and t_num_set:
                    intersect = a['num_toks'].intersection(t_num_set)
                    if not intersect:
                        ocr_ok = False
                        for an in a['num_toks']:
                            for tn in t_num_set:
                                if len(an) >= 2 and len(tn) >= 2 and (an.startswith(tn) or tn.startswith(an)) and abs(len(an) - len(tn)) <= 1:
                                    ocr_ok = True
                                    break
                            if ocr_ok: break
                        if not ocr_ok:
                            continue

                t_atok = set(t[1])
                addr_sim = 0.0
                if a['addr_toks'] and t_atok:
                    union_len = len(a['addr_toks'] | t_atok)
                    addr_sim = len(a['addr_toks'] & t_atok) / union_len if union_len > 0 else 0.0

                t_toks = set(t[0].split())
                name_overlap = len(a['toks'] & t_toks) if a['toks'] and t_toks else 0
                char_ratio = _char_similarity(a['concat'], t[5]) if a['concat'] and t[5] else 0.0

                # P01_86
                if addr_sim >= 0.86 and (name_overlap >= 1 or char_ratio >= 0.70):
                    final_s = 0.585
                    p01_86_triggered += 1
                else:
                    # P_POSTAL_080
                    a_post = a.get('postal', '')
                    t_post = t[4]
                    if a_post and t_post and a_post == t_post and len(a_post) >= 5:
                        if a['toks'] and t_toks:
                            name_jaccard = name_overlap / len(a['toks'] | t_toks)
                            if name_jaccard >= 0.80:
                                final_s = 0.585
                                postal_080_triggered += 1

            if final_s >= 0.58:
                scored.append((cid, final_s))

        scored.sort(key=lambda x: x[1], reverse=True)
        preds = set(x[0] for x in scored[:8])
        total_matches += len(preds)

        cur_tp = len(preds & gt_set)
        cur_fp = len(preds - gt_set)
        cur_fn = len(gt_set - preds)

        tp_all += cur_tp
        fp_all += cur_fp
        fn_all += cur_fn

        if aid in dev_ids:
            tp_dev += cur_tp
            fp_dev += cur_fp
            fn_dev += cur_fn
        else:
            tp_hold += cur_tp
            fp_hold += cur_fp
            fn_hold += cur_fn

    p_all, r_all, f_all = evaluate_metrics(tp_all, fp_all, fn_all)
    p_dev, r_dev, f_dev = evaluate_metrics(tp_dev, fp_dev, fn_dev)
    p_hold, r_hold, f_hold = evaluate_metrics(tp_hold, fp_hold, fn_hold)

    print(f"CHALLENGER_008 (#1 Configuration Details):")
    print(f"  P01_86 Triggered: {p01_86_triggered:,} | P_POSTAL_080 Triggered: {postal_080_triggered:,}")
    print(f"  Total Matches: {total_matches:,} (CH007 was 11,953, Champion was 11,905)")
    print(f"  OVERALL:  F0.5={f_all:.5f} | Precision={p_all*100:.2f}% | Recall={r_all*100:.2f}%")
    print(f"            TP={tp_all:,} | FP={fp_all:,} | FN={fn_all:,}")
    print(f"  DEV 4k:   F0.5={f_dev:.5f} | Precision={p_dev*100:.2f}% | Recall={r_dev*100:.2f}%")
    print(f"  HOLDOUT:  F0.5={f_hold:.5f} | Precision={p_hold*100:.2f}% | Recall={r_hold*100:.2f}%")
    print(f"            TP={tp_hold:,} | FP={fp_hold:,} | FN={fn_hold:,}")

if __name__ == "__main__":
    main()
