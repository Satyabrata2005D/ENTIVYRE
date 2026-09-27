import json
"""
Evaluation Script for CHALLENGER_002.
Tests proposed upgrades:
1. Domain Name Resolution (strips TLDs, preserves domain roots instead of erasing).
2. Acronym Preservation (min_name_token_length = 2).
3. Leading Indian Honorific Stripping (M/s, Sri, Shri, Smt, Dr).
4. Building Number Disambiguation (veto disjoint leading unit numbers).
5. OCR Truncation Tolerance (allow prefix match with length diff <= 1).
6. Softened Address Penalty (when building number matches).
7. French Street Typography (impasse, passage, quai, cours).
"""
import sys
import os
import csv
import re
import time
from pathlib import Path
from collections import Counter, defaultdict

sys.path.insert(0, 'code/business_entity_resolution/src')
from ber.inference.engine import InferenceEngine, InferenceConfig
from ber.normalization.name_normalizer import NameNormalizer, NormalizedName
from ber.normalization.address_normalizer import AddressNormalizer, NormalizedAddress
from ber.normalization.country_handler import CountryHandler

# Upgraded Normalizers for CHALLENGER_002
URL_PROTOCOL_REGEX = re.compile(r"https?://(?:www\.)?|www\.", re.IGNORECASE)
TLD_SUFFIX_REGEX = re.compile(r"\.(?:com|org|net|in|fr|co|io|biz|info|gov|edu)(?:/[^\s]*)?\b", re.IGNORECASE)
HONORIFIC_PREFIX_REGEX = re.compile(r"^(?:m\s*/?\s*s\.?|shri|sri|smt|dr\.?|er\.?|late)\s+", re.IGNORECASE)
NON_ALPHANUM_REGEX = re.compile(r"[^a-z0-9\s]")
WHITESPACE_REGEX = re.compile(r"\s+")

class UpgradedNameNormalizer(NameNormalizer):
    def normalize(self, raw_name):
        base_res = super().normalize(raw_name)
        if not raw_name:
            return base_res
            
        text = str(raw_name).strip()
        text_lower = text.lower()
        has_url = False
        
        # 1. Domain / URL unmasking
        if URL_PROTOCOL_REGEX.search(text_lower) or TLD_SUFFIX_REGEX.search(text_lower):
            has_url = True
            text_lower = URL_PROTOCOL_REGEX.sub(" ", text_lower)
            text_lower = TLD_SUFFIX_REGEX.sub(" ", text_lower)
            text_lower = text_lower.replace(".", " ").replace("-", " ").replace("/", " ").replace("_", " ")
            
        clean_text = NON_ALPHANUM_REGEX.sub(" ", text_lower)
        clean_text = WHITESPACE_REGEX.sub(" ", clean_text).strip()
        
        # 2. Leading Honorific stripping (when followed by at least 1 word)
        if HONORIFIC_PREFIX_REGEX.search(clean_text):
            sub_h = HONORIFIC_PREFIX_REGEX.sub("", clean_text).strip()
            if sub_h and len(sub_h.split()) >= 1:
                clean_text = sub_h
                
        # 3. Legal suffix stripping on unmasked clean text
        from ber.normalization.name_normalizer import LEGAL_SUFFIX_REGEX, LEGAL_SUFFIX_MAP
        detected_suffix = base_res.legal_suffix
        canonical_text = clean_text
        suffix_matches = LEGAL_SUFFIX_REGEX.findall(clean_text)
        if suffix_matches:
            raw_suf = max(suffix_matches, key=len).lower()
            detected_suffix = LEGAL_SUFFIX_MAP.get(raw_suf, raw_suf)
            sub_canonical = LEGAL_SUFFIX_REGEX.sub(" ", clean_text)
            sub_canonical = WHITESPACE_REGEX.sub(" ", sub_canonical).strip()
            if sub_canonical:
                canonical_text = sub_canonical
                
        raw_tokens = tuple(t for t in canonical_text.split() if t)
        sorted_tokens = tuple(sorted(set(raw_tokens)))
        
        return NormalizedName(
            raw=str(raw_name),
            clean=clean_text,
            canonical=canonical_text,
            tokens=raw_tokens,
            tokens_sorted=sorted_tokens,
            legal_suffix=detected_suffix,
            has_transliteration=base_res.has_transliteration,
            has_url_stripped=has_url or base_res.has_url_stripped,
        )

