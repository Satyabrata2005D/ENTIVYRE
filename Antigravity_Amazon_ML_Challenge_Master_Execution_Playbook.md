# ANTIGRAVITY - AMAZON ML CHALLENGE MASTER EXECUTION PLAYBOOK
This is the agent-facing companion to the large implementation plan. It is written as a build contract. The agent must implement the project incrementally, preserve the official challenge contract, and refuse any design that violates the challenge rules.
## Global agent rules
- Read the official challenge statement before changing architecture.
- Treat the uploaded challenge specification as authoritative for requirements.
- Treat advanced model/algorithm choices as experiments, not requirements.
- Never use external business databases, entity-resolution APIs, government registries, geocoding APIs, or internet-based entity augmentation.
- Keep raw inputs immutable.
- Every stage must be deterministic when given the same inputs, configuration, and seed.
- Every stage must have tests and a machine-readable artifact/log.
- Never silently discard rows because of memory pressure. Change batching or candidate strategy and measure the effect.
- Do not add a dependency without license/resource justification.
- Before declaring done, run the relevant tests and report exact commands and results.

# PHASE 01 - Specification and Contract
**Scope:** requirements matrix, exact output rules, fair play, licensing.

## 01.1 Agent task
### Objective
Implement the next smallest complete increment for **Specification and Contract**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 01.2 Agent task
### Objective
Implement the next smallest complete increment for **Specification and Contract**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 01.3 Agent task
### Objective
Implement the next smallest complete increment for **Specification and Contract**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 01.4 Agent task
### Objective
Implement the next smallest complete increment for **Specification and Contract**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 01.5 Agent task
### Objective
Implement the next smallest complete increment for **Specification and Contract**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 01.6 Agent task
### Objective
Implement the next smallest complete increment for **Specification and Contract**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 01.7 Agent task
### Objective
Implement the next smallest complete increment for **Specification and Contract**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 01.8 Agent task
### Objective
Implement the next smallest complete increment for **Specification and Contract**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 01.9 Agent task
### Objective
Implement the next smallest complete increment for **Specification and Contract**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 01.10 Agent task
### Objective
Implement the next smallest complete increment for **Specification and Contract**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 02 - Repository Bootstrap
**Scope:** folders, configs, package layout, tests, logging.

## 02.1 Agent task
### Objective
Implement the next smallest complete increment for **Repository Bootstrap**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 02.2 Agent task
### Objective
Implement the next smallest complete increment for **Repository Bootstrap**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 02.3 Agent task
### Objective
Implement the next smallest complete increment for **Repository Bootstrap**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 02.4 Agent task
### Objective
Implement the next smallest complete increment for **Repository Bootstrap**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 02.5 Agent task
### Objective
Implement the next smallest complete increment for **Repository Bootstrap**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 02.6 Agent task
### Objective
Implement the next smallest complete increment for **Repository Bootstrap**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 02.7 Agent task
### Objective
Implement the next smallest complete increment for **Repository Bootstrap**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 02.8 Agent task
### Objective
Implement the next smallest complete increment for **Repository Bootstrap**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 02.9 Agent task
### Objective
Implement the next smallest complete increment for **Repository Bootstrap**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 02.10 Agent task
### Objective
Implement the next smallest complete increment for **Repository Bootstrap**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 03 - Dataset Manifest
**Scope:** file checksums, sizes, row counts, schema manifest.

## 03.1 Agent task
### Objective
Implement the next smallest complete increment for **Dataset Manifest**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 03.2 Agent task
### Objective
Implement the next smallest complete increment for **Dataset Manifest**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 03.3 Agent task
### Objective
Implement the next smallest complete increment for **Dataset Manifest**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 03.4 Agent task
### Objective
Implement the next smallest complete increment for **Dataset Manifest**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 03.5 Agent task
### Objective
Implement the next smallest complete increment for **Dataset Manifest**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 03.6 Agent task
### Objective
Implement the next smallest complete increment for **Dataset Manifest**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 03.7 Agent task
### Objective
Implement the next smallest complete increment for **Dataset Manifest**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 03.8 Agent task
### Objective
Implement the next smallest complete increment for **Dataset Manifest**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 03.9 Agent task
### Objective
Implement the next smallest complete increment for **Dataset Manifest**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 03.10 Agent task
### Objective
Implement the next smallest complete increment for **Dataset Manifest**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 04 - Ingestion Engine
**Scope:** TSV parsing, chunking, dtypes, malformed row handling.

## 04.1 Agent task
### Objective
Implement the next smallest complete increment for **Ingestion Engine**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 04.2 Agent task
### Objective
Implement the next smallest complete increment for **Ingestion Engine**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 04.3 Agent task
### Objective
Implement the next smallest complete increment for **Ingestion Engine**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 04.4 Agent task
### Objective
Implement the next smallest complete increment for **Ingestion Engine**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 04.5 Agent task
### Objective
Implement the next smallest complete increment for **Ingestion Engine**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 04.6 Agent task
### Objective
Implement the next smallest complete increment for **Ingestion Engine**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 04.7 Agent task
### Objective
Implement the next smallest complete increment for **Ingestion Engine**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 04.8 Agent task
### Objective
Implement the next smallest complete increment for **Ingestion Engine**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 04.9 Agent task
### Objective
Implement the next smallest complete increment for **Ingestion Engine**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 04.10 Agent task
### Objective
Implement the next smallest complete increment for **Ingestion Engine**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 05 - Data Validation
**Scope:** schema, IDs, source prefixes, missingness.

