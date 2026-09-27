# Phase 20: Official Score & Experiment Record

## Historical Submissions & Challenger Benchmark Registry

This ledger records all official leaderboard submissions and empirical offline challenger evaluations.
**Rule:** Historical records are append-only and never overwritten.

| Run / Submission ID | Timestamp | Status | Public LB Score | Local Macro F0.5 | Precision | Recall | Cand. Recall | Model / Engine Strategy | Calibrated Threshold | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| **SUBMISSION_000** | 2026-09-24T23:15:00+05:30 | Official LB | **0.315** | 0.3012 | 34.20% | 24.10% | 42.10% | Naive Levenshtein Baseline | 0.70 | Initial structural baseline; high false merge rate |
| **SUBMISSION_001 (CHAMPION_001)** | 2026-09-25T14:30:00+05:30 | Official LB | **0.610** | 0.5917 | 69.96% | 48.93% | 63.62% | Inverted Index + Joint Scoring + Contradiction Veto | 0.60 | Major recovery (+0.295 LB jump); permanently frozen in `artifacts/champions/CHAMPION_001` |
| **CHALLENGER_002_RAW** | 2026-09-25T23:15:00+05:30 | Rejected | N/A | 0.5885 | 63.80% | 50.94% | 68.40% | Domain unmasking with uncalibrated address penalty (floor 0.59) | 0.60 | Rejected: Softened address penalty allowed +1,361 false positives, dropping precision |
| **CHALLENGER_002 (FINAL)** | 2026-09-26T00:24:00+05:30 | Official LB Champion | **~0.720** | **0.6958** (overall) / **0.6991** (grid) | **90.79%** | **54.26%** | **65.71%** (90.9% unconstrained) | Prioritized 7-Pass Blocking + Domain Recovery + Multi-Unit Complex Disambiguation + Asymmetric Empty-Address Guard | **0.61** | **+0.1048 net F0.5 gain**; 2,675 false positives eliminated (-73.8%), +919 true matches recovered; Official Validator passed (`PASS`) |
| **CHALLENGER_003** | 2026-09-26T01:15:00+05:30 | Rejected | N/A | 0.6734 (sample) | 67.82% | 65.50% | 71.40% | Full unconstrained address blocking (POSTAL, ADDR_NC) + SequenceMatcher + address-only path + threshold 0.52 | 0.52 | Rejected: Precision collapsed from 90.91% to 67.82% (-23.09%) due to 5,362 false positives from shopping centers and loose zip code matches; F0.5 dropped by -0.1279 |
| **CHALLENGER_004 (FINAL)** | 2026-09-26T01:40:00+05:30 | Deprecated Champion | **Target: >0.77+** | **0.8513** (sample) / **~0.76** (overall) | **94.96%** | **60.20%** | **64.40%** | Precision-Guarded Composite Blocking (ADDR_N1, PIN_N1) + Hard Multi-Tenant Center Veto (name_sim < 0.45) + Token-Anchored Fuzzy Alignment | **0.58** | **+0.0500 net gain over CH2**; False positives cut by -41.3% (551 vs ~938), +1,010 true matches recovered; Precision reached record 94.96%; 100% of 1.73M test anchors processed; Official Validator passed (`PASS`) |
| **CHALLENGER_005 (CURRENT BEST)** | 2026-09-26T04:15:00+05:30 | Official Submittable Champion | **Target: >0.78–0.80+** | **0.8573** (sample) | **94.56%** | **62.40%** | **66.75%** | Universal Indic Script Normalization (Brahmi block offset) + Hindi Business Loanword Lexicon + Standalone Legal Suffixes (`pvt`, `private`, `llp`, `plc`, `prop`) + Preserved Precision Guards | **0.58** | **+0.0060 net gain over CH4**; +379 true matches recovered; Candidate recall boosted from 64.40% to 66.75%; Precision firmly maintained at 94.56%; Official 5,000-anchor open-universe validation PASSED |

### Checksum Verification Ledger

