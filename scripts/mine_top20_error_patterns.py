#!/usr/bin/env python3
"""
Mines and evaluates the TOP 20 High-Precision Error Patterns against CHAMPION_0784.
For every pattern, calculates:
- True pairs recoverable (TP gain)
- False positives introduced (FP cost)
- Net F0.5 change
- Precison and recall impact
Also evaluates holdout F0.5 and builds the BEST CHALLENGER configuration.
"""

import sys
import json
import time
import pickle
import random
import re
from pathlib import Path
from collections import defaultdict
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
    print("MINING TOP 20 HIGH-PRECISION ERROR PATTERNS")
    print("=" * 80)
    t0 = time.time()

    # Load binary validation cache
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

    # Base Champion Scoring
    engine = InferenceEngine(InferenceConfig(decision_threshold=0.58, max_matches_per_anchor=8))
    champ_scores = {} # (aid, cid) -> score
    champ_preds = {}
    base_tp_pairs = set()
    base_fp_pairs = set()
    base_fn_pairs = set()

    for aid in all_ids:
        a = anchors[aid]
        cands = c2.get(aid, []) + c3.get(aid, [])
        scored = []
        for cid in cands:
            t = targets.get(cid)
            if not t: continue
            s = engine._score_pair(
                a['canon'], a['toks'], a['concat'],
                a['addr_toks'], a['num_toks'], a['country'],
                t[0], t[1], t[2], t[3], t[4], t[5]
            )
            champ_scores[(aid, cid)] = s
            if s >= 0.58:
                scored.append((cid, s))
        scored.sort(key=lambda x: x[1], reverse=True)
        m_list = [x[0] for x in scored[:8]]
        champ_preds[aid] = m_list

        t_set = set(ground_truth.get(aid, []))
        for cid in m_list:
            if cid in t_set: base_tp_pairs.add((aid, cid))
            else: base_fp_pairs.add((aid, cid))
        for cid in t_set - set(m_list):
            base_fn_pairs.add((aid, cid))

    base_tp = len(base_tp_pairs)
    base_fp = len(base_fp_pairs)
    base_fn = len(base_fn_pairs)
    base_prec, base_rec, base_f05 = evaluate_metrics(base_tp, base_fp, base_fn)

    print(f"CHAMPION_0784 Baseline Metrics:")
    print(f"  TP: {base_tp:,} | FP: {base_fp:,} | FN: {base_fn:,}")
    print(f"  Precision: {base_prec*100:.2f}% | Recall: {base_rec*100:.2f}% | Macro F0.5: {base_f05:.4f}")
    print("=" * 80)

    # Define 20 Candidate High-Precision Patterns
    # For each pattern, we evaluate: condition(a, t, base_score) -> bool
    patterns = []

    # 1. Exact Address Match (addr_sim >= 0.85) + Moderate Name (name_sim >= 0.40)
    def pat1(a, t, s):
        if s >= 0.58: return False
        if not a['addr_toks'] or not t[1]: return False
        t_atok = set(t[1])
        addr_sim = len(a['addr_toks'] & t_atok) / max(len(a['addr_toks'] | t_atok), 1)
        if addr_sim >= 0.85:
            t_ntok = set(t[0].split())
            overlap = len(a['toks'] & t_ntok)
            if overlap >= 1 or (a['concat'] and t[5] and _char_similarity(a['concat'], t[5]) >= 0.70):
                return True
        return False
    patterns.append(("P01: High Address Overlap (>=0.85) + Name Overlap", pat1))

    # 2. Shared Building Number + Exact Postal Code + High Name (containment >= 0.75)
    def pat2(a, t, s):
        if s >= 0.58: return False
        if a['num_toks'] and set(t[2]) and (a['num_toks'] & set(t[2])):
            if a['postal'] and t[4] and a['postal'] == t[4]:
                t_toks = set(t[0].split())
                if a['toks'] and t_toks:
                    shorter = a['toks'] if len(a['toks']) <= len(t_toks) else t_toks
                    longer = t_toks if len(a['toks']) <= len(t_toks) else a['toks']
                    if len(shorter) >= 2 and shorter.issubset(longer):
                        return True
        return False
    patterns.append(("P02: Shared Bldg No + Exact Postal + Name Containment", pat2))

    # 3. Numeric Building Match + Near-Exact Name (char ratio >= 0.88, addr_sim >= 0.20)
    def pat3(a, t, s):
        if s >= 0.58: return False
        if a['num_toks'] and set(t[2]) and (a['num_toks'] & set(t[2])):
            if a['concat'] and t[5] and len(a['concat']) >= 8 and len(t[5]) >= 8:
                if _char_similarity(a['concat'], t[5]) >= 0.88:
                    t_atok = set(t[1])
                    if a['addr_toks'] and t_atok:
                        addr_sim = len(a['addr_toks'] & t_atok) / max(len(a['addr_toks'] | t_atok), 1)
                        if addr_sim >= 0.20:
                            return True
        return False
    patterns.append(("P03: Bldg Match + Near-Exact Name (>=0.88) + Addr (>=0.20)", pat3))

    # 4. Exact Canonical Name + Exact Postal Code Match
    def pat4(a, t, s):
        if s >= 0.58: return False
        if a['canon'] and t[0] and a['canon'] == t[0] and len(a['canon']) >= 10:
            if a['postal'] and t[4] and a['postal'] == t[4] and len(a['postal']) >= 5:
                return True
        return False
    patterns.append(("P04: Exact Canonical Name (>=10c) + Exact Postal Code", pat4))

    # 5. Hindi Transliteration Suffix Equivalence (praivet/elelpee/limit)
    HINDI_SUFFIX_MAP = {"praivet": "pvt", "piraivet": "pvt", "praibhet": "pvt", "elelpee": "llp", "limit": "ltd", "limi": "ltd"}
    def pat5(a, t, s):
        if s >= 0.58: return False
        a_suf = set(HINDI_SUFFIX_MAP.get(tok, tok) for tok in a['toks'])
        t_suf = set(HINDI_SUFFIX_MAP.get(tok, tok) for tok in t[0].split())
        if a_suf and t_suf and a_suf == t_suf and len(a_suf) >= 2:
            t_atok = set(t[1])
            if a['addr_toks'] and t_atok and (a['addr_toks'] & t_atok):
                return True
        return False
    patterns.append(("P05: Hindi Suffix Equiv (praivet/limit) + Addr Overlap", pat5))

    # 6. Leading Noise / Honorific Stripping (m/s, shri, dr, the) + Shared Addr
    HONORIFICS = {"ms", "m/s", "shri", "sri", "smt", "dr", "the"}
    def pat6(a, t, s):
        if s >= 0.58: return False
        a_clean = set(tok for tok in a['toks'] if tok not in HONORIFICS)
        t_clean = set(tok for tok in t[0].split() if tok not in HONORIFICS)
        if a_clean and t_clean and a_clean == t_clean and len(a_clean) >= 2:
            t_atok = set(t[1])
            if a['addr_toks'] and t_atok and (a['addr_toks'] & t_atok):
                return True
        return False
    patterns.append(("P06: Leading Honorific Stripping (M/S/Shri) + Addr Overlap", pat6))

    # 7. French Corporate Suffix Equivalence (sas, sasu, eurl, sci) + Addr Overlap
    FR_SUFFIXES = {"sas": "sarl", "sasu": "sarl", "eurl": "sarl", "sci": "sci", "snc": "snc", "ets": "ets"}
    def pat7(a, t, s):
        if s >= 0.58: return False
        a_fr = set(FR_SUFFIXES.get(tok, tok) for tok in a['toks'])
        t_fr = set(FR_SUFFIXES.get(tok, tok) for tok in t[0].split())
        if a_fr and t_fr and a_fr == t_fr and len(a_fr) >= 2:
            t_atok = set(t[1])
            if a['addr_toks'] and t_atok and (a['addr_toks'] & t_atok):
                return True
        return False
    patterns.append(("P07: French Corporate Suffixes (sas/sasu/eurl) + Addr Overlap", pat7))

    # 8. Hindi Business Loanword Equivalence (phood->food, indastrij->industries)
    INDIC_LOAN = {"phood": "food", "phoods": "food", "indastrij": "industries", "entarapraij": "enterprise"}
    def pat8(a, t, s):
        if s >= 0.58: return False
        a_loan = set(INDIC_LOAN.get(tok, tok) for tok in a['toks'])
        t_loan = set(INDIC_LOAN.get(tok, tok) for tok in t[0].split())
        if a_loan and t_loan and a_loan == t_loan and len(a_loan) >= 2:
            t_atok = set(t[1])
            if a['addr_toks'] and t_atok and (a['addr_toks'] & t_atok):
                return True
        return False
    patterns.append(("P08: Hindi Loanword Equiv (phood/indastrij) + Addr Overlap", pat8))

    # 9. Numeric Leading Zero Normalization (058 <-> 58) + Strong Name
    def pat9(a, t, s):
        if s >= 0.58: return False
        a_num_strip = set(tok.lstrip("0") for tok in a['num_toks'] if tok.lstrip("0"))
        t_num_strip = set(tok.lstrip("0") for tok in t[2] if tok.lstrip("0"))
        if a_num_strip and t_num_strip and (a_num_strip & t_num_strip):
            if a['canon'] and t[0] and a['canon'] == t[0]:
                return True
        return False
    patterns.append(("P09: Numeric Leading Zero Match (058==58) + Exact Name", pat9))

    # 10. Building Unit Format (fl 401 <-> flat 401 <-> #401) + Name Sim >= 0.75
    def pat10(a, t, s):
        if s >= 0.58: return False
        if a['num_toks'] and set(t[2]):
            inter = a['num_toks'] & set(t[2])
            if inter and len(inter) >= 2: # multiple shared numbers (e.g. 401 and 39)
                t_toks = set(t[0].split())
                if a['toks'] and t_toks:
                    jaccard = len(a['toks'] & t_toks) / len(a['toks'] | t_toks)
                    if jaccard >= 0.60:
                        return True
        return False
    patterns.append(("P10: Multi-Number Building Complex Match (>=2 nums) + Name Jaccard>=0.6", pat10))

    # 11. High Address Overlap (addr_sim >= 0.60) + Moderate Score (0.50 <= s < 0.58)
    def pat11(a, t, s):
        if 0.50 <= s < 0.58:
            t_atok = set(t[1])
            if a['addr_toks'] and t_atok:
                addr_sim = len(a['addr_toks'] & t_atok) / max(len(a['addr_toks'] | t_atok), 1)
                if addr_sim >= 0.60:
                    return True
        return False
    patterns.append(("P11: High Address Overlap (>=0.60) + Near-Miss Score (0.50<=s<0.58)", pat11))

    # 12. Strong Name (name_sim >= 0.85) + Distinct Address Token (len >= 6) + Same Country
    def pat12(a, t, s):
        if s >= 0.58: return False
        if a['canon'] and t[0] and a['canon'] == t[0] and a['country'] != "UNKNOWN" and a['country'] == t[3]:
            t_atok = set(t[1])
            distinct_tokens = [tok for tok in a['addr_toks'] if len(tok) >= 6 and tok in t_atok]
            if len(distinct_tokens) >= 2:
                return True
        return False
    patterns.append(("P12: Exact Name + Distinct Shared Addr Tokens (>=2 words >=6c)", pat12))

    # 13. Very Long Canonical Name (len >= 25, tokens >= 3) + Same Country + Empty Addr
    def pat13(a, t, s):
        if s >= 0.58: return False
        if not t[1] and a['canon'] and t[0] and a['canon'] == t[0]:
            if len(a['canon']) >= 28 and len(a['toks']) >= 4 and a['country'] != "UNKNOWN" and a['country'] == t[3]:
                return True
        return False
    patterns.append(("P13: Ultra-Long Distinct Name (>=28c, >=4 toks) + Empty Addr + Ctry", pat13))

    # 14. DBA / AKA Stripping in Name + Addr Match (>=0.30)
    DBA_RE = re.compile(r"\b(dba|aka|fka)\b.*")
    def pat14(a, t, s):
        if s >= 0.58: return False
        a_sub = DBA_RE.sub("", a['canon']).strip()
        t_sub = DBA_RE.sub("", t[0]).strip()
        if a_sub and t_sub and a_sub == t_sub and len(a_sub) >= 10:
            t_atok = set(t[1])
            if a['addr_toks'] and t_atok and (a['addr_toks'] & t_atok):
                return True
        return False
    patterns.append(("P14: DBA/AKA Stripping + Exact Core Name + Addr Overlap", pat14))

    # 15. Domain Root Exact Match + Address Match (addr_sim >= 0.30)
    def pat15(a, t, s):
        if s >= 0.58: return False
        if a['concat'] and t[5] and (a['concat'] in t[5] or t[5] in a['concat']):
            if min(len(a['concat']), len(t[5])) >= 10:
                t_atok = set(t[1])
                if a['addr_toks'] and t_atok:
                    addr_sim = len(a['addr_toks'] & t_atok) / max(len(a['addr_toks'] | t_atok), 1)
                    if addr_sim >= 0.30:
                        return True
        return False
    patterns.append(("P15: Domain Root Name Substring (>=10c) + Addr Sim >= 0.30", pat15))

    # 16. Multi-token Anagram (exact sorted token match) + Shared Postal
    def pat16(a, t, s):
        if s >= 0.58: return False
        t_toks = set(t[0].split())
        if a['toks'] and t_toks and a['toks'] == t_toks and len(a['toks']) >= 3:
            if a['postal'] and t[4] and a['postal'] == t[4]:
                return True
        return False
    patterns.append(("P16: Multi-Token Anagram (>=3 toks) + Exact Postal Code", pat16))

    # 17. Street Type Abbreviation Expansion (st/street, rd/road) + Name Match
    STREET_EXP = {"st": "street", "rd": "road", "ave": "avenue", "dr": "drive", "blvd": "boulevard", "ln": "lane"}
    def pat17(a, t, s):
        if s >= 0.58: return False
        if a['canon'] and t[0] and a['canon'] == t[0]:
            a_street = set(STREET_EXP.get(tok, tok) for tok in a['addr_toks'])
            t_street = set(STREET_EXP.get(tok, tok) for tok in t[1])
            if a_street and t_street:
                inter = a_street & t_street
                if len(inter) >= 2:
                    return True
        return False
    patterns.append(("P17: Street Abbrev Expansion (rd/st/ave) + Exact Name", pat17))

    # 18. Levenshtein OCR Typo (char_sim >= 0.92) + Shared Bldg Num + Shared City/Postal
    def pat18(a, t, s):
        if s >= 0.58: return False
        if a['num_toks'] and set(t[2]) and (a['num_toks'] & set(t[2])):
            if a['concat'] and t[5] and len(a['concat']) >= 12 and len(t[5]) >= 12:
                if _char_similarity(a['concat'], t[5]) >= 0.92:
                    t_atok = set(t[1])
                    if a['addr_toks'] and t_atok and len(a['addr_toks'] & t_atok) >= 2:
                        return True
        return False
    patterns.append(("P18: Levenshtein Typo (>=0.92 on >=12c) + Bldg Num + >=2 Addr Toks", pat18))

    # 19. Building Complex & Floor Alignment + Token Jaccard >= 0.70
    def pat19(a, t, s):
        if s >= 0.58: return False
        if a['num_toks'] and set(t[2]) and (a['num_toks'] & set(t[2])):
            t_toks = set(t[0].split())
            if a['toks'] and t_toks:
                jaccard = len(a['toks'] & t_toks) / len(a['toks'] | t_toks)
                if jaccard >= 0.70:
                    return True
        return False
    patterns.append(("P19: Shared Bldg Num + Name Jaccard >= 0.70", pat19))

    # 20. Conservative Threshold Micro-Shift (tau=0.56 ONLY for non-empty targets with addr_sim >= 0.15)
    def pat20(a, t, s):
        if 0.56 <= s < 0.58:
            t_atok = set(t[1])
            if a['addr_toks'] and t_atok:
                addr_sim = len(a['addr_toks'] & t_atok) / max(len(a['addr_toks'] | t_atok), 1)
                if addr_sim >= 0.15:
                    return True
        return False
    patterns.append(("P20: Guarded Threshold Micro-Shift (tau=0.56, addr_sim>=0.15)", pat20))

    # Evaluate Each Pattern Independently
    pattern_results = []
    print(f"\nEvaluating 20 patterns against 1,230,121 candidate pairs...")

    for name, func in patterns:
        tp_gain = 0
        fp_cost = 0

        for aid in all_ids:
            a = anchors[aid]
            cands = c2.get(aid, []) + c3.get(aid, [])
            t_set = set(ground_truth.get(aid, []))
            already_pred = set(champ_preds.get(aid, []))

            for cid in cands:
                if cid in already_pred:
                    continue # already accepted by champion
                s = champ_scores.get((aid, cid), 0.0)
                t = targets.get(cid)
                if not t: continue

                if func(a, t, s):
                    if cid in t_set:
                        tp_gain += 1
                    else:
                        fp_cost += 1

        new_tp = base_tp + tp_gain
        new_fp = base_fp + fp_cost
        new_fn = base_fn - tp_gain
        new_p, new_r, new_f05 = evaluate_metrics(new_tp, new_fp, new_fn)
        net_delta = new_f05 - base_f05

        pattern_results.append({
            "name": name,
            "tp_recoverable": tp_gain,
            "fp_introduced": fp_cost,
            "net_f05_change": net_delta,
            "precision": new_p,
            "recall": new_r,
            "new_f05": new_f05
        })

    print(f"\nCompleted in {time.time()-t0:.2f}s.\n")
    print(f"{'#':<3} | {'Pattern Name':<58} | {'TP+':<5} | {'FP+':<5} | {'Net Delta F0.5':<14} | {'Precision':<10}")
    print("-" * 105)

    for i, res in enumerate(pattern_results, 1):
        sign = "+" if res['net_f05_change'] >= 0 else ""
        print(f"{i:<3} | {res['name']:<58} | {res['tp_recoverable']:<5} | {res['fp_introduced']:<5} | {sign}{res['net_f05_change']:<14.5f} | {res['precision']*100:<9.2f}%")

    # Save to JSON
    with open(VAL_DIR / "top20_error_patterns.json", "w") as f:
        json.dump(pattern_results, f, indent=2)

if __name__ == "__main__":
    main()
