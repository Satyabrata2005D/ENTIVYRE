#!/usr/bin/env python3
"""
Comprehensive Match-Cap and Threshold Audit for CHALLENGER_005.
Performs:
1. Ground Truth Match-Cap Audit on full 2,206,821 ground truth records.
2. Validation Threshold & Cap Sweep on 5,000 validation anchors:
   - Caps: 8, 12, 16, 24, 32, 64, uncapped
   - Thresholds: 0.54, 0.56, 0.57, 0.58, 0.59, 0.60, 0.62, 0.65
   - Metrics: Precision, Recall, Macro F0.5, Singleton FP Rate, Multi-match Recall
3. S2 vs S3 Independent Performance.
4. Country-Specific Performance.
5. Candidate-Set Efficiency Statistics.
"""

import sys
import gc
import re
import time
import csv
import json
from pathlib import Path
from collections import defaultdict, Counter
from difflib import SequenceMatcher

proj_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(proj_root / "code" / "business_entity_resolution" / "src"))

from ber.normalization.name_normalizer import NameNormalizer
from ber.normalization.address_normalizer import AddressNormalizer
from ber.normalization.country_handler import CountryHandler
import ber.normalization.transliteration as trm
import ber.normalization.name_normalizer as nnm

# Ensure Indic script and legal suffixes are active
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

class Scorer:
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
        print(f"  Indexed {count:,} records in {time.time()-t0:.1f}s")

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
            return 0.0

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

        print(f"  Scoring completed in {time.time()-t0:.1f}s")
        return results

