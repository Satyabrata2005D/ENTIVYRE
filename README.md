# ENTIVYRE: Business Entity Resolution Pipeline

**Amazon ML Challenge 2026 Submission System**

ENTIVYRE is an end-to-end, high-performance, air-gapped business entity resolution pipeline designed to resolve enterprise entities across three noisy, heterogeneous data sources (Source 1 reference anchor vs. Sources 2 and 3).

## Key Architecture & Guarantees
- **Strict Immuntability:** Raw dataset files (`student_resource/dataset/`) are strictly read-only and preserved untouched.
- **Air-Gapped Operation:** Zero external network calls, zero external geocoding, and zero third-party commercial registries.
- **Contract Enforcement:** Strictly compliant with `matching_results.tsv` and `candidate_pairs.tsv` contracts.
- **Macro $F_{0.5}$ Optimization:** Optimized for high-precision entity resolution with official singleton credit rules.
- **Streaming & Low-Memory:** Chunked ingestion and bounded candidate generation ($K \le 50$) preventing out-of-memory errors on 26M+ records.

## Directory Structure
```
ENTIVYRE/
├── configs/                              # Central YAML & configuration presets
│   ├── base.yaml                         # Master base configuration
│   ├── validation.yaml                   # Validation & cross-validation settings
│   └── inference.yaml                    # Full-scale test inference settings
├── code/                                 # Official submission code directory
│   └── business_entity_resolution/
│       ├── src/ber/                      # Core BER engine package
│       ├── tests/                        # Subpackage tests
│       ├── requirements.txt              # Pinned dependencies
│       └── README.md                     # Code module instructions
├── entivyre/                             # Modular Python package
│   ├── contracts/                        # Schemas, verifiers, metrics, rules
│   ├── utils/                            # Structured logging and helpers
│   └── config.py                         # Typed immutable config dataclasses
├── artifacts/                            # Derived intermediate artifacts & reports
├── output/                               # Official submission outputs
│   ├── matching_results.tsv              # S1 -> matched S2/S3 IDs
│   └── candidate_pairs.tsv               # S1 -> candidate S2/S3 IDs
├── docs/                                 # Methodology, experiment & decision logs
│   ├── methodology.md                    # Official solution methodology document
│   ├── experiment_log.md                 # Complete experiment tracking log
│   └── decision_log.md                   # Architectural and algorithmic decisions
└── scripts/                              # Executable pipeline CLI scripts
```

## Quick Start
```bash
# 1. Run readiness check
python3 scripts/check_readiness.py

# 2. Run unit and integration tests
python3 -m unittest discover tests
```
