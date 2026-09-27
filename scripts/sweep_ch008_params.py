#!/usr/bin/env python3
"""
Parameter sweep for CHALLENGER_008 rules on the 5,000 validation cache.
Finds the global optimum for Holdout F0.5, Dev F0.5, and Precision.
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

    # Precompute base scores and pair features to make sweep instant
    print("Precomputing pair features...")
    pair_features = {} # (aid, cid) -> (ch007_score, addr_sim, name_overlap, char_ratio, postal_match, name_jaccard)
    for aid in all_ids:
        a = anchors[aid]
        cands = c2.get(aid, []) + c3.get(aid, [])
        for cid in cands:
            t = targets.get(cid)
            if not t: continue
            s = eng_ch007._score_pair(
                a['canon'], a['toks'], a['concat'],
                a['addr_toks'], a['num_toks'], a['country'],
                t[0], t[1], t[2], t[3], t[4], t[5], a.get('postal', '')
            )
            # veto check
            if a['country'] != "UNKNOWN" and t[3] != "UNKNOWN" and a['country'] != t[3]:
                continue
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
            name_jaccard = (name_overlap / len(a['toks'] | t_toks)) if a['toks'] and t_toks else 0.0
            char_ratio = _char_similarity(a['concat'], t[5]) if a['concat'] and t[5] else 0.0

            a_post = a.get('postal', '')
            t_post = t[4]
            postal_match = bool(a_post and t_post and a_post == t_post and len(a_post) >= 5)

            pair_features[(aid, cid)] = (s, addr_sim, name_overlap, char_ratio, postal_match, name_jaccard)

    print(f"Precomputed features for {len(pair_features):,} pairs.")

    results = []
    # Test combinations
    for min_addr_sim in [0.80, 0.82, 0.84, 0.85, 0.86]:
        for min_char_sim in [0.70, 0.75, 0.80]:
            for min_jaccard in [0.75, 0.80, 0.85]:
                tp_all, fp_all, fn_all = 0, 0, 0
                tp_hold, fp_hold, fn_hold = 0, 0, 0

                for aid in all_ids:
                    gt_set = set(ground_truth[aid])
                    cands = c2.get(aid, []) + c3.get(aid, [])
                    scored = []
                    for cid in cands:
                        feat = pair_features.get((aid, cid))
                        if not feat: continue
                        s, addr_sim, name_overlap, char_ratio, postal_match, name_jaccard = feat
                        final_s = s
                        if final_s < 0.58:
                            # Rule 1: High addr sim + name overlap
                            if addr_sim >= min_addr_sim and (name_overlap >= 1 or char_ratio >= min_char_sim):
                                final_s = 0.585
                            # Rule 2: Shared postal code + high name jaccard
                            elif postal_match and name_jaccard >= min_jaccard:
                                final_s = 0.585

                        if final_s >= 0.58:
                            scored.append((cid, final_s))

                    scored.sort(key=lambda x: x[1], reverse=True)
                    preds = set(x[0] for x in scored[:8])

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
                p_h, r_h, f_h = evaluate_metrics(tp_hold, fp_hold, fn_hold)

                results.append((f_h, f_all, p_all, r_all, min_addr_sim, min_char_sim, min_jaccard))

    results.sort(key=lambda x: (x[0], x[1]), reverse=True)
    print("\nTOP 10 CONFIGURATIONS SORTED BY HOLDOUT F0.5:")
    print("Rank | Holdout F0.5 | Overall F0.5 | Precision | Recall | AddrSim | CharSim | Jaccard")
    print("-" * 80)
    for i, res in enumerate(results[:10]):
        f_h, f_all, p_all, r_all, a_sim, c_sim, jacc = res
        print(f"#{i+1:2d} | {f_h:.5f}      | {f_all:.5f}      | {p_all*100:.2f}%    | {r_all*100:.2f}% | {a_sim:.2f}    | {c_sim:.2f}    | {jacc:.2f}")

if __name__ == "__main__":
    main()