def main():
    print("=" * 70)
    print("MATCH-CAP AND THRESHOLD AUDIT FOR CHALLENGER_005")
    print("=" * 70)

    # 1. Full Ground Truth Match-Cap Audit
    print("\n[PART 1: Ground Truth Distribution Audit (2,206,821 Anchors)]")
    match_counts = []
    with open(GT_PATH, "r", encoding="utf-8") as f:
        f.readline()
        for line in f:
            parts = line.rstrip("\r\n").split("\t")
            if len(parts) >= 2 and parts[1]:
                matches = [x.strip() for x in parts[1].split(",") if x.strip()]
                match_counts.append(len(matches))
            else:
                match_counts.append(0)

    total_entities = len(match_counts)
    total_true_matches = sum(match_counts)
    max_m = max(match_counts)
    print(f"Total Ground Truth Anchors: {total_entities:,}")
    print(f"Total True Matches: {total_true_matches:,}")
    print(f"Maximum True Matches for any S1 Entity: {max_m}")

    gt_caps = [8, 12, 16, 24, 32, 64]
    gt_audit_results = {}
    for cap in gt_caps:
        over = [cnt for cnt in match_counts if cnt > cap]
        trunc = sum(cnt - cap for cnt in over)
        loss = trunc / total_true_matches if total_true_matches > 0 else 0.0
        gt_audit_results[cap] = {
            "truncated_entities": len(over),
            "truncated_matches": trunc,
            "recall_loss_pct": loss * 100
        }
        print(f"  Cap {cap:2d}: Truncated Entities={len(over):>5,}, Truncated Matches={trunc:>5,}, True Recall Loss={loss*100:.4f}%")

    # 2. Validation Run (5,000 Anchors)
    print("\n[PART 2: Empirical Validation on 5,000 Anchors]")
    gt_sample = {}
    with open(GT_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)
        for i, row in enumerate(reader):
            if i >= SAMPLE_SIZE:
                break
            s1_id = row[0].strip()
            m_str = row[1].strip() if len(row) > 1 else ""
            gt_sample[s1_id] = set(m_str.split(",")) if m_str else set()

    s1_records = {}
    with open(S1_PATH, "r", encoding="utf-8") as f:
        f.readline()
        for line in f:
            parts = line.rstrip("\r\n").split("\t")
            if len(parts) < 4: continue
            eid = parts[0].strip()
            if eid in gt_sample:
                s1_records[eid] = (parts[1], parts[2] if len(parts) > 2 else "", parts[3] if len(parts) > 3 else "")

    scorer = Scorer()
    scorer.index_target_file(S2_PATH)
    s2_scores = scorer.retrieve_and_score(s1_records, "Source 2")
    scorer.index.clear()
    scorer.target_records.clear()
    gc.collect()

    scorer.index_target_file(S3_PATH)
    s3_scores = scorer.retrieve_and_score(s1_records, "Source 3")
    scorer.index.clear()
    scorer.target_records.clear()
    gc.collect()

    combined_scores = defaultdict(list)
    cand_recall_hits = 0
    total_true = sum(len(v) for v in gt_sample.values())

    s2_hits = 0
    s2_true = 0
    s3_hits = 0
    s3_true = 0

    for s1_id, true_set in gt_sample.items():
        cands_s2 = s2_scores.get(s1_id, [])
        cands_s3 = s3_scores.get(s1_id, [])
        combined = cands_s2 + cands_s3
        combined_scores[s1_id] = combined
        c_set = set(c[0] for c in combined)
        cand_recall_hits += len(c_set.intersection(true_set))

        # S2 vs S3 split
        true_s2 = set(x for x in true_set if x.startswith("S2-"))
        true_s3 = set(x for x in true_set if x.startswith("S3-"))
        s2_true += len(true_s2)
        s3_true += len(true_s3)
        s2_hits += len(set(c[0] for c in cands_s2).intersection(true_s2))
        s3_hits += len(set(c[0] for c in cands_s3).intersection(true_s3))

    cand_recall = cand_recall_hits / total_true
    print(f"\nCandidate Recall: {cand_recall:.4f} ({cand_recall_hits}/{total_true})")
    print(f"  Source 2 Candidate Recall: {s2_hits/max(s2_true, 1):.4f} ({s2_hits}/{s2_true})")
    print(f"  Source 3 Candidate Recall: {s3_hits/max(s3_true, 1):.4f} ({s3_hits}/{s3_true})")

    # 3. Match-Cap Audit on Validation Set (at threshold = 0.58)
    print("\n[PART 3: Empirical Match-Cap Audit (at Threshold = 0.58)]")
    caps_to_test = [8, 12, 16, 24, 32, 64, 999999]  # 999999 represents uncapped
    tau_fixed = 0.58
    cap_results = {}

    print(f"{'Cap':<10} | {'TP':<6} | {'FP':<6} | {'FN':<6} | {'Precision':<10} | {'Recall':<10} | {'Macro F0.5':<10} | {'F0.5 vs Cap 8':<14}")
    print("-" * 85)

    base_f05 = 0.0
    for cap in caps_to_test:
        tp = fp = fn = 0
        cap_label = "Uncapped" if cap == 999999 else str(cap)
        for s1_id, true_set in gt_sample.items():
            cands = combined_scores.get(s1_id, [])
            matched_list = [c for c in cands if c[1] >= tau_fixed]
            if len(matched_list) > cap:
                matched_list.sort(key=lambda x: x[1], reverse=True)
                matched_list = matched_list[:cap]
            matched = set(c[0] for c in matched_list)

            tp += len(matched.intersection(true_set))
            fp += len(matched - true_set)
            fn += len(true_set - matched)

        prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f05 = 1.25 * prec * rec / (0.25 * prec + rec) if (0.25 * prec + rec) > 0 else 0.0

        if cap == 8:
            base_f05 = f05

        diff = f05 - base_f05
        diff_str = f"{'+' if diff >= 0 else ''}{diff:.6f}"
        print(f"{cap_label:<10} | {tp:<6} | {fp:<6} | {fn:<6} | {prec:<10.4f} | {rec:<10.4f} | {f05:<10.4f} | {diff_str:<14}")
        cap_results[cap_label] = {"tp": tp, "fp": fp, "fn": fn, "prec": prec, "rec": rec, "f05": f05, "diff": diff}

    # 4. Threshold Audit around 0.58 (with cap=8 and cap=12)
    print("\n[PART 4: Threshold Audit Around 0.58]")
    thresholds = [0.54, 0.56, 0.57, 0.58, 0.59, 0.60, 0.62, 0.65]

    for chosen_cap in [8, 12]:
        print(f"\n--- Threshold Audit with Cap = {chosen_cap} ---")
        print(f"{'Threshold':<10} | {'Precision':<10} | {'Recall':<10} | {'Macro F0.5':<10} | {'Singleton FP':<14} | {'Multi-Match Rec':<16}")
        print("-" * 85)

        for tau in thresholds:
            tp = fp = fn = 0
            singleton_fp = 0
            total_singletons = 0
            multi_true = 0
            multi_hits = 0

            for s1_id, true_set in gt_sample.items():
                cands = combined_scores.get(s1_id, [])
                matched_list = [c for c in cands if c[1] >= tau]
                if len(matched_list) > chosen_cap:
                    matched_list.sort(key=lambda x: x[1], reverse=True)
                    matched_list = matched_list[:chosen_cap]
                matched = set(c[0] for c in matched_list)

                tp += len(matched.intersection(true_set))
                fp += len(matched - true_set)
                fn += len(true_set - matched)

                # Singleton check
                if len(true_set) == 0:
                    total_singletons += 1
                    if len(matched) > 0:
                        singleton_fp += 1
                elif len(true_set) > 1:
                    multi_true += len(true_set)
                    multi_hits += len(matched.intersection(true_set))

            prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
            rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
            f05 = 1.25 * prec * rec / (0.25 * prec + rec) if (0.25 * prec + rec) > 0 else 0.0
            s_fp_rate = singleton_fp / max(total_singletons, 1)
            mm_rec = multi_hits / max(multi_true, 1)

            print(f"{tau:<10.2f} | {prec:<10.4f} | {rec:<10.4f} | {f05:<10.4f} | {s_fp_rate*100:<13.2f}% | {mm_rec*100:<15.2f}%")

    # 5. Country Specific Performance
    print("\n[PART 5: Country-Specific Performance (Tau=0.58, Cap=8)]")
    country_groups = defaultdict(lambda: {"tp": 0, "fp": 0, "fn": 0, "count": 0})
    for s1_id, (name, address, country) in s1_records.items():
        true_set = gt_sample.get(s1_id, set())
        cands = combined_scores.get(s1_id, [])
        matched_list = [c for c in cands if c[1] >= 0.58]
        if len(matched_list) > 8:
            matched_list.sort(key=lambda x: x[1], reverse=True)
            matched_list = matched_list[:8]
        matched = set(c[0] for c in matched_list)

        c_norm = scorer.ch.normalize(country).canonical or "UNKNOWN"
        country_groups[c_norm]["count"] += 1
        country_groups[c_norm]["tp"] += len(matched.intersection(true_set))
        country_groups[c_norm]["fp"] += len(matched - true_set)
        country_groups[c_norm]["fn"] += len(true_set - matched)

    for c_code, stats in sorted(country_groups.items()):
        tp = stats["tp"]
        fp = stats["fp"]
        fn = stats["fn"]
        p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f05 = 1.25 * p * r / (0.25 * p + r) if (0.25 * p + r) > 0 else 0.0
        print(f"  Country {c_code:<8}: Anchors={stats['count']:<5} Precision={p:.4f} Recall={r:.4f} F0.5={f05:.4f}")

    print("\n" + "=" * 70)
    print("AUDIT EXECUTION COMPLETE")
    print("=" * 70)

if __name__ == "__main__":
    main()
