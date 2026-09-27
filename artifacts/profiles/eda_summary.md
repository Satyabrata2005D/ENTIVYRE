# ENTIVYRE Exploratory Data Analysis & Profiling Summary
**Date:** 2026-09-25T12:51:06Z | **Runtime:** 2.78s

## 1. Ground Truth Multiplicity Distribution
- **Total S1 Anchors:** 50,000
- **Total Matches:** 172,731
- **Singletons (0 matches):** 2,820 (5.64%)
- **Single Matches (1 match):** 2,647 (5.294%)
- **Multi Matches (>=2 matches):** 44,533 (89.066%)
- **Max Matches for Single S1:** 11
- **Mean Matches per S1:** 3.46
- **Matches S2 only:** 3,240
- **Matches S3 only:** 3,600
- **Matches BOTH S2 and S3:** 40,340

## 2. Source Missingness & Text Distributions

| File | Total Records | Missing Addr % | Mean Name Chars | Devanagari Names | URL Names |
|---|---|---|---|---|---|
| `test_source1` | 50,000 | 0.00% | 23.83 | 0 | 0 |
| `test_source2` | 50,000 | 2.66% | 25.71 | 3,209 | 1,503 |
| `test_source3` | 50,000 | 2.76% | 25.74 | 1,751 | 1,566 |
| `train_source1` | 50,000 | 0.00% | 24.07 | 0 | 0 |
| `train_source2` | 50,000 | 3.36% | 25.03 | 2,566 | 1,956 |
| `train_source3` | 50,000 | 3.48% | 25.21 | 1,516 | 1,989 |
