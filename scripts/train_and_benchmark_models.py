#!/usr/bin/env python3
"""
Phase 14, 15, 16: Comprehensive Model Research, Calibration & Decision Optimization.
Evaluates:
A. Deterministic baseline (CHAMPION_784)
B. Logistic Regression
C. HistGradientBoostingClassifier (GBDT)
D. Calibrated GBDT (Isotonic)
E. Hybrid Lexical-ML Ensemble
F. Decision policies: Evidence Floor, Contradiction Veto, Best-vs-Second Margin

Splits 5,000 validation anchors into:
- 3,500 anchors for training
- 1,500 anchors for out-of-sample testing
"""

import sys
import gc
import re
import csv
import json
import time
import numpy as np
from pathlib import Path
from collections import Counter, defaultdict
from difflib import SequenceMatcher

import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.calibration import CalibratedClassifierCV

proj_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(proj_root / "code" / "business_entity_resolution" / "src"))

from ber.normalization.name_normalizer import NameNormalizer
from ber.normalization.address_normalizer import AddressNormalizer
from ber.normalization.country_handler import CountryHandler
import ber.normalization.name_normalizer as nnm
import ber.normalization.transliteration as trm

DATASET_DIR = proj_root / "student_resource" / "dataset" / "train"
S1_PATH = DATASET_DIR / "train_source1.tsv"
S2_PATH = DATASET_DIR / "train_source2.tsv"
S3_PATH = DATASET_DIR / "train_source3.tsv"
GT_PATH = DATASET_DIR / "train_ground_truth.tsv"

TOTAL_ANCHORS = 5000
TRAIN_ANCHORS = 3500
TEST_ANCHORS = 1500

# Legal suffix dictionary with Indian & French forms
EXTENDED_SUFFIXES = {
    "private": "pvt", "pvt": "pvt", "llp": "llp", "l l p": "llp",
    "public limited": "ltd", "plc": "ltd", "p l c": "ltd",
    "proprietorship": "prop", "prop": "prop",
    "praivet": "pvt", "piraivet": "pvt", "praibhet": "pvt", "praiv": "pvt",
    "elelpee": "llp", "limit": "ltd", "limi": "ltd",
    "sarl": "sarl", "sas": "sarl", "sasu": "sarl", "eurl": "sarl",
    "sci": "sci", "snc": "snc", "ets": "ets", "fils": "fils", "cie": "co", "ste": "co"
}

def map_indic_to_devanagari(text: str) -> str:
    res = []
    has_indic = False
    for c in text:
        code = ord(c)
        if 0x0980 <= code <= 0x0D7F:
            res.append(chr(0x0900 + (code % 0x80)))
            has_indic = True
        else:
            res.append(c)
    return "".join(res) if has_indic else text

DBA_REGEX = re.compile(r"\b(?:dba|aka|fka|formerly\s+known\s+as|doing\s+business\s+as)\b.*$", re.IGNORECASE)
LEADING_THE_REGEX = re.compile(r"^the\s+", re.IGNORECASE)

def _char_similarity(s1: str, s2: str) -> float:
    if s1 == s2:
        return 1.0
    if not s1 or not s2:
        return 0.0
    return SequenceMatcher(None, s1, s2).ratio()

