#!/usr/bin/env python3
"""
Targeted Enhancements Benchmark
Tests 6 root-cause derived improvements:
1. Building Conflict Logic Fix: If intersect is non-empty, do NOT veto on extra numbers.
2. Hindi Transliteration Suffix Expansion:
   praivet, piraivet, praibhet, praiv -> pvt
   elelpee -> llp
   limit, limi -> ltd
3. Noise Token Stripping:
   Leading 'the'
   DBA / AKA / Formerly prefixes in S3
4. Hindi & Tamil Loanword Expansion:
   phood -> food
   investments in Tamil pulli
5. Relaxed name floor for high address match:
   If addr_sim >= 0.50 and num_match, name_floor = 0.25 (instead of 0.45)
6. French house number & thoroughfare normalization
"""

import sys
import gc
import re
import csv
import json
import time
from pathlib import Path
from collections import Counter, defaultdict
from difflib import SequenceMatcher

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

SAMPLE_SIZE = 5000

# 1. Expand Hindi transliterated suffixes in LEGAL_SUFFIX_MAP
EXTENDED_SUFFIXES = {
    "private": "pvt", "pvt": "pvt", "llp": "llp", "l l p": "llp",
    "public limited": "ltd", "plc": "ltd", "p l c": "ltd",
    "proprietorship": "prop", "prop": "prop",
    "praivet": "pvt", "piraivet": "pvt", "praibhet": "pvt", "praiv": "pvt",
    "elelpee": "llp", "limit": "ltd", "limi": "ltd",
    "sarl": "sarl", "sas": "sarl", "sasu": "sarl", "eurl": "sarl",
    "sci": "sci", "snc": "snc", "ets": "ets", "fils": "fils", "cie": "co", "ste": "co"
}

# 2. Hindi Loanwords
trm.HINDI_BUSINESS_TERMS.update({
    "इंटरनेशनल": "international", "इन्टरनेशनल": "international",
    "लॉजिस्टिक्स": "logistics", "लॉजिस्टिक": "logistics",
    "टेक्नोलॉजी": "technology", "टेक्नोलॉजीज": "technologies",
    "इंजीनियरिंग": "engineering", "कंस्ट्रक्शन": "construction",
    "इंफ्रास्ट्रक्चर": "infrastructure", "इंफ्रा": "infra",
    "ग्लोबल": "global", "सिक्योरिटी": "security",
    "फाइनेंस": "finance", "फाइनेंशियल": "financial",
    "इंडिया": "india", "इंडियन": "indian",
    "डेवलपर्स": "developers", "प्रॉपर्टीज": "properties",
    "केमिकल्स": "chemicals", "इलेक्ट्रिकल्स": "electricals",
    "इलेक्ट्रॉनिक्स": "electronics", "मैनेजमेंट": "management",
    "कंसल्टेंसी": "consultancy", "कंसल्टेंट्स": "consultants",
    "एग्रो": "agro", "फूड्स": "foods", "फूड": "food",
    "पैकर्स": "packers", "मूवर्स": "movers",
    "इन्वेस्टमेंट्स": "investments", "इन्वेस्टमेंट": "investment",
    "ट्रेडर्स": "traders", "ट्रेडिंग": "trading",
    "एंटरप्राइजेज": "enterprises", "एंटरप्राइज": "enterprise",
    "एसोसिएट्स": "associates", "इंडस्ट्रीज": "industries"
})

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

# Strip DBA / AKA / Formerly prefixes
DBA_REGEX = re.compile(r"\b(?:dba|aka|fka|formerly\s+known\s+as|doing\s+business\s+as)\b.*$", re.IGNORECASE)
LEADING_THE_REGEX = re.compile(r"^the\s+", re.IGNORECASE)

def _char_similarity(s1: str, s2: str) -> float:
    if s1 == s2:
        return 1.0
    if not s1 or not s2:
        return 0.0
    return SequenceMatcher(None, s1, s2).ratio()

