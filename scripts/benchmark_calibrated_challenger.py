"""
Comprehensive Benchmark Script for Precision-Calibrated CHALLENGER.
Tests:
1. Multi-pass Blocking (Name + Domain Concat + Address Num-Word + Address Word-Word).
2. Domain URL Unmasking & Normalization.
3. Indian Leading Zero & Honorific Normalization.
4. Non-ASCII / Indic Script & Synthetic Name Address Corroboration.
5. Commercial Complex & Building Number Contradiction Veto.
6. Fine-grained Decision Threshold & Macro F0.5 Optimization.
"""
import sys
import os
import csv
import re
import time
from pathlib import Path
from collections import Counter, defaultdict

STOPWORDS = {
    'the', 'and', 'for', 'with', 'inc', 'llc', 'ltd', 'pvt', 'co', 'corp',
    'road', 'rd', 'street', 'st', 'avenue', 'ave', 'drive', 'dr', 'lane', 'ln',
    'way', 'blvd', 'boulevard', 'court', 'ct', 'circle', 'cir', 'floor', 'fl',
    'suite', 'ste', 'unit', 'apt', 'apartment', 'room', 'rm', 'building', 'bldg',
    'near', 'opp', 'opposite', 'behind', 'beside', 'above', 'below',
    'plot', 'no', 'number', 'door', 'house', 'flat', 'shop', 'gala', 'khasra',
    'block', 'sector', 'sec', 'phase', 'nagar', 'colony', 'marg', 'rasta',
    'city', 'town', 'village', 'dist', 'district', 'state', 'india', 'united', 'states',
    'us', 'usa', 'in', 'ny', 'ca', 'tx', 'fl', 'il', 'pa', 'oh', 'ga', 'nc', 'mi',
    'rue', 'imp', 'impasse', 'av', 'ave', 'avenue', 'boulevard', 'bd', 'all', 'allee', 'chemin'
}

URL_REGEX = re.compile(r"https?://(?:www\.)?|www\.", re.IGNORECASE)
TLD_REGEX = re.compile(r"\.(?:com|org|net|in|fr|co|io|biz|info|gov|edu)(?:/[^\s]*)?\b", re.IGNORECASE)
HONORIFIC_REGEX = re.compile(r"^(?:m\s*/?\s*s\.?|shri|sri|smt|dr\.?|er\.?|late)\s+", re.IGNORECASE)
NON_ALPHANUM_REGEX = re.compile(r"[^a-z0-9\s]")
WHITESPACE_REGEX = re.compile(r"\s+")

LEGAL_SUFFIXES = {
    "private limited", "pvt ltd", "pvt limited", "pvtltd", "limited", "ltd",
    "incorporated", "inc", "corporation", "corp", "llc", "company", "co",
    "sarl", "sa", "gmbh", "enterprises", "associates", "industries", "solutions", "services"
}

def clean_and_normalize_name(name):
    if not name:
        return "", (), ()
    text = str(name).strip().lower()
    # 1. Unmask URL
    if URL_REGEX.search(text) or TLD_REGEX.search(text):
        text = URL_REGEX.sub(" ", text)
        text = TLD_REGEX.sub(" ", text)
        text = text.replace(".", " ").replace("-", " ").replace("/", " ").replace("_", " ")
    # 2. Non-alphanumeric
    clean = NON_ALPHANUM_REGEX.sub(" ", text)
    clean = WHITESPACE_REGEX.sub(" ", clean).strip()
    # 3. Strip honorific
    clean = HONORIFIC_REGEX.sub("", clean).strip()
    # 4. Strip legal suffix
    words = clean.split()
    canon_words = []
    for w in words:
        if w not in LEGAL_SUFFIXES:
            canon_words.append(w)
    canon = " ".join(canon_words) if canon_words else clean
    toks = tuple(w for w in canon.split() if len(w) >= 2)
    return canon, toks, tuple(words)

def clean_and_normalize_address(addr):
    if not addr:
        return "", (), ()
    clean = NON_ALPHANUM_REGEX.sub(" ", str(addr).lower())
    clean = WHITESPACE_REGEX.sub(" ", clean).strip()
    raw_toks = clean.split()
    # Normalize numbers: strip leading zeros (e.g. 0684 -> 684)
    nums = tuple(t.lstrip('0') or '0' for t in raw_toks if t.isdigit() and len(t) <= 6)
    toks = tuple(t for t in raw_toks if len(t) >= 2 and t not in STOPWORDS)
    return clean, toks, nums

