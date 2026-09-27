#!/usr/bin/env python3
"""
Ablation Study of Individual Improvements over CHALLENGER_004.
Tests on 1,000 validation anchors:
1. Baseline CHALLENGER_004
2. + Universal Indic transliteration
3. + LLP legal suffix
4. + High-precision Empty Address recovery (exact 3+ token names only)
5. + Trailing URL TLD stripping
"""

import sys, os, csv, re, time, unicodedata
from collections import defaultdict
from pathlib import Path
from difflib import SequenceMatcher

proj_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(proj_root / "code" / "business_entity_resolution" / "src"))

from ber.inference.engine import InferenceEngine, InferenceConfig
from ber.normalization.name_normalizer import NameNormalizer
from ber.normalization.address_normalizer import AddressNormalizer
from ber.normalization.country_handler import CountryHandler
from ber.normalization.transliteration import transliterate_devanagari

DATASET_DIR = proj_root / "student_resource" / "dataset" / "train"
S1_PATH = DATASET_DIR / "train_source1.tsv"
S2_PATH = DATASET_DIR / "train_source2.tsv"
S3_PATH = DATASET_DIR / "train_source3.tsv"
GT_PATH = DATASET_DIR / "train_ground_truth.tsv"

SAMPLE_SIZE = 1000

