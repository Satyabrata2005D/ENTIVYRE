# ENTIVYRE Methodology & Architecture Specification
**Amazon ML Challenge 2026 — Production Business Entity Resolution System**

---

## 1. Problem Formulation & Challenge Objective

Business Entity Resolution (BER) in this challenge requires resolving entities across three heterogeneous, noisy data sources:
- **Source 1 ($S_1$):** Clean, deduplicated reference anchor source ($1,732,544$ records in test).
- **Source 2 ($S_2$) & Source 3 ($S_3$):** Scraped, unstructured, noisy web data sources ($4,887,273$ and $5,082,316$ records in test, totaling $9,969,589$ targets).
- **Mapping Multiplicity:** An anchor entity $s_1 \in S_1$ may link to:
  - $\emptyset$ (True Singleton): No corresponding records in $S_2$ or $S_3$.
  - $\{t\}$ (Single Match): Exactly one corresponding record in $S_2$ or $S_3$.
  - $\{t_1, t_2, \dots, t_m\}$ (Multi-Match): Multiple corresponding records across $S_2$ and $S_3$ (mean $3.46$ targets per matched anchor in ground truth).

### 1.1 Objective Metric: Macro-Averaged $F_{0.5}$ with Official Singleton Credit

The competition evaluation metric is the Macro-Averaged $F_{0.5}$ score calculated across all Source 1 anchor entities:

$$\text{Macro } F_{0.5} = \frac{1}{|S_1|} \sum_{i=1}^{|S_1|} F_{0.5}(T_i, \hat{T}_i)$$

where $T_i$ is the ground-truth set of matched targets for anchor $i$, and $\hat{T}_i$ is the predicted set of matched targets.

For any anchor entity $i$:
1. **Singleton Credit:** If $T_i = \emptyset$ and $\hat{T}_i = \emptyset$, then $F_{0.5}(T_i, \hat{T}_i) \equiv 1.0$.
2. **False Merge Penalty:** If $T_i = \emptyset$ and $\hat{T}_i \neq \emptyset$, then $F_{0.5}(T_i, \hat{T}_i) \equiv 0.0$.
3. **False Dismissal Penalty:** If $T_i \neq \emptyset$ and $\hat{T}_i = \emptyset$, then $F_{0.5}(T_i, \hat{T}_i) \equiv 0.0$.
4. **Matched Pairs:** If $T_i \neq \emptyset$ and $\hat{T}_i \neq \emptyset$:

$$P_i = \frac{|T_i \cap \hat{T}_i|}{|\hat{T}_i|}, \quad R_i = \frac{|T_i \cap \hat{T}_i|}{|T_i|}$$

$$F_{0.5}(T_i, \hat{T}_i) = \frac{(1 + 0.5^2) \cdot P_i \cdot R_i}{0.5^2 \cdot P_i + R_i} = \frac{1.25 \cdot P_i \cdot R_i}{0.25 \cdot P_i + R_i}$$

Because $\beta = 0.5$, precision is weighted twice as heavily as recall. False positive predictions (especially on singletons) destroy leaderboard score.

---

## 2. Mathematical Complexity & Combinatorial Blocking

A naive full Cartesian product across test anchors and targets would evaluate:

$$|S_1| \times (|S_2| + |S_3|) = 1.73 \times 10^6 \times 9.97 \times 10^6 \approx 1.73 \times 10^{13} \text{ pairs}$$

Evaluating $17.3$ trillion candidate pairs is computationally impossible. ENTIVYRE implements a multi-tiered inverted index blocking architecture bounding candidate comparisons to:

$$\text{Candidates} \le |S_1| \times K_{\max} = 1.73 \times 10^6 \times 50 \le 8.66 \times 10^7 \text{ pairs}$$

This achieves a reduction ratio of:

$$\text{Reduction Ratio} = 1 - \frac{8.66 \times 10^7}{1.73 \times 10^{13}} > 99.9994\%$$

### 2.1 Multi-Key Inverted Index Strategy
Candidates are generated through multi-key inverted indexing:
1. `NAME_CANON:<canonical_name>`: Exact canonical name match after legal suffix removal and noise stripping.
2. `CTRY_CANON:<country>:<canonical_name>`: Canonical name scoped within sovereign jurisdiction.
3. `NAME_SORTED:<token1_token2>`: Sorted tokens providing complete word-order invariance.
4. `NAME_PREF:<prefix_tokens>`: First two clean tokens catching prefix expansions.
5. `NAME_SINGLE:<token>`: Single high-entropy token ($\ge 4$ characters) for single-word enterprises.
6. `POSTAL_NAME:<postal_code>:<first_token>`: High-precision joint location and brand key.

To prevent stopword explosions on generic business nouns (e.g. "store", "restaurant", "solutions"), inverted index posting lists are frequency-capped at $\text{max\_postings} = 500$.

