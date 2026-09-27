#!/usr/bin/env python3
"""
Comprehensive Forensic Root Cause Analysis for CHAMPION_784 (Score: 0.784)
Produces: artifacts/forensics/score_0784_root_cause.json

Decomposes all errors into exact categories:
- blocking_miss: True match never generated into candidates
- feature_miss: Candidate generated, but features failed to detect similarity (e.g. OCR/typo/token distortion)
- model_miss: Candidate generated, but model similarity score < 0.45
- threshold_miss: Candidate generated and 0.45 <= score < 0.58 (near miss)
- singleton_error: False positive matches assigned to true singletons (dropping F0.5 from 1.0 to 0.0)
- multi_match_error: Truncation above cap (e.g. cap=8 truncating matches 9-11)
- false_merge: High-confidence false match assigned to a non-singleton
- other: Any other unaccounted errors
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

# Exact CHAMPION_784 Indic & Legal Suffix Setup
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

nnm.LEGAL_SUFFIX_MAP.update({
    "private": "pvt", "pvt": "pvt", "llp": "llp", "l l p": "llp",
    "public limited": "ltd", "plc": "ltd", "p l c": "ltd",
    "proprietorship": "prop", "prop": "prop",
})
patterns = sorted(nnm.LEGAL_SUFFIX_MAP.keys(), key=len, reverse=True)
nnm.LEGAL_SUFFIX_REGEX = re.compile(r"\b(" + "|".join(re.escape(k) for k in patterns) + r")\b", re.IGNORECASE)

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

def _char_similarity(s1: str, s2: str) -> float:
    if s1 == s2:
        return 1.0
    if not s1 or not s2:
        return 0.0
    return SequenceMatcher(None, s1, s2).ratio()

class Champion784Scorer:
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

    def stream_and_index_target(self, path: Path, active_keys: set):
        print(f"Scanning {path.name} against {len(active_keys):,} active keys...")
        t0 = time.time()
        self.index.clear()
        self.target_records.clear()
        gc.collect()

        indexed_count = 0
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

                keys = self.extract_blocking_keys(name, address, country)
                matching_keys = [k for k in keys if k in active_keys]
                if not matching_keys:
                    continue

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

                for k in matching_keys:
                    p = self.index.get(k)
                    if p is None:
                        self.index[k] = [eid]
                    elif len(p) < self.max_postings_per_key:
                        p.append(eid)
                indexed_count += 1

        print(f"  Indexed {indexed_count:,} candidate targets in {time.time()-t0:.1f}s")

    def score_pair(self, a_canon, a_toks, a_concat, a_addr_toks, a_num_toks, a_country,
                   t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat):
        if a_country != "UNKNOWN" and t_country != "UNKNOWN" and a_country != t_country:
            return 0.0, "country_conflict"

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
            return 0.0, "building_conflict"

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

        if name_sim < 0.85 and a_canon and t_canon:
            if a_concat and (a_concat == t_canon.replace(" ", "") or t_name_concat == a_canon.replace(" ", "") or a_concat == t_name_concat):
                name_sim = max(name_sim, 0.95)
            elif len(a_canon) >= 8 and len(t_canon) >= 8 and (a_canon in t_canon or t_canon in a_canon):
                name_sim = max(name_sim, 0.90)

        if name_sim < 0.80 and a_canon and t_canon:
            t_toks = set(t for t in t_canon.split() if len(t) >= 2)
            has_token_overlap = bool(a_toks.intersection(t_toks)) if a_toks and t_toks else False
            if has_token_overlap or num_match:
                if a_concat and t_name_concat and len(a_concat) >= 6 and len(t_name_concat) >= 6:
                    ratio = _char_similarity(a_concat, t_name_concat)
                    if ratio >= 0.78:
                        name_sim = max(name_sim, ratio * 0.90)

        addr_sim = 0.0
        t_atok_set = set(t for t in t_addr_toks if len(t) >= 2)
        if a_addr_toks and t_atok_set:
            overlap = len(a_addr_toks.intersection(t_atok_set))
            union_len = len(a_addr_toks.union(t_atok_set))
            addr_sim = overlap / union_len if union_len > 0 else 0.0

        if name_sim < 0.45:
            return 0.0, "low_name_similarity"

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

        return score, "ok"

    def retrieve_and_score(self, s1_records: dict, target_source_label: str):
        print(f"Scoring {len(s1_records)} anchors against {target_source_label}...")
        t0 = time.time()
        results = defaultdict(list)
        all_candidates = defaultdict(list)

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

            all_candidates[s1_id] = cands

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
                s, reason = self.score_pair(
                    a_canon, a_toks, a_concat, a_addr_toks, a_num_toks, a_country,
                    t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat
                )
                results[s1_id].append((cid, s, reason))

        print(f"  Scoring completed in {time.time()-t0:.1f}s")
        return results, all_candidates

def main():
    print("=" * 80)
    print("PHASE 1: ROOT CAUSE FAILURE DECOMPOSITION FOR CHAMPION_784")
    print("=" * 80)

    # 1. Load Ground Truth
    gt = {}
    with open(GT_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)
        for i, row in enumerate(reader):
            if i >= SAMPLE_SIZE: break
            s1 = row[0].strip()
            m = [x.strip() for x in row[1].split(",") if x.strip()] if len(row) > 1 and row[1].strip() else []
            gt[s1] = set(m)

    # 2. Load S1 Records
    needed_s1 = set(gt.keys())
    s1_records = {}
    with open(S1_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)
        for row in reader:
            eid = row[0].strip()
            if eid in needed_s1:
                s1_records[eid] = (row[1], row[2] if len(row)>2 else "", row[3] if len(row)>3 else "")

    scorer = Champion784Scorer()

    # Extract all active keys from S1 records to fast-filter target scanning
    active_keys = set()
    for s1_id, (n, a, c) in s1_records.items():
        for k in scorer.extract_blocking_keys(n, a, c):
            active_keys.add(k)
    print(f"Active blocking keys from {len(s1_records)} S1 anchors: {len(active_keys):,}")

    # Process S2
    scorer.stream_and_index_target(S2_PATH, active_keys)
    s2_scores, s2_cands = scorer.retrieve_and_score(s1_records, "Source 2")

    # Process S3
    scorer.stream_and_index_target(S3_PATH, active_keys)
    s3_scores, s3_cands = scorer.retrieve_and_score(s1_records, "Source 3")

    scorer.index.clear()
    scorer.target_records.clear()
    gc.collect()

    print("\n[PART 2: Comprehensive Error Decomposition]")
    tau = 0.58
    max_cap = 8

    # Decomposition counters
    counts = {
        "total_anchors": len(gt),
        "total_true_matches": sum(len(v) for v in gt.values()),
        "true_positives": 0,
        "false_positives": 0,
        "false_negatives": 0,
        "blocking_miss": 0,
        "feature_miss": 0,
        "model_miss": 0,
        "threshold_miss": 0,
        "singleton_error": 0,
        "multi_match_error": 0,
        "false_merge": 0,
        "other": 0
    }

    macro_f05_scores = []
    singleton_stats = {"true_singletons": 0, "correct_singletons": 0, "singleton_fps": 0}

    for s1_id, true_set in gt.items():
        cands_s2 = s2_cands.get(s1_id, [])
        cands_s3 = s3_cands.get(s1_id, [])
        cand_set = set(cands_s2) | set(cands_s3)

        scores_s2 = s2_scores.get(s1_id, [])
        scores_s3 = s3_scores.get(s1_id, [])
        all_scored = scores_s2 + scores_s3
        score_dict = {cid: (s, r) for cid, s, r in all_scored}

        # Filter and rank predictions
        passing = [item for item in all_scored if item[1] >= tau]
        passing.sort(key=lambda x: x[1], reverse=True)
        pred_set = set(x[0] for x in passing[:max_cap])
        truncated_away = set(x[0] for x in passing[max_cap:])

        # Singletons handling
        is_singleton = (len(true_set) == 0)
        if is_singleton:
            singleton_stats["true_singletons"] += 1
            if len(pred_set) == 0:
                singleton_stats["correct_singletons"] += 1
                entity_f05 = 1.0
            else:
                singleton_stats["singleton_fps"] += len(pred_set)
                counts["singleton_error"] += len(pred_set)
                counts["false_positives"] += len(pred_set)
                entity_f05 = 0.0
        else:
            tp = len(pred_set & true_set)
            fp = len(pred_set - true_set)
            fn = len(true_set - pred_set)
            counts["true_positives"] += tp
            counts["false_positives"] += fp
            counts["false_negatives"] += fn
            counts["false_merge"] += fp

            if tp == 0:
                entity_f05 = 0.0
            else:
                p_i = tp / (tp + fp)
                r_i = tp / len(true_set)
                entity_f05 = (1.25 * p_i * r_i) / (0.25 * p_i + r_i)

            # Analyze False Negatives (Missed True Matches)
            for tid in (true_set - pred_set):
                if tid in truncated_away:
                    counts["multi_match_error"] += 1
                elif tid not in cand_set:
                    counts["blocking_miss"] += 1
                else:
                    # In candidates, but didn't pass or was vetoed
                    s_info = score_dict.get(tid)
                    if not s_info:
                        counts["feature_miss"] += 1
                    else:
                        s_val, reason = s_info
                        if s_val == 0.0:
                            counts["feature_miss"] += 1
                        elif s_val < 0.45:
                            counts["model_miss"] += 1
                        elif s_val < tau:
                            counts["threshold_miss"] += 1
                        else:
                            counts["other"] += 1

        macro_f05_scores.append(entity_f05)

    macro_f05 = sum(macro_f05_scores) / len(macro_f05_scores)
    total_tp = counts["true_positives"]
    total_fp = counts["false_positives"]
    total_fn = counts["false_negatives"]
    micro_prec = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0.0
    micro_rec = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0.0
    micro_f05 = (1.25 * micro_prec * micro_rec) / (0.25 * micro_prec + micro_rec) if (0.25 * micro_prec + micro_rec) > 0 else 0.0

    cand_hits = sum(len((set(s2_cands.get(sid, [])) | set(s3_cands.get(sid, []))) & gt[sid]) for sid in gt)
    cand_recall = cand_hits / counts["total_true_matches"]

    print("\n--- RESULTS SUMMARY ---")
    print(f"Total Anchors: {counts['total_anchors']:,}")
    print(f"Total True Matches: {counts['total_true_matches']:,}")
    print(f"Candidate Recall: {cand_recall*100:.2f}% ({cand_hits:,}/{counts['total_true_matches']:,})")
    print(f"Macro F0.5: {macro_f05:.4f}")
    print(f"Micro F0.5: {micro_f05:.4f} (Precision: {micro_prec*100:.2f}%, Recall: {micro_rec*100:.2f}%)")
    print(f"True Singletons: {singleton_stats['true_singletons']} | Correct Singletons: {singleton_stats['correct_singletons']} | Singleton FP Rate: {(singleton_stats['true_singletons']-singleton_stats['correct_singletons'])/singleton_stats['true_singletons']*100:.2f}%")

    print("\n--- EXACT ROOT CAUSE BREAKDOWN ---")
    total_error_events = (
        counts["blocking_miss"] +
        counts["feature_miss"] +
        counts["model_miss"] +
        counts["threshold_miss"] +
        counts["singleton_error"] +
        counts["multi_match_error"] +
        counts["false_merge"] +
        counts["other"]
    )
    print(f"{'Error Category':<25} | {'Count':<8} | {'Pct of All Error Events':<25}")
    print("-" * 65)
    for cat in ["blocking_miss", "feature_miss", "model_miss", "threshold_miss", "singleton_error", "multi_match_error", "false_merge", "other"]:
        c = counts[cat]
        pct = (c / total_error_events * 100) if total_error_events > 0 else 0.0
        print(f"{cat:<25} | {c:<8,d} | {pct:6.2f}%")

    # Output JSON file
    out_json = {
        "champion_id": "CHAMPION_784",
        "public_score": 0.784,
        "evaluation_anchors": counts["total_anchors"],
        "total_true_matches": counts["total_true_matches"],
        "macro_f0_5": round(macro_f05, 4),
        "micro_f0_5": round(micro_f05, 4),
        "micro_precision": round(micro_prec, 4),
        "micro_recall": round(micro_rec, 4),
        "candidate_recall": round(cand_recall, 4),
        "error_decomposition": {
            "blocking_miss": counts["blocking_miss"],
            "feature_miss": counts["feature_miss"],
            "model_miss": counts["model_miss"],
            "threshold_miss": counts["threshold_miss"],
            "singleton_error": counts["singleton_error"],
            "multi_match_error": counts["multi_match_error"],
            "false_merge": counts["false_merge"],
            "other": counts["other"]
        },
        "percentages": {
            "blocking_miss": round(counts["blocking_miss"] / total_error_events * 100, 2),
            "feature_miss": round(counts["feature_miss"] / total_error_events * 100, 2),
            "model_miss": round(counts["model_miss"] / total_error_events * 100, 2),
            "threshold_miss": round(counts["threshold_miss"] / total_error_events * 100, 2),
            "singleton_error": round(counts["singleton_error"] / total_error_events * 100, 2),
            "multi_match_error": round(counts["multi_match_error"] / total_error_events * 100, 2),
            "false_merge": round(counts["false_merge"] / total_error_events * 100, 2),
            "other": round(counts["other"] / total_error_events * 100, 2)
        },
        "singleton_statistics": {
            "true_singletons": singleton_stats["true_singletons"],
            "correctly_identified_singletons": singleton_stats["correct_singletons"],
            "singleton_false_positives": singleton_stats["singleton_fps"],
            "singleton_accuracy": round(singleton_stats["correct_singletons"] / singleton_stats["true_singletons"], 4)
        }
    }

    out_path = proj_root / "artifacts" / "forensics" / "score_0784_root_cause.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out_json, f, indent=2)

    print(f"\nSaved root cause failure decomposition to: {out_path}")

if __name__ == "__main__":
    main()
