#!/usr/bin/env python3
"""
Test Improved Engine (CHALLENGER_005 Prototype) on 5,000 Validation Anchors.
Compares:
1. Baseline CHALLENGER_004 logic
2. CHALLENGER_005 logic (Indic script transliteration, expanded company suffixes,
   URL cleaning, empty address recovery, typo-resilient bldg number, prioritized blocking).
"""

import os
import sys
import gc
import re
import time
import csv
import unicodedata
from pathlib import Path
from collections import defaultdict
from difflib import SequenceMatcher

proj_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(proj_root / "code" / "business_entity_resolution" / "src"))

from ber.normalization.name_normalizer import NameNormalizer
from ber.normalization.address_normalizer import AddressNormalizer
from ber.normalization.country_handler import CountryHandler
from ber.normalization.transliteration import transliterate_devanagari

DATASET_DIR = proj_root / "student_resource" / "dataset" / "train"
S1_PATH = DATASET_DIR / "train_source1.tsv"
S2_PATH = DATASET_DIR / "train_source2.tsv"
S3_PATH = DATASET_DIR / "train_source3.tsv"
GT_PATH = DATASET_DIR / "train_ground_truth.tsv"

SAMPLE_SIZE = 5000

# Universal Indic Brahmi Block Offset Mapping
def map_indic_to_devanagari(text: str) -> str:
    """
    Maps all major Indic scripts (Bengali, Gurmukhi, Gujarati, Oriya, Tamil, Telugu,
    Kannada, Malayalam) to Devanagari by exploiting the exact 0x80 Unicode Brahmi alignment.
    """
    res = []
    has_indic = False
    for c in text:
        code = ord(c)
        if 0x0980 <= code <= 0x0D7F:
            # Map into Devanagari range 0x0900 - 0x097F
            res.append(chr(0x0900 + (code % 0x80)))
            has_indic = True
        else:
            res.append(c)
    return "".join(res) if has_indic else text

# Expanded Company / Legal Suffixes
EXPANDED_LEGAL_SUFFIXES = {
    "private limited": "pvt ltd", "pvt limited": "pvt ltd", "pvt ltd": "pvt ltd",
    "pvtltd": "pvt ltd", "p limited": "pvt ltd", "limited": "ltd", "ltd": "ltd",
    "incorporated": "inc", "inc": "inc", "corporation": "corp", "corp": "corp",
    "limited liability company": "llc", "llc": "llc", "l l c": "llc", "llp": "llp",
    "company": "co", "co": "co", "sarl": "sarl", "sa": "sa", "gmbh": "gmbh",
    "enterprise": "enterprises", "enterprises": "enterprises",
    "associates": "associates", "industries": "industries",
    "solutions": "solutions", "services": "services", "technologies": "technologies",
    "partners": "partners", "center": "center", "centre": "center",
    "foundation": "foundation", "group": "group", "holdings": "holdings",
    "commercial": "commercial", "trading": "trading", "marketing": "marketing"
}

SUFFIX_PATTERNS = sorted(EXPANDED_LEGAL_SUFFIXES.keys(), key=len, reverse=True)
LEGAL_SUFFIX_REGEX = re.compile(
    r"\b(" + "|".join(re.escape(k) for k in SUFFIX_PATTERNS) + r")\b",
    re.IGNORECASE
)

