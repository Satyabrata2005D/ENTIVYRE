#!/usr/bin/env python3
"""
Streaming Invariant & Structural Validator for Amazon ML Challenge 2026.
Validates 100% of rows line-by-line with bounded memory:
1. Exact row count: 1,732,544 S1 rows in matching_results.tsv and candidate_pairs.tsv
2. Exact header alignment
3. S1 ID alignment between matching and candidate files
4. Proper prefix validation (S2- and S3- only)
5. Zero intra-row duplicate IDs
6. Strict candidate subset invariant: matched_entity_ids <= candidate_entity_ids
"""
import sys
import time

def fast_validate(matching_path="output/matching_results.tsv", candidate_path="output/candidate_pairs.tsv"):
    t0 = time.time()
    print("==============================================================")
    print("FAST STREAMING INVARIANT VALIDATOR")
    print("==============================================================")
    print(f"Matching file:  {matching_path}")
    print(f"Candidate file: {candidate_path}")
    
    with open(matching_path, "r", encoding="utf-8") as f_m, open(candidate_path, "r", encoding="utf-8") as f_c:
        h_m = f_m.readline().rstrip("\r\n")
        h_c = f_c.readline().rstrip("\r\n")
        
        assert h_m == "source1_entity_id\tmatched_entity_ids", f"Invalid matching header: {h_m}"
        assert h_c == "source1_entity_id\tcandidate_entity_ids", f"Invalid candidate header: {h_c}"
        
        row_count = 0
        singleton_count = 0
        total_matches = 0
        total_cands = 0
        max_matches = 0
        
        subset_violations = 0
        intra_dupe_violations = 0
        prefix_violations = 0
        id_mismatch_violations = 0
        
        for line_m, line_c in zip(f_m, f_c):
            row_count += 1
            parts_m = line_m.rstrip("\r\n").split("\t")
            parts_c = line_c.rstrip("\r\n").split("\t")
            
            s1_m = parts_m[0]
            s1_c = parts_c[0]
            
            if s1_m != s1_c:
                id_mismatch_violations += 1
                if id_mismatch_violations <= 5:
                    print(f"ERROR: ID mismatch at row {row_count}: {s1_m} != {s1_c}")
            
            m_list = [x.strip() for x in parts_m[1].split(",") if x.strip()] if len(parts_m) > 1 and parts_m[1].strip() else []
            c_list = [x.strip() for x in parts_c[1].split(",") if x.strip()] if len(parts_c) > 1 and parts_c[1].strip() else []
            
            if len(m_list) > max_matches:
                max_matches = len(m_list)
                
            if not m_list:
                singleton_count += 1
            else:
                total_matches += len(m_list)
                
            total_cands += len(c_list)
            
            # Check duplicates
            if len(m_list) != len(set(m_list)) or len(c_list) != len(set(c_list)):
                intra_dupe_violations += 1
                
            # Check prefixes
            for mid in m_list:
                if not mid.startswith(("S2-", "S3-")):
                    prefix_violations += 1
            for cid in c_list:
                if not cid.startswith(("S2-", "S3-")):
                    prefix_violations += 1
                    
            # Check subset invariant: m_list <= c_list
            c_set = set(c_list)
            for mid in m_list:
                if mid not in c_set:
                    subset_violations += 1
                    if subset_violations <= 5:
                        print(f"ERROR: Subset violation at row {row_count} ({s1_m}): {mid} not in candidates!")
                        
            if row_count % 250000 == 0:
                print(f"  Processed {row_count:,} / 1,732,544 rows... ({time.time() - t0:.1f}s)")
                
        # Check trailing lines
        assert f_m.readline() == "", "Extra lines in matching file!"
        assert f_c.readline() == "", "Extra lines in candidate file!"
        
    print("--------------------------------------------------------------")
    print(f"Total Rows Verified:          {row_count:,}")
    print(f"Singletons (Empty matches):   {singleton_count:,} ({singleton_count/row_count:.2%})")
    print(f"Total Matches:                {total_matches:,} (avg {total_matches/row_count:.2f}/anchor, max {max_matches})")
    print(f"Total Candidates:             {total_cands:,} (avg {total_cands/row_count:.2f}/anchor)")
    print(f"ID Mismatch Violations:       {id_mismatch_violations}")
    print(f"Prefix Violations:            {prefix_violations}")
    print(f"Intra-row Duplicates:         {intra_dupe_violations}")
    print(f"Candidate Subset Violations:  {subset_violations}")
    print(f"Elapsed Time:                 {time.time() - t0:.2f}s")
    print("==============================================================")
    
    assert row_count == 1732544, f"Expected exactly 1,732,544 rows, found {row_count}"
    assert id_mismatch_violations == 0, "Found ID mismatch violations!"
    assert prefix_violations == 0, "Found prefix violations!"
    assert intra_dupe_violations == 0, "Found duplicate ID violations!"
    assert subset_violations == 0, "Found candidate subset violations!"
    print("PASS — 100% of submission invariants strictly satisfied!")

if __name__ == "__main__":
    m_p = sys.argv[1] if len(sys.argv) > 1 else "output/matching_results.tsv"
    c_p = sys.argv[2] if len(sys.argv) > 2 else "output/candidate_pairs.tsv"
    fast_validate(m_p, c_p)