def extract_blocking_keys(name, addr, ctry):
    keys = []
    canon, toks, raw_words = clean_and_normalize_name(name)
    clean_addr, addr_toks, nums = clean_and_normalize_address(addr)
    
    # 1. Ultra-specific exact canonical name
    if canon:
        keys.append(f"NC:{canon}")
        concat_str = "".join(toks)
        if len(concat_str) >= 6:
            keys.append(f"NCONCAT:{concat_str[:20]}")
            
    # 2. Ultra-specific Address Number + Distinctive Word (high precision)
    if nums and addr_toks:
        p_num = nums[0]
        for w in addr_toks[:3]:
            if len(w) >= 4:
                keys.append(f"ADDR_NW:{p_num}_{w}")
                
    # 3. Sorted tokens (word-order invariance)
    if canon and len(toks) >= 2:
        keys.append(f"NS:{'_'.join(sorted(toks[:4]))}")
        keys.append(f"NP:{toks[0]}_{toks[1]}")
    elif canon and len(toks) == 1 and len(toks[0]) >= 3:
        keys.append(f"N1:{toks[0]}")
        
    # 4. Two distinctive address words
    if len(addr_toks) >= 2:
        keys.append(f"ADDR_WW:{addr_toks[0]}_{addr_toks[1]}")
        
    return keys

