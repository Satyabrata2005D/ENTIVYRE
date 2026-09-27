<USER_REQUEST>
2. ( IMPLEMENTATION PLAN / Amazon_ML_Challenge_Master_Implementation_Plan_DETAILEDAmazon_ML_Challenge_Master_Implementation_Plan_DETAILED ) -->
_________________________________________________
[
ANTIGRAVITY - AMAZON ML CHALLENGE MASTER EXECUTION PLAYBOOK

This is the agent-facing companion to the large implementation plan. It is written as a build contract. The agent must implement the project incrementally, preserve the official challenge contract, and refuse any design that violates the challenge rules.

Global agent rules

Read the official challenge statement before changing architecture.

Treat the uploaded challenge specification as authoritative for requirements.

Treat advanced model/algorithm choices as experiments, not requirements.

Never use external business databases, entity-resolution APIs, government registries, geocoding APIs, or internet-based entity augmentation.

Keep raw inputs immutable.

Every stage must be deterministic when given the same inputs, configuration, and seed.

Every stage must have tests and a machine-readable artifact/log.

Never silently discard rows because of memory pressure. Change batching or candidate strategy and measure the effect.

Do not add a dependency without license/resource justification.

Before declaring done, run the relevant tests and report exact commands and results.

PHASE 01 - Specification and Contract

Scope: requirements matrix, exact output rules, fair play, licensing.

01.1 Agent task

Objective

Implement the next smallest complete increment for Specification and Contract. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

01.2 Agent task

Objective

Implement the next smallest complete increment for Specification and Contract. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

01.3 Agent task

Objective

Implement the next smallest complete increment for Specification and Contract. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

01.4 Agent task

Objective

Implement the next smallest complete increment for Specification and Contract. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

01.5 Agent task

Objective

Implement the next smallest complete increment for Specification and Contract. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

01.6 Agent task

Objective

Implement the next smallest complete increment for Specification and Contract. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

01.7 Agent task

Objective

Implement the next smallest complete increment for Specification and Contract. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

01.8 Agent task

Objective

Implement the next smallest complete increment for Specification and Contract. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

01.9 Agent task

Objective

Implement the next smallest complete increment for Specification and Contract. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

01.10 Agent task

Objective

Implement the next smallest complete increment for Specification and Contract. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

PHASE 02 - Repository Bootstrap

Scope: folders, configs, package layout, tests, logging.

02.1 Agent task

Objective

Implement the next smallest complete increment for Repository Bootstrap. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

02.2 Agent task

Objective

Implement the next smallest complete increment for Repository Bootstrap. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

02.3 Agent task

Objective

Implement the next smallest complete increment for Repository Bootstrap. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

02.4 Agent task

Objective

Implement the next smallest complete increment for Repository Bootstrap. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

02.5 Agent task

Objective

Implement the next smallest complete increment for Repository Bootstrap. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

02.6 Agent task

Objective

Implement the next smallest complete increment for Repository Bootstrap. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

02.7 Agent task

Objective

Implement the next smallest complete increment for Repository Bootstrap. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

02.8 Agent task

Objective

Implement the next smallest complete increment for Repository Bootstrap. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

02.9 Agent task

Objective

Implement the next smallest complete increment for Repository Bootstrap. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

02.10 Agent task

Objective

Implement the next smallest complete increment for Repository Bootstrap. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

PHASE 03 - Dataset Manifest

Scope: file checksums, sizes, row counts, schema manifest.

03.1 Agent task

Objective

Implement the next smallest complete increment for Dataset Manifest. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

03.2 Agent task

Objective

Implement the next smallest complete increment for Dataset Manifest. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

03.3 Agent task

Objective

Implement the next smallest complete increment for Dataset Manifest. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

03.4 Agent task

Objective

Implement the next smallest complete increment for Dataset Manifest. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

03.5 Agent task

Objective

Implement the next smallest complete increment for Dataset Manifest. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

03.6 Agent task

Objective

Implement the next smallest complete increment for Dataset Manifest. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

03.7 Agent task

Objective

Implement the next smallest complete increment for Dataset Manifest. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

03.8 Agent task

Objective

Implement the next smallest complete increment for Dataset Manifest. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

03.9 Agent task

Objective

Implement the next smallest complete increment for Dataset Manifest. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

03.10 Agent task

Objective

Implement the next smallest complete increment for Dataset Manifest. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

PHASE 04 - Ingestion Engine

Scope: TSV parsing, chunking, dtypes, malformed row handling.

04.1 Agent task

Objective

Implement the next smallest complete increment for Ingestion Engine. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

04.2 Agent task

Objective

Implement the next smallest complete increment for Ingestion Engine. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

04.3 Agent task

Objective

Implement the next smallest complete increment for Ingestion Engine. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

04.4 Agent task

Objective

Implement the next smallest complete increment for Ingestion Engine. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

04.5 Agent task

Objective

Implement the next smallest complete increment for Ingestion Engine. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

04.6 Agent task

Objective

Implement the next smallest complete increment for Ingestion Engine. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

04.7 Agent task

Objective

Implement the next smallest complete increment for Ingestion Engine. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

04.8 Agent task

Objective

Implement the next smallest complete increment for Ingestion Engine. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

04.9 Agent task

Objective

Implement the next smallest complete increment for Ingestion Engine. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

04.10 Agent task

Objective

Implement the next smallest complete increment for Ingestion Engine. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

PHASE 05 - Data Validation

Scope: schema, IDs, source prefixes, missingness.

05.1 Agent task

Objective

Implement the next smallest complete increment for Data Validation. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

05.2 Agent task

Objective

Implement the next smallest complete increment for Data Validation. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

05.3 Agent task

Objective

Implement the next smallest complete increment for Data Validation. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

05.4 Agent task

Objective

Implement the next smallest complete increment for Data Validation. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

05.5 Agent task

Objective

Implement the next smallest complete increment for Data Validation. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

05.6 Agent task

Objective

Implement the next smallest complete increment for Data Validation. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

05.7 Agent task

Objective

Implement the next smallest complete increment for Data Validation. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

05.8 Agent task

Objective

Implement the next smallest complete increment for Data Validation. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

05.9 Agent task

Objective

Implement the next smallest complete increment for Data Validation. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

05.10 Agent task

Objective

Implement the next smallest complete increment for Data Validation. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

PHASE 06 - Profiling

Scope: distributions, duplicates, noise, training label statistics.

06.1 Agent task

Objective

Implement the next smallest complete increment for Profiling. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

06.2 Agent task

Objective

Implement the next smallest complete increment for Profiling. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

06.3 Agent task

Objective

Implement the next smallest complete increment for Profiling. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

06.4 Agent task

Objective

Implement the next smallest complete increment for Profiling. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

06.5 Agent task

Objective

Implement the next smallest complete increment for Profiling. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

06.6 Agent task

Objective

Implement the next smallest complete increment for Profiling. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

06.7 Agent task

Objective

Implement the next smallest complete increment for Profiling. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

06.8 Agent task

Objective

Implement the next smallest complete increment for Profiling. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

06.9 Agent task

Objective

Implement the next smallest complete increment for Profiling. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

06.10 Agent task

Objective

Implement the next smallest complete increment for Profiling. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

PHASE 07 - Normalization Core

Scope: raw/canonical/token/character representations.

07.1 Agent task

Objective

Implement the next smallest complete increment for Normalization Core. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

07.2 Agent task

Objective

Implement the next smallest complete increment for Normalization Core. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

07.3 Agent task

Objective

Implement the next smallest complete increment for Normalization Core. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

07.4 Agent task

Objective

Implement the next smallest complete increment for Normalization Core. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

07.5 Agent task

Objective

Implement the next smallest complete increment for Normalization Core. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

07.6 Agent task

Objective

Implement the next smallest complete increment for Normalization Core. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

07.7 Agent task

Objective

Implement the next smallest complete increment for Normalization Core. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

07.8 Agent task

Objective

Implement the next smallest complete increment for Normalization Core. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

07.9 Agent task

Objective

Implement the next smallest complete increment for Normalization Core. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

07.10 Agent task

Objective

Implement the next smallest complete increment for Normalization Core. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

PHASE 08 - Address Intelligence

Scope: numbers, abbreviations, landmarks, components.

08.1 Agent task

Objective

Implement the next smallest complete increment for Address Intelligence. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

08.2 Agent task

Objective

Implement the next smallest complete increment for Address Intelligence. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

08.3 Agent task

Objective

Implement the next smallest complete increment for Address Intelligence. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

08.4 Agent task

Objective

Implement the next smallest complete increment for Address Intelligence. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

08.5 Agent task

Objective

Implement the next smallest complete increment for Address Intelligence. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

08.6 Agent task

Objective

Implement the next smallest complete increment for Address Intelligence. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

08.7 Agent task

Objective

Implement the next smallest complete increment for Address Intelligence. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

08.8 Agent task

Objective

Implement the next smallest complete increment for Address Intelligence. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

08.9 Agent task

Objective

Implement the next smallest complete increment for Address Intelligence. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

08.10 Agent task

Objective

Implement the next smallest complete increment for Address Intelligence. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

PHASE 09 - Country Open Set

Scope: generic country handling, France regression.

09.1 Agent task

Objective

Implement the next smallest complete increment for Country Open Set. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

09.2 Agent task

Objective

Implement the next smallest complete increment for Country Open Set. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

09.3 Agent task

Objective

Implement the next smallest complete increment for Country Open Set. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

09.4 Agent task

Objective

Implement the next smallest complete increment for Country Open Set. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

09.5 Agent task

Objective

Implement the next smallest complete increment for Country Open Set. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

09.6 Agent task

Objective

Implement the next smallest complete increment for Country Open Set. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

09.7 Agent task

Objective

Implement the next smallest complete increment for Country Open Set. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

09.8 Agent task

Objective

Implement the next smallest complete increment for Country Open Set. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

09.9 Agent task

Objective

Implement the next smallest complete increment for Country Open Set. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

09.10 Agent task

Objective

Implement the next smallest complete increment for Country Open Set. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

PHASE 10 - Ground Truth Builder

Scope: multi-ID labels, pair labels, negatives, singletons.

10.1 Agent task

Objective

Implement the next smallest complete increment for Ground Truth Builder. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

10.2 Agent task

Objective

Implement the next smallest complete increment for Ground Truth Builder. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

10.3 Agent task

Objective

Implement the next smallest complete increment for Ground Truth Builder. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

10.4 Agent task

Objective

Implement the next smallest complete increment for Ground Truth Builder. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

10.5 Agent task

Objective

Implement the next smallest complete increment for Ground Truth Builder. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

10.6 Agent task

Objective

Implement the next smallest complete increment for Ground Truth Builder. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

10.7 Agent task

Objective

Implement the next smallest complete increment for Ground Truth Builder. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

10.8 Agent task

Objective

Implement the next smallest complete increment for Ground Truth Builder. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

10.9 Agent task

Objective

Implement the next smallest complete increment for Ground Truth Builder. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

10.10 Agent task

Objective

Implement the next smallest complete increment for Ground Truth Builder. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

PHASE 11 - Validation Split

Scope: entity-aware split and frozen validation.

11.1 Agent task

Objective

Implement the next smallest complete increment for Validation Split. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

11.2 Agent task

Objective

Implement the next smallest complete increment for Validation Split. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

11.3 Agent task

Objective

Implement the next smallest complete increment for Validation Split. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

11.4 Agent task

Objective

Implement the next smallest complete increment for Validation Split. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

11.5 Agent task

Objective

Implement the next smallest complete increment for Validation Split. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

11.6 Agent task

Objective

Implement the next smallest complete increment for Validation Split. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

11.7 Agent task

Objective

Implement the next smallest complete increment for Validation Split. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

11.8 Agent task

Objective

Implement the next smallest complete increment for Validation Split. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

11.9 Agent task

Objective

Implement the next smallest complete increment for Validation Split. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

11.10 Agent task

Objective

Implement the next smallest complete increment for Validation Split. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

PHASE 12 - Blocking Baseline

Scope: exact and token blocking.

12.1 Agent task

Objective

Implement the next smallest complete increment for Blocking Baseline. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

12.2 Agent task

Objective

Implement the next smallest complete increment for Blocking Baseline. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

12.3 Agent task

Objective

Implement the next smallest complete increment for Blocking Baseline. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

12.4 Agent task

Objective

Implement the next smallest complete increment for Blocking Baseline. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

12.5 Agent task

Objective

Implement the next smallest complete increment for Blocking Baseline. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

12.6 Agent task

Objective

Implement the next smallest complete increment for Blocking Baseline. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

12.7 Agent task

Objective

Implement the next smallest complete increment for Blocking Baseline. Do not jump ahead to later phases. The increment must be usable by the pipeline and must not introduce an undocumented semantic change.

Required actions

Inspect the current repository state and identify the existing module, tests, configuration, and artifacts relevant to this phase.

Read the corresponding requirement/implementation section from the Master Implementation Plan before writing code.

Define or confirm the input contract and output contract.

Implement the smallest production-quality function/class/CLI required for this increment.

Add unit tests for the normal case, missing-data case, and at least one adversarial case.

Add structured logging sufficient to reproduce the run and diagnose failures.

Execute the targeted tests and a small fixture run.

Persist or update the stage artifact/manifest.

Measure runtime/memory or quality impact appropriate to the stage.

Update the decision log and report exactly what changed.

Antigravity must not

Rewrite unrelated modules merely to make the code look cleaner.

Introduce external data or network calls.

Change output semantics without a requirement/experiment record.

Treat a model score as an output match without an explicit decision policy.

Remove candidate records only to reduce runtime without measuring candidate recall.

Definition of done

The code exists, targeted tests pass, the fixture run passes, the artifact is reproducible, the failure mode is covered, and the next phase can consume the output without manual text editing.

12.8 Agent task

Objective

Implement the next smallest complete increment for Blocking Baseline. Do not ju
<truncated 1163198 bytes>

NOTE: The output was truncated because it was too long. Use a more targeted query or a smaller range to get the information you need.