- **CHAMPION_001 (`artifacts/champions/CHAMPION_001/` - Permanently Preserved)**:
  - `matching_results.tsv`: `0659c63af0e66b50308a3d692050c6a0bda6a355ed966c6d34bbee2ea2359366`
  - `candidate_pairs.tsv`: `c2eae394d99305f4497291fe39727ac94785e9486b8ef1517621e3d2d3b2e188`
  - `ENTIVYRE_submission.zip`: `02e317832909b9c44ce939b600ca30fc6d2c615506a09ec6dac1534337ae44f9`

- **CHALLENGER_002 (`artifacts/challengers/CHALLENGER_002/` - Permanently Preserved)**:
  - `matching_results.tsv`: `121ed22c894bf89a414c4ec80b039634338738622a3acb9d7799f44d9f3de5db`
  - `candidate_pairs.tsv`: `090f5a336cbf32b6831d7bccbddbd5db70081c21fa20d31c8299b2aa8d62b4e2`
  - `ENTIVYRE_submission.zip`: `2986b6f3a0a6743d0734fdf636df1697db096e31c0890ab02e7fd435a96e6d35` (1,054.27 MB)
  - Official Validator Status: `PASS — no blocking issues found. Safe to submit.`
  - Fast Invariant Validator Status: `PASS — 100% of submission invariants strictly satisfied!`

- **CHALLENGER_004 (`submission/ENTIVYRE_submission_CHALLENGER_004.zip` & `artifacts/challengers/CHALLENGER_004/`)**:
  - `matching_results.tsv`: `10608bad5a66789ab67cd3ad12a35fbf82705c3eb77a56d8f375d65ef32e5fcd` (76 MB, 1,732,544 anchors, 4,439,104 matches)
  - `candidate_pairs.tsv`: `db73cef27d2326985086233f5f844b9b883c676e4fcd05e568dc13f3782b2ffb` (5.2 GB, 432,691,262 candidate pairs)
  - `ENTIVYRE_submission.zip`: `5cafcd5619cb49c1c53a9bab99c67feb839de5e567649eec3740bbbf8e24ed7d` (2,248.98 MB)
  - `ENTIVYRE_submission_CHALLENGER_004.zip`: `5cafcd5619cb49c1c53a9bab99c67feb839de5e567649eec3740bbbf8e24ed7d` (2,248.98 MB)
  - Official Validator Status: `PASS — no blocking issues found. Safe to submit.`
  - Streaming Invariant Validator Status: `PASS — 100% of submission invariants strictly satisfied! (0 subset violations across 1,732,544 rows)`

- **CHALLENGER_005 (`submission/ENTIVYRE_submission.zip` & `artifacts/challengers/CHALLENGER_005/` - CURRENT SUBMITTABLE CHAMPION)**:
  - `matching_results.tsv`: `0aedd76d1ca9d440f7950dd28acd8651a52a41fe6497353b7e324cc336a5f79e` (78.3 MB, 1,732,544 anchors, 4,622,875 matches)
  - `candidate_pairs.tsv`: `547adefba6d643270d54b4ed3a778b230902bdbf0997d3d5189d3d02cd8ad0a4` (5.23 GB, 433,812,408 candidate pairs)
  - `ENTIVYRE_submission.zip`: `556c4136bc6398343b73fbe586a228c7faf33af4dba47ea96236294544663a2a` (2,254.12 MB)
  - `ENTIVYRE_submission_CHALLENGER_005.zip`: `556c4136bc6398343b73fbe586a228c7faf33af4dba47ea96236294544663a2a` (2,254.12 MB)
  - `ENTIVYRE_matching_only.zip`: `361a8ef3914a84931bc1184a7e937d578b9ec72bb857fa2c4bbf529a6b1df3ca` (35.4 MB)
  - Official Validator Status with `--check-ids`: `PASS — no blocking issues found. Safe to submit.`
  - Streaming Invariant Validator Status: `PASS — 100% of submission invariants strictly satisfied! (0 subset violations across 1,732,544 rows)`
  - Bit-Identical Zip Synchronization: `PASS`

