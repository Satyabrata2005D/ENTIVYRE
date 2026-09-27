import sys, os, csv, re
sys.path.insert(0, '.')
from scripts.benchmark_calibrated_challenger import clean_and_normalize_name, clean_and_normalize_address, extract_blocking_keys
from collections import defaultdict

# 1. Load validation ground truth
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

index = defaultdict(list)
target_cache = {}

def stream_s(path):
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        hdr = [c.lower() for c in next(reader)]
        i_idx, n_idx, a_idx, c_idx = hdr.index('entity_id'), hdr.index('business_name'), hdr.index('business_address'), hdr.index('country')
        for row in reader:
            tid = row[i_idx].strip()
            tname = row[n_idx]
            taddr = row[a_idx] if a_idx < len(row) else ''
            tctry = row[c_idx]
            keys = extract_blocking_keys(tname, taddr, tctry)
            valid_keys = [k for k in keys if k in val_keys and len(index[k]) < 300]
            if valid_keys or (tid in all_true_targets):
                canon, toks, raw_w = clean_and_normalize_name(tname)
                c_addr, addr_toks, nums = clean_and_normalize_address(taddr)
                target_cache[tid] = (tname, taddr, tctry, canon, toks, addr_toks, nums)
                for k in valid_keys:
                    plist = index[k]
                    if len(plist) < 300:
                        plist.append(tid)

stream_s('student_resource/dataset/train/train_source2.tsv')
stream_s('student_resource/dataset/train/train_source3.tsv')

fps = []
for s1_id, (s1_name, s1_addr, s1_ctry) in s1_records.items():
    true_set = set(gt_map.get(s1_id, []))
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

    a_canon, a_toks, a_raw_w = clean_and_normalize_name(s1_name)
    a_caddr, a_addr_toks, a_nums = clean_and_normalize_address(s1_addr)
    a_tok_set = set(a_toks)
    a_atok_set = set(a_addr_toks)
    a_num_set = set(a_nums)
    a_ctry = s1_ctry.strip().upper()

    scored = []
    for cid in cands:
        trec = target_cache.get(cid)
        if not trec: continue
        t_raw_n, t_raw_a, t_raw_c, t_canon, t_toks, t_addr_toks, t_nums = trec
        t_ctry = t_raw_c.strip().upper()
        if a_ctry and t_ctry and a_ctry != "UNKNOWN" and t_ctry != "UNKNOWN" and a_ctry != t_ctry: continue

        t_tok_set = set(t_toks)
        t_atok_set = set(t_addr_toks)
        t_num_set = set(t_nums)

        has_bldg_conflict = False
        num_match = False
        if a_num_set and t_num_set:
            intersect = a_num_set.intersection(t_num_set)
            if intersect:
                num_match = True
                if len(a_nums) >= 2 and len(t_nums) >= 2:
                    if a_nums[0] != t_nums[0] and a_nums[0] not in t_num_set and t_nums[0] not in a_num_set:
                        has_bldg_conflict = True
            else:
                ocr_ok = False
                for an in a_num_set:
                    for tn in t_num_set:
                        if len(an) >= 2 and len(tn) >= 2 and (an.startswith(tn) or tn.startswith(an)) and abs(len(an) - len(tn)) <= 1:
                            ocr_ok = True
                            break
                    if ocr_ok: break
                if ocr_ok: num_match = True
                else: has_bldg_conflict = True
        if has_bldg_conflict: continue

        name_sim = 0.0
        if a_canon and t_canon and a_canon == t_canon: name_sim = 1.0
        elif a_tok_set and t_tok_set:
            overlap = len(a_tok_set.intersection(t_tok_set))
            union_len = len(a_tok_set.union(t_tok_set))
            name_sim = overlap / union_len if union_len > 0 else 0.0

        if name_sim < 0.85 and a_canon and t_canon:
            a_concat = "".join(a_toks)
            t_concat = "".join(t_toks)
            if a_concat and (a_concat == t_canon or t_concat == a_canon or a_concat == t_concat): name_sim = max(name_sim, 0.95)
            elif len(a_canon) >= 8 and len(t_canon) >= 8 and (a_canon in t_canon or t_canon in a_canon): name_sim = max(name_sim, 0.90)

        addr_sim = 0.0
        if a_atok_set and t_atok_set:
            overlap = len(a_atok_set.intersection(t_atok_set))
            union_len = len(a_atok_set.union(t_atok_set))
            addr_sim = overlap / union_len if union_len > 0 else 0.0
        elif not a_atok_set or not t_atok_set:
            addr_sim = 0.5

        score = 0.0
        if name_sim >= 0.85:
            if addr_sim >= 0.20 or not t_atok_set: score = 0.65 * name_sim + 0.35 * addr_sim
            else: score = 0.40 * name_sim
        elif name_sim >= 0.50 and addr_sim >= 0.40:
            score = 0.50 * name_sim + 0.50 * addr_sim
        elif addr_sim >= 0.70 and num_match:
            is_non_ascii = any(ord(c) > 127 for c in t_raw_n)
            is_single_word = (len(t_raw_n.split()) == 1 and len(t_raw_n) >= 5)
            if is_non_ascii or is_single_word: score = 0.30 * max(name_sim, 0.50) + 0.70 * addr_sim
            elif name_sim >= 0.30: score = 0.40 * name_sim + 0.60 * addr_sim
        elif addr_sim >= 0.85 and num_match:
            score = 0.30 * max(name_sim, 0.50) + 0.70 * addr_sim

        if score >= 0.55:
            scored.append((cid, score, name_sim, addr_sim, t_raw_n, t_raw_a))

    scored.sort(key=lambda x: x[1], reverse=True)
    for cid, sc, n_sim, a_sim, tn, ta in scored[:6]:
        if cid not in true_set:
            fps.append((s1_id, cid, s1_name, tn, s1_addr, ta, sc, n_sim, a_sim))

print(f'Total False Positives: {len(fps)}')
print('Sample 15 False Positives:')
for fp in fps[:15]:
    print(f'S1: [{fp[2]}] | Addr: [{fp[4]}]')
    print(f'FP: [{fp[3]}] | Addr: [{fp[5]}]')
    print(f'Score: {fp[6]:.3f} (NameSim: {fp[7]:.3f}, AddrSim: {fp[8]:.3f})')
    print('-'*60)