---

## 3. Multilingual Normalization Engine

All normalization is conservative and non-destructive: raw input text is preserved alongside derived canonical representations.

### 3.1 Business Name Pipeline
1. **Transliteration:** Devanagari script transliterated into Latin characters via deterministic phonetic mapping.
2. **Noise Stripping:** Stripping URLs (`http://`, `www.*`, `.com`, `.in`, `.fr`), email addresses, phone numbers, and arbitrary non-alphanumeric punctuation.
3. **Legal Suffix Standardization:** Canonical replacement of corporate entity designations:
   - "Private Limited", "Pvt Ltd", "P. Ltd" $\to$ `pvt ltd`
   - "Corporation", "Corp" $\to$ `corp`
   - "Incorporated", "Inc" $\to$ `inc`
   - "Limited Liability Company", "LLC" $\to$ `llc`
   - "Société à Responsabilité Limitée", "SARL" $\to$ `sarl`
4. **Tokenization:** Multi-representation tokens: `raw_tokens`, `clean_tokens`, and `sorted_tokens`.

### 3.2 Address Intelligence & Contradiction Detection
1. **Keyword Standardizations:**
   - Road abbreviations: `st`, `rd`, `ave`, `blvd`, `dr`, `ln`, `pkwy`, `hwy`.
   - Building & unit designators: `ste`, `fl`, `apt`, `bldg`, `dept`.
   - International terms: `rue`, `boulevard`, `avenue`, `marche`, `nagar`, `colony`.
2. **Numeric Evidence Extraction:**
   - Street and plot numbers extracted via regex `\b\d+[a-zA-Z]?\b`.
   - **Contradiction Guard:** When both addresses contain non-empty sets of building numbers that share zero elements (e.g. `101 Main St` vs `105 Main St`), `address_numeric_contradiction` is set to $1.0$. This vetoes false merges on different branches of identical corporate chains.

### 3.3 Open-Set Sovereign Country Architecture
The test set contains countries not present in the training set (e.g., France represents $14.98\%$ of test anchors). ENTIVYRE implements open-set normalization:
- Canonical aliases for common forms (`US`, `USA`, `United States` $\to$ `US`; `India`, `Bharat`, `Ind` $\to$ `INDIA`; `France`, `FR`, `République Française` $\to$ `FRANCE`).
- Any unrecognized country is preserved as an uppercase alphanumeric canonical string.
- Contradiction occurs only when both entities have known, non-identical countries. Unseen countries are never rejected purely for being novel.

---

## 4. 33-Dimensional Feature Space Specification

All candidate pairs are vectorized into a fixed, immutable 33-dimensional feature space registered in `FeatureRegistry`:

| Index | Feature Name | Group | Type | Description |
|:---|:---|:---|:---|:---|
| 0 | `name_exact_match` | Name | float | Exact verbatim string equality on raw business names |
| 1 | `name_clean_exact_match` | Name | float | Equality after case folding and punctuation stripping |
| 2 | `name_canonical_exact_match` | Name | float | Equality after legal suffix normalization |
| 3 | `name_token_jaccard` | Name | float | Jaccard similarity across clean name tokens |
| 4 | `name_token_overlap_count` | Name | float | Absolute cardinality of intersecting name tokens |
| 5 | `name_token_containment` | Name | float | Asymmetric token containment: $\|A \cap B\| / \min(\|A\|, \|B\|)$ |
| 6 | `name_char_ngram_cosine` | Name | float | Cosine similarity on character 3-gram vectors |
| 7 | `name_levenshtein_sim` | Name | float | Normalized Levenshtein similarity on canonical names |
| 8 | `name_length_ratio` | Name | float | Length ratio: $\min(\text{len}_1, \text{len}_2) / \max(\text{len}_1, \text{len}_2)$ |
| 9 | `name_numeric_overlap` | Name | float | Overlap of digit sequences in business names |
| 10 | `address_exact_match` | Address | float | Exact verbatim string equality on raw addresses |
| 11 | `address_clean_exact_match` | Address | float | Equality after case folding and noise removal |
| 12 | `address_canonical_exact_match`| Address | float | Equality after street suffix normalization |
| 13 | `address_token_jaccard` | Address | float | Jaccard similarity across clean address tokens |
| 14 | `address_token_overlap_count` | Address | float | Absolute cardinality of intersecting address tokens |
| 15 | `address_char_ngram_cosine` | Address | float | Cosine similarity on character 3-gram address vectors |
| 16 | `address_levenshtein_sim` | Address | float | Normalized Levenshtein similarity on canonical addresses |
| 17 | `address_numeric_jaccard` | Address | float | Jaccard similarity of extracted street/building numbers |
| 18 | `address_numeric_contradiction`| Address | float | **Hard Negative Guard**: $1.0$ if street numbers strictly conflict |
| 19 | `address_postal_code_match` | Address | float | $1.0$ if postal/PIN codes match exactly |
| 20 | `address_is_missing` | Address | float | $1.0$ if either anchor or candidate address is missing |
| 21 | `country_exact_match` | Country | float | Exact match on canonical country |
| 22 | `country_compatible` | Country | float | True if identical or if either country is unknown |
| 23 | `country_contradiction` | Country | float | **Hard Negative Guard**: $1.0$ if countries strictly conflict |
| 24 | `country_has_unseen` | Country | float | $1.0$ if either entity exhibits a novel open-set country |
| 25 | `name_and_address_high_sim` | Cross-Field | float | Composite joint indicator ($J_{\text{name}} \ge 0.70 \land J_{\text{addr}} \ge 0.50$) |
| 26 | `name_high_address_contradiction`| Cross-Field| float | Multi-branch chain detector ($J_{\text{name}} \ge 0.80 \land \text{addr\_num\_conflict}$) |
| 27 | `name_exact_diff_country` | Cross-Field | float | Cross-border collision ($N_{\text{exact}} \land \text{country\_conflict}$) |
| 28 | `overall_composite_similarity` | Cross-Field | float | Adaptive weighted average across name, address, and country |
| 29 | `retrieval_pass1_standard` | Retrieval | float | $1.0$ if retrieved by deterministic inverted index |
| 30 | `retrieval_pass2_tfidf` | Retrieval | float | $1.0$ if retrieved by character n-gram TF-IDF pass |
| 31 | `retrieval_both_passes` | Retrieval | float | $1.0$ if candidate was independently retrieved by both passes |
| 32 | `tfidf_retrieval_score` | Retrieval | float | Dense cosine similarity score emitted during candidate retrieval |

