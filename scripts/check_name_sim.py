#!/usr/bin/env python3
import sys
import json
import pickle
from pathlib import Path
from difflib import SequenceMatcher

proj_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(proj_root / "code" / "business_entity_resolution" / "src"))
from ber.inference.engine import InferenceEngine, InferenceConfig, _char_similarity

VAL_DIR = proj_root / "artifacts" / "challengers" / "CHALLENGER_007" / "val_cache"

with open(VAL_DIR / "norm_anchors.pkl", "rb") as f:
    anchors = pickle.load(f)
with open(VAL_DIR / "norm_targets.pkl", "rb") as f:
    targets = pickle.load(f)
with open(VAL_DIR / "candidates_s2.json", "r", encoding="utf-8") as f:
    c2 = json.load(f)
with open(VAL_DIR / "candidates_s3.json", "r", encoding="utf-8") as f:
    c3 = json.load(f)
with open(VAL_DIR / "ground_truth.json", "r", encoding="utf-8") as f:
    ground_truth = json.load(f)

eng = InferenceEngine(InferenceConfig(enable_challenger_007=True))

under_45 = 0
over_45 = 0

for aid, a in anchors.items():
    cands = c2.get(aid, []) + c3.get(aid, [])
    for cid in cands:
        t = targets.get(cid)
        if not t: continue
        s = eng._score_pair(
            a['canon'], a['toks'], a['concat'],
            a['addr_toks'], a['num_toks'], a['country'],
            t[0], t[1], t[2], t[3], t[4], t[5], a.get('postal', '')
        )
        if s < 0.58:
            t_atok = set(t[1])
            addr_sim = 0.0
            if a['addr_toks'] and t_atok:
                union_len = len(a['addr_toks'] | t_atok)
                addr_sim = len(a['addr_toks'] & t_atok) / union_len if union_len > 0 else 0.0
            t_toks = set(t[0].split())
            name_overlap = len(a['toks'] & t_toks) if a['toks'] and t_toks else 0
            char_ratio = _char_similarity(a['concat'], t[5]) if a['concat'] and t[5] else 0.0
            if addr_sim >= 0.86 and (name_overlap >= 1 or char_ratio >= 0.70):
                # Calculate name_sim as computed in engine
                name_sim = 0.0
                if a['canon'] and t[0] and a['canon'] == t[0]:
                    name_sim = 1.0
                elif a['toks'] and t[0]:
                    if t_toks:
                        jaccard = name_overlap / len(a['toks'] | t_toks)
                        name_sim = jaccard
                        shorter = a['toks'] if len(a['toks']) <= len(t_toks) else t_toks
                        longer = t_toks if len(a['toks']) <= len(t_toks) else a['toks']
                        if len(shorter) >= 2 and shorter.issubset(longer):
                            name_sim = max(name_sim, 0.70 + 0.20 * (len(shorter)/len(longer)))
                if char_ratio >= 0.78:
                    name_sim = max(name_sim, char_ratio * 0.90)

                if name_sim < 0.45:
                    under_45 += 1
                else:
                    over_45 += 1

print(f"Triggered pairs: under 0.45 name_sim: {under_45}, >= 0.45 name_sim: {over_45}")
