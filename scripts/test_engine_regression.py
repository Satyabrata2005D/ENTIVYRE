#!/usr/bin/env python3
"""
Regression test suite for ENTIVYRE inference engine.
Validates the 4 mandatory requirements before production inference:
TEST 1: Shared building number with different unit/box numbers (922 Power Street, Unit 18 vs PMB 1192)
TEST 2: Exact canonical name + empty target address (score >= tau=0.56)
TEST 3: Floor/unit-prefixed address produces meaningful address blocking keys
TEST 4: Hindi/Devanagari equivalent names produce shared blocking keys
"""
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code" / "business_entity_resolution" / "src"))

from ber.inference.engine import InferenceEngine, InferenceConfig

def run_tests():
    print("=" * 70)
    print("RUNNING ENTIVYRE ENGINE REGRESSION TESTS")
    print("=" * 70)
    
    cfg = InferenceConfig()
    engine = InferenceEngine(cfg)
    all_passed = True
    
    # -------------------------------------------------------------
    # TEST 1: Building number bug (Unit 18 vs PMB 1192 on 922 Power St)
    # -------------------------------------------------------------
    s1_name = "Classic Pacific Iron Works"
    s1_addr = "922 Power Street, Unit 18, Clarksville, TN"
    s1_c = "US"
    t_name = "Classic Pacific Iron Wórks"
    t_addr = "922 POWER STREET, PMB 1192, CLARKSVILLE, TN"
    t_c = "US"
    
    s1_norm = engine.name_normalizer.normalize(s1_name)
    t_norm = engine.name_normalizer.normalize(t_name)
    s1_a = engine.address_normalizer.normalize(s1_addr)
    t_a = engine.address_normalizer.normalize(t_addr)
    
    score_1 = engine._score_pair(
        s1_norm.canonical, set(s1_norm.tokens), "".join(s1_norm.tokens),
        set(s1_a.tokens), set(s1_a.numeric_tokens), "US",
        t_norm.canonical, tuple(t_a.tokens), tuple(t_a.numeric_tokens), "US", t_a.postal_code or "", "".join(t_norm.tokens)
    )
    
    test_1_pass = (score_1 >= cfg.decision_threshold)
    print(f"TEST 1 (Shared Bldg 922, Unit 18 vs PMB 1192): Score = {score_1:.4f} (Threshold: {cfg.decision_threshold})")
    if test_1_pass:
        print("  -> PASS: Pair was NOT falsely vetoed by unit/box numbers!")
    else:
        print(f"  -> FAIL: Score {score_1:.4f} < {cfg.decision_threshold}")
        all_passed = False
        
    # -------------------------------------------------------------
    # TEST 2: Exact canonical name + empty target address
    # -------------------------------------------------------------
    s2_name = "Betts, Loredo & Rose LP"
    s2_addr = "1153 New Northrup Road, Lakehills/pipe Creek, TX"
    t2_name = "BETTS, LOREDO & ROSE LP"
    t2_addr = ""
    
    s2_norm = engine.name_normalizer.normalize(s2_name)
    t2_norm = engine.name_normalizer.normalize(t2_name)
    s2_a = engine.address_normalizer.normalize(s2_addr)
    t2_a = engine.address_normalizer.normalize(t2_addr)
    
    score_2 = engine._score_pair(
        s2_norm.canonical, set(s2_norm.tokens), "".join(s2_norm.tokens),
        set(s2_a.tokens), set(s2_a.numeric_tokens), "US",
        t2_norm.canonical, tuple(t2_a.tokens), tuple(t2_a.numeric_tokens), "US", "", "".join(t2_norm.tokens)
    )
    
    test_2_pass = (score_2 >= cfg.decision_threshold)
    print(f"\nTEST 2 (Exact Name + Empty Target Address): Score = {score_2:.4f} (Threshold: {cfg.decision_threshold})")
    if test_2_pass:
        print("  -> PASS: Score is above decision threshold!")
    else:
        print(f"  -> FAIL: Score {score_2:.4f} < {cfg.decision_threshold}")
        all_passed = False
        
    # -------------------------------------------------------------
    # TEST 3: Floor/unit-prefixed address blocking
    # -------------------------------------------------------------
    s3_addr = "2, Floor 2, Plot772, Shree Ram Bhavan, Parsi Colony 4Th Road, Mumbai"
    keys_3 = engine.extract_blocking_keys("Shree Ram Enterprises", s3_addr, "India")
    addr_keys = [k for k in keys_3 if k.startswith("ADDR_")]
    
    test_3_pass = len(addr_keys) > 0 and any("ADDR_NW:" in k for k in addr_keys)
    print(f"\nTEST 3 (Floor/unit-prefixed address blocking): Address keys = {addr_keys}")
    if test_3_pass:
        print("  -> PASS: Emitted meaningful address keys despite leading floor/unit numbers!")
    else:
        print("  -> FAIL: No valid ADDR_NW keys emitted.")
        all_passed = False
        
    # -------------------------------------------------------------
    # TEST 4: Hindi/Devanagari equivalent company names
    # -------------------------------------------------------------
    s4_name = "Hitech Estate Private Limited"
    t4_name = "हाईटेक एस्टेट प्राइवेट लिमिटेड"
    
    s4_keys = set(engine.extract_blocking_keys(s4_name, "", "India"))
    t4_keys = set(engine.extract_blocking_keys(t4_name, "", "India"))
    shared_4 = s4_keys & t4_keys
    
    s4_norm = engine.name_normalizer.normalize(s4_name)
    t4_norm = engine.name_normalizer.normalize(t4_name)
    
    test_4_pass = len(shared_4) > 0 or s4_norm.canonical == t4_norm.canonical
    print(f"\nTEST 4 (Hindi/Devanagari Transliteration):")
    print(f"  S1 Canon: '{s4_norm.canonical}' | Target Canon: '{t4_norm.canonical}'")
    print(f"  Shared Keys: {shared_4}")
    if test_4_pass:
        print("  -> PASS: Successfully shares normalized canonical representation / blocking keys!")
    else:
        print("  -> FAIL: No shared keys or canonical match.")
        all_passed = False
        
    print("\n" + "=" * 70)
    if all_passed:
        print("ALL 4 REGRESSION TESTS PASSED! Ready for production inference.")
        print("=" * 70)
        return 0
    else:
        print("REGRESSION TESTS FAILED!")
        print("=" * 70)
        return 1

if __name__ == "__main__":
    sys.exit(run_tests())