## 05.1 Agent task
### Objective
Implement the next smallest complete increment for **Data Validation**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 05.2 Agent task
### Objective
Implement the next smallest complete increment for **Data Validation**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 05.3 Agent task
### Objective
Implement the next smallest complete increment for **Data Validation**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 05.4 Agent task
### Objective
Implement the next smallest complete increment for **Data Validation**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 05.5 Agent task
### Objective
Implement the next smallest complete increment for **Data Validation**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 05.6 Agent task
### Objective
Implement the next smallest complete increment for **Data Validation**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 05.7 Agent task
### Objective
Implement the next smallest complete increment for **Data Validation**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 05.8 Agent task
### Objective
Implement the next smallest complete increment for **Data Validation**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 05.9 Agent task
### Objective
Implement the next smallest complete increment for **Data Validation**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 05.10 Agent task
### Objective
Implement the next smallest complete increment for **Data Validation**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 06 - Profiling
**Scope:** distributions, duplicates, noise, training label statistics.

## 06.1 Agent task
### Objective
Implement the next smallest complete increment for **Profiling**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 06.2 Agent task
### Objective
Implement the next smallest complete increment for **Profiling**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 06.3 Agent task
### Objective
Implement the next smallest complete increment for **Profiling**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 06.4 Agent task
### Objective
Implement the next smallest complete increment for **Profiling**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 06.5 Agent task
### Objective
Implement the next smallest complete increment for **Profiling**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 06.6 Agent task
### Objective
Implement the next smallest complete increment for **Profiling**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 06.7 Agent task
### Objective
Implement the next smallest complete increment for **Profiling**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 06.8 Agent task
### Objective
Implement the next smallest complete increment for **Profiling**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 06.9 Agent task
### Objective
Implement the next smallest complete increment for **Profiling**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 06.10 Agent task
### Objective
Implement the next smallest complete increment for **Profiling**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 07 - Normalization Core
**Scope:** raw/canonical/token/character representations.

## 07.1 Agent task
### Objective
Implement the next smallest complete increment for **Normalization Core**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 07.2 Agent task
### Objective
Implement the next smallest complete increment for **Normalization Core**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 07.3 Agent task
### Objective
Implement the next smallest complete increment for **Normalization Core**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 07.4 Agent task
### Objective
Implement the next smallest complete increment for **Normalization Core**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 07.5 Agent task
### Objective
Implement the next smallest complete increment for **Normalization Core**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 07.6 Agent task
### Objective
Implement the next smallest complete increment for **Normalization Core**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 07.7 Agent task
### Objective
Implement the next smallest complete increment for **Normalization Core**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 07.8 Agent task
### Objective
Implement the next smallest complete increment for **Normalization Core**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 07.9 Agent task
### Objective
Implement the next smallest complete increment for **Normalization Core**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 07.10 Agent task
### Objective
Implement the next smallest complete increment for **Normalization Core**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 08 - Address Intelligence
**Scope:** numbers, abbreviations, landmarks, components.

## 08.1 Agent task
### Objective
Implement the next smallest complete increment for **Address Intelligence**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 08.2 Agent task
### Objective
Implement the next smallest complete increment for **Address Intelligence**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 08.3 Agent task
### Objective
Implement the next smallest complete increment for **Address Intelligence**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 08.4 Agent task
### Objective
Implement the next smallest complete increment for **Address Intelligence**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 08.5 Agent task
### Objective
Implement the next smallest complete increment for **Address Intelligence**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 08.6 Agent task
### Objective
Implement the next smallest complete increment for **Address Intelligence**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 08.7 Agent task
### Objective
Implement the next smallest complete increment for **Address Intelligence**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 08.8 Agent task
### Objective
Implement the next smallest complete increment for **Address Intelligence**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 08.9 Agent task
### Objective
Implement the next smallest complete increment for **Address Intelligence**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 08.10 Agent task
### Objective
Implement the next smallest complete increment for **Address Intelligence**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 09 - Country Open Set
**Scope:** generic country handling, France regression.

## 09.1 Agent task
### Objective
Implement the next smallest complete increment for **Country Open Set**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 09.2 Agent task
### Objective
Implement the next smallest complete increment for **Country Open Set**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 09.3 Agent task
### Objective
Implement the next smallest complete increment for **Country Open Set**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 09.4 Agent task
### Objective
Implement the next smallest complete increment for **Country Open Set**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 09.5 Agent task
### Objective
Implement the next smallest complete increment for **Country Open Set**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 09.6 Agent task
### Objective
Implement the next smallest complete increment for **Country Open Set**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 09.7 Agent task
### Objective
Implement the next smallest complete increment for **Country Open Set**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 09.8 Agent task
### Objective
Implement the next smallest complete increment for **Country Open Set**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 09.9 Agent task
### Objective
Implement the next smallest complete increment for **Country Open Set**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 09.10 Agent task
### Objective
Implement the next smallest complete increment for **Country Open Set**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 10 - Ground Truth Builder
**Scope:** multi-ID labels, pair labels, negatives, singletons.

## 10.1 Agent task
### Objective
Implement the next smallest complete increment for **Ground Truth Builder**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 10.2 Agent task
### Objective
Implement the next smallest complete increment for **Ground Truth Builder**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 10.3 Agent task
### Objective
Implement the next smallest complete increment for **Ground Truth Builder**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 10.4 Agent task
### Objective
Implement the next smallest complete increment for **Ground Truth Builder**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 10.5 Agent task
### Objective
Implement the next smallest complete increment for **Ground Truth Builder**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 10.6 Agent task
### Objective
Implement the next smallest complete increment for **Ground Truth Builder**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 10.7 Agent task
### Objective
Implement the next smallest complete increment for **Ground Truth Builder**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 10.8 Agent task
### Objective
Implement the next smallest complete increment for **Ground Truth Builder**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 10.9 Agent task
### Objective
Implement the next smallest complete increment for **Ground Truth Builder**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 10.10 Agent task
### Objective
Implement the next smallest complete increment for **Ground Truth Builder**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 11 - Validation Split
**Scope:** entity-aware split and frozen validation.