def run_benchmark():
    print("==================================================================", flush=True)
    print("   PRECISION-CALIBRATED CHALLENGER BENCHMARK (5,000 ANCHORS)     ", flush=True)
    print("==================================================================", flush=True)
    t0 = time.time()
    
    # 1. Load ground truth
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
                
    val_keys = set()
    for s1_id, (name, addr, ctry) in s1_records.items():
        val_keys.update(extract_blocking_keys(name, addr, ctry))
    print(f"  Extracted {len(val_keys):,} validation keys from 5,000 S1 anchors.", flush=True)
    
    # 2. Stream S2 & S3
    print("[2/5] Streaming Source 2 & Source 3 against inverted index...", flush=True)
    index = defaultdict(list)
    target_cache = {}
    
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
                keys = extract_blocking_keys(tname, taddr, tctry)
                valid_keys = [k for k in keys if k in val_keys and len(index[k]) < 300]
                
                if valid_keys or is_true:
                    canon, toks, raw_w = clean_and_normalize_name(tname)
                    c_addr, addr_toks, nums = clean_and_normalize_address(taddr)
                    target_cache[tid] = (
                        tname, taddr, tctry, canon, toks, addr_toks, nums
                    )
                    for k in valid_keys:
                        plist = index[k]
                        if len(plist) < 300:
                            plist.append(tid)
                    count += 1
        print(f"  {src_label} streamed: {count:,} targets retained ({time.time() - t_start:.1f}s)", flush=True)
        
    stream_s('student_resource/dataset/train/train_source2.tsv', 'Source 2')
    stream_s('student_resource/dataset/train/train_source3.tsv', 'Source 3')
    print(f"  Total target records cached: {len(target_cache):,}", flush=True)
    
    # 3. Grid Search Decision Thresholds
    print("[3/5] Evaluating and scoring candidate pairs across decision thresholds...", flush=True)
    
    total_true_links = sum(len(t) for t in gt_map.values())
    recalled_links = 0
    candidate_counts = []
    
    # Pre-score all pairs for fast threshold tuning
    anchor_candidate_scores = {}
    
    for s1_id, (s1_name, s1_addr, s1_ctry) in s1_records.items():
        true_tgts = set(gt_map.get(s1_id, []))
        keys = extract_blocking_keys(s1_name, s1_addr, s1_ctry)
        
        seen = set()
        cands = []
        for k in keys:
            for tid in index.get(k, []):
                if tid not in seen and tid != s1_id:
                    seen.add(tid)
                    cands.append(tid)
                    if len(cands) >= 80: break
            if len(cands) >= 80: break
            
        candidate_counts.append(len(cands))
        for tt in true_tgts:
            if tt in seen:
                recalled_links += 1
                
        # S1 Normalization
        a_canon, a_toks, a_raw_w = clean_and_normalize_name(s1_name)
        a_caddr, a_addr_toks, a_nums = clean_and_normalize_address(s1_addr)
        a_tok_set = set(a_toks)
        a_atok_set = set(a_addr_toks)
        a_num_set = set(a_nums)
        a_ctry = s1_ctry.strip().upper()
        
        scored = []
        for cid in cands:
            trec = target_cache.get(cid)
            if not trec:
                continue
            t_raw_n, t_raw_a, t_raw_c, t_canon, t_toks, t_addr_toks, t_nums = trec
            t_ctry = t_raw_c.strip().upper()
            
            # Country veto
            if a_ctry and t_ctry and a_ctry != "UNKNOWN" and t_ctry != "UNKNOWN" and a_ctry != t_ctry:
                continue
                
            t_tok_set = set(t_toks)
            t_atok_set = set(t_addr_toks)
            t_num_set = set(t_nums)
            
            # Numeric / Building Number check
            has_bldg_conflict = False
            num_match = False
            if a_num_set and t_num_set:
                intersect = a_num_set.intersection(t_num_set)
                if intersect:
                    num_match = True
                    # Disambiguate commercial complexes:
                    # If both have multi-unit numbers, check for conflicting specific unit numbers
                    if len(a_nums) >= 2 and len(t_nums) >= 2:
                        # If first numbers conflict
                        if a_nums[0] != t_nums[0] and a_nums[0] not in t_num_set and t_nums[0] not in a_num_set:
                            has_bldg_conflict = True
                        # If last numbers conflict (e.g. #68/3/181 vs #68/3/194)
                        elif a_nums[-1] != t_nums[-1] and a_nums[-1] not in t_num_set and t_nums[-1] not in a_num_set:
                            has_bldg_conflict = True
                else:
                    # Check OCR prefix truncation (e.g. 9327 vs 932)
                    ocr_ok = False
                    for an in a_num_set:
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
                continue
                
            # 1. Name Similarity
            name_sim = 0.0
            if a_canon and t_canon and a_canon == t_canon:
                name_sim = 1.0
            elif a_tok_set and t_tok_set:
                overlap = len(a_tok_set.intersection(t_tok_set))
                union_len = len(a_tok_set.union(t_tok_set))
                name_sim = overlap / union_len if union_len > 0 else 0.0
                
            # Domain unmasked root match
            if name_sim < 0.85 and a_canon and t_canon:
                a_concat = "".join(a_toks)
                t_concat = "".join(t_toks)
                if a_concat and (a_concat == t_canon or t_concat == a_canon or a_concat == t_concat):
                    name_sim = max(name_sim, 0.95)
                elif len(a_canon) >= 8 and len(t_canon) >= 8 and (a_canon in t_canon or t_canon in a_canon):
                    name_sim = max(name_sim, 0.90)
                    
            # 2. Address Similarity
            addr_sim = 0.0
            if a_atok_set and t_atok_set:
                overlap = len(a_atok_set.intersection(t_atok_set))
                union_len = len(a_atok_set.union(t_atok_set))
                addr_sim = overlap / union_len if union_len > 0 else 0.0
                
            # 3. Precision-calibrated Composite Scoring
            score = 0.0
            if name_sim >= 0.85:
                if addr_sim >= 0.20:
                    score = 0.65 * name_sim + 0.35 * addr_sim
                elif not t_atok_set:
                    # Target has no address: conservative score to avoid common-name floods
                    score = 0.60 * name_sim
                else:
                    # Name is identical but address is totally different
                    score = 0.40 * name_sim
            elif name_sim >= 0.50 and addr_sim >= 0.40:
                score = 0.50 * name_sim + 0.50 * addr_sim
            elif addr_sim >= 0.90 and num_match:
                # Ultra-high identical address match (e.g. 90%+ address token overlap)
                score = 0.30 * max(name_sim, 0.50) + 0.70 * addr_sim
            elif addr_sim >= 0.75 and num_match and name_sim >= 0.25:
                score = 0.40 * name_sim + 0.60 * addr_sim
                
            if score > 0.40:
                scored.append((cid, score))
                
        scored.sort(key=lambda x: x[1], reverse=True)
        anchor_candidate_scores[s1_id] = scored
        
    cand_rec = recalled_links / total_true_links if total_true_links > 0 else 0.0
    avg_k = sum(candidate_counts) / len(candidate_counts)
    sorted_k = sorted(candidate_counts)
    p95_k = sorted_k[int(len(sorted_k)*0.95)]
    p99_k = sorted_k[int(len(sorted_k)*0.99)]
    max_k = sorted_k[-1]
    
    print(f"\n[4/5] CANDIDATE RETRIEVAL BENCHMARK RESULTS:", flush=True)
    print(f"  Candidate Recall: {cand_rec*100:.2f}% (vs CHAMPION_001 63.62%) [DELTA: {cand_rec*100 - 63.62:+.2f}%]")
    print(f"  Candidate Counts: Avg K={avg_k:.1f}, P95 K={p95_k}, P99 K={p99_k}, Max K={max_k}", flush=True)
    
    # 4. Grid Search Thresholds
    print("\n[5/5] DECISION THRESHOLD GRID SEARCH:", flush=True)
    print(f"{'Threshold':<10} | {'Precision':<10} | {'Recall':<10} | {'Non-Sing F0.5':<14} | {'Overall F0.5':<14} | {'TP':<7} | {'FP':<7} | {'FN':<7}")
    print("-" * 85)
    
    best_thresh = None
    best_ns_f05 = -1.0
    best_metrics = {}
    
    for tau_int in range(55, 75, 2):
        tau = tau_int / 100.0
        
        tp_tot = 0
        fp_tot = 0
        fn_tot = 0
        per_e_f05 = []
        non_s_f05 = []
        
        for s1_id, tgts in gt_map.items():
            true_set = set(tgts)
            scored = anchor_candidate_scores[s1_id]
            chosen = [cid for cid, sc in scored if sc >= tau][:6]
            pred_set = set(chosen)
            
            tp = len(pred_set.intersection(true_set))
            fp = len(pred_set - true_set)
            fn = len(true_set - pred_set)
            
            tp_tot += tp
            fp_tot += fp
            fn_tot += fn
            
            if len(true_set) == 0:
                e_f05 = 1.0 if len(pred_set) == 0 else 0.0
                per_e_f05.append(e_f05)
            else:
                if tp == 0:
                    e_f05 = 0.0
                else:
                    p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
                    r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
                    denom = 0.25 * p + r
                    e_f05 = 1.25 * p * r / denom if denom > 0 else 0.0
                per_e_f05.append(e_f05)
                non_s_f05.append(e_f05)
                
        p_val = tp_tot / (tp_tot + fp_tot) if (tp_tot + fp_tot) > 0 else 0.0
        r_val = tp_tot / (tp_tot + fn_tot) if (tp_tot + fn_tot) > 0 else 0.0
        s_f05 = sum(per_e_f05) / len(per_e_f05) if per_e_f05 else 0.0
        ns_f05 = sum(non_s_f05) / len(non_s_f05) if non_s_f05 else 0.0
        
        star = " *" if ns_f05 > best_ns_f05 else ""
        if ns_f05 > best_ns_f05:
            best_ns_f05 = ns_f05
            best_thresh = tau
            best_metrics = {
                "threshold": tau,
                "precision": p_val,
                "recall": r_val,
                "non_singleton_macro_f05": ns_f05,
                "overall_macro_f05": s_f05,
                "tp": tp_tot,
                "fp": fp_tot,
                "fn": fn_tot,
                "cand_rec": cand_rec
            }
            
        print(f"{tau:<10.2f} | {p_val*100:<9.2f}% | {r_val*100:<9.2f}% | {ns_f05:<14.4f} | {s_f05:<14.4f} | {tp_tot:<7,d} | {fp_tot:<7,d} | {fn_tot:<7,d}{star}")
        
    print("=" * 85)
    print(f"\nOPTIMAL CALIBRATED THRESHOLD: tau = {best_thresh:.2f}")
    print(f"  Precision: {best_metrics['precision']*100:.2f}% (vs CHAMPION_001 69.96%)")
    print(f"  Recall:    {best_metrics['recall']*100:.2f}% (vs CHAMPION_001 48.93%)")
    print(f"  Macro F0.5: {best_metrics['non_singleton_macro_f05']:.4f} (vs CHAMPION_001 0.5917)")
    print(f"  NET F0.5 GAIN: {best_metrics['non_singleton_macro_f05'] - 0.5917:+.4f}!")
    print(f"  Total Runtime: {time.time() - t0:.1f}s")
    
if __name__ == '__main__':
    run_benchmark()