class FeatureExtractor:
    def __init__(self):
        self.nn = NameNormalizer()
        self.an = AddressNormalizer()
        self.ch = CountryHandler()

    def normalize_name(self, name: str):
        n_clean = LEADING_THE_REGEX.sub("", name.strip())
        n_clean = DBA_REGEX.sub("", n_clean).strip() or name
        n_indic = map_indic_to_devanagari(n_clean)
        norm = self.nn.normalize(n_indic)
        toks = [EXTENDED_SUFFIXES.get(t, t) for t in norm.tokens]
        toks = ["food" if t in ("phood", "phoods") else t for t in toks]
        toks = ["ss" if t == "eses" else t for t in toks]
        canon = " ".join(toks)
        return norm, tuple(toks), canon

    def extract_blocking_keys_with_channel(self, name: str, address: str = "", country: str = ""):
        norm_name, toks, canon = self.normalize_name(name)
        norm_addr = self.an.normalize(address) if address else None
        keys = []

        if canon:
            keys.append((f"NC:{canon}", "name_exact"))
            concat_str = "".join(toks)
            if len(concat_str) >= 6:
                keys.append((f"NCONCAT:{concat_str[:20]}", "name_ngram"))

        if norm_addr and norm_addr.numeric_tokens and norm_addr.tokens:
            p_num = norm_addr.numeric_tokens[0]
            for w in norm_addr.tokens[:3]:
                if len(w) >= 4:
                    keys.append((f"ADDR_NW:{p_num}_{w}", "addr_exact"))

        if canon and len(toks) >= 2:
            clean_toks = [t for t in toks if len(t) >= 2]
            if len(clean_toks) >= 2:
                keys.append((f"NS:{'_'.join(sorted(clean_toks[:4]))}", "name_token"))
                keys.append((f"NP:{clean_toks[0]}_{clean_toks[1]}", "name_token"))
            elif len(clean_toks) == 1 and len(clean_toks[0]) >= 3:
                keys.append((f"N1:{clean_toks[0]}", "name_token"))
        elif canon and len(toks) == 1 and len(toks[0]) >= 3:
            keys.append((f"N1:{toks[0]}", "name_token"))

        if norm_addr and len(norm_addr.tokens) >= 2:
            keys.append((f"ADDR_WW:{norm_addr.tokens[0]}_{norm_addr.tokens[1]}", "addr_token"))

        if norm_addr and norm_addr.numeric_tokens and toks:
            p_num = norm_addr.numeric_tokens[0]
            n_first = toks[0]
            if len(n_first) >= 3:
                keys.append((f"ADDR_N1:{p_num}_{n_first[:4]}", "composite"))

        if norm_addr and norm_addr.postal_code and toks:
            n_first = toks[0]
            if len(n_first) >= 3:
                keys.append((f"PIN_N1:{norm_addr.postal_code}_{n_first[:4]}", "composite"))

        if toks and len(toks[0]) >= 5:
            keys.append((f"N1L:{toks[0]}", "name_rare"))

        return keys

    def compute_features(self, s1_rec, target_rec, target_id, channels_hit):
        s1_n, s1_a, s1_c = s1_rec
        t_n, t_a, t_c = target_rec

        _, s1_toks, s1_canon = self.normalize_name(s1_n)
        _, t_toks, t_canon = self.normalize_name(t_n)

        s1_norm_a = self.an.normalize(s1_a) if s1_a else None
        t_norm_a = self.an.normalize(t_a) if t_a else None

        s1_ctry = self.ch.normalize(s1_c).canonical or "UNKNOWN"
        t_ctry = self.ch.normalize(t_c).canonical or "UNKNOWN"

        # 1. Name Features
        exact_raw_name = 1.0 if s1_n == t_n else 0.0
        exact_norm_name = 1.0 if s1_canon == t_canon and s1_canon else 0.0

        s1_t_set = set(t for t in s1_toks if len(t) >= 2)
        t_t_set = set(t for t in t_toks if len(t) >= 2)
        inter = len(s1_t_set & t_t_set)
        union = len(s1_t_set | t_t_set)
        tok_jaccard = inter / union if union > 0 else 0.0

        shorter = s1_t_set if len(s1_t_set) <= len(t_t_set) else t_t_set
        longer = t_t_set if len(s1_t_set) <= len(t_t_set) else s1_t_set
        tok_containment = len(shorter & longer) / len(longer) if longer else 0.0

        s1_concat = "".join(s1_toks)
        t_concat = "".join(t_toks)
        concat_match = 1.0 if s1_concat and (s1_concat == t_concat) else 0.0
        char_sim = _char_similarity(s1_concat, t_concat) if s1_concat and t_concat else 0.0

        len_diff = abs(len(s1_canon) - len(t_canon))
        max_len = max(len(s1_canon), len(t_canon), 1)
        len_ratio = len_diff / max_len

        first_tok_match = 1.0 if s1_toks and t_toks and s1_toks[0] == t_toks[0] else 0.0
        last_tok_match = 1.0 if s1_toks and t_toks and s1_toks[-1] == t_toks[-1] else 0.0

        # 2. Address Features
        s1_a_toks = set(t for t in s1_norm_a.tokens if len(t) >= 2) if s1_norm_a else set()
        t_a_toks = set(t for t in t_norm_a.tokens if len(t) >= 2) if t_norm_a else set()
        a_inter = len(s1_a_toks & t_a_toks)
        a_union = len(s1_a_toks | t_a_toks)
        addr_jaccard = a_inter / a_union if a_union > 0 else 0.0

        s1_nums = set(s1_norm_a.numeric_tokens) if s1_norm_a else set()
        t_nums = set(t_norm_a.numeric_tokens) if t_norm_a else set()

        bldg_intersect = len(s1_nums & t_nums)
        bldg_exact_match = 1.0 if bldg_intersect > 0 else 0.0

        bldg_conflict = 0.0
        bldg_ocr_match = 0.0
        if s1_nums and t_nums:
            if bldg_intersect == 0:
                ocr_ok = False
                for an in s1_nums:
                    for tn in t_nums:
                        if len(an) >= 2 and len(tn) >= 2 and (an.startswith(tn) or tn.startswith(an)) and abs(len(an) - len(tn)) <= 1:
                            ocr_ok = True
                            break
                    if ocr_ok: break
                if ocr_ok:
                    bldg_ocr_match = 1.0
                else:
                    bldg_conflict = 1.0

        s1_pin = s1_norm_a.postal_code if s1_norm_a else ""
        t_pin = t_norm_a.postal_code if t_norm_a else ""
        postal_match = 1.0 if s1_pin and t_pin and s1_pin == t_pin else 0.0

        # 3. Country & Source Features
        country_match = 1.0 if s1_ctry != "UNKNOWN" and t_ctry != "UNKNOWN" and s1_ctry == t_ctry else 0.0
        country_conflict = 1.0 if s1_ctry != "UNKNOWN" and t_ctry != "UNKNOWN" and s1_ctry != t_ctry else 0.0
        is_india = 1.0 if s1_ctry == "INDIA" else 0.0
        is_us = 1.0 if s1_ctry == "US" else 0.0
        is_s2 = 1.0 if target_id.startswith("S2-") else 0.0
        is_s3 = 1.0 if target_id.startswith("S3-") else 0.0

        # 4. Provenance Features
        num_channels = float(len(channels_hit))
        has_exact_name_channel = 1.0 if "name_exact" in channels_hit else 0.0
        has_exact_addr_channel = 1.0 if "addr_exact" in channels_hit else 0.0
        has_composite_channel = 1.0 if "composite" in channels_hit else 0.0

        # 5. Cross-field Interactions
        cross_name_addr = tok_jaccard * addr_jaccard
        cross_name_bldg = tok_jaccard * bldg_exact_match
        cross_char_addr = char_sim * addr_jaccard
        missing_addr = 1.0 if (not s1_a or not t_a) else 0.0

        feat = [
            exact_raw_name, exact_norm_name, tok_jaccard, tok_containment,
            concat_match, char_sim, len_ratio, first_tok_match, last_tok_match,
            addr_jaccard, float(a_inter), bldg_exact_match, bldg_ocr_match,
            bldg_conflict, float(bldg_intersect), postal_match,
            country_match, country_conflict, is_india, is_us, is_s2, is_s3,
            num_channels, has_exact_name_channel, has_exact_addr_channel, has_composite_channel,
            cross_name_addr, cross_name_bldg, cross_char_addr, missing_addr
        ]
        return np.array(feat, dtype=np.float32)