## 11.1 Agent task
### Objective
Implement the next smallest complete increment for **Validation Split**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 11.2 Agent task
### Objective
Implement the next smallest complete increment for **Validation Split**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 11.3 Agent task
### Objective
Implement the next smallest complete increment for **Validation Split**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 11.4 Agent task
### Objective
Implement the next smallest complete increment for **Validation Split**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 11.5 Agent task
### Objective
Implement the next smallest complete increment for **Validation Split**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 11.6 Agent task
### Objective
Implement the next smallest complete increment for **Validation Split**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 11.7 Agent task
### Objective
Implement the next smallest complete increment for **Validation Split**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 11.8 Agent task
### Objective
Implement the next smallest complete increment for **Validation Split**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 11.9 Agent task
### Objective
Implement the next smallest complete increment for **Validation Split**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 11.10 Agent task
### Objective
Implement the next smallest complete increment for **Validation Split**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 12 - Blocking Baseline
**Scope:** exact and token blocking.

## 12.1 Agent task
### Objective
Implement the next smallest complete increment for **Blocking Baseline**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 12.2 Agent task
### Objective
Implement the next smallest complete increment for **Blocking Baseline**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 12.3 Agent task
### Objective
Implement the next smallest complete increment for **Blocking Baseline**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 12.4 Agent task
### Objective
Implement the next smallest complete increment for **Blocking Baseline**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 12.5 Agent task
### Objective
Implement the next smallest complete increment for **Blocking Baseline**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 12.6 Agent task
### Objective
Implement the next smallest complete increment for **Blocking Baseline**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 12.7 Agent task
### Objective
Implement the next smallest complete increment for **Blocking Baseline**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 12.8 Agent task
### Objective
Implement the next smallest complete increment for **Blocking Baseline**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 12.9 Agent task
### Objective
Implement the next smallest complete increment for **Blocking Baseline**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 12.10 Agent task
### Objective
Implement the next smallest complete increment for **Blocking Baseline**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 13 - Character Retrieval
**Scope:** n-gram TF-IDF sparse retrieval.

## 13.1 Agent task
### Objective
Implement the next smallest complete increment for **Character Retrieval**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 13.2 Agent task
### Objective
Implement the next smallest complete increment for **Character Retrieval**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 13.3 Agent task
### Objective
Implement the next smallest complete increment for **Character Retrieval**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 13.4 Agent task
### Objective
Implement the next smallest complete increment for **Character Retrieval**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 13.5 Agent task
### Objective
Implement the next smallest complete increment for **Character Retrieval**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 13.6 Agent task
### Objective
Implement the next smallest complete increment for **Character Retrieval**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 13.7 Agent task
### Objective
Implement the next smallest complete increment for **Character Retrieval**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 13.8 Agent task
### Objective
Implement the next smallest complete increment for **Character Retrieval**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 13.9 Agent task
### Objective
Implement the next smallest complete increment for **Character Retrieval**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 13.10 Agent task
### Objective
Implement the next smallest complete increment for **Character Retrieval**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 14 - Multi-pass Candidate Union
**Scope:** union, dedupe, provenance, candidate budget.

## 14.1 Agent task
### Objective
Implement the next smallest complete increment for **Multi-pass Candidate Union**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 14.2 Agent task
### Objective
Implement the next smallest complete increment for **Multi-pass Candidate Union**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 14.3 Agent task
### Objective
Implement the next smallest complete increment for **Multi-pass Candidate Union**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 14.4 Agent task
### Objective
Implement the next smallest complete increment for **Multi-pass Candidate Union**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 14.5 Agent task
### Objective
Implement the next smallest complete increment for **Multi-pass Candidate Union**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 14.6 Agent task
### Objective
Implement the next smallest complete increment for **Multi-pass Candidate Union**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 14.7 Agent task
### Objective
Implement the next smallest complete increment for **Multi-pass Candidate Union**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 14.8 Agent task
### Objective
Implement the next smallest complete increment for **Multi-pass Candidate Union**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 14.9 Agent task
### Objective
Implement the next smallest complete increment for **Multi-pass Candidate Union**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 14.10 Agent task
### Objective
Implement the next smallest complete increment for **Multi-pass Candidate Union**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 15 - Candidate Audit
**Scope:** recall ceiling, reduction ratio, missed-match analysis.

## 15.1 Agent task
### Objective
Implement the next smallest complete increment for **Candidate Audit**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 15.2 Agent task
### Objective
Implement the next smallest complete increment for **Candidate Audit**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 15.3 Agent task
### Objective
Implement the next smallest complete increment for **Candidate Audit**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 15.4 Agent task
### Objective
Implement the next smallest complete increment for **Candidate Audit**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 15.5 Agent task
### Objective
Implement the next smallest complete increment for **Candidate Audit**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 15.6 Agent task
### Objective
Implement the next smallest complete increment for **Candidate Audit**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 15.7 Agent task
### Objective
Implement the next smallest complete increment for **Candidate Audit**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 15.8 Agent task
### Objective
Implement the next smallest complete increment for **Candidate Audit**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 15.9 Agent task
### Objective
Implement the next smallest complete increment for **Candidate Audit**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 15.10 Agent task
### Objective
Implement the next smallest complete increment for **Candidate Audit**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 16 - Feature Registry
**Scope:** definitions, provenance, schemas.

