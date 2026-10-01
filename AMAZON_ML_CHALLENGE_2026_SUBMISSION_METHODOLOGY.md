# Amazon ML Challenge 2026 — Official Submission Methodology
## Business Entity Resolution Solution
**Team Name:** UNPAID ENGINEERS  
**Submission Portal:** Unstop (`unstop.com`)  
**Submission Deadline:** Friday, 2nd October  
**Team Members:** Satyabrat Das  
**Current Public Leaderboard Score:** 0.7840 (Macro $F_{0.5}$)  

---

## Executive Summary
**UNPAID ENGINEERS** presents an end-to-end, high-throughput, air-gapped Business Entity Resolution (BER) system engineered to maximize Macro-Averaged $F_{0.5}$ across three large-scale, heterogeneous data sources ($S_1$ reference anchors vs. $S_2$ and $S_3$ web-scraped targets). The solution combines a prioritized multi-pass inverted index blocking engine ($>99.9994\%$ search space reduction ratio), a 33-dimensional typed feature space, universal Indic and French normalization pipelines, dual hard-negative contradiction guards (vetoing conflicting building numbers and cross-border sovereign mismatches), and a calibrated decision threshold ($\tau^* = 0.58$) with match cardinality capping. Operating in pure Python with zero external API calls or commercial geocoders, the streaming pipeline processes all $1.73\text{M}$ test anchors against $9.97\text{M}$ target candidates in under two minutes with strictly bounded RAM ($<100\text{ MB}$ RSS), guaranteeing $100\%$ compliance with the official challenge submission validator.

---

## A. Methodology Used
The entity resolution challenge requires mapping clean reference entities in Source 1 ($S_1$) to partial, noisy web-scraped fragments in Source 2 ($S_2$) and Source 3 ($S_3$). Ground truth analysis revealed that $5.58\%$ of reference entities are true singletons (possessing 0 matches in $S_2$ and $S_3$), while matched entities link to an average of $3.46$ targets across $S_2$ and $S_3$ (maximum 11).

Because the official evaluation metric is Macro-Averaged $F_{0.5}$, precision is penalized **four times more severely** than recall ($0.25 P + R$ in the denominator). Furthermore, falsely merging even one target into a true singleton collapses its per-entity score from $1.0$ to $0.0$. Consequently, our methodology prioritizes **high-recall candidate retrieval paired with strict precision-guarded matching**:
1. **Multi-Representation Ingestion:** Ingesting entities line-by-line into multi-tier representations (raw, clean, canonical, and sub-word tokens) without modifying raw source text.
2. **Deterministic & Composite Inverted Index Blocking:** Bounding candidate comparisons to $< 250$ candidates per anchor via multi-key hashing, pruning high-frequency generic terms.
3. **Contradiction-Gated Similarity Scoring:** Systematically filtering pairs using hard geographic and street-number contradiction rules before computing similarity scores.
4. **Calibrated Decision Logic:** Admitting candidate matches above an empirically validated threshold ($\tau^* = 0.58$) and enforcing match cardinality caps ($\le 8$).
5. **Candidate-Subset Invariant Serialization:** Enforcing the strict mathematical invariant $\text{matching\_results.tsv} \subseteq \text{candidate\_pairs.tsv}$ at the streaming serializer level.

---

## B. Candidate Generation / Blocking Strategy
A full Cartesian comparison between $1,732,544$ test anchors and $9,969,589$ targets would require $1.73 \times 10^{13}$ pairwise comparisons ($17.3$ trillion), which is computationally intractable. 

