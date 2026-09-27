# ENTIVYRE — EXHAUSTIVE DOCUMENT ANALYSIS (PART 1 of 3)
## Official Challenge Contract + Dataset Forensics + Validator Dissection

> [!IMPORTANT]
> This document is a **pure observational analysis**. No code is being written. Every word, character, constraint, and implication from the official challenge documentation and the actual dataset files is catalogued here.

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## LAYER 1: THE OFFICIAL CONTRACT — [README.md](file:///Users/satyabratadas/Documents/ENTIVYRE/student_resource/README.md)
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 1.1 Title & Framing (Lines 1–5)

**Exact text:** `# ML Challenge 2026 Problem Statement` → `## Business Entity Resolution Challenge`

**Word-by-word observations:**
- **"ML Challenge 2026"** — establishes year, confirming this is a competition. The phrase "ML" signals that the expected solution is machine-learning-based, not rule-based.
- **"Business Entity Resolution"** — three keywords:
  - **"Business"** — the entities are commercial/business entities, NOT people, products, or locations.
  - **"Entity"** — refers to real-world objects. Each "entity" is a single business that may have multiple records.
  - **"Resolution"** — the act of *resolving* whether two records refer to the same entity. Synonyms in the literature: record linkage, deduplication, entity matching.

### 1.2 Problem Statement Paragraph (Line 5)

**Character-by-character critical phrases:**

| Exact Phrase | Implication |
|---|---|
| `"large-scale commercial platforms"` | Production-grade scale. Not a toy dataset. |
| `"multiple independent sources"` | Sources are **independent** — no shared identifier schema. |
| `"partial, noisy fragments"` | Data is intentionally incomplete and corrupted. Expect missing fields, abbreviations, typos. |
| `"no common identifiers"` | There is NO join key. Cannot do a simple SQL JOIN. Must use *similarity* signals. |
| `"determines which records across sources refer to the same real-world business entity"` | The fundamental task: pairwise entity matching across sources. |

### 1.3 Source Hierarchy Rule (Line 7)

**Exact text:** `"Source 1 is the deduplicated reference source. Your task is to find all matching records from Source 2 and Source 3 for each Source 1 entity."`

**Critical analysis:**
- **"deduplicated"** — Source 1 is clean. Each entity_id in Source 1 is guaranteed unique. No two S1 records refer to the same entity.
- **"reference source"** — Source 1 is the anchor. All matching is S1→S2 and S1→S3. There is NO S2↔S3 matching required.
- **"A Source 1 entity may match zero, one, or many records from Source 2 and Source 3"** — Three cardinality possibilities:
  - **Zero matches** = singleton (the entity exists only in S1)
  - **One match** = 1:1 from S1 to one record in S2 or S3
  - **Many matches** = 1:N where N can span both S2 and S3

### 1.4 File Format Section (Lines 9–18)

**Exact text:** `"All files in this challenge are tab-separated (.tsv)"`

**Word-by-word analysis:**
- **"tab-separated"** — delimiter is `\t` (Unicode U+0009, ASCII 0x09). NOT comma, NOT pipe, NOT semicolon.
- **"your submissions must be tab-separated too"** — output format must also be TSV.
- **"Tabs are used because business addresses and the ID list columns both contain commas"** — the reason for TSV over CSV: commas are data characters, not delimiters.
- The Python example is `pd.read_csv("...", sep="\t")` — critically, the function is `read_csv` but the separator overrides it to TSV.
- **"Reading a .tsv without sep='\t' will silently produce a single column containing the whole line"** — this is a **trap warning**. Pandas defaults to comma separation. Without explicit `sep="\t"`, the entire line becomes a single string in column 0. This is "silent" because no error is raised.

### 1.5 Data Schema (Lines 20–34)

**Column-by-column dissection:**

#### Column 1: `entity_id`
- **"Unique identifier for the record"** — each record has exactly one ID.
- **"The prefix indicates the source — S1-, S2-, or S3-"** — the prefix is the ONLY way to determine which source a record belongs to.
- Observed format from data: `S1-925783039`, `S2-166376419`, `S3-202863386` — prefix + hyphen + numeric string.
- The numeric part is NOT sequential (e.g., `S1-925783039` appears first in the file). IDs are randomly assigned.