## 16.1 Agent task
### Objective
Implement the next smallest complete increment for **Feature Registry**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 16.2 Agent task
### Objective
Implement the next smallest complete increment for **Feature Registry**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 16.3 Agent task
### Objective
Implement the next smallest complete increment for **Feature Registry**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 16.4 Agent task
### Objective
Implement the next smallest complete increment for **Feature Registry**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 16.5 Agent task
### Objective
Implement the next smallest complete increment for **Feature Registry**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 16.6 Agent task
### Objective
Implement the next smallest complete increment for **Feature Registry**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 16.7 Agent task
### Objective
Implement the next smallest complete increment for **Feature Registry**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 16.8 Agent task
### Objective
Implement the next smallest complete increment for **Feature Registry**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 16.9 Agent task
### Objective
Implement the next smallest complete increment for **Feature Registry**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 16.10 Agent task
### Objective
Implement the next smallest complete increment for **Feature Registry**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 17 - Similarity Features
**Scope:** Jaccard, Levenshtein, overlap, exact signals.

## 17.1 Agent task
### Objective
Implement the next smallest complete increment for **Similarity Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 17.2 Agent task
### Objective
Implement the next smallest complete increment for **Similarity Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 17.3 Agent task
### Objective
Implement the next smallest complete increment for **Similarity Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 17.4 Agent task
### Objective
Implement the next smallest complete increment for **Similarity Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 17.5 Agent task
### Objective
Implement the next smallest complete increment for **Similarity Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 17.6 Agent task
### Objective
Implement the next smallest complete increment for **Similarity Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 17.7 Agent task
### Objective
Implement the next smallest complete increment for **Similarity Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 17.8 Agent task
### Objective
Implement the next smallest complete increment for **Similarity Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 17.9 Agent task
### Objective
Implement the next smallest complete increment for **Similarity Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 17.10 Agent task
### Objective
Implement the next smallest complete increment for **Similarity Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 18 - TF-IDF Features
**Scope:** name/address cosine and sparse feature extraction.

## 18.1 Agent task
### Objective
Implement the next smallest complete increment for **TF-IDF Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 18.2 Agent task
### Objective
Implement the next smallest complete increment for **TF-IDF Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 18.3 Agent task
### Objective
Implement the next smallest complete increment for **TF-IDF Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 18.4 Agent task
### Objective
Implement the next smallest complete increment for **TF-IDF Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 18.5 Agent task
### Objective
Implement the next smallest complete increment for **TF-IDF Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 18.6 Agent task
### Objective
Implement the next smallest complete increment for **TF-IDF Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 18.7 Agent task
### Objective
Implement the next smallest complete increment for **TF-IDF Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 18.8 Agent task
### Objective
Implement the next smallest complete increment for **TF-IDF Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 18.9 Agent task
### Objective
Implement the next smallest complete increment for **TF-IDF Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 18.10 Agent task
### Objective
Implement the next smallest complete increment for **TF-IDF Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 19 - Address Features
**Scope:** numeric and structural signals.

## 19.1 Agent task
### Objective
Implement the next smallest complete increment for **Address Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 19.2 Agent task
### Objective
Implement the next smallest complete increment for **Address Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 19.3 Agent task
### Objective
Implement the next smallest complete increment for **Address Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 19.4 Agent task
### Objective
Implement the next smallest complete increment for **Address Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 19.5 Agent task
### Objective
Implement the next smallest complete increment for **Address Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 19.6 Agent task
### Objective
Implement the next smallest complete increment for **Address Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 19.7 Agent task
### Objective
Implement the next smallest complete increment for **Address Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 19.8 Agent task
### Objective
Implement the next smallest complete increment for **Address Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 19.9 Agent task
### Objective
Implement the next smallest complete increment for **Address Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 19.10 Agent task
### Objective
Implement the next smallest complete increment for **Address Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 20 - Cross-field Features
**Scope:** joint evidence and contradiction features.

## 20.1 Agent task
### Objective
Implement the next smallest complete increment for **Cross-field Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 20.2 Agent task
### Objective
Implement the next smallest complete increment for **Cross-field Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 20.3 Agent task
### Objective
Implement the next smallest complete increment for **Cross-field Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 20.4 Agent task
### Objective
Implement the next smallest complete increment for **Cross-field Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 20.5 Agent task
### Objective
Implement the next smallest complete increment for **Cross-field Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 20.6 Agent task
### Objective
Implement the next smallest complete increment for **Cross-field Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 20.7 Agent task
### Objective
Implement the next smallest complete increment for **Cross-field Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 20.8 Agent task
### Objective
Implement the next smallest complete increment for **Cross-field Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 20.9 Agent task
### Objective
Implement the next smallest complete increment for **Cross-field Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 20.10 Agent task
### Objective
Implement the next smallest complete increment for **Cross-field Features**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 21 - Deterministic Baseline
**Scope:** transparent rules and baseline score.

## 21.1 Agent task
### Objective
Implement the next smallest complete increment for **Deterministic Baseline**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 21.2 Agent task
### Objective
Implement the next smallest complete increment for **Deterministic Baseline**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 21.3 Agent task
### Objective
Implement the next smallest complete increment for **Deterministic Baseline**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 21.4 Agent task
### Objective
Implement the next smallest complete increment for **Deterministic Baseline**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 21.5 Agent task
### Objective
Implement the next smallest complete increment for **Deterministic Baseline**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 21.6 Agent task
### Objective
Implement the next smallest complete increment for **Deterministic Baseline**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 21.7 Agent task
### Objective
Implement the next smallest complete increment for **Deterministic Baseline**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 21.8 Agent task
### Objective
Implement the next smallest complete increment for **Deterministic Baseline**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 21.9 Agent task
### Objective
Implement the next smallest complete increment for **Deterministic Baseline**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 21.10 Agent task
### Objective
Implement the next smallest complete increment for **Deterministic Baseline**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 22 - Supervised Dataset
**Scope:** candidate-aware pair table.

