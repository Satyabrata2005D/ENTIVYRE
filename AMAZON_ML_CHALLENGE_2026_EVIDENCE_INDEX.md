# Forensic Technical Evidence Index
## Amazon ML Challenge 2026 — ENTIVYRE System Codebase
**Team Name:** UNPAID ENGINEERS  
**Index Specification:** Exhaustive grounding ledger linking all technical assertions to local project source files, line ranges, cryptographic hashes, data records, and execution outputs.  
**Auditor:** Senior ML Competition Reviewer & Software Auditor  
**Audit Date:** 2026-10-01  

---

## 1. Master Evidence Registry

### [E01] Cryptographic Dataset Manifest & Record Counts
- **File Path:** [`artifacts/dataset_manifest.json`](file:///Users/satyabratadas/Documents/ENTIVYRE/artifacts/dataset_manifest.json#L1-L200)
- **Line Numbers:** 1–200
- **Verifiable Claim:** Total challenge universe consists of 7 raw TSV files totaling 2.35 GB ($2,520,573,701$ bytes) and $26,435,994$ records.
- **Specific Evidence:**
  - `train_source1.tsv`: 2,206,821 data rows | MD5: `1a0c98e43dad1babed3c99bca2c7b5bd` | SHA-256: `591af0e1dfeb65cab71ea6ee8cb69df00f92d6ba6fa79e05746c938775d14973`
  - `train_source2.tsv`: 5,034,616 data rows | MD5: `a7bddba33ead4a85e6c088ad3b377fc2` | SHA-256: `6336c1a055eec79cf8a6d99fdc8d32a2e4d9dc2662e00963cb35d66b89ed09ed`
  - `train_source3.tsv`: 5,285,603 data rows | MD5: `5df07bf109f55a292bdfaa8c983cfa20` | SHA-256: `67da22f5151898ff3006febd836c1a159e97ae95efa7257a5aff4fda685e58e9`
  - `train_ground_truth.tsv`: 2,206,821 data rows | MD5: `3643443570b2c881c425d69c2d46e95d` | SHA-256: `70bc1d8a16c667e0155c2105d0ab2ebe41d7e7a85d8a529e3ca81c6c3a5af037`
  - `test_source1.tsv`: 1,732,544 data rows | MD5: `51a155b8c84bfefcf049e983f06c3cf4` | SHA-256: `3d4a32c54c2ca9c53fd7c2be105bf26f708f94c4d2f88eb370972a195665c2f5`
  - `test_source2.tsv`: 4,887,273 data rows | MD5: `ff8aba5701829a622ac05b2765c4eb5b` | SHA-256: `79d906c7497af2ace70aa277f6e334a652094909de99bd6c57b53420b6a7b2dd`
  - `test_source3.tsv`: 5,082,316 data rows | MD5: `5f48d48594dea3ea1455549eb5233ad8` | SHA-256: `850942b11d2a4343486ed0834e28bce9f3b385f3fd497fd60ccf4ea3b8bda035`

---

### [E02] Inverted Index Blocking Keys
- **File Path:** [`code/business_entity_resolution/src/ber/inference/engine.py`](file:///Users/satyabratadas/Documents/ENTIVYRE/code/business_entity_resolution/src/ber/inference/engine.py#L110-L173)
- **Function:** `InferenceEngine.extract_blocking_keys()`
- **Line Numbers:** 110–173
- **Verifiable Claim:** Candidate generation constructs up to 7 distinct multi-key inverted index representations per entity.
- **Specific Evidence:**
  - `NC:<canonical>` (Line 127)
  - `NCONCAT:<concat_first_20>` (Line 130)
  - `ADDR_NW:<p_num>_<word>` (Line 137)
  - `NS:<sorted_tokens>` (Line 143)
  - `NP:<tok0>_<tok1>` (Line 144)
  - `ADDR_WW:<tok0>_<tok1>` (Line 152)
  - `ADDR_N1:<p_num>_<n_first[:4]>` (Line 161)
  - `PIN_N1:<postal>_<n_first[:4]>` (Line 167)
  - `N1L:<tok>` (Line 171)

---

### [E03] Hard Contradiction Guards
- **File Path:** [`code/business_entity_resolution/src/ber/inference/engine.py`](file:///Users/satyabratadas/Documents/ENTIVYRE/code/business_entity_resolution/src/ber/inference/engine.py#L276-L312)
- **Function:** `InferenceEngine._score_pair()`
- **Line Numbers:** 276–312
- **Verifiable Claim:** Pairs with sovereign country conflicts or disjoint street building numbers are strictly vetoed with a score of 0.0.
- **Specific Evidence:**
  - Country contradiction veto: Lines 277–278:
    ```python
    if anchor_country != "UNKNOWN" and t_country != "UNKNOWN" and anchor_country != t_country:
        return 0.0
    ```
  - Building number contradiction veto: Lines 284–311:
    Verifies that if both addresses have numeric tokens and share zero intersection, they are checked for OCR single-digit prefix truncation; if not matched, `has_bldg_conflict = True` and line 311 returns `0.0`.

---

### [E04] Multi-Tenant Center / Mall Veto
- **File Path:** [`code/business_entity_resolution/src/ber/inference/engine.py`](file:///Users/satyabratadas/Documents/ENTIVYRE/code/business_entity_resolution/src/ber/inference/engine.py#L362-L372)
- **Function:** `InferenceEngine._score_pair()`
- **Line Numbers:** 362–372
- **Verifiable Claim:** Distinct businesses sharing an address (shopping malls, commercial plazas) are prevented from merging when name similarity is below 0.45.
- **Specific Evidence:**
  - Line 364: `if name_sim < 0.45: return 0.0` (with exception only for verified name overlap and address overlap $\ge 0.82$).

---

### [E05] Universal Brahmi Indic Script Alignment
- **File Path:** [`code/business_entity_resolution/src/ber/normalization/transliteration.py`](file:///Users/satyabratadas/Documents/ENTIVYRE/code/business_entity_resolution/src/ber/normalization/transliteration.py#L85-L100)
- **Function:** `map_indic_to_devanagari()`
- **Line Numbers:** 85–100
- **Verifiable Claim:** Maps all major Brahmi-derived Indic scripts (Tamil, Telugu, Bengali, Gujarati, Kannada, Malayalam) to Devanagari using 128-byte block modulo offset alignment.
- **Specific Evidence:**
  - Line 95: `chr(0x0900 + (code % 0x80))` maps any character in range `[0x0980, 0x0D7F]` to its Devanagari phonetic equivalent.

---

### [E06] Hindi Commercial Lexicon
- **File Path:** [`code/business_entity_resolution/src/ber/normalization/transliteration.py`](file:///Users/satyabratadas/Documents/ENTIVYRE/code/business_entity_resolution/src/ber/normalization/transliteration.py#L11-L84)
- **Variable:** `HINDI_BUSINESS_TERMS`
- **Line Numbers:** 11–84
- **Verifiable Claim:** Translates over 80 frequent commercial Hindi loanwords into English Latin tokens.
- **Specific Evidence:**
  - Contains exact mappings for `एंटरप्राइजेज`, `उद्योग`, `प्राइवेट`, `लिमिटेड`, `ट्रेडर्स`, `स्टोर्स`, `सर्विसेज`, `महालक्ष्मी`, `होटल`, `लॉजिस्टिक्स`, `टेक्नोलॉजीज`, `कंस्ट्रक्शन`, `डेवलपर्स`.

---

### [E07] Legal Suffix Normalization Map
- **File Path:** [`code/business_entity_resolution/src/ber/normalization/name_normalizer.py`](file:///Users/satyabratadas/Documents/ENTIVYRE/code/business_entity_resolution/src/ber/normalization/name_normalizer.py#L30-L76)
- **Variable:** `LEGAL_SUFFIX_MAP`
- **Line Numbers:** 30–76
- **Verifiable Claim:** Standardizes 38 corporate entity types across US, India, and France into canonical forms.
- **Specific Evidence:**
  - Mappings include `"private limited"` $\to$ `"pvt ltd"`, `"limited"` $\to$ `"ltd"`, `"incorporated"` $\to$ `"inc"`, `"corporation"` $\to$ `"corp"`, `"limited liability company"` $\to$ `"llc"`, `"sarl"` $\to$ `"sarl"`, `"gmbh"` $\to$ `"gmbh"`, `"proprietorship"` $\to$ `"prop"`.

---

### [E08] Address Normalization & Numeric Evidence
- **File Path:** [`code/business_entity_resolution/src/ber/normalization/address_normalizer.py`](file:///Users/satyabratadas/Documents/ENTIVYRE/code/business_entity_resolution/src/ber/normalization/address_normalizer.py#L30-L72, #L176-L206)
- **Functions:** `AddressNormalizer.normalize()`, `compare_numeric_evidence()`
- **Line Numbers:** 30–72, 176–206
- **Verifiable Claim:** Standardizes road abbreviations across US, India, and France, extracts postal codes and building numbers, and isolates numeric contradictions.
- **Specific Evidence:**
  - Road abbreviations in `ADDRESS_KEYWORD_MAP` (Lines 31–72).
  - Numeric contradiction extraction in `compare_numeric_evidence` (Lines 176–206).

---

### [E09] Open-Set Sovereign Country Handler
- **File Path:** [`code/business_entity_resolution/src/ber/normalization/country_handler.py`](file:///Users/satyabratadas/Documents/ENTIVYRE/code/business_entity_resolution/src/ber/normalization/country_handler.py#L24-L71, #L150-L166)
- **Class:** `CountryHandler`
- **Line Numbers:** 24–71, 150–166
- **Verifiable Claim:** Handles open-set country representations without crashing on unseen countries like France.
- **Specific Evidence:**
  - `COUNTRY_ALIAS_MAP` maps aliases for US, India, France, UK, Canada, Germany, Australia, Singapore, Japan (Lines 24–71).
  - Line 157: `canonical = self.alias_map.get(clean_text, clean_text.upper())` provides an open-set string fallback.

---

### [E10] 33-Dimensional Feature Registry
- **File Path:** [`code/business_entity_resolution/src/ber/features/registry.py`](file:///Users/satyabratadas/Documents/ENTIVYRE/code/business_entity_resolution/src/ber/features/registry.py#L144-L441)
- **Function:** `build_default_feature_registry()`
- **Line Numbers:** 144–441
- **Verifiable Claim:** Declares and validates exactly 33 typed features across 5 groups with missing-value contracts.
- **Specific Evidence:**
  - 10 Name features (Lines 152–233)
  - 11 Address features (Lines 236–325)
  - 4 Country features (Lines 328–361)
  - 4 Cross-Field features (Lines 364–397)
  - 4 Retrieval features (Lines 400–433)

---

### [E11] Gradient Boosted Decision Stumps
- **File Path:** [`code/business_entity_resolution/src/ber/models/tree_ensemble.py`](file:///Users/satyabratadas/Documents/ENTIVYRE/code/business_entity_resolution/src/ber/models/tree_ensemble.py#L56-L241)
- **Class:** `GradientBoostedDecisionStumps`
- **Line Numbers:** 56–241
- **Verifiable Claim:** Implements a pure-Python gradient boosting ensemble optimizing log-loss with second-order Newton-Raphson leaf updates.
- **Specific Evidence:**
  - Line 126: Newton-Raphson regularized leaf output calculation: `left_out = g_left / (h_left + self.l2_reg)`.
  - Line 179: Binary cross-entropy log-loss computation.

---

### [E12] Official Macro F0.5 Metric Contract
- **File Path:** [`code/business_entity_resolution/src/entivyre/contracts/metrics.py`](file:///Users/satyabratadas/Documents/ENTIVYRE/code/business_entity_resolution/src/entivyre/contracts/metrics.py#L64-L130)
- **Function:** `compute_entity_f05()`
- **Line Numbers:** 64–130
- **Verifiable Claim:** Implements the official Macro-Averaged $F_{0.5}$ metric with exact singleton credit and penalty mechanics.
- **Specific Evidence:**
  - Lines 89–95: Singletons with 0 predicted matches receive $F_{0.5} = 1.0$; singletons with $\ge 1$ match receive $0.0$.
  - Line 82: `F_0.5 = (1.25 * precision * recall) / (0.25 * precision + recall)`.

---

### [E13] Official Validator Verification
- **File Path:** [`student_resource/utils/validate_submission.py`](file:///Users/satyabratadas/Documents/ENTIVYRE/student_resource/utils/validate_submission.py#L1-L353)
- **Execution Run:** Task-161 (2026-10-01T12:56:25Z)
- **Verifiable Claim:** Both generated submission files pass 100% of formatting, entity count, and candidate subset rules.
- **Specific Evidence:**
  - `matching_results.tsv`: 1,732,544 rows ($190,885$ empty, $1,541,659$ non-empty).
  - `candidate_pairs.tsv`: 1,732,544 rows ($179$ empty, $1,732,365$ non-empty).
  - Validator Output: `PASS — no blocking issues found. Safe to submit.`

---

### [E14] MD5 Hash Identity of Final Matching Output
- **File Paths:**
  - [`output/matching_results.tsv`](file:///Users/satyabratadas/Documents/ENTIVYRE/output/matching_results.tsv)
  - [`artifacts/challengers/CHALLENGER_007/full_test/matching_results.tsv`](file:///Users/satyabratadas/Documents/ENTIVYRE/artifacts/challengers/CHALLENGER_007/full_test/matching_results.tsv)
  - [`submission/matching_results.tsv`](file:///Users/satyabratadas/Documents/ENTIVYRE/submission/matching_results.tsv)
- **Verifiable Claim:** The file in `output/matching_results.tsv` is identical to the challenger run and submission staging directory.
- **Specific Evidence:**
  - MD5 hash across all three locations: `8f72cff9c104db5a072bc4e2bb19925b`.

---

### [E15] Public Leaderboard Score Record
- **File Path:** [`artifacts/forensics/score_record_table.md`](file:///Users/satyabratadas/Documents/ENTIVYRE/artifacts/forensics/score_record_table.md#L8-L17)
- **Table:** Historical Submissions & Challenger Benchmark Registry
- **Line Numbers:** 8–17
- **Verifiable Claim:** The team achieved a public leaderboard score of 0.7840 with CHALLENGER_005.
- **Specific Evidence:**
  - `SUBMISSION_000`: 0.315 LB
  - `CHAMPION_001`: 0.610 LB
  - `CHALLENGER_002`: ~0.720 LB
  - `CHALLENGER_004`: ~0.769 LB
  - `CHALLENGER_005`: 0.7840 LB

---

### [E16] 10 Structural Failure Axes Decomposition
- **File Path:** [`public_local_gap_0784.md`](file:///Users/satyabratadas/Documents/ENTIVYRE/public_local_gap_0784.md#L1-L116)
- **Line Numbers:** 1–116
- **Verifiable Claim:** Explains the structural gap between local validation (0.8573) and public leaderboard (0.7840).
- **Specific Evidence:**
  - Documents the 14.98% France shift (Line 40), Indic script expansion (Line 46), singleton rate divergence (Line 50), candidate recall upper bound of 66.75% (Line 60), and commercial chain repetition (Line 68).

---

### [E17] Air-Gapped Network Enforcement
- **File Path:** [`code/business_entity_resolution/src/ber/security/fair_play.py`](file:///Users/satyabratadas/Documents/ENTIVYRE/code/business_entity_resolution/src/ber/security/fair_play.py#L54-L83)
- **Class:** `NetworkIsolationGuard`
- **Line Numbers:** 54–83
- **Verifiable Claim:** The pipeline strictly enforces air-gapped execution by intercepting socket connections.
- **Specific Evidence:**
  - Lines 70–75 monkey-patch `socket.socket.connect` to raise `NetworkBlockedException`.
