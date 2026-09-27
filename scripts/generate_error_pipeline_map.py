"""
Generate artifacts/forensics/error_pipeline_map.csv for Phase 2.
Maps every true match in the 5,000 validation split to its exact pipeline failure stage:
- RETRIEVAL_MISS
- BUILDING_NUM_VETO
- COUNTRY_VETO
- BELOW_THRESHOLD
- MATCH_CAP_EXCLUDED
- SUCCESS (TP)
"""
import sys, csv, time
from collections import defaultdict, Counter
from pathlib import Path

sys.path.insert(0, 'code/business_entity_resolution/src')
from ber.inference.engine import InferenceEngine, InferenceConfig

def generate_error_pipeline_map():
    print("=== GENERATING ERROR PIPELINE MAP ===", flush=True)
    t0 = time.time()
    
    eng = InferenceEngine()
    
    # 1. Load 5,000 validation anchors & ground truth
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
        keys = eng.extract_blocking_keys(name, addr, ctry)
        val_keys.update(keys)
        
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
                keys = eng.extract_blocking_keys(tname, taddr, tctry)
                valid_keys = [k for k in keys if k in val_keys and len(index[k]) < eng.config.max_postings_per_key]
                
                if valid_keys or is_true:
                    norm_name = eng.name_normalizer.normalize(tname)
                    norm_addr = eng.address_normalizer.normalize(taddr) if taddr else None
                    norm_ctry = eng.country_handler.normalize(tctry).canonical or "UNKNOWN"
                    
                    target_cache[tid] = (
                        tname,
                        taddr,
                        tctry,
                        norm_name.canonical,
                        norm_addr.tokens if norm_addr else (),
                        norm_addr.numeric_tokens if norm_addr else (),
                        norm_ctry,
                    )
                    
                    for k in valid_keys:
                        plist = index[k]
                        if len(plist) < eng.config.max_postings_per_key:
                            plist.append(tid)
                    count += 1
        print(f"  {src_label} streamed: {count:,} targets retained ({time.time() - t_start:.1f}s)", flush=True)
        
    stream_s('student_resource/dataset/train/train_source2.tsv', 'Source 2')
    stream_s('student_resource/dataset/train/train_source3.tsv', 'Source 3')
    
    # Trace pipeline failure stages
    pipeline_records = []
    stage_counts = Counter()
    
    for s1_id, (s1_name, s1_addr, s1_ctry) in s1_records.items():
        true_tgts = gt_map.get(s1_id, [])
        keys = eng.extract_blocking_keys(s1_name, s1_addr, s1_ctry)
        seen_cands = set()
        cands_list = []
        for k in keys:
            for tid in index.get(k, []):
                if tid not in seen_cands and tid != s1_id:
                    seen_cands.add(tid)
                    cands_list.append(tid)
                    if len(cands_list) >= eng.config.max_candidates_per_anchor:
                        break
            if len(cands_list) >= eng.config.max_candidates_per_anchor:
                break
                
        norm_anchor_name = eng.name_normalizer.normalize(s1_name)
        norm_anchor_addr = eng.address_normalizer.normalize(s1_addr) if s1_addr else None
        anchor_canon = norm_anchor_name.canonical
        anchor_toks = set(t for t in norm_anchor_name.tokens if len(t) >= eng.config.min_name_token_length)
        anchor_addr_toks = set(t for t in norm_anchor_addr.tokens if len(t) >= eng.config.min_addr_token_length) if norm_anchor_addr else set()
        anchor_num_toks = set(norm_anchor_addr.numeric_tokens) if norm_anchor_addr else set()
        anchor_country = eng.country_handler.normalize(s1_ctry).canonical or "UNKNOWN"
        
        # Score all candidates
        candidate_scores = {}
        candidate_failure = {}
        
        for cid in cands_list:
            trec = target_cache.get(cid)
            if not trec:
                continue
            t_raw_name, t_raw_addr, t_raw_ctry, t_canon, t_addr_toks, t_num_toks, t_country = trec
            
            # Contradictions
            if anchor_country != "UNKNOWN" and t_country != "UNKNOWN" and anchor_country != t_country:
                candidate_failure[cid] = "COUNTRY_VETO"
                candidate_scores[cid] = 0.0
                continue
                
            t_num_set = set(t_num_toks)
            if anchor_num_toks and t_num_set and not anchor_num_toks.intersection(t_num_set):
                candidate_failure[cid] = "BUILDING_NUM_VETO"
                candidate_scores[cid] = 0.0
                continue
                
            name_sim = 0.0
            if anchor_canon and t_canon and anchor_canon == t_canon:
                name_sim = 1.0
            elif anchor_toks and t_canon:
                t_toks = set(t for t in t_canon.split() if len(t) >= eng.config.min_name_token_length)
                if t_toks:
                    overlap = len(anchor_toks.intersection(t_toks))
                    union_len = len(anchor_toks.union(t_toks))
                    name_sim = overlap / union_len if union_len > 0 else 0.0
                    
            addr_sim = 0.0
            t_atok_set = set(t for t in t_addr_toks if len(t) >= eng.config.min_addr_token_length)
            if anchor_addr_toks and t_atok_set:
                overlap = len(anchor_addr_toks.intersection(t_atok_set))
                union_len = len(anchor_addr_toks.union(t_atok_set))
                addr_sim = overlap / union_len if union_len > 0 else 0.0
            elif not anchor_addr_toks or not t_atok_set:
                addr_sim = 0.5
                
            if name_sim >= 0.85:
                if addr_sim >= 0.20 or not t_atok_set:
                    score = 0.65 * name_sim + 0.35 * addr_sim
                else:
                    score = 0.40 * name_sim
            elif name_sim >= 0.50 and addr_sim >= 0.50:
                score = 0.50 * name_sim + 0.50 * addr_sim
            elif addr_sim >= 0.80 and name_sim >= 0.35:
                score = 0.40 * name_sim + 0.60 * addr_sim
            else:
                score = 0.0
                
            candidate_scores[cid] = score
            if score < eng.config.decision_threshold:
                candidate_failure[cid] = "BELOW_THRESHOLD"
                
        # Top matches
        accepted_cands = [(cid, sc) for cid, sc in candidate_scores.items() if sc >= eng.config.decision_threshold and cid not in candidate_failure]
        accepted_cands.sort(key=lambda x: x[1], reverse=True)
        top_k_ids = set(c[0] for c in accepted_cands[:eng.config.max_matches_per_anchor])
        
        for tt in true_tgts:
            if tt not in seen_cands:
                cand_gen = False
                m_score = 0.0
                f_decision = "REJECTED"
                f_stage = "RETRIEVAL_MISS"
            else:
                cand_gen = True
                m_score = candidate_scores.get(tt, 0.0)
                if tt in top_k_ids:
                    f_decision = "MATCHED"
                    f_stage = "SUCCESS"
                else:
                    f_decision = "REJECTED"
                    if tt in candidate_failure:
                        f_stage = candidate_failure[tt]
                    elif m_score >= eng.config.decision_threshold:
                        f_stage = "MATCH_CAP_EXCLUDED"
                    else:
                        f_stage = "BELOW_THRESHOLD"
                        
            stage_counts[f_stage] += 1
            pipeline_records.append({
                "s1_id": s1_id,
                "true_match_id": tt,
                "candidate_generated": cand_gen,
                "model_score": f"{m_score:.4f}",
                "threshold": f"{eng.config.decision_threshold:.2f}",
                "final_decision": f_decision,
                "failure_stage": f_stage
            })
            
    out_dir = Path("artifacts/forensics")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / "error_pipeline_map.csv"
    with open(out_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(pipeline_records[0].keys()))
        writer.writeheader()
        for r in pipeline_records:
            writer.writerow(r)
            
    print(f"\nGenerated {out_csv} with {len(pipeline_records):,} records!", flush=True)
    print("Failure Stage Distribution:")
    for stage, cnt in stage_counts.most_common():
        pct = cnt / len(pipeline_records) * 100
        print(f"  {stage:<20}: {cnt:6,d} ({pct:5.2f}%)")

if __name__ == '__main__':
    generate_error_pipeline_map()
