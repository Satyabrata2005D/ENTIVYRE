# Phase 03: Blocking Optimization & Candidate Recall Recovery Report

## Executive Summary
Prior to this investigation, `CHAMPION_001` (LB 0.610) operated with a Candidate Recall of only **63.62%**, establishing an insurmountable theoretical ceiling of 63.62% on overall recall. Forensic analysis revealed that **71.23% of all false negatives** were caused by retrieval misses where true matching targets were never admitted into the candidate pool.

By systematically analyzing the 3,407 blocking misses and classifying the 17,250 true matches in the 5,000 validation split, we discovered two major structural phenomena in the Amazon ML Challenge dataset:
1. **Transliterated / Indic Script Names (13.95% of True Matches):** 2,406 true targets have business names in non-Latin Indic scripts (Devanagari, Tamil, Telugu, Bengali, Gujarati, Kannada) while their addresses match Latin anchors nearly identically.
2. **Synthetic Pseudonym Names (3.51% of True Matches):** 605 true targets have synthetic nonsense names (`Dréxkor`, `Solkeloquo`, `Xylonexbrix`) generated as adversarial perturbation tests, where grounding relies entirely on exact building numbers and street/locality tokens.
3. **Domain / URL Names (4.81% of True Matches):** 830 targets had raw domain names (e.g. `maurewilliamscolombier.com`), which were previously stripped to noise or single unmatchable tokens.

## Blocking Strategies Evaluated

| Strategy | Description | Candidate Recall | Selectivity (Keys/Anchor) | Max Postings Cap |
|---|---|---|---|---|
| **A. NAME_CANON** | Full canonical normalized name | 34.21% | 1.0 | 500 |
| **B. NAME_SORTED** | Sorted first 4 tokens | 52.14% | 1.0 | 500 |
| **C. NAME_PREF** | First 2 tokens | 58.70% | 1.0 | 500 |
| **D. NAME_SINGLE** | Single distinctive token >= 3 chars | 41.30% | 0.8 | 500 |
| **E. NCONCAT** | Unmasked domain / concatenated root | 4.81% (unique) | 1.0 | 300 |
| **F. ADDR_PREF (Legacy)** | First 2 address tokens (`tok0_tok1`) | 14.20% | 1.0 | 500 (noisy) |
| **G. ADDR_NW (New)** | Primary building number + distinctive non-stopword | **62.27%** | 2.2 | 300 |
| **H. ADDR_WW (New)** | Two distinctive non-stopwords | 48.90% | 1.8 | 300 |
| **I. MULTI-PASS UNION** | **Union of A, B, C, D, E, G, H** | **90.91%** | **7.1** | **300** |

## Key Empirical Findings

1. **Massive Candidate Recall Breakthrough:**
   - `CHAMPION_001` Candidate Recall: **63.62%** (10,975 / 17,250)
   - Multi-Pass Union Candidate Recall: **90.91%** (15,682 / 17,250)
   - **Net Gain:** **+4,707 true matches recovered (+27.29% absolute gain)**.

2. **Controlled Candidate Volume:**
   - Total keys across 5,000 anchors: 33,243 keys (~6.6 keys per anchor).
   - Average candidates per anchor: ~18–25 candidates.
   - P95 candidate count: <= 50 candidates.
   - P99 candidate count: <= 60 candidates.
   - Zero memory explosion; fully compatible with streaming architecture.

3. **India Candidate Recall Recovery:**
   - India accounted for 61.7% of all blocking misses in CHAMPION_001 due to leading zeros (`0684` vs `684`), prefixes (`Plot No`, `House No`, `H.No`, `Shop No`), and non-Latin scripts.
   - Normalizing building numbers by stripping leading zeros and indexing by `ADDR_NW` eliminates this geographic discrepancy.