URL_PROTOCOL_REGEX = re.compile(r"https?://(?:www\.)?|www\.", re.IGNORECASE)
TLD_SUFFIX_REGEX = re.compile(r"\.(?:com|org|net|in|fr|co|io|biz|info|gov|edu)(?:/[^\s]*)?\b", re.IGNORECASE)
TRAILING_TLD_REGEX = re.compile(r"(?:com|org|net|gov|edu)$", re.IGNORECASE)
HONORIFIC_PREFIX_REGEX = re.compile(r"^(?:m\s*/?\s*s\.?|shri|sri|smt|dr\.?|er\.?|late)\s+", re.IGNORECASE)
PHONE_REGEX = re.compile(r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b|\b\d{10}\b")
NON_ALPHANUM_REGEX = re.compile(r"[^a-z0-9\s]")
WHITESPACE_REGEX = re.compile(r"\s+")

def clean_and_normalize_name_enhanced(raw_name: str):
    if not raw_name:
        return "", (), ""
    text = str(raw_name).strip()
    
    # 1. Map Indic scripts to Devanagari and transliterate
    text = map_indic_to_devanagari(text)
    text, _ = transliterate_devanagari(text)
    
    # 2. Accent stripping
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text_lower = text.lower()
    
    # 3. URL and domain unmasking
    if URL_PROTOCOL_REGEX.search(text_lower) or TLD_SUFFIX_REGEX.search(text_lower):
        text_lower = URL_PROTOCOL_REGEX.sub(" ", text_lower)
        text_lower = TLD_SUFFIX_REGEX.sub(" ", text_lower)
        text_lower = text_lower.replace(".", " ").replace("-", " ").replace("/", " ").replace("_", " ")
    text_lower = PHONE_REGEX.sub(" ", text_lower)
    
    # 4. Clean punctuation to whitespace
    clean_text = NON_ALPHANUM_REGEX.sub(" ", text_lower)
    clean_text = WHITESPACE_REGEX.sub(" ", clean_text).strip()
    
    # 5. Honorific prefix
    if HONORIFIC_PREFIX_REGEX.search(clean_text):
        clean_text = HONORIFIC_PREFIX_REGEX.sub("", clean_text).strip()
        
    # 6. Suffix stripping
    sub_canonical = LEGAL_SUFFIX_REGEX.sub(" ", clean_text)
    sub_canonical = WHITESPACE_REGEX.sub(" ", sub_canonical).strip()
    canonical_text = sub_canonical if sub_canonical else clean_text
    
    # 7. Trailing TLD in single token (e.g. "kinnisonbutlerroycecom" -> "kinnisonbutlerroyce")
    words = canonical_text.split()
    if len(words) == 1 and len(words[0]) >= 8 and TRAILING_TLD_REGEX.search(words[0]):
        trimmed = TRAILING_TLD_REGEX.sub("", words[0])
        if len(trimmed) >= 4:
            canonical_text = trimmed
            words = [trimmed]

    tokens = tuple(w for w in words if w)
    concat_str = "".join(tokens)
    return canonical_text, tokens, concat_str

def extract_blocking_keys_enhanced(name: str, address: str, country: str, an_normalizer):
    canon, tokens, concat_str = clean_and_normalize_name_enhanced(name)
    norm_addr = an_normalizer.normalize(address) if address else None
    keys = []
    
    # PRIORITIZE NAME-GROUNDED KEYS FIRST
    if canon:
        keys.append(f"NC:{canon}")
        if len(concat_str) >= 6:
            keys.append(f"NCONCAT:{concat_str[:20]}")
            
    if canon and len(tokens) >= 2:
        clean_toks = [t for t in tokens if len(t) >= 2]
        if len(clean_toks) >= 2:
            keys.append(f"NS:{'_'.join(sorted(clean_toks[:4]))}")
            keys.append(f"NP:{clean_toks[0]}_{clean_toks[1]}")
        elif len(clean_toks) == 1 and len(clean_toks[0]) >= 3:
            keys.append(f"N1:{clean_toks[0]}")
    elif canon and len(tokens) == 1 and len(tokens[0]) >= 3:
        keys.append(f"N1:{tokens[0]}")
        
    if norm_addr and norm_addr.numeric_tokens and tokens:
        p_num = norm_addr.numeric_tokens[0]
        n_first = tokens[0]
        if len(n_first) >= 3:
            keys.append(f"ADDR_N1:{p_num}_{n_first[:4]}")
            
    if norm_addr and norm_addr.postal_code and tokens:
        n_first = tokens[0]
        if len(n_first) >= 3:
            keys.append(f"PIN_N1:{norm_addr.postal_code}_{n_first[:4]}")
            
    if tokens and len(tokens[0]) >= 5:
        keys.append(f"N1L:{tokens[0]}")
        
    # PURE ADDRESS KEYS AT THE END (fallback only)
    if norm_addr and norm_addr.numeric_tokens and norm_addr.tokens:
        p_num = norm_addr.numeric_tokens[0]
        for w in norm_addr.tokens[:2]:
            if len(w) >= 4:
                keys.append(f"ADDR_NW:{p_num}_{w}")
                
    if norm_addr and len(norm_addr.tokens) >= 2:
        keys.append(f"ADDR_WW:{norm_addr.tokens[0]}_{norm_addr.tokens[1]}")
        
    return keys

def _char_similarity(s1: str, s2: str) -> float:
    if s1 == s2: return 1.0
    if not s1 or not s2: return 0.0
    return SequenceMatcher(None, s1, s2).ratio()

def score_pair_enhanced(
    a_canon, a_toks, a_concat, a_addr_toks, a_num_toks, a_country,
    t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat
) -> float:
    # 1. Country contradiction check
    if a_country != "UNKNOWN" and t_country != "UNKNOWN" and a_country != t_country:
        return 0.0

    # 2. Name similarity
    name_sim = 0.0
    if a_canon and t_canon and a_canon == t_canon:
        name_sim = 1.0
    elif a_toks and t_canon:
        t_toks = set(t for t in t_canon.split() if len(t) >= 2)
        if t_toks:
            overlap = len(a_toks.intersection(t_toks))
            union_len = len(a_toks.union(t_toks))
            jaccard = overlap / union_len if union_len > 0 else 0.0
            name_sim = jaccard
            
            # Subset match
            if jaccard < 0.85:
                shorter, longer = (a_toks, t_toks) if len(a_toks) <= len(t_toks) else (t_toks, a_toks)
                if len(shorter) >= 2 and shorter.issubset(longer):
                    containment = len(shorter) / len(longer) if longer else 0.0
                    name_sim = max(name_sim, 0.70 + 0.20 * containment)

    # Domain unmasking / concat match
    if name_sim < 0.85 and a_canon and t_canon:
        if a_concat and (a_concat == t_canon.replace(" ", "") or t_name_concat == a_canon.replace(" ", "") or a_concat == t_name_concat):
            name_sim = max(name_sim, 0.95)
        elif a_concat and t_name_concat and len(a_concat) >= 6 and len(t_name_concat) >= 6:
            if a_concat.startswith(t_name_concat) or t_name_concat.startswith(a_concat):
                ratio = min(len(a_concat), len(t_name_concat)) / max(len(a_concat), len(t_name_concat))
                if ratio >= 0.70:
                    name_sim = max(name_sim, 0.88 * ratio)
            elif len(a_canon) >= 8 and len(t_canon) >= 8 and (a_canon in t_canon or t_canon in a_canon):
                name_sim = max(name_sim, 0.90)

    # Fuzzy similarity
    t_num_set = set(t_num_toks)
    num_match = bool(a_num_toks.intersection(t_num_set)) if a_num_toks and t_num_set else False
    if name_sim < 0.80 and a_canon and t_canon:
        t_toks = set(t for t in t_canon.split() if len(t) >= 2)
        has_token_overlap = bool(a_toks.intersection(t_toks)) if a_toks and t_toks else False
        if has_token_overlap or num_match:
            if a_concat and t_name_concat and len(a_concat) >= 6 and len(t_name_concat) >= 6:
                ratio = _char_similarity(a_concat, t_name_concat)
                if ratio >= 0.78:
                    name_sim = max(name_sim, ratio * 0.90)

    # 3. Numeric Building Check with OCR tolerance & Name Guard
    has_bldg_conflict = False
    if a_num_toks and t_num_set:
        intersect = a_num_toks.intersection(t_num_set)
        if intersect:
            num_match = True
            if len(a_num_toks) >= 2 and len(t_num_set) >= 2:
                a_l = sorted(a_num_toks); t_l = sorted(t_num_set)
                if (a_l[0] != t_l[0] and a_l[0] not in t_num_set and t_l[0] not in a_num_toks) or \
                   (a_l[-1] != t_l[-1] and a_l[-1] not in t_num_set and t_l[-1] not in a_num_toks):
                    # DO NOT VETO if name is practically identical!
                    if name_sim < 0.88:
                        has_bldg_conflict = True
        else:
            # Check OCR truncation (e.g. 3784 vs 784, 9327 vs 932)
            ocr_ok = False
            for an_val in a_num_toks:
                for tn_val in t_num_set:
                    if len(an_val) >= 2 and len(tn_val) >= 2:
                        if (an_val.startswith(tn_val) or tn_val.startswith(an_val) or 
                            an_val.endswith(tn_val) or tn_val.endswith(an_val)) and abs(len(an_val) - len(tn_val)) <= 1:
                            ocr_ok = True
                            break
                if ocr_ok: break
            if ocr_ok:
                num_match = True
            else:
                # If name is identical (>= 0.92), do not veto!
                if name_sim < 0.92:
                    has_bldg_conflict = True

    if has_bldg_conflict:
        return 0.0

    # 4. Address similarity
    addr_sim = 0.0
    t_atok_set = set(t for t in t_addr_toks if len(t) >= 2)
    if a_addr_toks and t_atok_set:
        overlap = len(a_addr_toks.intersection(t_atok_set))
        union_len = len(a_addr_toks.union(t_atok_set))
        addr_sim = overlap / union_len if union_len > 0 else 0.0

    # Precision guard: multi-tenant center veto
    if name_sim < 0.45:
        return 0.0

    # 5. Composite Scoring
    score = 0.0
    if name_sim >= 0.85:
        if addr_sim >= 0.20:
            score = 0.60 * name_sim + 0.40 * addr_sim
        elif not t_atok_set:
            # Target has EMPTY address:
            # If name is exact match (>= 0.95), allow match with score 0.72!
            if name_sim >= 0.95 and (len(a_toks) >= 2 or len(a_canon) >= 6):
                score = 0.75 * name_sim
            else:
                score = 0.60 * name_sim
        else:
            # Target has address but low Jaccard (e.g. different length or city match)
            if a_addr_toks.intersection(t_atok_set) or num_match:
                score = 0.62 * name_sim + 0.38 * addr_sim
            else:
                score = 0.45 * name_sim
    elif name_sim >= 0.65:
        if addr_sim >= 0.30:
            score = 0.50 * name_sim + 0.50 * addr_sim
        elif not t_atok_set:
            score = 0.50 * name_sim
        else:
            score = 0.40 * name_sim
    elif name_sim >= 0.50 and addr_sim >= 0.40:
        score = 0.45 * name_sim + 0.55 * addr_sim

    return score


def main():
    print("==================================================================", flush=True)
    print("   CHALLENGER_005 BENCHMARK & COMPARISON (5,000 ANCHORS)         ", flush=True)
    print("==================================================================", flush=True)
    t0 = time.time()
    an_norm = AddressNormalizer()
    ch_handler = CountryHandler()
    
    # 1. Load ground truth
    print("[1/5] Loading 5,000 validation anchors...", flush=True)
    gt = {}
    with open(GT_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)
        count = 0
        for row in reader:
            if count >= SAMPLE_SIZE:
                break
            s1_id = row[0].strip()
            matched_str = row[1].strip() if len(row) > 1 else ""
            gt[s1_id] = set(matched_str.split(",")) if matched_str else set()
            count += 1
            
    total_true_pairs = sum(len(v) for v in gt.values())
    all_needed_targets = set(t for tgts in gt.values() for t in tgts)
    print(f"  Loaded {len(gt):,} anchors ({total_true_pairs:,} true links, {len(all_needed_targets):,} unique targets).", flush=True)

    # 2. Load S1 records
    print("[2/5] Loading S1 records and extracting keys...", flush=True)
    s1_records = {}
    with open(S1_PATH, "r", encoding="utf-8") as f:
        f.readline()
        for line in f:
            parts = line.rstrip("\r\n").split("\t")
            if parts[0].strip() in gt:
                s1_records[parts[0].strip()] = (parts[1], parts[2] if len(parts) > 2 else "", parts[3] if len(parts) > 3 else "")

    val_keys = set()
    s1_precomputed = {}
    for s1_id, (name, address, country) in s1_records.items():
        keys = extract_blocking_keys_enhanced(name, address, country, an_norm)
        val_keys.update(keys)
        canon, toks, concat_str = clean_and_normalize_name_enhanced(name)
        norm_addr = an_norm.normalize(address) if address else None
        s1_precomputed[s1_id] = {
            "name": name, "address": address, "country": country,
            "keys": keys, "canon": canon,
            "toks": set(t for t in toks if len(t) >= 2),
            "concat": concat_str,
            "addr_toks": set(t for t in norm_addr.tokens if len(t) >= 2) if norm_addr else set(),
            "num_toks": set(norm_addr.numeric_tokens) if norm_addr else set(),
            "ctry": ch_handler.normalize(country).canonical or "UNKNOWN"
        }
    print(f"  Extracted {len(val_keys):,} validation blocking keys.", flush=True)

    # 3. Stream S2 & S3 into partition index
    def process_target_source(path: Path, label: str):
        print(f"\n[3/5] Processing {label} ({path.name})...", flush=True)
        t_start = time.time()
        index = defaultdict(list)
        target_recs = {}
        
        with open(path, "r", encoding="utf-8") as f:
            f.readline()
            for line in f:
                parts = line.rstrip("\r\n").split("\t")
                if len(parts) < 4: continue
                eid = parts[0].strip()
                name = parts[1]
                addr = parts[2] if len(parts) > 2 else ""
                ctry = parts[3] if len(parts) > 3 else ""
                
                is_needed = eid in all_needed_targets
                keys = extract_blocking_keys_enhanced(name, addr, ctry, an_norm)
                matched_val_keys = [k for k in keys if k in val_keys and len(index[k]) < 300]
                
                if matched_val_keys or is_needed:
                    canon, toks, concat_str = clean_and_normalize_name_enhanced(name)
                    norm_addr = an_norm.normalize(addr) if addr else None
                    target_recs[eid] = (
                        canon,
                        norm_addr.tokens if norm_addr else (),
                        norm_addr.numeric_tokens if norm_addr else (),
                        ch_handler.normalize(ctry).canonical or "UNKNOWN",
                        norm_addr.postal_code if norm_addr else "",
                        concat_str
                    )
                    for k in matched_val_keys:
                        plist = index[k]
                        if len(plist) < 300:
                            plist.append(eid)

        print(f"  {label} indexed: {len(target_recs):,} relevant records in {time.time()-t_start:.1f}s", flush=True)
        
        # Score anchors against this partition
        t_score = time.time()
        scores = defaultdict(list)
        for s1_id, p in s1_precomputed.items():
            seen = set()
            cands = []
            for k in p["keys"]:
                plist = index.get(k)
                if plist:
                    for tid in plist:
                        if tid not in seen and tid != s1_id:
                            seen.add(tid)
                            cands.append(tid)
                            if len(cands) >= 75: break
                if len(cands) >= 75: break
                
            for cid in cands:
                rec = target_recs.get(cid)
                if not rec: continue
                t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat = rec
                s = score_pair_enhanced(
                    p["canon"], p["toks"], p["concat"], p["addr_toks"], p["num_toks"], p["ctry"],
                    t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat
                )
                if s > 0.0:
                    scores[s1_id].append((cid, s))
                    
        print(f"  {label} scored in {time.time()-t_score:.1f}s", flush=True)
        return scores

    s2_scores = process_target_source(S2_PATH, "Source 2")
    s3_scores = process_target_source(S3_PATH, "Source 3")

    # 4. Merge scores and evaluate
    print("\n[4/5] Merging scores and evaluating metrics across thresholds...", flush=True)
    combined_scores = defaultdict(list)
    cand_hits = 0
    for s1_id in gt:
        c_list = s2_scores.get(s1_id, []) + s3_scores.get(s1_id, [])
        combined_scores[s1_id] = c_list
        c_set = set(c[0] for c in c_list)
        cand_hits += len(c_set.intersection(gt[s1_id]))

    cand_rec = cand_hits / max(total_true_pairs, 1)
    print(f"  CANDIDATE RECALL (score > 0.0): {cand_rec:.4f} ({cand_hits}/{total_true_pairs}) [CH4 was 0.6440]")

    thresholds = [0.50, 0.52, 0.55, 0.58, 0.60, 0.62, 0.65, 0.68, 0.70]
    print("\n" + "=" * 90)
    print(f"{'Tau':<6} | {'TP':<6} | {'FP':<6} | {'FN':<6} | {'Precision':<10} | {'Recall':<10} | {'F1':<10} | {'F0.5':<10} | {'Gain vs CH4':<12}")
    print("-" * 90)

    best_tau = None
    best_f05 = -1.0
    best_metrics = {}

    for tau in thresholds:
        tp = fp = fn = 0
        for s1_id, true_matches in gt.items():
            cands = combined_scores.get(s1_id, [])
            matched_list = [c for c in cands if c[1] >= tau]
            if len(matched_list) > 8:
                matched_list.sort(key=lambda x: x[1], reverse=True)
                matched_list = matched_list[:8]
            matched = set(c[0] for c in matched_list)

            tp += len(matched.intersection(true_matches))
            fp += len(matched - true_matches)
            fn += len(true_matches - matched)

        prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0
        f05 = 1.25 * prec * rec / (0.25 * prec + rec) if (0.25 * prec + rec) > 0 else 0.0
        gain = f05 - 0.8513  # Gain vs CHALLENGER_004

        if f05 > best_f05:
            best_f05 = f05
            best_tau = tau
            best_metrics = {"tp": tp, "fp": fp, "fn": fn, "prec": prec, "rec": rec, "f1": f1, "f05": f05}

        print(f"{tau:<6.2f} | {tp:<6} | {fp:<6} | {fn:<6} | {prec:<10.4f} | {rec:<10.4f} | {f1:<10.4f} | {f05:<10.4f} | {'+' if gain>=0 else ''}{gain:<12.4f}")

    print("=" * 90)
    print(f"CHALLENGER_005 BEST RESULT: tau = {best_tau}")
    print(f"  Precision: {best_metrics['prec']:.4f}")
    print(f"  Recall:    {best_metrics['rec']:.4f}")
    print(f"  F0.5:      {best_metrics['f05']:.4f}")
    print(f"  TP: {best_metrics['tp']:,}  FP: {best_metrics['fp']:,}  FN: {best_metrics['fn']:,}")
    improvement = best_f05 - 0.8513
    print(f"  NET GAIN VS CHALLENGER_004: {'+' if improvement>=0 else ''}{improvement:.4f} F0.5")
    print(f"Total benchmark elapsed time: {time.time()-t0:.1f}s")

if __name__ == "__main__":
    main()
