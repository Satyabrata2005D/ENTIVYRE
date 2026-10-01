# Business Entity Resolution Engine (`ber`)
**UNPAID ENGINEERS — Official Submission Codebase for Amazon ML Challenge 2026**

---

## 1. System Overview
`ber` is a high-throughput, pure-Python Business Entity Resolution (BER) system designed to resolve entities across three heterogeneous, noisy data sources ($S_1$ reference anchors vs. $S_2$ and $S_3$ noisy scraped web sources).

The pipeline strictly guarantees:
1. **Official Competition Metric ($F_{0.5}$):** Precision-heavy matching with full 1.0 singleton credit on true unlinked entities.
2. **Candidate-Subset Invariant:** $\text{matching\_results.tsv} \subseteq \text{candidate\_pairs.tsv}$.
3. **Open-Set Robustness:** Handles unseen test countries (such as France) seamlessly.
4. **Air-Gapped Compliance:** Zero external network requests, commercial APIs, or geocoding lookups.
5. **Constant Memory Footprint:** Streaming $O(1)$ memory execution processing 1.73M test records with < 100 MB RSS memory.

---

## 2. Directory Architecture
```
code/business_entity_resolution/
├── src/
│   └── ber/
│       ├── io/             # Chunked streaming TSV readers & writers
│       ├── validation/     # Schema integrity & official submission validator bridge
│       ├── normalization/  # Transliteration, legal suffix canonicalizer, address normalizer, open-set country mapper
│       ├── blocking/       # Multi-key inverted index blocking engine
│       ├── retrieval/      # Pure-Python character 3-gram sparse TF-IDF cosine retriever
│       ├── features/       # 33-dimensional typed FeatureRegistry & extraction pipeline
│       ├── models/         # Deterministic baseline, calibrated logistic regression, boosted decision stumps
│       ├── decision/       # Calibrated threshold optimizer (tau*=0.70) & singleton matcher
│       ├── evaluation/     # Entity-grouped validation splitter & forensic error analyzer
│       ├── experiments/    # 5-way architectural ablation engine
│       ├── inference/      # High-throughput streaming test inference engine
│       ├── security/       # Air-gapped network isolation guard & static fair-play auditor
│       ├── outputs/        # Strict TSV serializer & format validator
│       └── utils/          # Profiler, logger, and memory monitor
├── README.md               # End-to-end reproduction guide
└── requirements.txt        # Environment specification (Python 3.8+ standard library)
```

---

## 3. End-to-End Reproduction Instructions

To reproduce `output/matching_results.tsv` and `output/candidate_pairs.tsv` from the test dataset:

### Step 1: Set Environment
```bash
export PYTHONPATH="src:${PYTHONPATH}"
```

### Step 2: Run Test Inference Pipeline
From the submission root directory:
```bash
python3 -m ber.inference.engine \
    --test-dir student_resource/dataset/test \
    --output-dir output
```
Or use the convenience CLI runner:
```bash
python3 scripts/run_test_inference.py \
    --test-dir student_resource/dataset/test \
    --output-dir output
```

### Step 3: Validate Outputs with Official Validator
```bash
python3 scripts/run_official_validator.py \
    --matching output/matching_results.tsv \
    --candidate output/candidate_pairs.tsv \
    --test-dir student_resource/dataset/test
```

---

## 4. Running the Test Suite
The codebase includes 151 unit, integration, adversarial, and contract tests:
```bash
PYTHONPATH=src python3 -m unittest discover tests
```
All tests pass in < 0.25 seconds with 100% standard library compliance.