#### Column 2: `business_name`
- **"may contain abbreviations, legal suffixes, typos, transliterations"** — four noise categories:
  - **Abbreviations:** `Corp` vs `Corporation`, `Pvt` vs `Private`, `Ltd` vs `Limited`
  - **Legal suffixes:** `Inc`, `LLC`, `SARL`, `SASU`, `EURL`, `GmbH`, `Pvt Ltd`
  - **Typos:** random character errors
  - **Transliterations:** Hindi/Devanagari text transliterated to Latin or vice versa (observed: `राम मार्केटिंग` in Source 2)

#### Column 3: `business_address`
- **"may contain partial addresses, format variations, missing components, landmark-based references"** — four noise categories:
  - **Partial:** missing ZIP/PIN, missing state
  - **Format variations:** `Rd` vs `Road`, `St` vs `Street`
  - **Missing components:** observed 168,967 empty addresses in S2 and 175,916 in S3
  - **Landmark-based references:** `"Near SBI ATM"`, `"Opp.Rta Office"` — India-specific addressing

#### Column 4: `country`
> [!CAUTION]
> **THE FRANCE TRAP** — This is the single most critical word in the entire document:
> 
> `"The test set additionally contains a third country, France, that does not appear in the training data."`

**Character-level implications:**
- Training data: `{US, India}` ONLY (confirmed empirically: 1,323,633 US + 883,188 India in S1)
- Test data: `{US, India, France}` (confirmed: 663,106 US + 809,986 India + **259,452 France** in S1)
- **"Treat country as an open set of string labels"** — do NOT create an enum/one-hot of {US, India}. Must handle unseen countries.
- **"do not hard-code, filter, or one-hot your pipeline to only {US, India}"** — three specific anti-patterns explicitly prohibited.
- **"every test entity — France included — must appear in your submission"** — France entities MUST be in output. Cannot be skipped.

#### The `matched_entity_ids` column in ground truth:
- **"Comma-separated list"** — within the TSV, the second column uses commas to separate IDs.
- **"empty when the entity has no matches"** — singletons have an empty string in column 2.

### 1.6 Noise Patterns — Exact Enumeration (Lines 36–39)

**Name variations** (8 sub-types documented):
1. Abbreviations: `Corp` ↔ `Corporation`, `Pvt` ↔ `Private`, `Ltd` ↔ `Limited`
2. Legal suffix inconsistencies (presence/absence of `Inc`, `LLC`, etc.)
3. DBA/trade names (entirely different name for same entity)
4. Punctuation differences: `&` vs `"and"`
5. Word-order transpositions: `"Grain & Fils"` vs `"Fils Grain"`
6. Typos: random character substitutions, insertions, deletions

**Address variations** (6 sub-types documented):
1. Abbreviations: `Rd` ↔ `Road`, `St` ↔ `Street`
2. Transliteration variants (Hindi → Latin)
3. Missing components (no PIN code, no state)
4. Landmark-based references: `"Near SBI ATM"`
5. Municipal numbering formats
6. Component reordering: `"IA, Iowa City, 1064 Newton Rd"` vs `"1064 Newton Rd, Iowa City, IA"`

### 1.7 Output Format — Dual-File Requirement (Lines 63–129)

> [!IMPORTANT]
> The challenge requires **TWO** output files, not one.

#### File 1: `matching_results.tsv` (Lines 73–97)
- **Columns:** `source1_entity_id` (tab) `matched_entity_ids`
- **Scored on leaderboard** — this is THE file that determines ranking.
- **Rules (5 strict rules, each causes REJECTION if violated):**
  1. Every S1 entity in test must have exactly one row
  2. Empty `matched_entity_ids` for singletons (no matches)
  3. No duplicate entity IDs within a single ID list
  4. Only S2/S3 IDs allowed (no S1 self-matches)
  5. IDs must exist in the test set

#### File 2: `candidate_pairs.tsv` (Lines 98–129)
- **Columns:** `source1_entity_id` (tab) `candidate_entity_ids`
- **NOT scored** — used for pipeline verification and blocking analysis.
- **"the exact set of records you feed into your matching model for inference"** — this is NOT early blocking output. It is the FINAL candidate set before scoring.
- **"Every ID in matching_results.tsv should therefore appear here"** — matches ⊆ candidates. A match not in candidates = pipeline bug.
- Same format rules as matching_results.tsv.

### 1.8 Validator Script Usage (Lines 131–145)

