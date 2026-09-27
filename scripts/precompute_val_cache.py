#!/usr/bin/env python3
"""
Precomputes normalized representation of anchors and unique targets for the 5,000 validation set.
Enables sub-second scoring iterations across all candidate pairs.
"""
import sys
import json
import time
import pickle
from pathlib import Path

proj_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(proj_root / "code" / "business_entity_resolution" / "src"))

from ber.normalization.name_normalizer import NameNormalizer
from ber.normalization.address_normalizer import AddressNormalizer
from ber.normalization.country_handler import CountryHandler

VAL_DIR = proj_root / "artifacts" / "challengers" / "CHALLENGER_007" / "val_cache"

def main():
    print("=" * 70)
    print("PRECOMPUTING NORMALIZED VALIDATION CACHE")
    print("=" * 70)
    t0 = time.time()

    nn = NameNormalizer()
    an = AddressNormalizer()
    ch = CountryHandler()

    # 1. Load Anchors
    print("Loading anchors...")
    with open(VAL_DIR / "anchors.json", "r", encoding="utf-8") as f:
        anchors = json.load(f)

    # 2. Collect unique target IDs needed
    print("Collecting unique needed target IDs...")
    with open(VAL_DIR / "candidates_s2.json", "r", encoding="utf-8") as f:
        c2 = json.load(f)
    with open(VAL_DIR / "candidates_s3.json", "r", encoding="utf-8") as f:
        c3 = json.load(f)
    with open(VAL_DIR / "ground_truth.json", "r", encoding="utf-8") as f:
        gt = json.load(f)

    needed_targets = set()
    for l in c2.values(): needed_targets.update(l)
    for l in c3.values(): needed_targets.update(l)
    for l in gt.values(): needed_targets.update(l)
    print(f"Total unique target IDs to normalize: {len(needed_targets):,}")

    # 3. Load target records
    print("Loading target records...")
    with open(VAL_DIR / "target_records.json", "r", encoding="utf-8") as f:
        all_tr = json.load(f)

    # 4. Normalize Anchors
    print("Normalizing anchors...")
    norm_anchors = {}
    for aid, rec in anchors.items():
        n_norm = nn.normalize(rec["name"])
        a_norm = an.normalize(rec["address"]) if rec["address"] else None
        c_norm = ch.normalize(rec["country"]).canonical or "UNKNOWN"
        norm_anchors[aid] = {
            "canon": n_norm.canonical,
            "toks": set(t for t in n_norm.tokens if len(t) >= 2),
            "concat": "".join(n_norm.tokens),
            "addr_toks": set(a_norm.tokens) if a_norm else set(),
            "num_toks": set(a_norm.numeric_tokens) if a_norm else set(),
            "postal": a_norm.postal_code if a_norm else "",
            "country": c_norm
        }

    # 5. Normalize Targets
    print("Normalizing needed targets...")
    norm_targets = {}
    count = 0
    t_norm_start = time.time()
    for tid in needed_targets:
        rec = all_tr.get(tid)
        if not rec: continue
        n_norm = nn.normalize(rec["name"])
        a_norm = an.normalize(rec["address"]) if rec["address"] else None
        c_norm = ch.normalize(rec["country"]).canonical or "UNKNOWN"
        norm_targets[tid] = (
            n_norm.canonical,
            tuple(a_norm.tokens) if a_norm else (),
            tuple(a_norm.numeric_tokens) if a_norm else (),
            c_norm,
            a_norm.postal_code if a_norm else "",
            "".join(n_norm.tokens)
        )
        count += 1
        if count % 200000 == 0:
            print(f"  Processed {count:,}/{len(needed_targets):,} ({time.time()-t_norm_start:.1f}s)...")

    print(f"Normalized {len(norm_targets):,} targets in {time.time()-t_norm_start:.1f}s")

    # 6. Save binary caches
    out_anchors = VAL_DIR / "norm_anchors.pkl"
    out_targets = VAL_DIR / "norm_targets.pkl"
    print(f"Saving {out_anchors.name} and {out_targets.name}...")
    with open(out_anchors, "wb") as f:
        pickle.dump(norm_anchors, f, protocol=pickle.HIGHEST_PROTOCOL)
    with open(out_targets, "wb") as f:
        pickle.dump(norm_targets, f, protocol=pickle.HIGHEST_PROTOCOL)

    print(f"Done in {time.time()-t0:.1f}s! Anchor cache: {out_anchors.stat().st_size/(1024*1024):.1f} MB, Target cache: {out_targets.stat().st_size/(1024*1024):.1f} MB")

if __name__ == "__main__":
    main()
