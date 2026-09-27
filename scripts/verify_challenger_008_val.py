#!/usr/bin/env python3
"""
Verify and Benchmark CHALLENGER_008 against CHALLENGER_007 and CHAMPION_0784 on the 5,000 validation cache.
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
    print("=" * 80)
    print("BENCHMARKING CANDIDATE CONFIGURATIONS ON 5,000 VALIDATION ANCHORS")
    print("=" * 80)

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

    # Base engine with CH007
    eng_ch007 = InferenceEngine(InferenceConfig(enable_challenger_007=True))
    eng_base = InferenceEngine(InferenceConfig(enable_challenger_007=False))

    def evaluate_scorer(score_fn, name=""):
        t0 = time.time()
        tp_dev, fp_dev, fn_dev = 0, 0, 0
        tp_hold, fp_hold, fn_hold = 0, 0, 0
        tp_all, fp_all, fn_all = 0, 0, 0
        match_count = 0

        for aid in all_ids:
            a = anchors[aid]
            gt_set = set(ground_truth[aid])
            cands = c2.get(aid, []) + c3.get(aid, [])
            scored = []
            for cid in cands:
                t = targets.get(cid)
                if not t: continue
                s = score_fn(a, t, cid)
                if s >= 0.58:
                    scored.append((cid, s))
            scored.sort(key=lambda x: x[1], reverse=True)
            preds = [x[0] for x in scored[:8]]
            match_count += len(preds)
            pred_set = set(preds)

            cur_tp = len(pred_set & gt_set)
            cur_fp = len(pred_set - gt_set)
            cur_fn = len(gt_set - pred_set)

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
        elapsed = time.time() - t0

        print(f"\n[{name}] ({elapsed:.2f}s, Total matches: {match_count:,}):")
        print(f"  OVERALL:  F0.5={f_all:.5f} | Prec={p_all*100:.2f}% | Rec={r_all*100:.2f}% | TP={tp_all:,}, FP={fp_all:,}, FN={fn_all:,}")
        print(f"  DEV 4k:   F0.5={f_dev:.5f} | Prec={p_dev*100:.2f}% | Rec={r_dev*100:.2f}%")
        print(f"  HOLDOUT:  F0.5={f_hold:.5f} | Prec={p_hold*100:.2f}% | Rec={r_hold*100:.2f}% | TP={tp_hold:,}, FP={fp_hold:,}, FN={fn_hold:,}")
        return f_all, p_all, r_all, match_count

    # 1. Base Champion (0.784)
    def score_champ(a, t, cid):
        return eng_base._score_pair(
            a['canon'], a['toks'], a['concat'],
            a['addr_toks'], a['num_toks'], a['country'],
            t[0], t[1], t[2], t[3], t[4], t[5], a.get('postal', '')
        )
    evaluate_scorer(score_champ, "CHAMPION_0784 (Base)")

    # 2. CHALLENGER_007
    def score_ch007(a, t, cid):
        return eng_ch007._score_pair(
            a['canon'], a['toks'], a['concat'],
            a['addr_toks'], a['num_toks'], a['country'],
            t[0], t[1], t[2], t[3], t[4], t[5], a.get('postal', '')
        )
    evaluate_scorer(score_ch007, "CHALLENGER_007")

    # 3. CHALLENGER_008 (Base + CH007 + P01_82 + P_POSTAL_080)
    def score_ch008(a, t, cid):
        s = eng_ch007._score_pair(
            a['canon'], a['toks'], a['concat'],
            a['addr_toks'], a['num_toks'], a['country'],
            t[0], t[1], t[2], t[3], t[4], t[5], a.get('postal', '')
        )
        if s >= 0.58:
            return s

        # Country and bldg contradiction veto check
        if a['country'] != "UNKNOWN" and t[3] != "UNKNOWN" and a['country'] != t[3]:
            return 0.0

        t_num_set = set(t[2])
        if a['num_toks'] and t_num_set:
            intersect = a['num_toks'].intersection(t_num_set)
            if not intersect:
                # Check OCR prefix truncation
                ocr_ok = False
                for an in a['num_toks']:
                    for tn in t_num_set:
                        if len(an) >= 2 and len(tn) >= 2 and (an.startswith(tn) or tn.startswith(an)) and abs(len(an) - len(tn)) <= 1:
                            ocr_ok = True
                            break
                    if ocr_ok: break
                if not ocr_ok:
                    return 0.0

        # P01_82: Address overlap >= 0.82 + business name overlap
        t_atok = set(t[1])
        if a['addr_toks'] and t_atok:
            union_len = len(a['addr_toks'] | t_atok)
            addr_sim = len(a['addr_toks'] & t_atok) / union_len if union_len > 0 else 0.0
            if addr_sim >= 0.82:
                t_toks = set(t[0].split())
                overlap = len(a['toks'] & t_toks) if a['toks'] and t_toks else 0
                if overlap >= 1 or (a['concat'] and t[5] and _char_similarity(a['concat'], t[5]) >= 0.75):
                    return 0.585

        # P_POSTAL_080: Shared exact postal code (>= 5 digits) + name Jaccard >= 0.80
        a_post = a.get('postal', '')
        t_post = t[4]
        if a_post and t_post and a_post == t_post and len(a_post) >= 5:
            t_toks = set(t[0].split())
            if a['toks'] and t_toks:
                jaccard = len(a['toks'] & t_toks) / len(a['toks'] | t_toks)
                if jaccard >= 0.80:
                    return 0.585

        return 0.0

    evaluate_scorer(score_ch008, "CHALLENGER_008 (P01_82 + P_POSTAL_080)")

if __name__ == "__main__":
    main()