class EnhancedScorer:
    def __init__(self, fix_bldg_conflict=True, expand_suffixes=True, relax_name_floor=True):
        self.nn = NameNormalizer()
        self.an = AddressNormalizer()
        self.ch = CountryHandler()
        self.fix_bldg_conflict = fix_bldg_conflict
        self.expand_suffixes = expand_suffixes
        self.relax_name_floor = relax_name_floor

    def normalize_name(self, name: str):
        # 1. Strip leading 'The'
        n_clean = LEADING_THE_REGEX.sub("", name.strip())
        # 2. Strip DBA/AKA trailing
        n_clean = DBA_REGEX.sub("", n_clean).strip()
        if not n_clean:
            n_clean = name

        # 3. Transliterate Indic
        n_indic = map_indic_to_devanagari(n_clean)
        norm = self.nn.normalize(n_indic)

        # 4. Standardize suffixes in tokens if expand_suffixes is on
        toks = list(norm.tokens)
        if self.expand_suffixes:
            toks = [EXTENDED_SUFFIXES.get(t, t) for t in toks]
            # Replace common transliteration artifacts
            toks = ["food" if t in ("phood", "phoods") else t for t in toks]
            toks = ["ss" if t == "eses" else t for t in toks]

        canon = " ".join(toks)
        return norm, tuple(toks), canon

    def extract_blocking_keys(self, name: str, address: str = "", country: str = ""):
        norm_name, toks, canon = self.normalize_name(name)
        norm_addr = self.an.normalize(address) if address else None
        keys = []

        if canon:
            keys.append(f"NC:{canon}")
            concat_str = "".join(toks)
            if len(concat_str) >= 6:
                keys.append(f"NCONCAT:{concat_str[:20]}")

        if norm_addr and norm_addr.numeric_tokens and norm_addr.tokens:
            p_num = norm_addr.numeric_tokens[0]
            for w in norm_addr.tokens[:3]:
                if len(w) >= 4:
                    keys.append(f"ADDR_NW:{p_num}_{w}")

        if canon and len(toks) >= 2:
            clean_toks = [t for t in toks if len(t) >= 2]
            if len(clean_toks) >= 2:
                keys.append(f"NS:{'_'.join(sorted(clean_toks[:4]))}")
                keys.append(f"NP:{clean_toks[0]}_{clean_toks[1]}")
            elif len(clean_toks) == 1 and len(clean_toks[0]) >= 3:
                keys.append(f"N1:{clean_toks[0]}")
        elif canon and len(toks) == 1 and len(toks[0]) >= 3:
            keys.append(f"N1:{toks[0]}")

        if norm_addr and len(norm_addr.tokens) >= 2:
            keys.append(f"ADDR_WW:{norm_addr.tokens[0]}_{norm_addr.tokens[1]}")

        if norm_addr and norm_addr.numeric_tokens and toks:
            p_num = norm_addr.numeric_tokens[0]
            n_first = toks[0]
            if len(n_first) >= 3:
                keys.append(f"ADDR_N1:{p_num}_{n_first[:4]}")

        if norm_addr and norm_addr.postal_code and toks:
            n_first = toks[0]
            if len(n_first) >= 3:
                keys.append(f"PIN_N1:{norm_addr.postal_code}_{n_first[:4]}")

        if toks and len(toks[0]) >= 5:
            keys.append(f"N1L:{toks[0]}")

        return keys

    def score_pair(self, a_canon, a_toks, a_concat, a_addr_toks, a_num_toks, a_country,
                   t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat):
        if a_country != "UNKNOWN" and t_country != "UNKNOWN" and a_country != t_country:
            return 0.0

        t_num_set = set(t_num_toks)
        has_bldg_conflict = False
        num_match = False

        if a_num_toks and t_num_set:
            intersect = a_num_toks.intersection(t_num_set)
            if intersect:
                num_match = True
                if not self.fix_bldg_conflict:
                    # Old buggy conflict check
                    if len(a_num_toks) >= 2 and len(t_num_toks) >= 2:
                        a_num_list = sorted(a_num_toks)
                        t_num_list = sorted(t_num_set)
                        if a_num_list[0] != t_num_list[0] and a_num_list[0] not in t_num_set and t_num_list[0] not in a_num_toks:
                            has_bldg_conflict = True
                        elif a_num_list[-1] != t_num_list[-1] and a_num_list[-1] not in t_num_set and t_num_list[-1] not in a_num_toks:
                            has_bldg_conflict = True
                else:
                    # Fixed: if intersect is non-empty, they share at least one building number -> NO conflict!
                    pass
            else:
                ocr_ok = False
                for an in a_num_toks:
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

        # Name similarity
        name_sim = 0.0
        if a_canon and t_canon and a_canon == t_canon:
            name_sim = 1.0
        elif a_toks and t_canon:
            t_tok_set = set(t for t in t_canon.split() if len(t) >= 2)
            if t_tok_set:
                overlap = len(a_toks.intersection(t_tok_set))
                union_len = len(a_toks.union(t_tok_set))
                jaccard = overlap / union_len if union_len > 0 else 0.0
                name_sim = jaccard
                if jaccard < 0.85:
                    shorter, longer = (a_toks, t_tok_set) if len(a_toks) <= len(t_tok_set) else (t_tok_set, a_toks)
                    if len(shorter) >= 2 and shorter.issubset(longer):
                        containment = len(shorter) / len(longer) if longer else 0.0
                        name_sim = max(name_sim, 0.70 + 0.20 * containment)

        if name_sim < 0.85 and a_canon and t_canon:
            if a_concat and (a_concat == t_canon.replace(" ", "") or t_name_concat == a_canon.replace(" ", "") or a_concat == t_name_concat):
                name_sim = max(name_sim, 0.95)
            elif len(a_canon) >= 8 and len(t_canon) >= 8 and (a_canon in t_canon or t_canon in a_canon):
                name_sim = max(name_sim, 0.90)

        if name_sim < 0.80 and a_canon and t_canon:
            t_tok_set = set(t for t in t_canon.split() if len(t) >= 2)
            has_token_overlap = bool(a_toks.intersection(t_tok_set)) if a_toks and t_tok_set else False
            if has_token_overlap or num_match:
                if a_concat and t_name_concat and len(a_concat) >= 6 and len(t_name_concat) >= 6:
                    ratio = _char_similarity(a_concat, t_name_concat)
                    if ratio >= 0.78:
                        name_sim = max(name_sim, ratio * 0.90)

        # Address similarity
        addr_sim = 0.0
        t_atok_set = set(t for t in t_addr_toks if len(t) >= 2)
        if a_addr_toks and t_atok_set:
            overlap = len(a_addr_toks.intersection(t_atok_set))
            union_len = len(a_addr_toks.union(t_atok_set))
            addr_sim = overlap / union_len if union_len > 0 else 0.0

        # Name floor
        effective_name_floor = 0.45
        if self.relax_name_floor:
            if addr_sim >= 0.50 and num_match:
                effective_name_floor = 0.25

        if name_sim < effective_name_floor:
            return 0.0

        # Composite Scoring
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
        elif name_sim >= 0.25 and addr_sim >= 0.60 and num_match:
            score = 0.30 * name_sim + 0.70 * addr_sim

        return score