## 22.1 Agent task
### Objective
Implement the next smallest complete increment for **Supervised Dataset**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 22.2 Agent task
### Objective
Implement the next smallest complete increment for **Supervised Dataset**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 22.3 Agent task
### Objective
Implement the next smallest complete increment for **Supervised Dataset**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 22.4 Agent task
### Objective
Implement the next smallest complete increment for **Supervised Dataset**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 22.5 Agent task
### Objective
Implement the next smallest complete increment for **Supervised Dataset**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 22.6 Agent task
### Objective
Implement the next smallest complete increment for **Supervised Dataset**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 22.7 Agent task
### Objective
Implement the next smallest complete increment for **Supervised Dataset**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 22.8 Agent task
### Objective
Implement the next smallest complete increment for **Supervised Dataset**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 22.9 Agent task
### Objective
Implement the next smallest complete increment for **Supervised Dataset**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 22.10 Agent task
### Objective
Implement the next smallest complete increment for **Supervised Dataset**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 23 - Model Training
**Scope:** classifier pipeline and reproducibility.

## 23.1 Agent task
### Objective
Implement the next smallest complete increment for **Model Training**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 23.2 Agent task
### Objective
Implement the next smallest complete increment for **Model Training**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 23.3 Agent task
### Objective
Implement the next smallest complete increment for **Model Training**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 23.4 Agent task
### Objective
Implement the next smallest complete increment for **Model Training**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 23.5 Agent task
### Objective
Implement the next smallest complete increment for **Model Training**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 23.6 Agent task
### Objective
Implement the next smallest complete increment for **Model Training**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 23.7 Agent task
### Objective
Implement the next smallest complete increment for **Model Training**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 23.8 Agent task
### Objective
Implement the next smallest complete increment for **Model Training**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 23.9 Agent task
### Objective
Implement the next smallest complete increment for **Model Training**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 23.10 Agent task
### Objective
Implement the next smallest complete increment for **Model Training**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 24 - Tree Models
**Scope:** boosting experiments and license gate.

## 24.1 Agent task
### Objective
Implement the next smallest complete increment for **Tree Models**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 24.2 Agent task
### Objective
Implement the next smallest complete increment for **Tree Models**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 24.3 Agent task
### Objective
Implement the next smallest complete increment for **Tree Models**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 24.4 Agent task
### Objective
Implement the next smallest complete increment for **Tree Models**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 24.5 Agent task
### Objective
Implement the next smallest complete increment for **Tree Models**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 24.6 Agent task
### Objective
Implement the next smallest complete increment for **Tree Models**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 24.7 Agent task
### Objective
Implement the next smallest complete increment for **Tree Models**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 24.8 Agent task
### Objective
Implement the next smallest complete increment for **Tree Models**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 24.9 Agent task
### Objective
Implement the next smallest complete increment for **Tree Models**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 24.10 Agent task
### Objective
Implement the next smallest complete increment for **Tree Models**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 25 - Threshold Search
**Scope:** F0.5-aligned threshold sweep.

## 25.1 Agent task
### Objective
Implement the next smallest complete increment for **Threshold Search**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 25.2 Agent task
### Objective
Implement the next smallest complete increment for **Threshold Search**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 25.3 Agent task
### Objective
Implement the next smallest complete increment for **Threshold Search**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 25.4 Agent task
### Objective
Implement the next smallest complete increment for **Threshold Search**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 25.5 Agent task
### Objective
Implement the next smallest complete increment for **Threshold Search**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 25.6 Agent task
### Objective
Implement the next smallest complete increment for **Threshold Search**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 25.7 Agent task
### Objective
Implement the next smallest complete increment for **Threshold Search**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 25.8 Agent task
### Objective
Implement the next smallest complete increment for **Threshold Search**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 25.9 Agent task
### Objective
Implement the next smallest complete increment for **Threshold Search**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 25.10 Agent task
### Objective
Implement the next smallest complete increment for **Threshold Search**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 26 - Singleton Decision
**Scope:** empty-list policy and evidence floors.

## 26.1 Agent task
### Objective
Implement the next smallest complete increment for **Singleton Decision**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 26.2 Agent task
### Objective
Implement the next smallest complete increment for **Singleton Decision**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 26.3 Agent task
### Objective
Implement the next smallest complete increment for **Singleton Decision**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 26.4 Agent task
### Objective
Implement the next smallest complete increment for **Singleton Decision**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 26.5 Agent task
### Objective
Implement the next smallest complete increment for **Singleton Decision**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 26.6 Agent task
### Objective
Implement the next smallest complete increment for **Singleton Decision**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 26.7 Agent task
### Objective
Implement the next smallest complete increment for **Singleton Decision**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 26.8 Agent task
### Objective
Implement the next smallest complete increment for **Singleton Decision**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 26.9 Agent task
### Objective
Implement the next smallest complete increment for **Singleton Decision**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 26.10 Agent task
### Objective
Implement the next smallest complete increment for **Singleton Decision**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 27 - Multi-match Assembly
**Scope:** zero/one/many matches and dedupe.

## 27.1 Agent task
### Objective
Implement the next smallest complete increment for **Multi-match Assembly**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 27.2 Agent task
### Objective
Implement the next smallest complete increment for **Multi-match Assembly**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 27.3 Agent task
### Objective
Implement the next smallest complete increment for **Multi-match Assembly**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 27.4 Agent task
### Objective
Implement the next smallest complete increment for **Multi-match Assembly**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 27.5 Agent task
### Objective
Implement the next smallest complete increment for **Multi-match Assembly**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 27.6 Agent task
### Objective
Implement the next smallest complete increment for **Multi-match Assembly**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 27.7 Agent task
### Objective
Implement the next smallest complete increment for **Multi-match Assembly**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 27.8 Agent task
### Objective
Implement the next smallest complete increment for **Multi-match Assembly**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 27.9 Agent task
### Objective
Implement the next smallest complete increment for **Multi-match Assembly**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 27.10 Agent task
### Objective
Implement the next smallest complete increment for **Multi-match Assembly**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 28 - Error Analysis
**Scope:** FP/FN taxonomy and review artifacts.