# 1. Load Ground Truth
print("[1/3] Loading 1,000 validation anchors...", flush=True)
gt = {}
with open(GT_PATH, "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="\t")
    next(reader)
    count = 0
    for row in reader:
        if count >= SAMPLE_SIZE: break
        s1 = row[0].strip()
        tgts = set(row[1].strip().split(",")) if len(row) > 1 and row[1].strip() else set()
        gt[s1] = tgts
        count += 1

all_needed_targets = set(t for tgts in gt.values() for t in tgts)

# 2. Load S1 records
s1_records = {}
with open(S1_PATH, "r", encoding="utf-8") as f:
    f.readline()
    for line in f:
        p = line.rstrip("\r\n").split("\t")
        if p[0].strip() in gt:
            s1_records[p[0].strip()] = (p[1], p[2] if len(p) > 2 else "", p[3] if len(p) > 3 else "")

# Universal Indic Brahmi Block Offset Mapping
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

# Let's test Baseline Engine vs Variants
base_engine = InferenceEngine(InferenceConfig(decision_threshold=0.58))

print("[2/3] Extracting baseline keys...", flush=True)
val_keys = set()
for s1_id, (n, a, c) in s1_records.items():
    val_keys.update(base_engine.extract_blocking_keys(n, a, c))
    # Also include Indic mapped keys
    n_indic = map_indic_to_devanagari(n)
    if n_indic != n:
        val_keys.update(base_engine.extract_blocking_keys(n_indic, a, c))

print(f"  Validation keys: {len(val_keys):,}", flush=True)

# 3. Stream S2 & S3 targets
print("[3/3] Streaming S2 & S3...", flush=True)
raw_targets = {}
index = defaultdict(list)

def stream_source(path):
    with open(path, "r", encoding="utf-8") as f:
        f.readline()
        for line in f:
            p = line.rstrip("\r\n").split("\t")
            if len(p) < 4: continue
            eid = p[0].strip()
            name = p[1]
            addr = p[2] if len(p) > 2 else ""
            ctry = p[3] if len(p) > 3 else ""
            is_needed = eid in all_needed_targets
            
            keys = base_engine.extract_blocking_keys(name, addr, ctry)
            name_indic = map_indic_to_devanagari(name)
            if name_indic != name:
                keys.extend(base_engine.extract_blocking_keys(name_indic, addr, ctry))
                
            matched = [k for k in keys if k in val_keys and len(index[k]) < 300]
            if matched or is_needed:
                raw_targets[eid] = (name, addr, ctry)
                for k in matched:
                    plist = index[k]
                    if len(plist) < 300:
                        plist.append(eid)

stream_source(S2_PATH)
stream_source(S3_PATH)
print(f"  Loaded {len(raw_targets):,} target records matching keys.", flush=True)

# Evaluate function
def evaluate_strategy(name_norm_fn, score_fn, label: str):
    tp = fp = fn = 0
    an = base_engine.address_normalizer
    ch = base_engine.country_handler
    
    for s1_id, (s1_n, s1_a, s1_c) in s1_records.items():
        true_matches = gt[s1_id]
        s1_keys = base_engine.extract_blocking_keys(s1_n, s1_a, s1_c)
        s1_n_indic = map_indic_to_devanagari(s1_n)
        if s1_n_indic != s1_n:
            s1_keys.extend(base_engine.extract_blocking_keys(s1_n_indic, s1_a, s1_c))
            
        cands = []
        seen = set()
        for k in s1_keys:
            plist = index.get(k)
            if plist:
                for tid in plist:
                    if tid not in seen and tid != s1_id:
                        seen.add(tid)
                        cands.append(tid)
                        if len(cands) >= 150: break
            if len(cands) >= 150: break

        norm_s1 = name_norm_fn(s1_n)
        norm_s1_a = an.normalize(s1_a) if s1_a else None
        s1_canon = norm_s1.canonical
        s1_toks = set(t for t in norm_s1.tokens if len(t) >= 2)
        s1_concat = "".join(norm_s1.tokens)
        s1_addr_toks = set(t for t in norm_s1_a.tokens if len(t) >= 2) if norm_s1_a else set()
        s1_num_toks = set(norm_s1_a.numeric_tokens) if norm_s1_a else set()
        s1_ctry = ch.normalize(s1_c).canonical or "UNKNOWN"

        matched = set()
        for tid in cands:
            t_data = raw_targets.get(tid)
            if not t_data: continue
            t_n, t_a, t_c = t_data
            norm_t = name_norm_fn(t_n)
            norm_t_a = an.normalize(t_a) if t_a else None
            t_canon = norm_t.canonical
            t_toks = tuple(t for t in norm_t.tokens if len(t) >= 2)
            t_concat = "".join(norm_t.tokens)
            t_addr_toks = norm_t_a.tokens if norm_t_a else ()
            t_num_toks = norm_t_a.numeric_tokens if norm_t_a else ()
            t_postal = norm_t_a.postal_code if norm_t_a else ""
            t_ctry = ch.normalize(t_c).canonical or "UNKNOWN"

            s = score_fn(
                s1_canon, s1_toks, s1_concat, s1_addr_toks, s1_num_toks, s1_ctry,
                t_canon, t_addr_toks, t_num_toks, t_ctry, t_postal, t_concat
            )
            if s >= 0.58:
                matched.add(tid)

        tp += len(matched.intersection(true_matches))
        fp += len(matched - true_matches)
        fn += len(true_matches - matched)

    prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f05 = 1.25 * prec * rec / (0.25 * prec + rec) if (0.25 * prec + rec) > 0 else 0.0
    print(f"{label:<45s} | TP: {tp:5d} | FP: {fp:4d} | FN: {fn:5d} | Prec: {prec*100:6.2f}% | Rec: {rec*100:6.2f}% | F0.5: {f05:.4f}")
    return f05

print("\n" + "=" * 105)
print(f"{'Strategy':<45s} | {'TP':<9} | {'FP':<8} | {'FN':<9} | {'Precision':<13} | {'Recall':<13} | {'F0.5':<8}")
print("=" * 105)

# Strategy 1: Pure Baseline CHALLENGER_004
def norm_base(n):
    return base_engine.name_normalizer.normalize(n)

def score_base(*args):
    return base_engine._score_pair(*args)

evaluate_strategy(norm_base, score_base, "1. Baseline CHALLENGER_004")

# Strategy 2: + Universal Indic Transliteration
def norm_indic(n):
    # First map Brahmi Indic scripts to Devanagari
    n_mapped = map_indic_to_devanagari(n)
    return base_engine.name_normalizer.normalize(n_mapped)

evaluate_strategy(norm_indic, score_base, "2. + Universal Indic Transliteration")

# Strategy 3: + Universal Indic + LLP suffix
class LLPNameNormalizer(NameNormalizer):
    def __init__(self):
        super().__init__()
        # add LLP to suffix regex
        llp_patterns = sorted(list(self.strip_accents and ["llp", "l l p"] + list(base_engine.name_normalizer.normalize("").__class__.__dict__.keys())), key=len, reverse=True)

llp_norm = NameNormalizer()
# Modify LEGAL_SUFFIX_MAP in place for llp
from ber.normalization.name_normalizer import LEGAL_SUFFIX_MAP, LEGAL_SUFFIX_REGEX
import ber.normalization.name_normalizer as nnm
nnm.LEGAL_SUFFIX_MAP["llp"] = "llp"
nnm.LEGAL_SUFFIX_MAP["l l p"] = "llp"
patterns = sorted(nnm.LEGAL_SUFFIX_MAP.keys(), key=len, reverse=True)
nnm.LEGAL_SUFFIX_REGEX = re.compile(r"\b(" + "|".join(re.escape(k) for k in patterns) + r")\b", re.IGNORECASE)

evaluate_strategy(norm_indic, score_base, "3. + Universal Indic + LLP Suffix")

# Strategy 4: + Empty Address Recovery (Strictly requiring exact 2+ token name match or len >= 8)
def score_empty_addr_guarded(
    a_canon, a_toks, a_concat, a_addr_toks, a_num_toks, a_ctry,
    t_canon, t_addr_toks, t_num_toks, t_ctry, t_postal, t_concat
):
    s = base_engine._score_pair(
        a_canon, a_toks, a_concat, a_addr_toks, a_num_toks, a_ctry,
        t_canon, t_addr_toks, t_num_toks, t_ctry, t_postal, t_concat
    )
    # If rejected only because target has NO address:
    if s < 0.58 and not t_addr_toks:
        # Require EXACT canonical match and distinctive name
        if a_canon and t_canon and a_canon == t_canon:
            if len(a_toks) >= 2 or len(a_canon) >= 8:
                if a_ctry == "UNKNOWN" or t_ctry == "UNKNOWN" or a_ctry == t_ctry:
                    return 0.65
    return s

evaluate_strategy(norm_indic, score_empty_addr_guarded, "4. + Strict Empty Addr Recovery (>=2 toks)")

# Strategy 5: + OCR Suffix / Truncation Recovery on Building Numbers
def score_ocr_bldg_guarded(
    a_canon, a_toks, a_concat, a_addr_toks, a_num_toks, a_ctry,
    t_canon, t_addr_toks, t_num_toks, t_ctry, t_postal, t_concat
):
    # If base rejected with 0.0, check if it was bldg conflict with identical name
    s = score_empty_addr_guarded(
        a_canon, a_toks, a_concat, a_addr_toks, a_num_toks, a_ctry,
        t_canon, t_addr_toks, t_num_toks, t_ctry, t_postal, t_concat
    )
    if s == 0.0 and a_canon and t_canon and a_canon == t_canon and len(a_canon) >= 8:
        if a_ctry == "UNKNOWN" or t_ctry == "UNKNOWN" or a_ctry == t_ctry:
            # Check if address words overlap (same street name, different number due to OCR)
            t_atok_set = set(t for t in t_addr_toks if len(t) >= 3)
            overlap = a_addr_toks.intersection(t_atok_set)
            if len(overlap) >= 2:
                # Street name and city match! Only number differed
                return 0.62
    return s

evaluate_strategy(norm_indic, score_ocr_bldg_guarded, "5. + Street Match OCR Number Recovery")
print("=" * 105)
