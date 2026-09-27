#!/usr/bin/env python3
"""
Test InferenceEngine with CHALLENGER_008 logic implemented inside the class.
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

# Subclass InferenceEngine to test the exact proposed implementation
class CH008InferenceEngine(InferenceEngine):
    def _score_pair(
        self,
        anchor_canon: str,
        anchor_toks,
        anchor_concat: str,
        anchor_addr_toks,
        anchor_num_toks,
        anchor_country: str,
        t_canon: str,
        t_addr_toks,
        t_num_toks,
        t_country: str,
        t_postal: str,
        t_name_concat: str,
        anchor_postal: str = "",
    ) -> float:
        # Base engine contradiction checks
        if anchor_country != "UNKNOWN" and t_country != "UNKNOWN" and anchor_country != t_country:
            return 0.0

        t_num_set = set(t_num_toks)
        has_bldg_conflict = False
        num_match = False
        if anchor_num_toks and t_num_set:
            intersect = anchor_num_toks.intersection(t_num_set)
            if intersect:
                num_match = True
                if len(anchor_num_toks) >= 2 and len(t_num_toks) >= 2:
                    a_num_list = sorted(anchor_num_toks)
                    t_num_list = sorted(t_num_set)
                    if a_num_list[0] != t_num_list[0] and a_num_list[0] not in t_num_set and t_num_list[0] not in anchor_num_toks:
                        has_bldg_conflict = True
                    elif a_num_list[-1] != t_num_list[-1] and a_num_list[-1] not in t_num_set and t_num_list[-1] not in anchor_num_toks:
                        has_bldg_conflict = True
            else:
                ocr_ok = False
                for an in anchor_num_toks:
                    for tn in t_num_set:
                        if len(an) >= 2 and len(tn) >= 2 and (an.startswith(tn) or tn.startswith(an)) and abs(len(an) - len(tn)) <= 1:
                            ocr_ok = True
                            break
                    if ocr_ok: break
                if ocr_ok:
                    num_match = True
                else:
                    has_bldg_conflict = True

        if has_bldg_conflict:
            return 0.0

        # === NAME SIMILARITY ===
        name_sim = 0.0
        if anchor_canon and t_canon and anchor_canon == t_canon:
            name_sim = 1.0
        elif anchor_toks and t_canon:
            t_toks = set(t for t in t_canon.split() if len(t) >= self.config.min_name_token_length)
            if t_toks:
                overlap = len(anchor_toks.intersection(t_toks))
                union_len = len(anchor_toks.union(t_toks))
                jaccard = overlap / union_len if union_len > 0 else 0.0
                name_sim = jaccard
                if jaccard < 0.85:
                    shorter, longer = (anchor_toks, t_toks) if len(anchor_toks) <= len(t_toks) else (t_toks, anchor_toks)
                    if len(shorter) >= 2 and shorter.issubset(longer):
                        containment = len(shorter) / len(longer) if longer else 0.0
                        name_sim = max(name_sim, 0.70 + 0.20 * containment)

        if name_sim < 0.85 and anchor_canon and t_canon:
            a_concat = anchor_concat
            t_concat = t_name_concat
            if a_concat and (a_concat == t_canon.replace(" ", "") or t_concat == anchor_canon.replace(" ", "") or a_concat == t_concat):
                name_sim = max(name_sim, 0.95)
            elif len(anchor_canon) >= 8 and len(t_canon) >= 8 and (anchor_canon in t_canon or t_canon in anchor_canon):
                name_sim = max(name_sim, 0.90)

        from ber.inference.engine import _char_similarity
        if name_sim < 0.80 and anchor_canon and t_canon:
            t_toks = set(t for t in t_canon.split() if len(t) >= self.config.min_name_token_length)
            has_token_overlap = bool(anchor_toks.intersection(t_toks)) if anchor_toks and t_toks else False
            if has_token_overlap or num_match:
                if anchor_concat and t_name_concat and len(anchor_concat) >= 6 and len(t_name_concat) >= 6:
                    ratio = _char_similarity(anchor_concat, t_name_concat)
                    if ratio >= 0.78:
                        name_sim = max(name_sim, ratio * 0.90)

        # === ADDRESS SIMILARITY ===
        addr_sim = 0.0
        t_atok_set = set(t for t in t_addr_toks if len(t) >= self.config.min_addr_token_length)
        if anchor_addr_toks and t_atok_set:
            overlap = len(anchor_addr_toks.intersection(t_atok_set))
            union_len = len(anchor_addr_toks.union(t_atok_set))
            addr_sim = overlap / union_len if union_len > 0 else 0.0

        # PRECISION GUARD WITH CHALLENGER_008 EXCEPTION
        if name_sim < 0.45:
            if getattr(self.config, 'enable_challenger_008', True):
                if t_atok_set and anchor_addr_toks and addr_sim >= 0.82:
                    t_toks = set(t for t in t_canon.split() if len(t) >= self.config.min_name_token_length)
                    overlap = len(anchor_toks.intersection(t_toks)) if anchor_toks and t_toks else 0
                    if overlap >= 1 or (anchor_concat and t_name_concat and _char_similarity(anchor_concat, t_name_concat) >= 0.70):
                        return 0.585
            return 0.0

        # === COMPOSITE SCORING ===
        score = 0.0
        if name_sim >= 0.85:
            if addr_sim >= 0.20:
                score = 0.60 * name_sim + 0.40 * addr_sim
            elif not t_atok_set:
                score = 0.55 * name_sim
            else:
                score = 0.40 * name_sim
        elif name_sim >= 0.65:
            if addr_sim >= 0.30:
                score = 0.50 * name_sim + 0.50 * addr_sim
            elif not t_atok_set:
                score = 0.45 * name_sim
            else:
                score = 0.35 * name_sim
        elif name_sim >= 0.50 and addr_sim >= 0.40:
            score = 0.45 * name_sim + 0.55 * addr_sim

        if score >= self.config.decision_threshold:
            return score

        # CHALLENGER_007 RULES
        if self.config.enable_challenger_007:
            if anchor_canon and t_canon and anchor_canon == t_canon and len(anchor_canon) >= 10:
                if anchor_postal and t_postal and anchor_postal == t_postal and len(anchor_postal) >= 5:
                    return 0.59
            if num_match and anchor_num_toks and t_num_set and (anchor_num_toks & t_num_set):
                if anchor_postal and t_postal and anchor_postal == t_postal:
                    t_toks = set(t for t in t_canon.split() if len(t) >= self.config.min_name_token_length)
                    if anchor_toks and t_toks:
                        shorter, longer = (anchor_toks, t_toks) if len(anchor_toks) <= len(t_toks) else (t_toks, anchor_toks)
                        if len(shorter) >= 2 and shorter.issubset(longer):
                            return 0.585
            if anchor_toks and len(anchor_toks) >= 3:
                t_toks = set(t for t in t_canon.split() if len(t) >= self.config.min_name_token_length)
                if anchor_toks == t_toks:
                    if anchor_postal and t_postal and anchor_postal == t_postal:
                        return 0.585
            if 0.56 <= score < 0.58:
                if t_atok_set and addr_sim >= 0.15:
                    return 0.5801 + (score - 0.56) * 0.1

        # CHALLENGER_008 RULES
        if getattr(self.config, 'enable_challenger_008', True):
            if t_atok_set and anchor_addr_toks and addr_sim >= 0.82:
                t_toks = set(t for t in t_canon.split() if len(t) >= self.config.min_name_token_length)
                overlap = len(anchor_toks.intersection(t_toks)) if anchor_toks and t_toks else 0
                if overlap >= 1 or (anchor_concat and t_name_concat and _char_similarity(anchor_concat, t_name_concat) >= 0.70):
                    return 0.585

            if anchor_postal and t_postal and anchor_postal == t_postal and len(anchor_postal) >= 5:
                t_toks = set(t for t in t_canon.split() if len(t) >= self.config.min_name_token_length)
                if anchor_toks and t_toks:
                    name_jaccard = len(anchor_toks.intersection(t_toks)) / len(anchor_toks.union(t_toks))
                    if name_jaccard >= 0.80:
                        return 0.585

        return 0.0

engine = CH008InferenceEngine(InferenceConfig())

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
        if s >= 0.58:
            scored.append((cid, s))
    scored.sort(key=lambda x: x[1], reverse=True)
    preds = set(x[0] for x in scored[:8])
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

print(f"VERIFIED CLASS IMPLEMENTATION:")
print(f"  Total Matches: {total_matches:,}")
print(f"  OVERALL:  F0.5={f_all:.5f} | Precision={p_all*100:.2f}% | Recall={r_all*100:.2f}%")
print(f"  HOLDOUT:  F0.5={f_hold:.5f} | Precision={p_hold*100:.2f}% | Recall={r_hold*100:.2f}%")