## 28.1 Agent task
### Objective
Implement the next smallest complete increment for **Error Analysis**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 28.2 Agent task
### Objective
Implement the next smallest complete increment for **Error Analysis**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 28.3 Agent task
### Objective
Implement the next smallest complete increment for **Error Analysis**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 28.4 Agent task
### Objective
Implement the next smallest complete increment for **Error Analysis**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 28.5 Agent task
### Objective
Implement the next smallest complete increment for **Error Analysis**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 28.6 Agent task
### Objective
Implement the next smallest complete increment for **Error Analysis**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 28.7 Agent task
### Objective
Implement the next smallest complete increment for **Error Analysis**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 28.8 Agent task
### Objective
Implement the next smallest complete increment for **Error Analysis**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 28.9 Agent task
### Objective
Implement the next smallest complete increment for **Error Analysis**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 28.10 Agent task
### Objective
Implement the next smallest complete increment for **Error Analysis**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 29 - Ablation Experiments
**Scope:** blocking/features/model/threshold ablations.

## 29.1 Agent task
### Objective
Implement the next smallest complete increment for **Ablation Experiments**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 29.2 Agent task
### Objective
Implement the next smallest complete increment for **Ablation Experiments**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 29.3 Agent task
### Objective
Implement the next smallest complete increment for **Ablation Experiments**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 29.4 Agent task
### Objective
Implement the next smallest complete increment for **Ablation Experiments**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 29.5 Agent task
### Objective
Implement the next smallest complete increment for **Ablation Experiments**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 29.6 Agent task
### Objective
Implement the next smallest complete increment for **Ablation Experiments**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 29.7 Agent task
### Objective
Implement the next smallest complete increment for **Ablation Experiments**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 29.8 Agent task
### Objective
Implement the next smallest complete increment for **Ablation Experiments**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 29.9 Agent task
### Objective
Implement the next smallest complete increment for **Ablation Experiments**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 29.10 Agent task
### Objective
Implement the next smallest complete increment for **Ablation Experiments**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 30 - Performance Engineering
**Scope:** memory, batching, sparse data, caching.

## 30.1 Agent task
### Objective
Implement the next smallest complete increment for **Performance Engineering**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 30.2 Agent task
### Objective
Implement the next smallest complete increment for **Performance Engineering**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 30.3 Agent task
### Objective
Implement the next smallest complete increment for **Performance Engineering**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 30.4 Agent task
### Objective
Implement the next smallest complete increment for **Performance Engineering**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 30.5 Agent task
### Objective
Implement the next smallest complete increment for **Performance Engineering**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 30.6 Agent task
### Objective
Implement the next smallest complete increment for **Performance Engineering**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 30.7 Agent task
### Objective
Implement the next smallest complete increment for **Performance Engineering**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 30.8 Agent task
### Objective
Implement the next smallest complete increment for **Performance Engineering**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 30.9 Agent task
### Objective
Implement the next smallest complete increment for **Performance Engineering**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 30.10 Agent task
### Objective
Implement the next smallest complete increment for **Performance Engineering**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 31 - Security and Fair Play
**Scope:** offline operation, dependency and provenance controls.

## 31.1 Agent task
### Objective
Implement the next smallest complete increment for **Security and Fair Play**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 31.2 Agent task
### Objective
Implement the next smallest complete increment for **Security and Fair Play**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 31.3 Agent task
### Objective
Implement the next smallest complete increment for **Security and Fair Play**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 31.4 Agent task
### Objective
Implement the next smallest complete increment for **Security and Fair Play**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 31.5 Agent task
### Objective
Implement the next smallest complete increment for **Security and Fair Play**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 31.6 Agent task
### Objective
Implement the next smallest complete increment for **Security and Fair Play**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 31.7 Agent task
### Objective
Implement the next smallest complete increment for **Security and Fair Play**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 31.8 Agent task
### Objective
Implement the next smallest complete increment for **Security and Fair Play**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 31.9 Agent task
### Objective
Implement the next smallest complete increment for **Security and Fair Play**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 31.10 Agent task
### Objective
Implement the next smallest complete increment for **Security and Fair Play**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 32 - Output Serializer
**Scope:** matching_results and candidate_pairs.

## 32.1 Agent task
### Objective
Implement the next smallest complete increment for **Output Serializer**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 32.2 Agent task
### Objective
Implement the next smallest complete increment for **Output Serializer**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 32.3 Agent task
### Objective
Implement the next smallest complete increment for **Output Serializer**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 32.4 Agent task
### Objective
Implement the next smallest complete increment for **Output Serializer**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 32.5 Agent task
### Objective
Implement the next smallest complete increment for **Output Serializer**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 32.6 Agent task
### Objective
Implement the next smallest complete increment for **Output Serializer**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 32.7 Agent task
### Objective
Implement the next smallest complete increment for **Output Serializer**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 32.8 Agent task
### Objective
Implement the next smallest complete increment for **Output Serializer**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 32.9 Agent task
### Objective
Implement the next smallest complete increment for **Output Serializer**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 32.10 Agent task
### Objective
Implement the next smallest complete increment for **Output Serializer**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 33 - Official Validator
**Scope:** automated release gate.