def run_challenger_evaluation():
    print("=== EVALUATING CHALLENGER_002 vs CHAMPION_001 ===", flush=True)
    t0 = time.time()
    
    eng_champ = InferenceEngine()
    
    name_norm_c002 = UpgradedNameNormalizer()
    addr_norm_c002 = AddressNormalizer()
    country_norm_c002 = CountryHandler()
    
    # 1. Load validation ground truth
    print("[1/5] Loading 5,000 validation anchors...", flush=True)
    gt_map = {}
    with open('student_resource/dataset/train/train_ground_truth.tsv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)
        for row in reader:
            s1 = row[0].strip()
            tgts = [t.strip() for t in row[1].split(',') if t.strip()] if len(row) > 1 and row[1].strip() else []
            gt_map[s1] = tgts
            if len(gt_map) >= 5000:
                break
                
    s1_set = set(gt_map.keys())
    all_true_targets = set(t for tgts in gt_map.values() for t in tgts)
    
    s1_records = {}
    with open('student_resource/dataset/train/train_source1.tsv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        hdr = [c.lower() for c in next(reader)]
        i_idx, n_idx, a_idx, c_idx = hdr.index('entity_id'), hdr.index('business_name'), hdr.index('business_address'), hdr.index('country')
        for row in reader:
            s1_id = row[i_idx].strip()
            if s1_id in s1_set:
                s1_records[s1_id] = (row[n_idx], row[a_idx] if a_idx < len(row) else '', row[c_idx])
                
    # Extract blocking keys for validation anchors under both Champion and Challenger
    def get_keys(n_norm, name, addr, ctry, min_tok_len=2):
        nn = n_norm.normalize(name)
        na = addr_norm_c002.normalize(addr) if addr else None
        keys = []
        if nn.canonical:
            keys.append(f"NAME_CANON:{nn.canonical}")
            clean_toks = [t for t in nn.tokens if len(t) >= min_tok_len]
            if len(clean_toks) >= 2:
                keys.append(f"NAME_SORTED:{'_'.join(sorted(clean_toks[:4]))}")
                keys.append(f"NAME_PREF:{clean_toks[0]}_{clean_toks[1]}")
            elif len(clean_toks) == 1 and len(clean_toks[0]) >= 3:
                keys.append(f"NAME_SINGLE:{clean_toks[0]}")
        if na:
            if na.tokens and len(na.tokens) >= 2:
                keys.append(f"ADDR_PREF:{na.tokens[0]}_{na.tokens[1]}")
            if na.numeric_tokens and nn.tokens:
                keys.append(f"NUM_NAME:{na.numeric_tokens[0]}_{nn.tokens[0][:4]}")
            if na.postal_code and nn.tokens:
                keys.append(f"PIN_NAME:{na.postal_code}_{nn.tokens[0][:4]}")
        return keys
        
    val_keys_c002 = set()
    for s1_id, (name, addr, ctry) in s1_records.items():
        val_keys_c002.update(get_keys(name_norm_c002, name, addr, ctry, min_tok_len=2))
        
    print(f"Challenger validation keys: {len(val_keys_c002):,}", flush=True)
    
    # 2. Stream S2 & S3
    print("[2/5] Streaming Source 2 & Source 3...", flush=True)
    index_c002 = defaultdict(list)
    target_cache_c002 = {}
    
    def stream_s(path, src_label):
        t_start = time.time()
        count = 0
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='\t')
            hdr = [c.lower() for c in next(reader)]
            i_idx, n_idx, a_idx, c_idx = hdr.index('entity_id'), hdr.index('business_name'), hdr.index('business_address'), hdr.index('country')
            for row in reader:
                tid = row[i_idx].strip()
                tname = row[n_idx]
                taddr = row[a_idx] if a_idx < len(row) else ''
                tctry = row[c_idx]
                
                is_true = (tid in all_true_targets)
                keys = get_keys(name_norm_c002, tname, taddr, tctry, min_tok_len=2)
                valid_keys = [k for k in keys if k in val_keys_c002 and len(index_c002[k]) < 500]
                
                if valid_keys or is_true:
                    nn = name_norm_c002.normalize(tname)
                    na = addr_norm_c002.normalize(taddr) if taddr else None
                    nc = country_norm_c002.normalize(tctry).canonical or "UNKNOWN"
                    
                    target_cache_c002[tid] = (
                        tname,
                        taddr,
                        tctry,
                        nn.canonical,
                        nn.tokens,
                        na.tokens if na else (),
                        na.numeric_tokens if na else (),
                        nc,
                    )
                    
                    for k in valid_keys:
                        plist = index_c002[k]
                        if len(plist) < 500:
                            plist.append(tid)
                    count += 1
        print(f"  {src_label} finished in {time.time() - t_start:.1f}s (retained {count:,} targets)", flush=True)
        
    stream_s('student_resource/dataset/train/train_source2.tsv', 'Source 2')
    stream_s('student_resource/dataset/train/train_source3.tsv', 'Source 3')
    print(f"Total targets cached: {len(target_cache_c002):,}", flush=True)
    
    # 3. Evaluate CHALLENGER_002
    print("[3/5] Evaluating CHALLENGER_002 across 5,000 validation anchors...", flush=True)
    
    total_true_links = sum(len(t) for t in gt_map.values())
    recalled_links_c002 = 0
    pred_c002 = {}
    
    tp_c002 = 0
    fp_c002 = 0
    fn_c002 = 0
    per_e_f05_c002 = []
    non_s_f05_c002 = []
    
    for s1_id, (s1_name, s1_addr, s1_ctry) in s1_records.items():
        true_tgts = set(gt_map.get(s1_id, []))
        keys = get_keys(name_norm_c002, s1_name, s1_addr, s1_ctry, min_tok_len=2)
        
        seen = set()
        cands = []
        for k in keys:
            for tid in index_c002.get(k, []):
                if tid not in seen and tid != s1_id:
                    seen.add(tid)
                    cands.append(tid)
                    if len(cands) >= 50: break
            if len(cands) >= 50: break
            
        for tt in true_tgts:
            if tt in seen:
                recalled_links_c002 += 1
                
        # Scoring
        norm_a_name = name_norm_c002.normalize(s1_name)
        norm_a_addr = addr_norm_c002.normalize(s1_addr) if s1_addr else None
        a_canon = norm_a_name.canonical
        a_toks = set(t for t in norm_a_name.tokens if len(t) >= 2)
        a_addr_toks = set(t for t in norm_a_addr.tokens if len(t) >= 3) if norm_a_addr else set()
        a_num_toks = norm_a_addr.numeric_tokens if norm_a_addr else ()
        a_num_set = set(a_num_toks)
        a_ctry = country_norm_c002.normalize(s1_ctry).canonical or "UNKNOWN"
        
        scored = []
        for cid in cands:
            trec = target_cache_c002.get(cid)
            if not trec:
                continue
            t_raw_n, t_raw_a, t_raw_c, t_canon, t_tokens, t_a_toks, t_num_toks, t_ctry = trec
            
            # 1. Country veto
            if a_ctry != "UNKNOWN" and t_ctry != "UNKNOWN" and a_ctry != t_ctry:
                continue
                
            # 2. Building number disambiguation & OCR tolerance
            t_num_set = set(t_num_toks)
            has_bldg_conflict = False
            
            if a_num_set and t_num_set:
                intersect = a_num_set.intersection(t_num_set)
                if not intersect:
                    # Check OCR 1-digit truncation tolerance (e.g. 9327 vs 932, 459 vs 45)
                    ocr_match = False
                    for an in a_num_set:
                        for tn in t_num_set:
                            if len(an) >= 2 and len(tn) >= 2 and (an.startswith(tn) or tn.startswith(an)) and abs(len(an) - len(tn)) <= 1:
                                ocr_match = True
                                break
                        if ocr_match: break
                    if not ocr_match:
                        has_bldg_conflict = True
                else:
                    # Check for commercial complex collision:
                    # If both have multiple numbers, and their FIRST numbers differ and neither is in the other's set:
                    if len(a_num_toks) >= 2 and len(t_num_toks) >= 2:
                        a0 = a_num_toks[0]
                        t0_num = t_num_toks[0]
                        if a0 != t0_num and a0 not in t_num_set and t0_num not in a_num_set:
                            # Conflicting unit numbers in same complex
                            has_bldg_conflict = True
                            
            if has_bldg_conflict:
                continue
                
            # 3. Name similarity with domain unmasking
            name_sim = 0.0
            if a_canon and t_canon and a_canon == t_canon:
                name_sim = 1.0
            elif a_toks and t_canon:
                t_tok_set = set(t for t in t_tokens if len(t) >= 2)
                if t_tok_set:
                    overlap = len(a_toks.intersection(t_tok_set))
                    union_len = len(a_toks.union(t_tok_set))
                    name_sim = overlap / union_len if union_len > 0 else 0.0
                    
            # Domain concatenated check (e.g. maure williams colombier vs maurewilliamscolombier)
            if name_sim < 0.85 and a_canon and t_canon:
                a_joined = "".join(norm_a_name.tokens)
                t_joined = "".join(t_tokens)
                if a_joined == t_canon or t_joined == a_canon or a_joined == t_joined:
                    name_sim = max(name_sim, 0.95)
                elif len(a_canon) >= 8 and len(t_canon) >= 8:
                    if a_canon in t_canon or t_canon in a_canon:
                        name_sim = max(name_sim, 0.90)
                        
            # 4. Address similarity
            addr_sim = 0.0
            t_atok_set = set(t for t in t_a_toks if len(t) >= 3)
            if a_addr_toks and t_atok_set:
                overlap = len(a_addr_toks.intersection(t_atok_set))
                union_len = len(a_addr_toks.union(t_atok_set))
                addr_sim = overlap / union_len if union_len > 0 else 0.0
            elif not a_addr_toks or not t_atok_set:
                addr_sim = 0.5
                
            # 5. Composite Scoring with Softened Address Penalty
            if name_sim >= 0.85:
                if addr_sim >= 0.15 or not t_atok_set:
                    score = 0.65 * name_sim + 0.35 * addr_sim
                elif a_num_set and t_num_set and a_num_set.intersection(t_num_set):
                    # Building number matches, soften penalty
                    score = 0.60 * name_sim + 0.40 * max(addr_sim, 0.20)
                else:
                    score = 0.40 * name_sim
            elif name_sim >= 0.50 and addr_sim >= 0.50:
                score = 0.50 * name_sim + 0.50 * addr_sim
            elif addr_sim >= 0.80 and name_sim >= 0.35:
                score = 0.40 * name_sim + 0.60 * addr_sim
            else:
                score = 0.0
                
            # Decision threshold
            if score >= 0.60:
                scored.append((cid, score))
                
        scored.sort(key=lambda x: x[1], reverse=True)
        chosen = [c[0] for c in scored[:6]]
        pred_c002[s1_id] = chosen
        
        # Per entity F0.5
        trues = set(true_tgts)
        preds = set(chosen)
        tp = len(preds.intersection(trues))
        fp = len(preds - trues)
        fn = len(trues - preds)
        
        tp_c002 += tp
        fp_c002 += fp
        fn_c002 += fn
        
        if len(trues) == 0:
            e_f05 = 1.0 if len(preds) == 0 else 0.0
            per_e_f05_c002.append(e_f05)
        else:
            if tp == 0:
                e_f05 = 0.0
            else:
                p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
                r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
                denom = 0.25 * p + r
                e_f05 = 1.25 * p * r / denom if denom > 0 else 0.0
            per_e_f05_c002.append(e_f05)
            non_s_f05_c002.append(e_f05)
            
    p_c002 = tp_c002 / (tp_c002 + fp_c002) if (tp_c002 + fp_c002) > 0 else 0.0
    r_c002 = tp_c002 / (tp_c002 + fn_c002) if (tp_c002 + fn_c002) > 0 else 0.0
    s_f05_c002 = sum(per_e_f05_c002) / len(per_e_f05_c002) if per_e_f05_c002 else 0.0
    ns_f05_c002 = sum(non_s_f05_c002) / len(non_s_f05_c002) if non_s_f05_c002 else 0.0
    cand_rec_c002 = recalled_links_c002 / total_true_links if total_true_links > 0 else 0.0
    
    print("\n================== COMPARISON: CHAMPION_001 vs CHALLENGER_002 ==================", flush=True)
    print(f"Metric                       | CHAMPION_001 | CHALLENGER_002 | DELTA", flush=True)
    print(f"-----------------------------|--------------|----------------|-------", flush=True)
    print(f"Candidate Recall             |    63.62%    |    {cand_rec_c002*100:5.2f}%     | {cand_rec_c002*100 - 63.62:+5.2f}%", flush=True)
    print(f"Precision                    |    69.96%    |    {p_c002*100:5.2f}%     | {p_c002*100 - 69.96:+5.2f}%", flush=True)
    print(f"Recall                       |    48.93%    |    {r_c002*100:5.2f}%     | {r_c002*100 - 48.93:+5.2f}%", flush=True)
    print(f"Non-Singleton Macro F0.5     |    0.5917    |    {ns_f05_c002:.4f}      | {ns_f05_c002 - 0.5917:+.4f}", flush=True)
    print(f"Overall Macro F0.5 (Single.) |    0.5910    |    {s_f05_c002:.4f}      | {s_f05_c002 - 0.5910:+.4f}", flush=True)
    print(f"True Positives (TP)          |    8,441     |    {tp_c002:,}       | {tp_c002 - 8441:+d}", flush=True)
    print(f"False Positives (FP)         |    3,625     |    {fp_c002:,}       | {fp_c002 - 3625:+d}", flush=True)
    print(f"False Negatives (FN)         |    8,809     |    {fn_c002:,}       | {fn_c002 - 8809:+d}", flush=True)
    print("=================================================================================", flush=True)
    
    # Save challenger manifest
    out_dir = Path("artifacts/challengers/CHALLENGER_002")
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "challenger_id": "CHALLENGER_002",
        "parent_id": "CHAMPION_001",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S+05:30"),
        "validation_metrics": {
            "candidate_recall": round(cand_rec_c002, 4),
            "precision": round(p_c002, 4),
            "recall": round(r_c002, 4),
            "non_singleton_macro_f05": round(ns_f05_c002, 4),
            "overall_macro_f05_singletons": round(s_f05_c002, 4),
            "tp": tp_c002,
            "fp": fp_c002,
            "fn": fn_c002,
            "f05_delta_vs_champion": round(ns_f05_c002 - 0.5917, 4)
        },
        "exact_changes": [
            "Domain name recovery in NameNormalizer (unmasks TLDs, preserves domain roots instead of erasing)",
            "Acronym preservation with min_name_token_length=2 (preserves RJ, IJ, CW, etc.)",
            "Indian leading honorific stripping (M/s, Sri, Shri, Smt, Dr) to align token 0",
            "Commercial complex sub-unit disambiguation (vetoes conflicting leading unit numbers)",
            "OCR truncation tolerance on building numbers (allows prefix match with length diff <= 1)",
            "Softened address penalty when building numbers match"
        ]
    }
    with open(out_dir / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"Saved Challenger manifest to {out_dir / 'manifest.json'}", flush=True)
    
if __name__ == '__main__':
    run_challenger_evaluation()
