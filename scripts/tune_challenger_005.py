#!/usr/bin/env python3
"""
CHALLENGER_005 Partitioned Tuning & Threshold Sweep Script.
Evaluates on 5,000 validation anchors using memory-safe partitioned streaming.
Incorporates:
1. Universal Indic Script Normalization (Brahmi alignment for Tamil, Telugu, Bengali, Punjabi, Gujarati, Oriya, Kannada, Malayalam)
2. Hindi Business Loanword Dictionary (International, Logistics, Solutions, Global, Infra, etc.)
3. Strict Legal Entity Suffixes (pvt, private, llp, plc, proprietorship)
4. Preserves 100% of CHALLENGER_004's precision-guarded scoring and multi-tenant center vetoes!
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
from ber.normalization.transliteration import transliterate_devanagari, HINDI_BUSINESS_TERMS
import ber.normalization.name_normalizer as nnm
import ber.normalization.transliteration as trm

# 1. Expand Hindi Business Loanwords
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
    "एग्रो": "agro", "फूड्स": "foods",
    "पैकर्स": "packers", "मूवर्स": "movers",
})

# 2. Expand Strict Legal Suffixes
nnm.LEGAL_SUFFIX_MAP.update({
    "private": "pvt", "pvt": "pvt", "llp": "llp", "l l p": "llp",
    "public limited": "ltd", "plc": "ltd", "p l c": "ltd",
    "proprietorship": "prop", "prop": "prop",
})
patterns = sorted(nnm.LEGAL_SUFFIX_MAP.keys(), key=len, reverse=True)
nnm.LEGAL_SUFFIX_REGEX = re.compile(r"\b(" + "|".join(re.escape(k) for k in patterns) + r")\b", re.IGNORECASE)

# 3. Universal Indic Mapping
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

DATASET_DIR = proj_root / "student_resource" / "dataset" / "train"
S1_PATH = DATASET_DIR / "train_source1.tsv"
S2_PATH = DATASET_DIR / "train_source2.tsv"
S3_PATH = DATASET_DIR / "train_source3.tsv"
GT_PATH = DATASET_DIR / "train_ground_truth.tsv"

SAMPLE_SIZE = 5000

def load_ground_truth(gt_path, limit):
    gt = {}
    with open(gt_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)
        count = 0
        for row in reader:
            if count >= limit:
                break
            s1_id = row[0].strip()
            matched_str = row[1].strip() if len(row) > 1 else ""
            gt[s1_id] = set(matched_str.split(",")) if matched_str else set()
            count += 1
    return gt

def load_source_records(path, id_set=None):
    records = {}
    with open(path, 'r', encoding='utf-8') as f:
        f.readline()
        for line in f:
            parts = line.rstrip('\r\n').split('\t')
            if len(parts) < 4:
                continue
            eid = parts[0].strip()
            if id_set is not None and eid not in id_set:
                continue
            records[eid] = (parts[1], parts[2] if len(parts) > 2 else "", parts[3] if len(parts) > 3 else "")
    return records

def _char_similarity(s1: str, s2: str) -> float:
    if s1 == s2:
        return 1.0
    if not s1 or not s2:
        return 0.0
    return SequenceMatcher(None, s1, s2).ratio()

class PartitionedScorerCH5:
    def __init__(self):
        self.nn = NameNormalizer()
        self.an = AddressNormalizer()
        self.ch = CountryHandler()
        self.index = {}
        self.target_records = {}
        self.max_postings_per_key = 300
        self.max_candidates_per_source = 75

    def normalize_name(self, name: str):
        return self.nn.normalize(map_indic_to_devanagari(name))

    def extract_blocking_keys(self, name: str, address: str = "", country: str = ""):
        norm_name = self.normalize_name(name)
        norm_addr = self.an.normalize(address) if address else None
        keys = []

        if norm_name.canonical:
            keys.append(f"NC:{norm_name.canonical}")
            concat_str = "".join(norm_name.tokens)
            if len(concat_str) >= 6:
                keys.append(f"NCONCAT:{concat_str[:20]}")

        if norm_addr and norm_addr.numeric_tokens and norm_addr.tokens:
            p_num = norm_addr.numeric_tokens[0]
            for w in norm_addr.tokens[:3]:
                if len(w) >= 4:
                    keys.append(f"ADDR_NW:{p_num}_{w}")

        if norm_name.canonical and len(norm_name.tokens) >= 2:
            clean_toks = [t for t in norm_name.tokens if len(t) >= 2]
            if len(clean_toks) >= 2:
                keys.append(f"NS:{'_'.join(sorted(clean_toks[:4]))}")
                keys.append(f"NP:{clean_toks[0]}_{clean_toks[1]}")
            elif len(clean_toks) == 1 and len(clean_toks[0]) >= 3:
                keys.append(f"N1:{clean_toks[0]}")
        elif norm_name.canonical and len(norm_name.tokens) == 1 and len(norm_name.tokens[0]) >= 3:
            keys.append(f"N1:{norm_name.tokens[0]}")

        if norm_addr and len(norm_addr.tokens) >= 2:
            keys.append(f"ADDR_WW:{norm_addr.tokens[0]}_{norm_addr.tokens[1]}")

        # CHALLENGER_004 Composite precision-guarded keys:
        if norm_addr and norm_addr.numeric_tokens and norm_name.tokens:
            p_num = norm_addr.numeric_tokens[0]
            n_first = norm_name.tokens[0]
            if len(n_first) >= 3:
                keys.append(f"ADDR_N1:{p_num}_{n_first[:4]}")

        if norm_addr and norm_addr.postal_code and norm_name.tokens:
            n_first = norm_name.tokens[0]
            if len(n_first) >= 3:
                keys.append(f"PIN_N1:{norm_addr.postal_code}_{n_first[:4]}")

        if norm_name.tokens and len(norm_name.tokens[0]) >= 5:
            keys.append(f"N1L:{norm_name.tokens[0]}")

        return keys

    def index_target_file(self, path: Path):
        print(f"Indexing {path.name}...")
        t0 = time.time()
        self.index.clear()
        self.target_records.clear()
        gc.collect()

        count = 0
        with open(path, "r", encoding="utf-8") as f:
            header = f.readline().rstrip("\r\n").split("\t")
            id_idx = header.index("entity_id")
            name_idx = header.index("business_name")
            addr_idx = header.index("business_address")
            country_idx = header.index("country")

            for line in f:
                parts = line.rstrip("\r\n").split("\t")
                if len(parts) <= max(id_idx, name_idx, country_idx):
                    continue
                eid = parts[id_idx].strip()
                name = parts[name_idx]
                address = parts[addr_idx] if addr_idx < len(parts) else ""
                country = parts[country_idx]

                norm_name = self.normalize_name(name)
                norm_addr = self.an.normalize(address) if address else None
                norm_country = self.ch.normalize(country).canonical or "UNKNOWN"

                addr_toks = norm_addr.tokens if norm_addr else ()
                num_toks = norm_addr.numeric_tokens if norm_addr else ()
                postal = norm_addr.postal_code if norm_addr else ""
                name_concat = "".join(norm_name.tokens)

                self.target_records[eid] = (
                    norm_name.canonical,
                    addr_toks,
                    num_toks,
                    norm_country,
                    postal or "",
                    name_concat,
                )

                keys = self.extract_blocking_keys(name, address, country)
                for k in keys:
                    p = self.index.get(k)
                    if p is None:
                        self.index[k] = [eid]
                    elif len(p) < self.max_postings_per_key:
                        p.append(eid)

                count += 1

        elapsed = time.time() - t0
        print(f"  Indexed {count:,} records into {len(self.index):,} keys ({elapsed:.1f}s)")

    def score_pair(
        self,
        a_canon: str, a_toks: set, a_concat: str, a_addr_toks: set, a_num_toks: set, a_country: str,
        t_canon: str, t_addr_toks: tuple, t_num_toks: tuple, t_country: str, t_postal: str, t_name_concat: str
    ) -> float:
        # Contradiction check: country mismatch
        if a_country != "UNKNOWN" and t_country != "UNKNOWN" and a_country != t_country:
            return 0.0

        # Contradiction check: numeric building number verification
        t_num_set = set(t_num_toks)
        has_bldg_conflict = False
        num_match = False
        if a_num_toks and t_num_set:
            intersect = a_num_toks.intersection(t_num_set)
            if intersect:
                num_match = True
                if len(a_num_toks) >= 2 and len(t_num_toks) >= 2:
                    a_num_list = sorted(a_num_toks)
                    t_num_list = sorted(t_num_set)
                    if a_num_list[0] != t_num_list[0] and a_num_list[0] not in t_num_set and t_num_list[0] not in a_num_toks:
                        has_bldg_conflict = True
                    elif a_num_list[-1] != t_num_list[-1] and a_num_list[-1] not in t_num_set and t_num_list[-1] not in a_num_toks:
                        has_bldg_conflict = True
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
            t_toks = set(t for t in t_canon.split() if len(t) >= 2)
            if t_toks:
                overlap = len(a_toks.intersection(t_toks))
                union_len = len(a_toks.union(t_toks))
                jaccard = overlap / union_len if union_len > 0 else 0.0
                name_sim = jaccard
                if jaccard < 0.85:
                    shorter, longer = (a_toks, t_toks) if len(a_toks) <= len(t_toks) else (t_toks, a_toks)
                    if len(shorter) >= 2 and shorter.issubset(longer):
                        containment = len(shorter) / len(longer) if longer else 0.0
                        name_sim = max(name_sim, 0.70 + 0.20 * containment)

        # Domain unmasked root match
        if name_sim < 0.85 and a_canon and t_canon:
            if a_concat and (a_concat == t_canon.replace(" ", "") or t_name_concat == a_canon.replace(" ", "") or a_concat == t_name_concat):
                name_sim = max(name_sim, 0.95)
            elif len(a_canon) >= 8 and len(t_canon) >= 8 and (a_canon in t_canon or t_canon in a_canon):
                name_sim = max(name_sim, 0.90)

        # Precision-guarded character fuzzy similarity
        if name_sim < 0.80 and a_canon and t_canon:
            t_toks = set(t for t in t_canon.split() if len(t) >= 2)
            has_token_overlap = bool(a_toks.intersection(t_toks)) if a_toks and t_toks else False
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

        # CRITICAL PRECISION GUARD:
        if name_sim < 0.45:
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

        return score

    def retrieve_and_score(self, s1_records: dict, target_source_label: str):
        print(f"Scoring {len(s1_records)} anchors against {target_source_label}...")
        t0 = time.time()
        results = defaultdict(list)

        for s1_id, (name, address, country) in s1_records.items():
            keys = self.extract_blocking_keys(name, address, country)
            seen = set()
            cands = []
            for k in keys:
                p = self.index.get(k)
                if p:
                    for tid in p:
                        if tid not in seen and tid != s1_id:
                            seen.add(tid)
                            cands.append(tid)
                            if len(cands) >= self.max_candidates_per_source:
                                break
                if len(cands) >= self.max_candidates_per_source:
                    break

            norm_name = self.normalize_name(name)
            norm_addr = self.an.normalize(address) if address else None
            a_canon = norm_name.canonical
            a_toks = set(t for t in norm_name.tokens if len(t) >= 2)
            a_concat = "".join(norm_name.tokens)
            a_addr_toks = set(t for t in norm_addr.tokens if len(t) >= 2) if norm_addr else set()
            a_num_toks = set(norm_addr.numeric_tokens) if norm_addr else set()
            a_country = self.ch.normalize(country).canonical or "UNKNOWN"

            for cid in cands:
                rec = self.target_records.get(cid)
                if not rec: continue
                t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat = rec
                s = self.score_pair(
                    a_canon, a_toks, a_concat, a_addr_toks, a_num_toks, a_country,
                    t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat
                )
                if s > 0.0:
                    results[s1_id].append((cid, s))

        print(f"  Scoring completed in {time.time()-t0:.1f}s.")
        return results

def main():
    print("==================================================")
    print("CHALLENGER_005 PARTITIONED EVALUATION & TUNING")
    print("==================================================")

    gt = load_ground_truth(GT_PATH, SAMPLE_SIZE)
    total_true_pairs = sum(len(v) for v in gt.values())
    print(f"Loaded {len(gt)} anchors from ground truth ({total_true_pairs} true pairs)")

    s1_records = load_source_records(S1_PATH, set(gt.keys()))
    print(f"Loaded {len(s1_records)} S1 records")

    scorer = PartitionedScorerCH5()

    # Part 1: Index & Score S2
    scorer.index_target_file(S2_PATH)
    s2_scores = scorer.retrieve_and_score(s1_records, "Source 2")

    scorer.index.clear()
    scorer.target_records.clear()
    gc.collect()

    # Part 2: Index & Score S3
    scorer.index_target_file(S3_PATH)
    s3_scores = scorer.retrieve_and_score(s1_records, "Source 3")

    scorer.index.clear()
    scorer.target_records.clear()
    gc.collect()

    # Merge scores
    combined_scores = defaultdict(list)
    cand_recall_hits = 0
    for s1_id in gt:
        all_c = s2_scores.get(s1_id, []) + s3_scores.get(s1_id, [])
        combined_scores[s1_id] = all_c
        c_set = set(cid for cid, s in all_c)
        cand_recall_hits += len(c_set.intersection(gt[s1_id]))

    overall_cand_recall = cand_recall_hits / max(total_true_pairs, 1)
    print("\n" + "=" * 80)
    print(f"CANDIDATE RETRIEVAL RECALL: {overall_cand_recall:.4f} ({cand_recall_hits}/{total_true_pairs}) [CH4 was 0.6440]")
    print("=" * 80)

    # Threshold Sweep
    thresholds = [0.55, 0.58, 0.60, 0.61, 0.62, 0.63, 0.64, 0.65]
    print("\n" + "=" * 85)
    print("CHALLENGER_005 THRESHOLD SWEEP & OPTIMIZATION")
    print("=" * 85)
    print(f"{'Tau':<6} | {'TP':<6} | {'FP':<6} | {'FN':<6} | {'Precision':<10} | {'Recall':<10} | {'F1':<10} | {'F0.5':<10} | {'Gain vs CH4':<12}")
    print("-" * 85)

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
        gain = f05 - 0.8513

        if f05 > best_f05:
            best_f05 = f05
            best_tau = tau
            best_metrics = {"tp": tp, "fp": fp, "fn": fn, "prec": prec, "rec": rec, "f1": f1, "f05": f05}

        print(f"{tau:<6.2f} | {tp:<6} | {fp:<6} | {fn:<6} | {prec:<10.4f} | {rec:<10.4f} | {f1:<10.4f} | {f05:<10.4f} | {'+' if gain>=0 else ''}{gain:<12.4f}")

    print("=" * 85)
    print(f"OPTIMAL THRESHOLD: tau = {best_tau}")
    print(f"BEST METRICS: TP={best_metrics['tp']}, FP={best_metrics['fp']}, FN={best_metrics['fn']}")
    print(f"Precision: {best_metrics['prec']:.4f}, Recall: {best_metrics['rec']:.4f}, F0.5: {best_metrics['f05']:.4f}")
    improvement = best_f05 - 0.8513
    print(f"NET GAIN VS CHALLENGER_004: {'+' if improvement >= 0 else ''}{improvement:.4f} F0.5")
    print("=" * 85)

if __name__ == "__main__":
    main()
