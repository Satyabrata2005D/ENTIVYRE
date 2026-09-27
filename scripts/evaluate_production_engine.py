"""
Validation Script for Production InferenceEngine (CHALLENGER_002).
Directly tests the production InferenceEngine against the 5,000 validation split.
Measures:
- Precision
- Recall
- Non-Singleton Macro F0.5
- Overall Macro F0.5
- Candidate Recall
- TP, FP, FN
"""
import sys, os, csv, time
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, 'code/business_entity_resolution/src')
from ber.inference.engine import InferenceEngine, InferenceConfig

def evaluate_production_engine():
    print("==================================================================", flush=True)
    print("   PRODUCTION INFERENCE ENGINE VALIDATION (CHALLENGER_002)       ", flush=True)
    print("==================================================================", flush=True)
    t0 = time.time()
    
    config = InferenceConfig(
        max_candidates_per_anchor=80,
        max_matches_per_anchor=6,
        max_postings_per_key=300,
        decision_threshold=0.61,
        min_name_token_length=2,
        min_addr_token_length=2
    )
    eng = InferenceEngine(config)
    
    # 1. Load 5,000 validation ground truth
    print("[1/4] Loading 5,000 validation anchors...", flush=True)
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
        val_keys.update(eng.extract_blocking_keys(name, addr, ctry))
    print(f"  Extracted {len(val_keys):,} validation keys.", flush=True)
    
    # 2. Stream S2 & S3 into engine index
    print("[2/4] Streaming Source 2 & Source 3 into engine index...", flush=True)
    
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
                keys = eng.extract_blocking_keys(tname, taddr, tctry)
                valid_keys = [k for k in keys if k in val_keys and len(eng.index.get(k, [])) < eng.config.max_postings_per_key]
                
                if valid_keys or is_true:
                    norm_name = eng.name_normalizer.normalize(tname)
                    norm_addr = eng.address_normalizer.normalize(taddr) if taddr else None
                    norm_country = eng.country_handler.normalize(tctry).canonical or "UNKNOWN"
                    addr_toks = norm_addr.tokens if norm_addr else ()
                    num_toks = norm_addr.numeric_tokens if norm_addr else ()
                    
                    eng.target_records[tid] = (
                        norm_name.canonical,
                        addr_toks,
                        num_toks,
                        norm_country,
                    )
                    for k in valid_keys:
                        posting = eng.index.get(k)
                        if posting is None:
                            eng.index[k] = [tid]
                        elif len(posting) < eng.config.max_postings_per_key:
                            posting.append(tid)
                    count += 1
        print(f"  {src_label} streamed: {count:,} targets retained ({time.time() - t_start:.1f}s)", flush=True)
        
    stream_s('student_resource/dataset/train/train_source2.tsv', 'Source 2')
    stream_s('student_resource/dataset/train/train_source3.tsv', 'Source 3')
    print(f"  Total target records indexed: {len(eng.target_records):,}", flush=True)
    
    # 3. Run validation inference
    print("[3/4] Running validation inference across 5,000 anchors...", flush=True)
    
    total_true_links = sum(len(t) for t in gt_map.values())
    recalled_links = 0
    candidate_counts = []
    
    tp_tot = 0
    fp_tot = 0
    fn_tot = 0
    per_e_f05 = []
    non_s_f05 = []
    
    for s1_id, (s1_name, s1_addr, s1_ctry) in s1_records.items():
        true_set = set(gt_map.get(s1_id, []))
        keys = eng.extract_blocking_keys(s1_name, s1_addr, s1_ctry)
        
        seen = set()
        cands = []
        for k in keys:
            posting = eng.index.get(k)
            if posting:
                for tid in posting:
                    if tid not in seen and tid != s1_id:
                        seen.add(tid)
                        cands.append(tid)
                        if len(cands) >= eng.config.max_candidates_per_anchor:
                            break
            if len(cands) >= eng.config.max_candidates_per_anchor:
                break
                
        candidate_counts.append(len(cands))
        for tt in true_set:
            if tt in seen:
                recalled_links += 1
                
        # Normalization
        norm_anchor_name = eng.name_normalizer.normalize(s1_name)
        norm_anchor_addr = eng.address_normalizer.normalize(s1_addr) if s1_addr else None
        anchor_canon = norm_anchor_name.canonical
        anchor_toks = set(t for t in norm_anchor_name.tokens if len(t) >= eng.config.min_name_token_length)
        anchor_addr_toks = set(t for t in norm_anchor_addr.tokens if len(t) >= eng.config.min_addr_token_length) if norm_anchor_addr else set()
        anchor_num_toks = set(norm_anchor_addr.numeric_tokens) if norm_anchor_addr else set()
        anchor_country = eng.country_handler.normalize(s1_ctry).canonical or "UNKNOWN"
        
        scored_candidates = []
        for cid in cands:
            trec = eng.target_records.get(cid)
            if not trec:
                continue
            t_canon, t_addr_toks, t_num_toks, t_country = trec
            
            # Contradiction check: country mismatch
            if anchor_country != "UNKNOWN" and t_country != "UNKNOWN" and anchor_country != t_country:
                continue
                
            # Numeric check
            t_num_set = set(t_num_toks)
            has_bldg_conflict = False
            num_match = False
            if anchor_num_toks and t_num_set:
                intersect = anchor_num_toks.intersection(t_num_set)
                if intersect:
                    num_match = True
                    if len(anchor_num_toks) >= 2 and len(t_num_toks) >= 2:
                        a_num_list = list(anchor_num_toks)
                        t_num_list = list(t_num_toks)
                        if a_num_list[0] != t_num_list[0] and a_num_list[0] not in t_num_set and t_num_list[0] not in anchor_num_toks:
                            has_bldg_conflict = True
                        elif a_num_list[-1] != t_num_list[-1] and a_num_list[-1] not in t_num_set and t_num_list[-1] not in anchor_num_toks:
                            has_bldg_conflict = True
                else:
                    ocr_ok = False
                    for an in anchor_num_toks:
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
                
            # Name similarity
            name_sim = 0.0
            if anchor_canon and t_canon and anchor_canon == t_canon:
                name_sim = 1.0
            elif anchor_toks and t_canon:
                t_toks = set(t for t in t_canon.split() if len(t) >= eng.config.min_name_token_length)
                if t_toks:
                    overlap = len(anchor_toks.intersection(t_toks))
                    union_len = len(anchor_toks.union(t_toks))
                    name_sim = overlap / union_len if union_len > 0 else 0.0
                    
            # Domain unmasked root match
            if name_sim < 0.85 and anchor_canon and t_canon:
                a_concat = "".join(norm_anchor_name.tokens)
                t_concat = "".join(t_canon.split())
                if a_concat and (a_concat == t_canon or t_concat == anchor_canon or a_concat == t_concat):
                    name_sim = max(name_sim, 0.95)
                elif len(anchor_canon) >= 8 and len(t_canon) >= 8 and (anchor_canon in t_canon or t_canon in anchor_canon):
                    name_sim = max(name_sim, 0.90)
                    
            # Address similarity
            addr_sim = 0.0
            t_atok_set = set(t for t in t_addr_toks if len(t) >= eng.config.min_addr_token_length)
            if anchor_addr_toks and t_atok_set:
                overlap = len(anchor_addr_toks.intersection(t_atok_set))
                union_len = len(anchor_addr_toks.union(t_atok_set))
                addr_sim = overlap / union_len if union_len > 0 else 0.0
                
            # Scoring
            score = 0.0
            if name_sim >= 0.85:
                if addr_sim >= 0.20:
                    score = 0.65 * name_sim + 0.35 * addr_sim
                elif not t_atok_set:
                    score = 0.60 * name_sim
                else:
                    score = 0.40 * name_sim
            elif name_sim >= 0.50 and addr_sim >= 0.40:
                score = 0.50 * name_sim + 0.50 * addr_sim
            elif addr_sim >= 0.90 and num_match:
                score = 0.30 * max(name_sim, 0.50) + 0.70 * addr_sim
            elif addr_sim >= 0.75 and num_match and name_sim >= 0.25:
                score = 0.40 * name_sim + 0.60 * addr_sim
                
            if score >= eng.config.decision_threshold:
                scored_candidates.append((cid, score))
                
        scored_candidates.sort(key=lambda x: x[1], reverse=True)
        chosen = [c[0] for c in scored_candidates[:eng.config.max_matches_per_anchor]]
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
    cand_rec = recalled_links / total_true_links if total_true_links > 0 else 0.0
    
    print("\n[4/4] ================== FINAL PRODUCTION ENGINE COMPARISON ==================", flush=True)
    print(f"Metric                       | CHAMPION_001 | CHALLENGER_002 | DELTA", flush=True)
    print(f"-----------------------------|--------------|----------------|-------", flush=True)
    print(f"Candidate Recall             |    63.62%    |    {cand_rec*100:5.2f}%     | {cand_rec*100 - 63.62:+5.2f}%", flush=True)
    print(f"Precision                    |    69.96%    |    {p_val*100:5.2f}%     | {p_val*100 - 69.96:+5.2f}%", flush=True)
    print(f"Recall                       |    48.93%    |    {r_val*100:5.2f}%     | {r_val*100 - 48.93:+5.2f}%", flush=True)
    print(f"Non-Singleton Macro F0.5     |    0.5917    |    {ns_f05:.4f}      | {ns_f05 - 0.5917:+.4f}", flush=True)
    print(f"Overall Macro F0.5 (Single.) |    0.5910    |    {s_f05:.4f}      | {s_f05 - 0.5910:+.4f}", flush=True)
    print(f"True Positives (TP)          |    8,441     |    {tp_tot:,}       | {tp_tot - 8441:+d}", flush=True)
    print(f"False Positives (FP)         |    3,625     |    {fp_tot:,}         | {fp_tot - 3625:+d}", flush=True)
    print(f"False Negatives (FN)         |    8,809     |    {fn_tot:,}       | {fn_tot - 8809:+d}", flush=True)
    print(f"Execution Time               |     N/A      |    {time.time() - t0:.1f}s       | -", flush=True)
    print("=============================================================================", flush=True)

if __name__ == '__main__':
    evaluate_production_engine()