Our candidate generation module reduces the candidate search space by **$>99.9994\%$**, generating at most $4.34 \times 10^8$ total candidate pairs (an average of $250$ candidates per anchor) using a multi-pass inverted index:
- **Pass 1 — Canonical Name Hash (`NC`):** Exact match on business name after legal suffix standardization (e.g. `pvt ltd`, `inc`, `corp`, `llc`, `sarl`) and punctuation removal.
- **Pass 2 — Domain Root Hash (`NCONCAT`):** Concatenated alphanumeric name string (first 20 characters) resolving domain-masked web names (e.g. `wilfordhancock.com` $\to$ `wilfordhancock`).
- **Pass 3 — Sorted Token Key (`NS`):** Alphabetically sorted distinctive name tokens, guaranteeing word-order invariance (e.g. "Paris Cafe" vs "Cafe Paris").
- **Pass 4 — Name Token Prefix (`NP`):** First two clean tokens, capturing brand extensions and corporate divisions.
- **Pass 5 — Single Distinctive Word (`N1` / `N1L`):** High-entropy single words ($\ge 5$ characters) for single-token corporate names.
- **Pass 6 — Composite Building Number + Name Prefix (`ADDR_N1`):** Combines the street building number with the first 4 characters of the business name (e.g. `85_maur` for "85 Wayne Ave, Maure Williams"), rescuing candidates with street spelling differences.
- **Pass 7 — Composite Postal Code + Name Prefix (`PIN_N1`):** Combines the postal/PIN code with the first 4 characters of the business name (e.g. `90210_burg`).
- **Frequency Capping Safeguard:** Posting lists are strictly capped at $\text{max\_postings} = 300$ elements. Highly frequent generic business nouns (e.g. "store", "restaurant", "solutions") are automatically truncated to prevent Cartesian explosion.
- **Candidate Cap:** Maximum $150$ candidates per target source ($K \le 250$ combined) per anchor.

---

## C. Feature Engineering
Our architecture extracts a comprehensive, typed 33-dimensional feature space spanning five distinct evidential dimensions:

### 1. Name Features (10 Features)
- `name_exact_match`: Binary indicator of raw name identity.
- `name_clean_exact_match`: Binary indicator of cleaned name identity.
- `name_canonical_exact_match`: Binary indicator of canonicalized root identity.
- `name_token_jaccard`: Jaccard similarity over distinctive token sets.
- `name_token_overlap_count`: Integer count of shared distinct tokens.
- `name_token_containment`: Asymmetric token containment ratio ($\ge 2$ tokens).
- `name_char_ngram_cosine`: Sub-word character 3-gram TF-IDF cosine similarity.
- `name_levenshtein_sim`: Normalized Levenshtein edit similarity.
- `name_length_ratio`: Ratio of shorter name length to longer name length.
- `name_numeric_overlap`: Jaccard overlap of numbers occurring inside names.

### 2. Address Features (11 Features)
- `address_exact_match`: Binary indicator of raw address identity.
- `address_clean_exact_match`: Binary indicator of cleaned address identity.
- `address_canonical_exact_match`: Binary indicator of standardized address identity.
- `address_token_jaccard`: Jaccard similarity over address token sets.
- `address_token_overlap_count`: Count of shared distinct address tokens.
- `address_char_ngram_cosine`: Character 3-gram TF-IDF cosine similarity over addresses.
- `address_levenshtein_sim`: Normalized Levenshtein edit similarity over addresses.
- `address_numeric_jaccard`: Jaccard overlap of building/plot numbers.
- `address_numeric_contradiction`: **Hard Contradiction Flag** (1.0 if both addresses specify numbers but share zero common numbers).
- `address_postal_code_match`: Binary indicator of 5-digit/6-digit postal code identity.
- `address_is_missing`: Indicator if either address string is missing/empty ($3.31\%$ baseline rate).

### 3. Country Features (4 Features)
- `country_exact_match`: Binary indicator of canonical country identity.
- `country_compatible`: 1.0 if countries match or either is unknown.
- `country_contradiction`: **Hard Contradiction Flag** (1.0 if both countries are known but conflict).
- `has_unseen_country`: Indicator for unseen test countries (e.g. France).

### 4. Cross-Field Features (4 Features)
- `name_and_address_high_sim`: Joint composite flag (`name_jaccard >= 0.70` AND `address_jaccard >= 0.50`).
- `name_high_address_contradiction`: Identical name with conflicting street numbers.
- `name_exact_diff_country`: Identical name in conflicting sovereign jurisdictions.
- `overall_composite_similarity`: Weighted harmonic mean of name, address, and geographic scores.

### 5. Retrieval Provenance Features (4 Features)
- `in_standard_blocker`: Retrieved by deterministic multi-key index.
- `in_tfidf_retriever`: Retrieved by sub-word character TF-IDF pass.
- `in_both_retrieval_passes`: Captured in both candidate retrieval passes.
- `tfidf_retrieval_score`: Dense TF-IDF cosine similarity score.

---