---

## 5. Machine Learning Models & Calibrated Decision Logic

### 5.1 Calibrated Logistic Regression
$$P(y=1 \mid \mathbf{x}) = \sigma(\mathbf{w}^T \tilde{\mathbf{x}} + b), \quad \tilde{\mathbf{x}} = \frac{\mathbf{x} - \boldsymbol{\mu}}{\boldsymbol{\sigma}}$$
Trained via mini-batch stochastic gradient descent with $L_2$ weight regularization:
$$\mathcal{L}(\mathbf{w}, b) = -\frac{1}{N}\sum_{i=1}^N \left[ y_i \log p_i + (1 - y_i) \log(1 - p_i) \right] + \frac{\lambda}{2} \|\mathbf{w}\|_2^2$$

### 5.2 Gradient Boosted Decision Stumps
Ensemble of $M$ regularized decision stumps trained on log-loss pseudo-residuals $r_i = y_i - p_i$:
$$F_m(\mathbf{x}) = F_{m-1}(\mathbf{x}) + \eta \cdot h_m(\mathbf{x})$$
Optimal Newton-Raphson leaf updates with $L_2$ shrinkage:
$$\gamma_{jm} = \frac{\sum_{i \in R_{jm}} r_i}{\sum_{i \in R_{jm}} p_i(1 - p_i) + \lambda}$$

### 5.3 Optimal Decision Threshold Tuning
Threshold $\tau^*$ is selected by grid search $\tau \in [0.30, 0.95]$ on entity-grouped validation folds optimizing Macro $F_{0.5}$. The calibrated threshold $\tau^* = 0.70$ balances precision against recall, eliminating low-confidence false positives.

---

## 6. Official Submission Contracts & Invariant Guarantees

ENTIVYRE strictly enforces all submission formatting and semantic invariants:
1. **Filename & Encoding:** Output files are strictly UTF-8 plain text:
   - `output/matching_results.tsv`
   - `output/candidate_pairs.tsv`
2. **Column Headers:**
   - `matching_results.tsv`: `source1_entity_id\tmatched_entity_ids`
   - `candidate_pairs.tsv`: `source1_entity_id\tcandidate_entity_ids`
3. **Delimiter Standards:** Tab (`\t`) between columns; comma (`,`) between IDs within lists; zero spaces.
4. **Singletons:** Represented by empty string `""` after the tab (e.g. `S1-00003\t\n`).
5. **Exact 100% S1 Coverage:** Exactly one row per test Source 1 entity; zero duplicates; zero omissions.
6. **Candidate-Subset Invariant:**
   $$\forall s_1 \in S_1: \quad \hat{T}(s_1) \subseteq C(s_1)$$
   Every target ID predicted in `matching_results.tsv` is audited and guaranteed to exist in the corresponding row of `candidate_pairs.tsv`.
7. **Strict Air-Gapped Fair Play:**
   Runtime socket interceptors (`NetworkIsolationGuard`) and static codebase auditors (`FairPlayAuditor`) enforce zero external web calls, commercial APIs, or geocoding services.