## 33.1 Agent task
### Objective
Implement the next smallest complete increment for **Official Validator**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 33.2 Agent task
### Objective
Implement the next smallest complete increment for **Official Validator**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 33.3 Agent task
### Objective
Implement the next smallest complete increment for **Official Validator**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 33.4 Agent task
### Objective
Implement the next smallest complete increment for **Official Validator**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 33.5 Agent task
### Objective
Implement the next smallest complete increment for **Official Validator**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 33.6 Agent task
### Objective
Implement the next smallest complete increment for **Official Validator**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 33.7 Agent task
### Objective
Implement the next smallest complete increment for **Official Validator**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 33.8 Agent task
### Objective
Implement the next smallest complete increment for **Official Validator**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 33.9 Agent task
### Objective
Implement the next smallest complete increment for **Official Validator**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 33.10 Agent task
### Objective
Implement the next smallest complete increment for **Official Validator**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 34 - Full Test Inference
**Scope:** deterministic end-to-end run.

## 34.1 Agent task
### Objective
Implement the next smallest complete increment for **Full Test Inference**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 34.2 Agent task
### Objective
Implement the next smallest complete increment for **Full Test Inference**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 34.3 Agent task
### Objective
Implement the next smallest complete increment for **Full Test Inference**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 34.4 Agent task
### Objective
Implement the next smallest complete increment for **Full Test Inference**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 34.5 Agent task
### Objective
Implement the next smallest complete increment for **Full Test Inference**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 34.6 Agent task
### Objective
Implement the next smallest complete increment for **Full Test Inference**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 34.7 Agent task
### Objective
Implement the next smallest complete increment for **Full Test Inference**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 34.8 Agent task
### Objective
Implement the next smallest complete increment for **Full Test Inference**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 34.9 Agent task
### Objective
Implement the next smallest complete increment for **Full Test Inference**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 34.10 Agent task
### Objective
Implement the next smallest complete increment for **Full Test Inference**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 35 - Methodology Documentation
**Scope:** challenge-aligned write-up.

## 35.1 Agent task
### Objective
Implement the next smallest complete increment for **Methodology Documentation**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 35.2 Agent task
### Objective
Implement the next smallest complete increment for **Methodology Documentation**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 35.3 Agent task
### Objective
Implement the next smallest complete increment for **Methodology Documentation**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 35.4 Agent task
### Objective
Implement the next smallest complete increment for **Methodology Documentation**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 35.5 Agent task
### Objective
Implement the next smallest complete increment for **Methodology Documentation**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 35.6 Agent task
### Objective
Implement the next smallest complete increment for **Methodology Documentation**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 35.7 Agent task
### Objective
Implement the next smallest complete increment for **Methodology Documentation**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 35.8 Agent task
### Objective
Implement the next smallest complete increment for **Methodology Documentation**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 35.9 Agent task
### Objective
Implement the next smallest complete increment for **Methodology Documentation**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 35.10 Agent task
### Objective
Implement the next smallest complete increment for **Methodology Documentation**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 36 - Experiment Tracking
**Scope:** run registry and champion/challenger.

## 36.1 Agent task
### Objective
Implement the next smallest complete increment for **Experiment Tracking**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 36.2 Agent task
### Objective
Implement the next smallest complete increment for **Experiment Tracking**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 36.3 Agent task
### Objective
Implement the next smallest complete increment for **Experiment Tracking**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 36.4 Agent task
### Objective
Implement the next smallest complete increment for **Experiment Tracking**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 36.5 Agent task
### Objective
Implement the next smallest complete increment for **Experiment Tracking**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 36.6 Agent task
### Objective
Implement the next smallest complete increment for **Experiment Tracking**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 36.7 Agent task
### Objective
Implement the next smallest complete increment for **Experiment Tracking**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 36.8 Agent task
### Objective
Implement the next smallest complete increment for **Experiment Tracking**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 36.9 Agent task
### Objective
Implement the next smallest complete increment for **Experiment Tracking**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 36.10 Agent task
### Objective
Implement the next smallest complete increment for **Experiment Tracking**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 37 - Robustness Testing
**Scope:** noise, unseen country, missing fields, hard negatives.

## 37.1 Agent task
### Objective
Implement the next smallest complete increment for **Robustness Testing**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 37.2 Agent task
### Objective
Implement the next smallest complete increment for **Robustness Testing**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 37.3 Agent task
### Objective
Implement the next smallest complete increment for **Robustness Testing**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 37.4 Agent task
### Objective
Implement the next smallest complete increment for **Robustness Testing**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 37.5 Agent task
### Objective
Implement the next smallest complete increment for **Robustness Testing**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 37.6 Agent task
### Objective
Implement the next smallest complete increment for **Robustness Testing**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 37.7 Agent task
### Objective
Implement the next smallest complete increment for **Robustness Testing**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 37.8 Agent task
### Objective
Implement the next smallest complete increment for **Robustness Testing**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 37.9 Agent task
### Objective
Implement the next smallest complete increment for **Robustness Testing**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 37.10 Agent task
### Objective
Implement the next smallest complete increment for **Robustness Testing**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 38 - Packaging
**Scope:** ZIP structure and dependencies.

## 38.1 Agent task
### Objective
Implement the next smallest complete increment for **Packaging**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 38.2 Agent task
### Objective
Implement the next smallest complete increment for **Packaging**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 38.3 Agent task
### Objective
Implement the next smallest complete increment for **Packaging**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 38.4 Agent task
### Objective
Implement the next smallest complete increment for **Packaging**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 38.5 Agent task
### Objective
Implement the next smallest complete increment for **Packaging**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 38.6 Agent task
### Objective
Implement the next smallest complete increment for **Packaging**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 38.7 Agent task
### Objective
Implement the next smallest complete increment for **Packaging**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 38.8 Agent task
### Objective
Implement the next smallest complete increment for **Packaging**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 38.9 Agent task
### Objective
Implement the next smallest complete increment for **Packaging**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 38.10 Agent task
### Objective
Implement the next smallest complete increment for **Packaging**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 39 - Clean-room Reproduction
**Scope:** rebuild from package only.