## D. Model Architecture
The ENTIVYRE codebase provides two complementary modeling paradigms:
1. **Supervised Gradient Boosted Decision Stumps (`ber.models.tree_ensemble`):**
   - Pure-Python gradient boosting tree classifier optimizing binary logistic cross-entropy loss.
   - Second-order Newton-Raphson leaf updates with $L_2$ regularization:
     $$\text{leaf\_value} = \frac{\sum r_i}{\sum h_i + \lambda}$$
   - Monotonic threshold splits over all 33 feature dimensions.
   - Hyperparameters: $30$ estimators, learning rate $\eta = 0.10$, $L_2$ leaf penalty $\lambda = 1.0$, subsampling ratio $1.0$.
2. **High-Throughput Streaming Scoring Engine (`ber.inference.engine`):**
   - Deployed for full $1.73\text{M}$ test inference to maintain linear $O(N)$ runtime in strictly bounded RAM ($<100\text{ MB}$).
   - Integrates non-linear multi-tier scoring with explicit contradiction veto gates:
     - **Sovereign Conflict Veto:** Drops score to `0.0` if country codes conflict.
     - **Building Number Conflict Veto:** Drops score to `0.0` if street building numbers conflict (with OCR single-digit truncation fallback).
     - **Shopping Center / Mall Guard:** Vetoes pairs with `name_sim < 0.45` to prevent distinct storefronts at the same postal address from merging.
     - **Adaptive Composite Weighting:** Dynamically balances name and address weights depending on name match strength and address missingness.

---

## E. Training Procedure
- **Validation Splitting:** Entity-grouped cross-validation splitting (`ber.evaluation.splitter`). Matches are partitioned by connected components so that all targets associated with an anchor remain together. Zero anchor or target overlap exists between training and validation folds.
- **Negative Sampling:** Hard negative sampling (`ber.data.pair_dataset`). Positive pairs are mined from `train_ground_truth.tsv`. Negative pairs are sampled from blocking candidates that do not appear in ground truth, forcing the model to distinguish true matches from same-street or similar-name distractors.
- **Optimization Objective:** Binary cross-entropy (log-loss).
- **Threshold Calibration:** Optimal threshold $\tau^*$ was derived by executing an exhaustive grid sweep over $\tau \in [0.30, 0.95]$ evaluating the official Macro $F_{0.5}$ metric with full singleton credit.

---

## F. Matching / Decision Strategy
The final match decision pipeline enforces the following deterministic rules for every anchor $s_1 \in S_1$:
1. If no candidates were retrieved or all candidates were eliminated by contradiction guards, emit an empty match list `""` (yielding $1.0$ singleton credit).
2. For each candidate $t \in C(s_1)$, compute composite score $S(s_1, t)$.
3. Admit candidate $t$ as a match if:
   $$S(s_1, t) \ge \tau^* \quad (\tau^* = 0.58)$$
   or if $t$ qualifies under specific high-precision expansion rules (e.g. `P04`: exact canonical name $\ge 10$ chars + exact 5-digit postal code).
4. Sort admitted matches in descending order of confidence score.
5. Deduplicate targets and truncate to at most $\text{max\_matches} = 8$ targets per anchor.
6. Verify that all predicted targets are strictly present in $C(s_1)$ before writing to disk.

---

## G. Post-Processing
1. **Match Truncation Cap:** Capped at $8$ matches per anchor. Analysis of $2.2\text{M}$ training ground truth rows proved that $99.78\%$ of matched entities have $\le 8$ targets (maximum observed is 11). This cap eliminates tail-end false positive cascades while retaining $99.93\%$ of true links.
2. **Singleton Empty String Formatting:** Unmatched entities are written with an empty second column (`s1_id\t\n`), strictly matching the format required by the official scorer.
3. **Format Integrity:** Outputs are serialized strictly as tab-delimited (`\t`) text files with Unix line endings (`\n`), preventing the common comma-separated CSV formatting failure.

---

## H. Validation
Output files were validated using the official challenge validator (`student_resource/utils/validate_submission.py`):
```
ML Challenge 2026 — submission validator
  test dir: student_resource/dataset/test
  required S1 entities: 1732544
  matching_results.tsv: 1732544 rows (190885 empty, 1541659 non-empty).
  candidate_pairs.tsv: 1732544 rows (179 empty, 1732365 non-empty).
PASS — no blocking issues found. Safe to submit.
```
- **Row Count Fidelity:** Exactly $1,732,544$ rows in both files, matching `test_source1.tsv` row-for-row.
- **Subset Invariant:** Exactly $0$ subset violations. Every matched ID in `matching_results.tsv` is certified to be present in `candidate_pairs.tsv`.
- **ID Existence:** All target IDs begin with `S2-` or `S3-`. Zero self-matches (`S1-`). Zero duplicates.

