#!/usr/bin/env python3
"""
Fast Error Analysis: Only loads records relevant to 5000 sample anchors.
Categorizes errors as blocking failures vs scoring failures.
"""
import sys, os, time, random
from pathlib import Path
from collections import Counter
from difflib import SequenceMatcher

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "code" / "business_entity_resolution" / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from ber.inference.engine import InferenceEngine, InferenceConfig
from ber.normalization.name_normalizer import NameNormalizer
from ber.normalization.address_normalizer import AddressNormalizer
from ber.normalization.country_handler import CountryHandler

DATA_DIR = Path(__file__).resolve().parent.parent / "student_resource" / "dataset" / "train"

def main():
    print("=" * 80)
    print("FAST ERROR ANALYSIS — 5000 Anchor Sample")
    print("=" * 80)
    
    SAMPLE = 5000
    nn = NameNormalizer()
    an = AddressNormalizer()
    ch = CountryHandler()
    
    # 1. Load ground truth and sample
    print("[1/5] Loading ground truth...")
    gt = {}
    with open(DATA_DIR / "train_ground_truth.tsv", "r") as f:
        next(f)
        for line in f:
            p = line.rstrip("\r\n").split("\t")
            s1 = p[0].strip()
            gt[s1] = set(p[1].strip().split(",")) if len(p) > 1 and p[1].strip() else set()
    
    random.seed(42)
    # Sample anchors that have matches (we care most about FN on non-singletons)
    non_singleton_ids = [k for k, v in gt.items() if v]
    sample_ids = set(random.sample(non_singleton_ids, min(SAMPLE, len(non_singleton_ids))))
    
    # Get all needed target IDs
    needed_targets = set()
    for sid in sample_ids:
        needed_targets.update(gt[sid])
    print(f"  Sample: {len(sample_ids)} anchors, {len(needed_targets)} needed targets")
    
    # 2. Load S1 records for sample
    print("[2/5] Loading S1 records...")
    s1_records = {}
    with open(DATA_DIR / "train_source1.tsv", "r") as f:
        header = f.readline()
        cols = [c.strip().lower() for c in header.rstrip("\r\n").split("\t")]
        id_idx = cols.index("entity_id")
        name_idx = cols.index("business_name")
        addr_idx = cols.index("business_address")
        country_idx = cols.index("country")
        for line in f:
            parts = line.rstrip("\r\n").split("\t")
            if len(parts) <= max(id_idx, name_idx, country_idx):
                continue
            eid = parts[id_idx].strip()
            if eid in sample_ids:
                s1_records[eid] = (parts[name_idx], parts[addr_idx] if addr_idx < len(parts) else "", parts[country_idx])
    print(f"  Loaded {len(s1_records)} S1 records")
    
    # 3. Load target records (only needed ones + some extras for blocking test)
    # First compute blocking keys for all sample anchors
    print("[3/5] Loading target records and building index...")
    
    config = InferenceConfig()
    engine = InferenceEngine(config)
    
    # Compute anchor blocking keys
    anchor_keys_set = set()
    for s1_id in sample_ids:
        if s1_id not in s1_records:
            continue
        name, addr, country = s1_records[s1_id]
        keys = engine.extract_blocking_keys(name, addr, country)
        anchor_keys_set.update(keys)
    
    # Load S2 records
    target_raw = {}  # eid -> (name, addr, country)
    with open(DATA_DIR / "train_source2.tsv", "r") as f:
        header = f.readline()
        cols = [c.strip().lower() for c in header.rstrip("\r\n").split("\t")]
        id_idx = cols.index("entity_id")
        name_idx = cols.index("business_name")
        addr_idx = cols.index("business_address")
        country_idx = cols.index("country")
        for line in f:
            parts = line.rstrip("\r\n").split("\t")
            if len(parts) <= max(id_idx, name_idx, country_idx):
                continue
            eid = parts[id_idx].strip()
            name = parts[name_idx]
            addr = parts[addr_idx] if addr_idx < len(parts) else ""
            country = parts[country_idx]
            
            is_needed = eid in needed_targets
            keys = engine.extract_blocking_keys(name, addr, country)
            has_relevant_key = any(k in anchor_keys_set for k in keys)
            
            if is_needed or has_relevant_key:
                target_raw[eid] = (name, addr, country)
                norm_name = nn.normalize(name)
                norm_addr = an.normalize(addr) if addr else None
                norm_country = ch.normalize(country).canonical or "UNKNOWN"
                
                engine.target_records[eid] = (
                    norm_name.canonical,
                    norm_addr.tokens if norm_addr else (),
                    norm_addr.numeric_tokens if norm_addr else (),
                    norm_country,
                    norm_addr.postal_code if norm_addr else "",
                    "".join(norm_name.tokens),
                )
                
                for k in keys:
                    if k in anchor_keys_set:
                        posting = engine.index.get(k)
                        if posting is None:
                            engine.index[k] = [eid]
                        elif len(posting) < config.max_postings_per_key:
                            posting.append(eid)
    
    print(f"  S2 loaded: {len([k for k in engine.target_records if k.startswith('S2-')])} records")
    
    # Load S3 records
    with open(DATA_DIR / "train_source3.tsv", "r") as f:
        header = f.readline()
        cols = [c.strip().lower() for c in header.rstrip("\r\n").split("\t")]
        id_idx = cols.index("entity_id")
        name_idx = cols.index("business_name")
        addr_idx = cols.index("business_address")
        country_idx = cols.index("country")
        for line in f:
            parts = line.rstrip("\r\n").split("\t")
            if len(parts) <= max(id_idx, name_idx, country_idx):
                continue
            eid = parts[id_idx].strip()
            name = parts[name_idx]
            addr = parts[addr_idx] if addr_idx < len(parts) else ""
            country = parts[country_idx]
            
            is_needed = eid in needed_targets
            keys = engine.extract_blocking_keys(name, addr, country)
            has_relevant_key = any(k in anchor_keys_set for k in keys)
            
            if is_needed or has_relevant_key:
                target_raw[eid] = (name, addr, country)
                norm_name = nn.normalize(name)
                norm_addr = an.normalize(addr) if addr else None
                norm_country = ch.normalize(country).canonical or "UNKNOWN"
                
                engine.target_records[eid] = (
                    norm_name.canonical,
                    norm_addr.tokens if norm_addr else (),
                    norm_addr.numeric_tokens if norm_addr else (),
                    norm_country,
                    norm_addr.postal_code if norm_addr else "",
                    "".join(norm_name.tokens),
                )
                
                for k in keys:
                    if k in anchor_keys_set:
                        posting = engine.index.get(k)
                        if posting is None:
                            engine.index[k] = [eid]
                        elif len(posting) < config.max_postings_per_key:
                            posting.append(eid)
    
    print(f"  S3 loaded: {len([k for k in engine.target_records if k.startswith('S3-')])} records")
    print(f"  Total targets: {len(engine.target_records)}, Index keys: {len(engine.index)}")
    
    # 4. Run inference
    print("\n[4/5] Running inference...")
    predictions = {}
    blocking_miss_count = 0
    scoring_miss_count = 0
    fn_blocking = []
    fn_scoring = []
    fp_examples = []
    
    for i, s1_id in enumerate(sample_ids):
        if s1_id not in s1_records:
            continue
        name, addr, country = s1_records[s1_id]
        
        keys = engine.extract_blocking_keys(name, addr, country)
        seen = set()
        candidates = []
        for k in keys:
            posting = engine.index.get(k)
            if posting:
                for tid in posting:
                    if tid not in seen:
                        seen.add(tid)
                        candidates.append(tid)
                        if len(candidates) >= config.max_candidates_per_anchor:
                            break
            if len(candidates) >= config.max_candidates_per_anchor:
                break
        
        norm_name = nn.normalize(name)
        norm_addr = an.normalize(addr) if addr else None
        anchor_canon = norm_name.canonical
        anchor_toks = set(t for t in norm_name.tokens if len(t) >= config.min_name_token_length)
        anchor_addr_toks = set(t for t in norm_addr.tokens if len(t) >= config.min_addr_token_length) if norm_addr else set()
        anchor_num_toks = set(norm_addr.numeric_tokens) if norm_addr else set()
        anchor_country = ch.normalize(country).canonical or "UNKNOWN"
        anchor_concat = "".join(norm_name.tokens)
        
        matched = set()
        for cid in candidates:
            target_rec = engine.target_records.get(cid)
            if not target_rec:
                continue
            t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat = target_rec
            score = engine._score_pair(
                anchor_canon, anchor_toks, anchor_concat,
                anchor_addr_toks, anchor_num_toks, anchor_country,
                t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat,
            )
            if score >= config.decision_threshold:
                matched.add(cid)
        
        predictions[s1_id] = matched
        true_matches = gt.get(s1_id, set())
        
        for fn_id in true_matches - matched:
            if fn_id in seen:
                scoring_miss_count += 1
                if len(fn_scoring) < 80:
                    target_rec = engine.target_records.get(fn_id)
                    if target_rec:
                        t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat = target_rec
                        score = engine._score_pair(
                            anchor_canon, anchor_toks, anchor_concat,
                            anchor_addr_toks, anchor_num_toks, anchor_country,
                            t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat,
                        )
                        fn_raw = target_raw.get(fn_id, ("?", "?", "?"))
                        fn_scoring.append({
                            "s1_id": s1_id, "s1_name": name, "s1_addr": addr,
                            "fn_id": fn_id, "fn_name": fn_raw[0], "fn_addr": fn_raw[1],
                            "score": score, "anchor_canon": anchor_canon, "target_canon": t_canon,
                        })
            else:
                blocking_miss_count += 1
                if len(fn_blocking) < 80:
                    fn_raw = target_raw.get(fn_id)
                    if fn_raw:
                        fn_blocking.append({
                            "s1_id": s1_id, "s1_name": name, "s1_addr": addr,
                            "fn_id": fn_id, "fn_name": fn_raw[0], "fn_addr": fn_raw[1],
                            "anchor_canon": anchor_canon,
                            "target_canon": nn.normalize(fn_raw[0]).canonical,
                        })
                    else:
                        fn_blocking.append({
                            "s1_id": s1_id, "s1_name": name, "s1_addr": addr,
                            "fn_id": fn_id, "fn_name": "NOT LOADED", "fn_addr": "",
                            "anchor_canon": anchor_canon, "target_canon": "NOT LOADED",
                        })
        
        for fp_id in matched - true_matches:
            if len(fp_examples) < 80:
                fp_raw = target_raw.get(fp_id, ("?", "?", "?"))
                target_rec = engine.target_records.get(fp_id)
                if target_rec:
                    t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat = target_rec
                    score = engine._score_pair(
                        anchor_canon, anchor_toks, anchor_concat,
                        anchor_addr_toks, anchor_num_toks, anchor_country,
                        t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat,
                    )
                    fp_examples.append({
                        "s1_id": s1_id, "s1_name": name, "s1_addr": addr,
                        "fp_id": fp_id, "fp_name": fp_raw[0], "fp_addr": fp_raw[1],
                        "score": score, "anchor_canon": anchor_canon, "target_canon": t_canon,
                    })
        
        if (i + 1) % 1000 == 0:
            print(f"  Processed {i+1}/{len(sample_ids)}")
    
    # 5. Compute metrics
    print("\n[5/5] Computing metrics...")
    total_tp = total_fp = total_fn = 0
    f05_sum = 0
    n_anchors = 0
    
    for s1_id in sample_ids:
        pred = predictions.get(s1_id, set())
        true = gt.get(s1_id, set())
        tp = len(pred & true)
        fp = len(pred - true)
        fn = len(true - pred)
        total_tp += tp; total_fp += fp; total_fn += fn
        
        p = tp / (tp + fp) if tp + fp else (1.0 if not true else 0.0)
        r = tp / (tp + fn) if tp + fn else (1.0 if not pred else 0.0)
        f05 = (1.25 * p * r) / (0.25 * p + r) if p + r > 0 else 0.0
        f05_sum += f05
        n_anchors += 1
    
    macro_f05 = f05_sum / n_anchors if n_anchors else 0
    overall_p = total_tp / (total_tp + total_fp) if total_tp + total_fp else 0
    overall_r = total_tp / (total_tp + total_fn) if total_tp + total_fn else 0
    
    print(f"\n{'='*80}")
    print(f"RESULTS ON {n_anchors} NON-SINGLETON ANCHORS")
    print(f"{'='*80}")
    print(f"  Macro F0.5:  {macro_f05:.4f}")
    print(f"  Precision:   {overall_p:.4f}")
    print(f"  Recall:      {overall_r:.4f}")
    print(f"  TP: {total_tp:,}  FP: {total_fp:,}  FN: {total_fn:,}")
    print(f"  Blocking misses: {blocking_miss_count:,}")
    print(f"  Scoring misses:  {scoring_miss_count:,}")
    tot_fn = blocking_miss_count + scoring_miss_count
    if tot_fn > 0:
        print(f"  FN from blocking: {blocking_miss_count/tot_fn*100:.1f}%")
        print(f"  FN from scoring:  {scoring_miss_count/tot_fn*100:.1f}%")
    
    # Print examples
    print(f"\n{'='*80}")
    print(f"FALSE NEGATIVE — BLOCKING FAILURES (top 40)")
    print(f"{'='*80}")
    for i, ex in enumerate(fn_blocking[:40]):
        print(f"\n  [{i+1}] S1: {ex['s1_name'][:75]}")
        print(f"      S1 addr: {ex['s1_addr'][:75]}")
        print(f"      TARGET ({ex['fn_id']}): {ex['fn_name'][:75]}")
        print(f"      TARGET addr: {ex['fn_addr'][:75]}")
        print(f"      S1 canon: '{ex['anchor_canon'][:65]}'")
        print(f"      TGT canon: '{ex['target_canon'][:65]}'")
    
    print(f"\n{'='*80}")
    print(f"FALSE NEGATIVE — SCORING FAILURES (top 40)")
    print(f"{'='*80}")
    for i, ex in enumerate(fn_scoring[:40]):
        print(f"\n  [{i+1}] S1: {ex['s1_name'][:75]}")
        print(f"      S1 addr: {ex['s1_addr'][:75]}")
        print(f"      TARGET ({ex['fn_id']}): {ex['fn_name'][:75]}")
        print(f"      TARGET addr: {ex['fn_addr'][:75]}")
        print(f"      Score: {ex['score']:.4f} (threshold: {config.decision_threshold})")
        print(f"      S1 canon: '{ex['anchor_canon'][:65]}'")
        print(f"      TGT canon: '{ex['target_canon'][:65]}'")
    
    print(f"\n{'='*80}")
    print(f"FALSE POSITIVE EXAMPLES (top 40)")
    print(f"{'='*80}")
    for i, ex in enumerate(fp_examples[:40]):
        print(f"\n  [{i+1}] S1: {ex['s1_name'][:75]}")
        print(f"      S1 addr: {ex['s1_addr'][:75]}")
        print(f"      FP ({ex['fp_id']}): {ex['fp_name'][:75]}")
        print(f"      FP addr: {ex['fp_addr'][:75]}")
        print(f"      Score: {ex['score']:.4f}")
        print(f"      S1 canon: '{ex['anchor_canon'][:65]}'")
        print(f"      TGT canon: '{ex['target_canon'][:65]}'")
    
    # Pattern analysis
    print(f"\n{'='*80}")
    print(f"BLOCKING FAILURE PATTERNS")
    print(f"{'='*80}")
    patterns = Counter()
    for ex in fn_blocking:
        s1c = ex["anchor_canon"]; tc = ex["target_canon"]
        s1_toks = set(s1c.split()) if s1c else set()
        t_toks = set(tc.split()) if tc else set()
        shared = s1_toks & t_toks
        if not s1c or not tc or tc == "NOT LOADED":
            patterns["not_loaded_or_empty"] += 1
        elif s1c == tc:
            patterns["IDENTICAL_CANON_MISSED"] += 1
        elif shared and len(shared) / max(len(s1_toks), len(t_toks)) >= 0.5:
            patterns["high_overlap_missed"] += 1
        elif shared:
            patterns["partial_overlap"] += 1
        else:
            ratio = SequenceMatcher(None, s1c, tc).ratio()
            if ratio >= 0.6:
                patterns["high_char_sim"] += 1
            elif ratio >= 0.3:
                patterns["moderate_char_sim"] += 1
            else:
                patterns["completely_different"] += 1
    for p, c in patterns.most_common():
        print(f"  {p}: {c}")
    
    print(f"\n{'='*80}")
    print(f"SCORING FAILURE SCORE DISTRIBUTION")
    print(f"{'='*80}")
    bins = Counter()
    for ex in fn_scoring:
        s = ex["score"]
        if s == 0.0: bins["0.00 (vetoed)"] += 1
        elif s < 0.30: bins["0.01-0.29"] += 1
        elif s < 0.50: bins["0.30-0.49"] += 1
        elif s < config.decision_threshold: bins[f"0.50-{config.decision_threshold:.2f} (just below)"] += 1
        else: bins["above threshold??"] += 1
    for b, c in bins.most_common():
        print(f"  {b}: {c}")

if __name__ == "__main__":
    main()
