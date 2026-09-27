# Phase 05: Normalization Exhaustion Report

## Overview
Phase 05 requires building exhaustive, multi-tier normalized representations across business names, addresses, and geographic tokens to ensure that neither noise nor format shift prevents matching.

## Name Normalization Architecture

1. **Domain & URL Unmasking:**
   - **Problem in CHAMPION_001:** Any entity with a web domain or URL in `Source 2` or `Source 3` (e.g., `maurewilliamscolombier.com`, `zanderblue.com`) was matched by `URL_REGEX` and erased completely to an empty string. Over 412,000 domain targets were destroyed.
   - **Solution in CHALLENGER_002:** Regex protocol stripping (`https?://(?:www\.)?`) and TLD stripping (`\.(?:com|org|net|in|fr|co|io|biz|info)`) preserves the unmasked root (`maurewilliamscolombier`, `zanderblue`), mapping directly to the Latin anchor tokens.

2. **Honorific & Title Prefix Stripping:**
   - **Problem in CHAMPION_001:** Indian business names frequently prefix titles (`M/s`, `Shri`, `Sri`, `Smt`, `Dr.`, `Er.`, `Late`). This displaced Token 0, preventing 2-token prefix keys (`NP:m_s` vs `NP:burger_solution`) from matching.
   - **Solution in CHALLENGER_002:** Standardized regex stripping aligns Token 0 to the actual distinctive business word.

3. **Multi-representation Hierarchy:**
   - `RAW`: Exact input preserved verbatim.
   - `CLEAN`: Lowercase, non-alphanumeric stripped, whitespace collapsed.
   - `CANONICAL`: Legal suffixes stripped (`pvt ltd`, `inc`, `llc`, etc.) and mapped to canonical roots.
   - `TOKENS`: Word tokens of length >= 2 (preserving acronyms like `RJ`, `IJ`, `CW`).
   - `TOKENS_SORTED`: Word-order invariant token tuple.
   - `CONCAT_ROOT`: Concatenated clean tokens for matching against compound domain strings.

## Address Normalization Architecture

1. **Numeric Normalization (Leading Zero Stripping):**
   - **Problem in CHAMPION_001:** Indian addresses frequently format street/plot numbers with leading zeros (e.g. `AF-0684` vs `Af-684`). String comparison marked these as contradictory disjoint numbers, vetoing true matches.
   - **Solution in CHALLENGER_002:** Normalizes numeric tokens by stripping leading zeros (`t.lstrip('0') or '0'`), ensuring `0684 == 684`.

2. **French Thoroughfare Abbreviations:**
   - France represents **14.98% of the test set** (unseen in training).
   - Added bidirectional French abbreviations: `rue`, `impasse` -> `imp`, `passage` -> `pas`, `cours` -> `crs`, `quai`, `allee` -> `all`, `chemin` -> `ch`, `zone industrielle` -> `zi`.

3. **Component Isolation:**
   - `postal_code`: Extracted 5-digit (US/FR) or 6-digit (IN) postal code.
   - `numeric_tokens`: Sorted, zero-stripped numeric tokens representing building/unit numbers.
   - `distinctive_words`: Address words of length >= 4 excluding standardized stopwords and generic street labels.