## 39.1 Agent task
### Objective
Implement the next smallest complete increment for **Clean-room Reproduction**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 39.2 Agent task
### Objective
Implement the next smallest complete increment for **Clean-room Reproduction**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 39.3 Agent task
### Objective
Implement the next smallest complete increment for **Clean-room Reproduction**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 39.4 Agent task
### Objective
Implement the next smallest complete increment for **Clean-room Reproduction**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 39.5 Agent task
### Objective
Implement the next smallest complete increment for **Clean-room Reproduction**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 39.6 Agent task
### Objective
Implement the next smallest complete increment for **Clean-room Reproduction**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 39.7 Agent task
### Objective
Implement the next smallest complete increment for **Clean-room Reproduction**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 39.8 Agent task
### Objective
Implement the next smallest complete increment for **Clean-room Reproduction**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 39.9 Agent task
### Objective
Implement the next smallest complete increment for **Clean-room Reproduction**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 39.10 Agent task
### Objective
Implement the next smallest complete increment for **Clean-room Reproduction**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# PHASE 40 - Release and Submission
**Scope:** final audit and release candidate.

## 40.1 Agent task
### Objective
Implement the next smallest complete increment for **Release and Submission**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 40.2 Agent task
### Objective
Implement the next smallest complete increment for **Release and Submission**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 40.3 Agent task
### Objective
Implement the next smallest complete increment for **Release and Submission**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 40.4 Agent task
### Objective
Implement the next smallest complete increment for **Release and Submission**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 40.5 Agent task
### Objective
Implement the next smallest complete increment for **Release and Submission**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 40.6 Agent task
### Objective
Implement the next smallest complete increment for **Release and Submission**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 40.7 Agent task
### Objective
Implement the next smallest complete increment for **Release and Submission**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 40.8 Agent task
### Objective
Implement the next smallest complete increment for **Release and Submission**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 40.9 Agent task
### Objective
Implement the next smallest complete increment for **Release and Submission**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

## 40.10 Agent task
### Objective
Implement the next smallest complete increment for **Release and Submission**. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.
### Required actions
1. Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.
2. Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.
3. Define or confirm the input contract and output contract.
4. Implement the smallest production-quality function/class/CLI required for this increment.
5. Add unit tests for the normal case, missing-data case, and at least one adversarial case.
6. Add structured logging sufficient to reproduce the run and diagnose failures.
7. Execute the targeted tests and a small fixture run.
8. Persist or update the stage artifact/manifest.
9. Measure runtime/memory or quality impact appropriate to the stage.
10. Update the decision log and report exactly what changed.
### Antigravity must not
- Rewrite unrelated modules merely to make the code look cleaner.
- Introduce external data or network calls.
- Change output semantics without a requirement/experiment record.
- Treat a model score as an output match without an explicit decision policy.
- Remove candidate records only to reduce runtime without measuring candidate recall.
### Definition of done
The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

# MASTER AGENT RUNBOOK

## Runbook 01 - `bootstrap`
**Purpose:** Create the repository and environment.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 02 - `manifest`
**Purpose:** Record the seven source/test files and checksums.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 03 - `validate`
**Purpose:** Run schema/ID/data integrity checks.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 04 - `profile`
**Purpose:** Generate the first EDA and noise report.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 05 - `normalize`
**Purpose:** Build versioned raw/canonical/token/char views.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 06 - `split`
**Purpose:** Freeze an entity-aware validation set.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 07 - `ground_truth`
**Purpose:** Build pair labels from multi-ID ground truth.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 08 - `block`
**Purpose:** Benchmark blocking passes and candidate recall.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 09 - `retrieve`
**Purpose:** Add character n-gram retrieval if justified.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 10 - `candidates`
**Purpose:** Persist the exact final candidate set.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 11 - `features`
**Purpose:** Build and version the feature table.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 12 - `baseline`
**Purpose:** Train/evaluate deterministic baseline.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 13 - `ml`
**Purpose:** Train supervised candidate-aware model.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 14 - `threshold`
**Purpose:** Sweep threshold against macro F0.5.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 15 - `decide`
**Purpose:** Implement singleton and multi-match policy.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 16 - `analyze`
**Purpose:** Generate FP/FN/hard-negative review tables.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 17 - `ablate`
**Purpose:** Run controlled ablations.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 18 - `optimize`
**Purpose:** Improve resource efficiency without semantic regression.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 19 - `infer`
**Purpose:** Run deterministic inference on all test S1 entities.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 20 - `serialize`
**Purpose:** Write both TSV outputs.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 21 - `validate_submission`
**Purpose:** Run official validator.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 22 - `reproduce`
**Purpose:** Run clean-room reproduction.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 23 - `package`
**Purpose:** Create final ZIP.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 24 - `audit`
**Purpose:** Perform licensing/fair-play/requirements audit.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

## Runbook 25 - `release`
**Purpose:** Freeze release candidate and record final evidence.
**Agent output required:** changed files, exact command, test result, artifact path, key metrics, unresolved risks, next recommended step.

# ANTIGRAVITY FINAL RESPONSE TEMPLATE
When a phase is complete, respond with:

```text
PHASE: <id/name>
IMPLEMENTED: <concise description>
FILES CHANGED: <paths>
TESTS: <commands + PASS/FAIL>
ARTIFACTS: <paths>
METRICS: <quality/runtime/memory as applicable>
ASSUMPTIONS: <list>
RISKS: <list>
DECISION: <keep/revise/block>
NEXT PHASE: <id/name>
```