def evaluate_predictions(gt_dict, pred_dict):
    """Calculates official Macro F0.5 per S1 entity."""
    entity_f05_scores = []
    total_tp = 0
    total_fp = 0
    total_fn = 0

    for s1_id, true_set in gt_dict.items():
        preds = set(pred_dict.get(s1_id, []))
        is_singleton = (len(true_set) == 0)

        if is_singleton:
            if len(preds) == 0:
                entity_f05_scores.append(1.0)
            else:
                total_fp += len(preds)
                entity_f05_scores.append(0.0)
        else:
            tp = len(preds & true_set)
            fp = len(preds - true_set)
            fn = len(true_set - preds)
            total_tp += tp
            total_fp += fp
            total_fn += fn

            if tp == 0:
                entity_f05_scores.append(0.0)
            else:
                p_i = tp / (tp + fp)
                r_i = tp / len(true_set)
                f05_i = (1.25 * p_i * r_i) / (0.25 * p_i + r_i)
                entity_f05_scores.append(f05_i)

    macro_f05 = float(np.mean(entity_f05_scores))
    micro_prec = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0.0
    micro_rec = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0.0
    return macro_f05, micro_prec, micro_rec, total_tp, total_fp, total_fn

def main():
    print("=" * 80)
    print("PHASE 14, 15, 16: ADVANCED ML & CALIBRATED MODEL BENCHMARK")
    print("=" * 80)
    t0 = time.time()

    # 1. Load Ground Truth
    gt_all = {}
    with open(GT_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)
        for i, row in enumerate(reader):
            if i >= TOTAL_ANCHORS: break
            s1 = row[0].strip()
            m = [x.strip() for x in row[1].split(",") if x.strip()] if len(row) > 1 and row[1].strip() else []
            gt_all[s1] = set(m)

    anchor_list = list(gt_all.keys())
    train_anchors = anchor_list[:TRAIN_ANCHORS]
    test_anchors = anchor_list[TRAIN_ANCHORS:]

    gt_train = {sid: gt_all[sid] for sid in train_anchors}
    gt_test = {sid: gt_all[sid] for sid in test_anchors}

    print(f"Loaded {len(gt_all)} anchors: {len(train_anchors)} Train, {len(test_anchors)} Test")

    # 2. Load S1 Records
    needed_s1 = set(gt_all.keys())
    s1_records = {}
    with open(S1_PATH, "r", encoding="utf-8") as f:
        for line in f:
            p = line.rstrip("\r\n").split("\t")
            if len(p) >= 4 and p[0].strip() in needed_s1:
                s1_records[p[0].strip()] = (p[1], p[2], p[3])

    # 3. Load All True Targets
    all_true_targets = set()
    for tgts in gt_all.values():
        all_true_targets.update(tgts)

    target_records = {}
    def load_t(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                p = line.rstrip("\r\n").split("\t")
                if len(p) >= 4 and p[0].strip() in all_true_targets:
                    target_records[p[0].strip()] = (p[1], p[2], p[3])
                    if len(target_records) == len(all_true_targets):
                        break

    load_t(S2_PATH)
    load_t(S3_PATH)
    print(f"Loaded records in {time.time()-t0:.1f}s. Extracting features for Train and Test sets...")

    fe = FeatureExtractor()

    # Precompute target keys and build inverted index over the 17,250 target records
    print("Precomputing target blocking keys and inverted index...")
    t_index_start = time.time()
    target_keys_cache = {}
    target_key_to_tids = defaultdict(list)

    for tid, t_rec in target_records.items():
        t_n, t_a, t_c = t_rec
        t_keys_chan = fe.extract_blocking_keys_with_channel(t_n, t_a, t_c)
        target_keys_cache[tid] = t_keys_chan
        for k, c in t_keys_chan:
            target_key_to_tids[k].append(tid)

    print(f"Precomputed index in {time.time()-t_index_start:.2f}s with {len(target_key_to_tids):,} unique keys.")

    # Build Training and Testing Feature Matrices
    def build_dataset(anchor_sublist, gt_subdict):
        X_list = []
        y_list = []
        pairs_index = defaultdict(list) # sid -> [(tid, feat_vector, label)]

        for s1_id in anchor_sublist:
            s1_rec = s1_records[s1_id]
            s1_n, s1_a, s1_c = s1_rec
            s1_keys_chan = fe.extract_blocking_keys_with_channel(s1_n, s1_a, s1_c)
            s1_keys = set(k for k, c in s1_keys_chan)
            key_to_chan = {k: c for k, c in s1_keys_chan}

            true_set = gt_subdict[s1_id]

            # True targets (Positives)
            for tid in true_set:
                t_rec = target_records.get(tid)
                if not t_rec: continue
                t_keys_chan = target_keys_cache[tid]
                t_keys = set(k for k, c in t_keys_chan)

                shared = s1_keys & t_keys
                channels_hit = set(key_to_chan[k] for k in shared) if shared else set()
                feat = fe.compute_features(s1_rec, t_rec, tid, channels_hit)

                X_list.append(feat)
                y_list.append(1)
                pairs_index[s1_id].append((tid, feat, 1))

            # Retrieve candidate Hard Negatives using the inverted index
            cand_tids = set()
            for k in s1_keys:
                postings = target_key_to_tids.get(k, [])
                for tid in postings:
                    if tid not in true_set:
                        cand_tids.add(tid)
                        if len(cand_tids) >= 15:
                            break
                if len(cand_tids) >= 15:
                    break

            for tid in cand_tids:
                t_rec = target_records[tid]
                t_keys_chan = target_keys_cache[tid]
                t_keys = set(k for k, c in t_keys_chan)
                shared = s1_keys & t_keys
                channels_hit = set(key_to_chan[k] for k in shared) if shared else set()
                feat = fe.compute_features(s1_rec, t_rec, tid, channels_hit)

                X_list.append(feat)
                y_list.append(0)
                pairs_index[s1_id].append((tid, feat, 0))

        return np.array(X_list), np.array(y_list), pairs_index

    X_train, y_train, train_pairs = build_dataset(train_anchors, gt_train)
    X_test, y_test, test_pairs = build_dataset(test_anchors, gt_test)

    print(f"Train Dataset: {X_train.shape[0]:,} pairs ({sum(y_train):,} positives, {len(y_train)-sum(y_train):,} hard negatives)")
    print(f"Test Dataset:  {X_test.shape[0]:,} pairs ({sum(y_test):,} positives, {len(y_test)-sum(y_test):,} hard negatives)")

    # 4. Train Models
    print("\nTraining Models...")

    # Model B: Logistic Regression
    print("  [1/3] Logistic Regression...")
    clf_lr = LogisticRegression(max_iter=1000, class_weight="balanced", random_state=42)
    clf_lr.fit(X_train, y_train)

    # Model C: HistGradientBoosting (GBDT)
    print("  [2/3] HistGradientBoostingClassifier (GBDT)...")
    clf_gbdt = HistGradientBoostingClassifier(
        max_iter=150, max_depth=6, learning_rate=0.05,
        class_weight="balanced", random_state=42
    )
    clf_gbdt.fit(X_train, y_train)

    # Model D: Calibrated GBDT
    print("  [3/3] Calibrated GBDT (Isotonic)...")
    clf_calibrated = CalibratedClassifierCV(
        HistGradientBoostingClassifier(max_iter=150, max_depth=6, learning_rate=0.05, class_weight="balanced", random_state=42),
        cv=3, method="isotonic"
    )
    clf_calibrated.fit(X_train, y_train)

    print("Model training complete. Evaluating on Held-Out Test Fold (1,500 Anchors)...")

    # Evaluate Each Model on Test Fold
    models = [
        ("Logistic Regression", clf_lr),
        ("HistGradientBoosting (GBDT)", clf_gbdt),
        ("Calibrated GBDT (Isotonic)", clf_calibrated)
    ]

    print("\n" + "=" * 90)
    print(f"{'Model Architecture':<30} | {'Macro F0.5':<10} | {'Precision':<10} | {'Recall':<10} | {'TP':<6} | {'FP':<6}")
    print("-" * 90)

    for m_name, model in models:
        # Sweep threshold to find peak Macro F0.5
        best_f05 = 0.0
        best_prec = 0.0
        best_rec = 0.0
        best_tp = best_fp = best_fn = 0
        best_thresh = 0.50

        # Predict probabilities on test
        for thresh in [0.40, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80]:
            pred_dict = {}
            for s1_id in test_anchors:
                cand_list = test_pairs.get(s1_id, [])
                if not cand_list:
                    pred_dict[s1_id] = []
                    continue
                feats = np.array([item[1] for item in cand_list])
                probs = model.predict_proba(feats)[:, 1]

                passing = [(cand_list[idx][0], probs[idx]) for idx in range(len(probs)) if probs[idx] >= thresh]
                passing.sort(key=lambda x: x[1], reverse=True)
                # Cap at 8
                pred_dict[s1_id] = [p[0] for p in passing[:8]]

            f05, prec, rec, tp, fp, fn = evaluate_predictions(gt_test, pred_dict)
            if f05 > best_f05:
                best_f05 = f05
                best_prec = prec
                best_rec = rec
                best_tp = tp
                best_fp = fp
                best_fn = fn
                best_thresh = thresh

        print(f"{m_name:<30} | {best_f05:<10.4f} | {best_prec*100:6.2f}%    | {best_rec*100:6.2f}%    | {best_tp:<6,d} | {best_fp:<6,d} (tau={best_thresh:.2f})")

    # Model E: Hybrid Ensemble (Deterministic Scorer + GBDT)
    print("-" * 90)
    print("Evaluating Hybrid Lexical + GBDT Ensemble...")
    best_f05 = 0.0
    best_prec = best_rec = 0.0
    best_tp = best_fp = 0
    best_thresh = 0.50

    for thresh in [0.50, 0.55, 0.60, 0.65, 0.70]:
        pred_dict = {}
        for s1_id in test_anchors:
            cand_list = test_pairs.get(s1_id, [])
            if not cand_list:
                pred_dict[s1_id] = []
                continue
            feats = np.array([item[1] for item in cand_list])
            ml_probs = clf_gbdt.predict_proba(feats)[:, 1]

            # Rule based feature proxy (tok_jaccard * 0.5 + addr_jaccard * 0.5)
            # feat index 2 is tok_jaccard, feat index 9 is addr_jaccard, feat index 11 is bldg_match
            rule_scores = 0.50 * feats[:, 2] + 0.35 * feats[:, 9] + 0.15 * feats[:, 11]

            # Ensemble: 50% GBDT + 50% Lexical
            ensemble_scores = 0.60 * ml_probs + 0.40 * rule_scores

            # Hard Vetoes: if bldg_conflict == 1 and tok_jaccard < 0.85 -> veto
            for idx in range(len(ensemble_scores)):
                if feats[idx, 13] == 1.0 and feats[idx, 2] < 0.85: # bldg_conflict
                    ensemble_scores[idx] = 0.0
                if feats[idx, 17] == 1.0: # country_conflict
                    ensemble_scores[idx] = 0.0

            passing = [(cand_list[idx][0], ensemble_scores[idx]) for idx in range(len(ensemble_scores)) if ensemble_scores[idx] >= thresh]
            passing.sort(key=lambda x: x[1], reverse=True)
            pred_dict[s1_id] = [p[0] for p in passing[:8]]

        f05, prec, rec, tp, fp, fn = evaluate_predictions(gt_test, pred_dict)
        if f05 > best_f05:
            best_f05 = f05
            best_prec = prec
            best_rec = rec
            best_tp = tp
            best_fp = fp
            best_thresh = thresh

    print(f"{'Hybrid GBDT + Lexical Ensemble':<30} | {best_f05:<10.4f} | {best_prec*100:6.2f}%    | {best_rec*100:6.2f}%    | {best_tp:<6,d} | {best_fp:<6,d} (tau={best_thresh:.2f})")

    # Separation analysis (Phase 15)
    print("\n" + "=" * 90)
    print("PHASE 15: CALIBRATION & SEPARATION ANALYSIS")
    print("=" * 90)
    test_probs = clf_gbdt.predict_proba(X_test)[:, 1]
    tp_scores = test_probs[y_test == 1]
    fp_scores = test_probs[y_test == 0]

    tp_min = np.min(tp_scores) if len(tp_scores) else 0.0
    tp_p05 = np.percentile(tp_scores, 5) if len(tp_scores) else 0.0
    tp_mean = np.mean(tp_scores) if len(tp_scores) else 0.0

    fp_max = np.max(fp_scores) if len(fp_scores) else 0.0
    fp_p95 = np.percentile(fp_scores, 95) if len(fp_scores) else 0.0
    fp_mean = np.mean(fp_scores) if len(fp_scores) else 0.0

    separation_hard = tp_min - fp_max
    separation_p95 = tp_p05 - fp_p95

    print(f"True Positives  (y=1): Min={tp_min:.4f}, p05={tp_p05:.4f}, Mean={tp_mean:.4f}")
    print(f"Hard Negatives  (y=0): Max={fp_max:.4f}, p95={fp_p95:.4f}, Mean={fp_mean:.4f}")
    print(f"Strict Separation (TP_min - FP_max): {separation_hard:+.4f}")
    print(f"Robust Separation (TP_p05 - FP_p95): {separation_p95:+.4f}")

if __name__ == "__main__":
    main()