def main():
    print("=" * 80)
    print("EVALUATING TARGETED ROOT-CAUSE ENHANCEMENTS")
    print("=" * 80)
    t0 = time.time()

    # Load 5k anchors
    gt = {}
    with open(GT_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)
        for i, row in enumerate(reader):
            if i >= SAMPLE_SIZE: break
            s1 = row[0].strip()
            m = [x.strip() for x in row[1].split(",") if x.strip()] if len(row) > 1 and row[1].strip() else []
            gt[s1] = set(m)

    needed_s1 = set(gt.keys())
    needed_targets = set()
    for sid, targets in gt.items():
        needed_targets.update(targets)

    s1_records = {}
    with open(S1_PATH, "r", encoding="utf-8") as f:
        for line in f:
            p = line.rstrip("\r\n").split("\t")
            if len(p) >= 4 and p[0].strip() in needed_s1:
                s1_records[p[0].strip()] = (p[1], p[2], p[3])

    target_records = {}
    def load_t(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                p = line.rstrip("\r\n").split("\t")
                if len(p) >= 4 and p[0].strip() in needed_targets:
                    target_records[p[0].strip()] = (p[1], p[2], p[3])
                    if len(target_records) == len(needed_targets):
                        break

    load_t(S2_PATH)
    load_t(S3_PATH)
    print(f"Loaded {len(s1_records)} S1 and {len(target_records)} target records in {time.time()-t0:.2f}s")

    # Benchmark configurations
    configs = [
        ("CHAMPION_784 Baseline", False, False, False),
        ("+ Fix Building Conflict Bug", True, False, False),
        ("+ Hindi Suffixes (praivet/elelpee/limit)", True, True, False),
        ("+ Full (Bldg Fix + Suffixes + Relaxed Name Floor)", True, True, True),
    ]

    print("\n" + "=" * 80)
    print(f"{'Configuration':<45} | {'TP':<6} | {'True Rec%':<10} | {'Gain vs Base'}")
    print("-" * 80)

    base_tp = 0
    for name, bldg_fix, suf_exp, name_fl in configs:
        scorer = EnhancedScorer(fix_bldg_conflict=bldg_fix, expand_suffixes=suf_exp, relax_name_floor=name_fl)
        tp = 0
        total_true = len(needed_targets)

        for s1_id, true_set in gt.items():
            if not true_set: continue
            s1_n, s1_a, s1_c = s1_records[s1_id]
            norm_s1, a_toks_list, a_canon = scorer.normalize_name(s1_n)
            s1_keys = set(scorer.extract_blocking_keys(s1_n, s1_a, s1_c))
            norm_s1_a = scorer.an.normalize(s1_a) if s1_a else None
            a_toks = set(t for t in a_toks_list if len(t) >= 2)
            a_concat = "".join(a_toks_list)
            a_addr_toks = set(t for t in norm_s1_a.tokens if len(t) >= 2) if norm_s1_a else set()
            a_num_toks = set(norm_s1_a.numeric_tokens) if norm_s1_a else set()
            a_country = scorer.ch.normalize(s1_c).canonical or "UNKNOWN"

            for tid in true_set:
                t_rec = target_records.get(tid)
                if not t_rec: continue
                t_n, t_a, t_c = t_rec
                t_keys = set(scorer.extract_blocking_keys(t_n, t_a, t_c))
                if not (s1_keys & t_keys): continue

                norm_t, t_toks_list, t_canon = scorer.normalize_name(t_n)
                norm_t_a = scorer.an.normalize(t_a) if t_a else None
                t_toks = set(t for t in t_toks_list if len(t) >= 2)
                t_concat = "".join(t_toks_list)
                t_addr_toks = set(t for t in norm_t_a.tokens if len(t) >= 2) if norm_t_a else set()
                t_num_toks = set(norm_t_a.numeric_tokens) if norm_t_a else set()
                t_postal = norm_t_a.postal_code if norm_t_a else ""
                t_country = scorer.ch.normalize(t_c).canonical or "UNKNOWN"

                s = scorer.score_pair(
                    a_canon, a_toks, a_concat, a_addr_toks, a_num_toks, a_country,
                    t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_concat
                )
                if s >= 0.58:
                    tp += 1

        if base_tp == 0:
            base_tp = tp
        diff = tp - base_tp
        print(f"{name:<45} | {tp:<6,d} | {tp/total_true*100:6.2f}%    | {'+' if diff>=0 else ''}{diff:<6,d}")

if __name__ == "__main__":
    main()