---

## I. Computational Environment
- **Hardware Architecture:** Apple Silicon Mac (ARM64) / Standard Linux x86_64 compatible.
- **Operating System:** macOS Darwin / Ubuntu 22.04 LTS.
- **Python Version:** Python 3.8+ (tested on Python 3.10, 3.12, and 3.14).
- **RAM Footprint:** Strictly bounded under **`100 MB RSS`** using partitioned streaming execution.
- **Execution Runtime:** **`118.4 seconds`** for full test inference ($1.73\text{M}$ anchors across $9.97\text{M}$ targets).
- **GPU Requirements:** None ($0$ GB VRAM required). 100% CPU execution.
- **External Network Access:** None. Fully air-gapped execution.

---

## J. Reproducibility
The solution is fully self-contained in `code/business_entity_resolution/`. To reproduce the official outputs:

```bash
# 1. Install pinned dependencies (standard Python environment)
pip install -r requirements.txt

# 2. Add source directory to PYTHONPATH
export PYTHONPATH="code/business_entity_resolution/src:${PYTHONPATH}"

# 3. Execute streaming test inference
python3 scripts/run_test_inference.py \
    --test-dir student_resource/dataset/test \
    --output-dir output \
    --partitioned

# 4. Verify outputs with the official challenge validator
python3 scripts/run_official_validator.py \
    --matching output/matching_results.tsv \
    --candidate output/candidate_pairs.tsv \
    --test-dir student_resource/dataset/test
```

---

## K. Results
### Leaderboard Progression:
- **Baseline (Naive Levenshtein):** $0.3150$ Macro $F_{0.5}$ (Local: $0.3012$)
- **CHAMPION_001 (Multi-Key Index + Basic Veto):** $0.6100$ Macro $F_{0.5}$ (Local: $0.5917$)
- **CHALLENGER_002 (Domain Recovery + 7-Pass Blocking):** $\approx 0.7200$ Macro $F_{0.5}$ (Local: $0.6958$)
- **CHALLENGER_004 (Precision Composite Blocking + Center Veto):** $\approx 0.7690$ Macro $F_{0.5}$ (Local: $0.8513$)
- **CHALLENGER_005 (Universal Brahmi Offset + Hindi Lexicon):** **`0.7840` Macro $F_{0.5}$** (Local: $0.8573$)
- **CHALLENGER_007 (Active Submission Base):** Local Validation Macro $F_{0.5}$: **`0.8694`** ($P = 94.74\%$, $R = 65.39\%$).

---

## L. Important Implementation Details
1. **Universal Brahmi Script Unicode Offset:**
   Rather than training massive multilingual transformer models, we exploited the mathematical regularity of the Unicode standard for Brahmi-derived Indic scripts. Devanagari, Bengali, Gurmukhi, Gujarati, Oriya, Tamil, Telugu, Kannada, and Malayalam occupy contiguous 128-byte (`0x80`) blocks with identical relative phonetic codepoints. Mapping characters via `chr(0x0900 + (code % 0x80))` maps Dravidian and eastern Indic scripts into Devanagari in $O(1)$ time, yielding an immediate $+0.0150$ jump on the public leaderboard.
2. **Partitioned Streaming Memory Management:**
   By indexing Source 2, streaming Source 1, clearing memory via garbage collection, indexing Source 3, streaming Source 1, and then performing a 2-way streaming merge of the intermediate files, the pipeline processes 64 GB worth of data in under $100\text{ MB}$ RAM.

---

## M. Limitations / Known Constraints
1. **Candidate Recall Floor ($66.75\%$):** Offline blocking audits reveal that $33.25\%$ of true matches fail to trigger any of the 7 blocking keys. Because a classification model cannot predict an entity that was never retrieved, candidate recall forms an absolute upper bound on model recall.
2. **Severe Address Missingness ($3.31\%$):** Web-scraped target entities lacking address strings cannot utilize building-number or postal-code features, forcing the model to rely solely on string similarity and occasionally falling below the conservative threshold floor.
3. **Multi-Tenant Commercial Centers:** Distinct retail businesses sharing a shopping plaza with identical street numbers and missing unit/suite numbers remain a source of rare false positive merges.
