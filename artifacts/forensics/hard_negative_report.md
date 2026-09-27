# Phase 07: Hard Negative Engineering & Contradiction Veto Report

## Overview
Macro F0.5 heavily penalizes False Positives ($\beta = 0.5$, precision weighted $4\times$ more than recall in the denominator). Forensic inspection of false positive candidates in the validation split revealed three distinct archetypes of hard negatives that previously leaked past threshold.

## Hard Negative Archetypes Identified

### 1. Multi-Tenant Commercial Complex Collisions
- **Symptom:** Two distinct businesses in the same commercial plaza or office park (e.g., `#68/3/181` vs `#68/3/194` Nexsa Royal, Bangalore).
- **Mechanism:** Both entities share the parent plot/road numbers (`68` and `3`), creating a non-empty numeric intersection.
- **Solution:** Multi-unit numeric disambiguation. When both addresses contain multiple numeric tokens, we check both the leading building number and trailing sub-unit numbers. If specific unit numbers conflict (`181 != 194`), a hard building conflict veto is triggered.

### 2. Common-Name Empty-Address Floods
- **Symptom:** Entities with high name similarity (e.g. `Shakti Agro Limited`, `Lotus Media Private Limited`) where the candidate in `Source 2` or `Source 3` has an empty address string (`business_address == ""`).
- **Mechanism:** When `t_addr` was empty, the scoring function awarded a default neutral similarity of 0.50. For common corporate names occurring across multiple districts or states, 4–5 different entities received scores of 0.825 and were falsely merged into the anchor.
- **Solution:** Asymmetric address penalty. If the anchor has address evidence but the target has zero address evidence, the composite score is capped at `0.60 * name_sim` (score <= 0.60). Only candidates that actually corroborate address evidence can achieve top-tier scores.

### 3. Coworking / Shared Office Collisions
- **Symptom:** Two completely different businesses sharing an identical building/flat address (e.g. `Life Consultancy` and `Rama Labour` at `47/1A, S.N. Roy Road, Flat No. 8`).
- **Mechanism:** Pure address matching without name corroboration ($name\_sim == 0.0$) previously received high composite scores ($0.85+$) due to strong address token overlap.
- **Solution:** Strict address-only threshold. Address-only matching without any Latin name overlap is restricted to ultra-high similarity (>= 0.90) and requires affirmative building number match without contradictory legal/business-type descriptors.