```bash
python3 utils/validate_submission.py \
    --matching output/matching_results.tsv \
    --candidate output/candidate_pairs.tsv \
    --test-dir dataset/test
```

- **Exit 0** = `PASS` (safe to submit)
- **Exit 1** = numbered list of issues
- **Does NOT compute score** — only checks format.

### 1.9 Final Submission Package (Lines 147–178)

**Exact directory structure:**
```
<team_name>_submission.zip
├── output/
│   ├── matching_results.tsv
│   └── candidate_pairs.tsv
├── code/
│   └── business_entity_resolution/
│       ├── src/
│       ├── README.md
│       └── requirements.txt
└── Documentation_template.md
```

**Critical constraints:**
- `requirements.txt` must have **pinned versions**
- Must be **self-contained and runnable** — "Anyone should be able to regenerate both output files"
- Code path is specifically `code/business_entity_resolution/src/`

### 1.10 Hard Constraints (Lines 180–186)

| # | Constraint | Violation Consequence |
|---|---|---|
| 1 | Format exactly as described | Not evaluated |
| 2 | Only S2/S3 IDs in matched_entity_ids | Rejected |
| 3 | Every S1 entity must appear | Rejected |
| 4 | No duplicate IDs | Rejected |
| 5 | **MIT/Apache 2.0 License model, up to 8B parameters** | Disqualification |

> [!WARNING]
> Constraint 5 is the **model license gate**: Only open-source models with MIT or Apache 2.0 license, maximum 8 billion parameters. This eliminates: GPT-4, Claude, Gemini, Llama 70B, Mixtral 8x22B, etc.

### 1.11 Evaluation Metric — F₀.₅ (Lines 188–209)

**Formula:** `F_0.5 = (1.25 × Precision × Recall) / (0.25 × Precision + Recall)`

**Computation method:** **Macro-average** — F₀.₅ is calculated PER S1 entity, then averaged across ALL S1 entities.

**Precision-weighting analysis:**
- β = 0.5 means β² = 0.25
- The formula weights precision **4× more** than recall (not 2× as stated — the document says "2×" but mathematically, the weight ratio is `1/β² = 4`)
- Wait — re-reading: "F_0.5 weights precision 2× over recall." This is the conventional statement. The actual emphasis ratio in the harmonic mean is `(1+β²)/β² = 1.25/0.25 = 5:1` for precision vs recall... but the standard interpretation is that precision matters ~2× as much in terms of the effective tradeoff.

**Singleton scoring rule:**
- Singleton with no true matches → predict empty → F₀.₅ = **1.0** (full credit!)
- Singleton with no true matches → predict any match → F₀.₅ = **0.0** (complete penalty!)
- This means: **conservative predictions are rewarded**. Every false positive on a singleton costs a full 1.0 in the average.

**Worked example from the document:**
- Predicted: [S2-00047, S2-00193, S3-00812]
- Ground truth: [S2-00047, S3-00812]
- Precision = 2/3 = 0.667 (one false positive: S2-00193)
- Recall = 2/2 = 1.0 (both true matches found)
- F₀.₅ = (1.25 × 0.667 × 1.0) / (0.25 × 0.667 + 1.0) = 0.8333 / 1.1667 = **0.714**

### 1.12 Leaderboard Structure (Lines 211–217)

- **Public leaderboard:** subset of test set, visible during challenge
- **Private leaderboard:** remaining test subset, revealed after challenge ends
- **Final rankings = private leaderboard** — public score is meaningless for final ranking
- "You submit predictions for the full test set in both cases; the split is applied during scoring."

### 1.13 Academic Integrity (Lines 238–254)

**STRICTLY PROHIBITED (exact enumeration):**
1. Commercial entity resolution APIs
2. Business registration lookups from government databases
3. Geocoding APIs to normalize addresses
4. Any external data augmentation from internet sources

**Enforcement:** "thoroughly reviewed and verified" — code is audited.

### 1.14 Tips for Success (Lines 256–264)

Six tips, verbatim analysis:

| Tip | Decoded Meaning |
|---|---|
| "Invest in a strong blocking/candidate generation strategy" | Blocking determines recall ceiling. If a true match isn't in your candidate set, your model can never find it. |
| "Explore string similarity features (Jaccard, Levenshtein, TF-IDF cosine)" | These three specific algorithms are recommended. |
| "Pay attention to country specific address patterns" | US, India, and France addresses have different structures. |
| "Consider the precision-recall trade-off carefully" | Conservative > aggressive. High threshold > low threshold. |
| "Do not neglect singletons" | 123,247 singletons in training = 5.58% of S1 entities. Each correct singleton = +1.0 to average. |
| "Validate your own output format" | Use the provided validator before submitting. |

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## LAYER 2: EMPIRICAL DATASET FORENSICS
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 2.1 File Size & Scale Audit

| File | Rows (incl. header) | Bytes | Records |
|---|---|---|---|
| [train_source1.tsv](file:///Users/satyabratadas/Documents/ENTIVYRE/student_resource/dataset/train/train_source1.tsv) | 2,206,822 | 210 MB | 2,206,821 |
| [train_source2.tsv](file:///Users/satyabratadas/Documents/ENTIVYRE/student_resource/dataset/train/train_source2.tsv) | 5,034,617 | 489 MB | 5,034,616 |
| [train_source3.tsv](file:///Users/satyabratadas/Documents/ENTIVYRE/student_resource/dataset/train/train_source3.tsv) | 5,285,604 | 503 MB | 5,285,603 |
| [train_ground_truth.tsv](file:///Users/satyabratadas/Documents/ENTIVYRE/student_resource/dataset/train/train_ground_truth.tsv) | 2,206,822 | 127 MB | 2,206,821 |
| [test_source1.tsv](file:///Users/satyabratadas/Documents/ENTIVYRE/student_resource/dataset/test/test_source1.tsv) | 1,732,545 | 175 MB | 1,732,544 |
| [test_source2.tsv](file:///Users/satyabratadas/Documents/ENTIVYRE/student_resource/dataset/test/test_source2.tsv) | 4,887,274 | 509 MB | 4,887,273 |
| [test_source3.tsv](file:///Users/satyabratadas/Documents/ENTIVYRE/student_resource/dataset/test/test_source3.tsv) | 5,082,317 | 506 MB | 5,082,316 |

**Total records: ~26.4 million** across all files.
**Total bytes: ~2.5 GB** on disk.

### 2.2 Source-to-Source Ratio Analysis

**Training set:**
- S1: 2,206,821 entities (reference, deduplicated)
- S2: 5,034,616 records (~2.28× S1)
- S3: 5,285,603 records (~2.39× S1)
- **S2+S3 combined: 10,320,219** records to match against 2.2M S1 entities

**Test set:**
- S1: 1,732,544 entities
- S2: 4,887,273 records (~2.82× S1)
- S3: 5,082,316 records (~2.93× S1)
- **S2+S3 combined: 9,969,589** records to match against 1.7M S1 entities

**Naive comparison space:** Each S1 entity must be compared against ALL S2+S3 entities.
- Training: 2,206,821 × 10,320,219 = **~22.8 trillion** comparisons
- Test: 1,732,544 × 9,969,589 = **~17.3 trillion** comparisons
- **Without blocking, this is computationally infeasible.**

### 2.3 Country Distribution — Deep Analysis

**Training data (S1):**
| Country | Count | Percentage |
|---|---|---|
| US | 1,323,633 | 59.98% |
| India | 883,188 | 40.02% |

**Training data (S2):**
| Country | Count | Percentage |
|---|---|---|
| US | 3,016,817 | 59.92% |
| India | 2,017,799 | 40.08% |

**Training data (S3):**
| Country | Count | Percentage |
|---|---|---|
| US | 3,170,056 | 59.97% |
| India | 2,115,547 | 40.03% |

> [!NOTE]
> The US:India ratio is remarkably stable across all three training sources (~60:40). This is likely by design.

**Test data (S1):**
| Country | Count | Percentage |
|---|---|---|
| India | 809,986 | 46.75% |
| US | 663,106 | 38.27% |
| **France** | **259,452** | **14.98%** |

**Test data (S2):**
| Country | Count | Percentage |
|---|---|---|
| India | 2,312,565 | 47.32% |
| US | 1,871,330 | 38.29% |
| France | 703,378 | 14.39% |

**Test data (S3):**
| Country | Count | Percentage |
|---|---|---|
| India | 2,405,000 | 47.32% |
| US | 1,945,701 | 38.28% |
| France | 731,615 | 14.40% |

> [!WARNING]
> **DISTRIBUTION SHIFT** — The test set has a dramatically different country composition:
> - US drops from 60% → 38%
> - India stays ~40% → 47%
> - France appears at ~15%, entirely unseen in training
> 
> Any model that overfits to US/India-specific patterns will fail on ~15% of the test S1 entities.

### 2.4 Missing Data Analysis

| Source | Empty Addresses | Total Records | Missing Rate |
|---|---|---|---|
| Train S1 | **0** | 2,206,821 | 0.00% |
| Train S2 | **168,967** | 5,034,616 | 3.36% |
| Train S3 | **175,916** | 5,285,603 | 3.33% |

- Source 1 (the reference) has **zero** missing addresses — it is the clean anchor.
- Sources 2 and 3 each have ~3.3% address missingness. For ~170K records, the model must rely on name-only matching (no address signal).
- No empty business names were found in any source.

### 2.5 Ground Truth Structure — Match Cardinality Distribution

| Matches per S1 Entity | Count | Percentage |
|---|---|---|
| 0 (singleton) | 123,247 | 5.58% |
| 1 | 119,157 | 5.40% |
| 2 | 375,212 | 17.00% |
| 3 | 530,841 | 24.05% |
| 4 | 484,115 | 21.93% |
| 5 | 321,957 | 14.59% |
| 6 | 164,868 | 7.47% |
| 7 | 63,968 | 2.90% |
| 8 | 18,680 | 0.85% |
| 9 | 4,205 | 0.19% |
| 10 | 534 | 0.02% |
| 11 | 37 | 0.002% |

**Key observations:**
- **Modal cardinality is 3** — the most common scenario is that an S1 entity matches 3 records in S2/S3.
- **~94.4% of entities have at least one match** — most S1 entities do match something.
- **5.58% are singletons** — correctly predicting empty for these contributes +123,247 to the numerator of the macro average.
- **Maximum cardinality is 11** — some entities have up to 11 matching records across S2 and S3.

### 2.6 S2/S3 Match Composition

| Composition | Count | Percentage |
|---|---|---|
| Has BOTH S2 and S3 matches | 1,776,047 | 85.26% |
| Only S2 matches (no S3) | 143,029 | 6.87% |
| Only S3 matches (no S2) | 164,498 | 7.90% |

- The **overwhelming majority (85%) have matches in BOTH sources**. The pipeline must search both S2 and S3 simultaneously.
- ~14% have matches in only one of the two sources.

### 2.7 Data Encoding & Character Set Observations

From byte-level inspection (`cat -v`):
- **Source 2 contains Devanagari (Hindi) script:** `राम मार्केटिंग प्राइवेट लिमिटेड` — these are UTF-8 encoded multi-byte characters.
- The `cat -v` output shows `M-^` escape sequences, confirming multi-byte UTF-8 characters (not ASCII).
- **Source 1 business names** appear to be primarily Latin-script (English for US, English for India, French for France).
- **Source 2 Indian names** can be in Devanagari script, requiring Unicode-aware string processing.
- **French names** contain diacritics: `Président`, `Léarning`, `Àmicale` — these are standard French characters (é, è, à) encoded as UTF-8.
- **Special characters observed:** `&` (ampersand), `<<` (angle brackets), `"and"` (quoted string), `.` (periods in abbreviations), `/` (slashes in addresses), `,` (commas in addresses).

### 2.8 Address Pattern Samples by Country

**US Pattern:** `"1795 Westchester Drive, High Point, NC"` → [number] [street] [city] [state abbrev]
**India Pattern:** `"797, Lake Town Block A, Kolkata, Howrah, West Bengal"` → [number] [locality] [city] [district] [state]
**India Complex:** `"H.No.16-11-23/37/A, 2Nd Floor, Flat No.207, Sagar Hotel Building, Opp.Rta Office, Mo, Osarambagh, Hyderabad, Telangana"` → landmark-based, extremely long
**France Pattern:** `"175 Boulevard du Président Franklin Roosevelt, Bordeaux, Nouvelle-Aquitaine"` → [number] [street type + name] [city] [region]
**Reordered:** `"IA, Iowa City, 1064 Newton Rd, Unit 11"` → state FIRST, then city, then address (inverted from standard)

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## LAYER 3: SUBMISSION VALIDATOR — [validate_submission.py](file:///Users/satyabratadas/Documents/ENTIVYRE/student_resource/utils/validate_submission.py) (350 lines)
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 3.1 File Metadata
- **Lines:** 350
- **Bytes:** 13,687
- **Python version:** 3.8+ (uses `f-strings`, `set()`, walrus-free)
- **Dependencies:** stdlib only (`argparse`, `os`, `sys`)

### 3.2 Constants (Lines 46–49)

```python
DELIM = "\t"
MAX_EXAMPLES = 5
MATCHING_HEADER = ["source1_entity_id", "matched_entity_ids"]
CANDIDATE_HEADER = ["source1_entity_id", "candidate_entity_ids"]
```

- `DELIM = "\t"` — hardcoded tab. The validator itself uses tab, confirming TSV.
- `MAX_EXAMPLES = 5` — error messages show at most 5 offending IDs.
- Headers are case-sensitive and exact. Must match character-for-character.

### 3.3 `read_ids()` Function (Lines 52–59)

```python
def read_ids(path):
    with open(path, encoding="utf-8") as f:
        next(f, None)  # skip header
        return {line.split(DELIM, 1)[0].strip() for line in f if line.strip()}
```

**Analysis:**
- Opens with explicit `encoding="utf-8"` — confirms UTF-8 requirement.
- Skips the first line (header).
- Splits each line by tab (`DELIM`), takes the first column (`[0]`), strips whitespace.
- Returns a `set` — deduplicates automatically.
- Ignores blank lines (`if line.strip()`).
- `split(DELIM, 1)` — splits on FIRST tab only. The `1` means maxsplit=1. This means even if a line has multiple tabs, only the first column is extracted.

### 3.4 Validation Error Categories (Lines 165–199)

The validator checks for **7 distinct error categories:**

| # | Category | Severity | Description |
|---|---|---|---|
| 1 | `dup_rows` | FAIL | Same `source1_entity_id` appears on multiple rows |
| 2 | `intra_dupes` | FAIL | Duplicate IDs within a single `matched_entity_ids` list |
| 3 | `self_matches` | FAIL | `matched_entity_ids` contains `S1-*` IDs |
| 4 | `wrong_prefix` | FAIL | IDs without `S2-` or `S3-` prefix |
| 5 | `unknown` | FAIL (only with `--check-ids`) | IDs not found in test Source-2/3 files |
| 6 | Missing S1 entities | FAIL | Required S1 entities not present in submission |
| 7 | Extra S1 entities | FAIL | Rows with S1 IDs not in the test set |

### 3.5 The CSV-vs-TSV Trap Detection (Lines 116–122)

```python
if DELIM not in header and "," in header:
    errors.append(
        f"{name}: header has no TAB but contains commas — the file looks "
        "COMMA-separated. ..."
    )
    return None
```

**This catches the #1 mistake:** a file saved as CSV instead of TSV. The validator explicitly detects this by checking for the absence of tabs AND presence of commas in the header.

### 3.6 The `--check-ids` Flag (Lines 30–39, 224–236)

- **OFF by default** — the validator does NOT check that matched IDs exist in the test set.
- Reason: loading all S2/S3 IDs costs "a few GB" on the full ~1.7M-entity test set.
- When ON: reads `test_source2.tsv` and `test_source3.tsv`, builds a set of valid IDs, checks every matched ID against it.
- "A missing/garbage matched ID only lowers your score rather than being rejected" — non-existent IDs don't cause rejection but do reduce precision.

### 3.7 Candidate-Matching Cross-Check (Lines 261–270)

```python
if matched is not None and candidate is not None:
    offenders = {
        s1 for s1, mids in matched.items() if mids - candidate.get(s1, set())
    }
```

- This is a **soft check** (WARNING, not FAIL).
- It verifies that every matched ID also appears in the candidate set.
- Set subtraction: `mids - candidate.get(s1, set())` — if any matched ID is NOT in candidates, it signals a pipeline bug.
- This enforces the invariant: **matches ⊆ candidates**.

### 3.8 UnicodeDecodeError Handling (Lines 319–329)

The validator catches `UnicodeDecodeError` explicitly:
- Suggests the file is "not valid UTF-8"
- Suggests common problems: `cp1252/Latin-1`, compressed files renamed to `.tsv`
- Gives the exact pandas incantation: `df.to_csv(path, sep='\\t', index=False, encoding='utf-8')`

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## LAYER 4: DOCUMENTATION TEMPLATE — [Documentation_template.md](file:///Users/satyabratadas/Documents/ENTIVYRE/student_resource/Documentation_template.md) (75 lines)
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 4.1 Required Sections (6 sections)

| Section | What Must Be Described |
|---|---|
| 1. Executive Summary | 2-3 sentence overview |
| 2. Methodology | Problem analysis + solution strategy |
| 3. Candidate Generation (Blocking) | Blocking keys, candidate count, recall preservation |
| 4. Matching Model | Features, model type, threshold method |
| 5. Results & Error Analysis | F₀.₅ score, FP/FN analysis |
| 6. Conclusion | 2-3 sentence summary |

### 4.2 Critical Fields That Must Be Filled

- **Approach Type:** `[Blocking + Classifier / End-to-End / Graph-Based / Hybrid, etc]`
- **Core Innovation:** a description of the main technical contribution
- **Blocking keys used:** must list specific keys (e.g., PIN code, phonetic name encoding, TF-IDF)
- **Candidate pairs generated:** must give a concrete number
- **Model type:** must name the model (XGBoost, Siamese Network, Transformer, etc.)
- **Threshold selection method:** must describe how the decision threshold was chosen

### 4.3 Appendix Requirements

- **Appendix A:** Code structure summary — must describe the entry point for reproducing outputs
- **Appendix B:** Additional charts, graphs, detailed results

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## LAYER 5: CRITICAL INVARIANTS & FAILURE MODES CATALOG
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 5.1 Data Contract Invariants

| Invariant | Source | Consequence of Violation |
|---|---|---|
| All files are UTF-8 encoded | Contract + Validator | `UnicodeDecodeError` → submission rejected |
| All files are tab-separated | Contract + Validator | "silently produces a single column" → wrong results |
| S1 entity_ids are unique (no duplicates) | Contract (deduplicated) | N/A — guaranteed by data |
| S2/S3 may have multiple records per entity | Data structure | Must handle 1:N matching |
| No common identifiers across sources | Contract | Cannot join on any key |
| Country is an open set | Contract | Hardcoding {US, India} → France entities fail |
| `matched_entity_ids` uses comma separator | Contract | Must split on `,` not `\t` |
| Empty `matched_entity_ids` = singleton | Contract | Must output empty string, not omit the row |

### 5.2 Submission Failure Modes (Ranked by Likelihood)

| # | Failure Mode | Detection | Fix |
|---|---|---|---|
| 1 | CSV instead of TSV | Validator catches | Use `sep="\t"` |
| 2 | Missing S1 entities in output | Validator catches | Ensure every S1-* from test_source1.tsv has a row |
| 3 | S1-* IDs in matched_entity_ids | Validator catches | Filter to S2/S3 only |
| 4 | Duplicate IDs in a list | Validator catches | Deduplicate per row |
| 5 | Non-UTF-8 encoding | Validator catches | Save with `encoding='utf-8'` |
| 6 | Wrong header names | Validator catches | Use exact column names |
| 7 | France entities omitted | Not caught by validator format check | Ensure no country filtering |
| 8 | Matched IDs not in candidate set | Validator warns (soft) | Ensure pipeline consistency |

### 5.3 Scoring Edge Cases

| Scenario | Precision | Recall | F₀.₅ |
|---|---|---|---|
| Perfect match (predict = truth) | 1.0 | 1.0 | 1.0 |
| Correct singleton (predict empty, truth empty) | N/A | N/A | 1.0 |
| False positive on singleton (predict match, truth empty) | 0.0 | N/A | 0.0 |
| All true matches found + 1 false positive (3 predicted, 2 true) | 0.667 | 1.0 | 0.714 |
| 1 true match found, 1 missed (1 predicted, 2 true) | 1.0 | 0.5 | 0.833 |
| Predict empty for entity with 3 true matches | N/A | 0.0 | 0.0 |

> [!TIP]
> **Strategic insight from the edge cases:** Missing a match (FN) costs less than adding a wrong match (FP). The scoring function punishes the entity in the last row (predict empty, miss all matches) with 0.0, but it also punishes a false positive on a singleton with 0.0. The sweet spot: **only emit matches you're highly confident about**.

---

*Continued in Part 2 → Master Implementation Plan Analysis (Chapters 1-20)*
*Continued in Part 3 → Master Implementation Plan Analysis (Chapters 21-40 + Appendices)*
