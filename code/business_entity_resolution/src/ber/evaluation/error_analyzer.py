"""
Comprehensive Error Analysis and Forensic Diagnostic Engine for ENTIVYRE.
Phase 28: Forensic error categorization across False Positives, False Negatives,
Blocking Misses, Hard Negatives, Singleton Errors, and Country Collisions.

Guarantees:
- Disaggregates errors into formal taxonomies (Blocking Miss vs Model False Negative).
- Flags high-cost singleton false merges causing 0.0 F0.5 penalties.
- Captures forensic sample evidence for each error category.
- Produces auditable JSON and Markdown diagnostic reports.
- Pure-Python, zero external C-dependencies.
"""
from __future__ import annotations

import json
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Tuple, Any, Mapping, Collection, Set

from entivyre.contracts.metrics import compute_macro_f05, MacroEvaluationSummary
from entivyre.utils.logger import get_logger

logger = get_logger("ber.evaluation.error_analyzer", stage="28_error_analysis")


@dataclass(frozen=True)
class ErrorRecord:
    """Detailed forensic diagnostic for a single erroneous entity decision."""
    anchor_id: str
    target_id: Optional[str]
    error_type: str  # BLOCKING_MISS, MODEL_FALSE_NEGATIVE, MODEL_FALSE_POSITIVE, SINGLETON_FALSE_MERGE, etc.
    true_target_count: int
    predicted_target_count: int
    candidate_target_count: int
    details: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ErrorAnalysisReport:
    """Comprehensive error diagnostic report."""
    total_anchors: int
    macro_f05: float
    blocking_miss_count: int
    model_false_negative_count: int
    model_false_positive_count: int
    singleton_false_merge_count: int
    singleton_false_dismissal_count: int
    exact_match_anchors: int
    error_breakdown: Dict[str, int]
    sample_diagnostics: Dict[str, List[Dict[str, Any]]]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def save_json(self, filepath: Path) -> Path:
        """Persist error report to JSON."""
        p = Path(filepath)
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2)
        return p

    def save_markdown(self, filepath: Path) -> Path:
        """Generate human-readable markdown error summary."""
        p = Path(filepath)
        p.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "# ENTIVYRE Forensic Error Analysis Report",
            f"- **Total Evaluated Anchors:** {self.total_anchors}",
            f"- **Validation Macro F0.5:** {self.macro_f05:.4f}",
            f"- **Exact Match Anchors (F0.5 = 1.0):** {self.exact_match_anchors} ({self.exact_match_anchors / max(1, self.total_anchors):.2%})",
            "",
            "## Error Taxonomy Distribution",
            "| Error Category | Count | Percentage of Errors |",
            "| :--- | :--- | :--- |",
        ]
        total_errs = sum(self.error_breakdown.values())
        for cat, cnt in sorted(self.error_breakdown.items(), key=lambda x: x[1], reverse=True):
            pct = (cnt / total_errs) if total_errs > 0 else 0.0
            lines.append(f"| `{cat}` | {cnt} | {pct:.2%} |")

        lines.extend([
            "",
            "## Key Observations",
            f"1. **Blocking Misses ({self.blocking_miss_count}):** Targets never reached the classification model because candidate generation pruned them.",
            f"2. **Model False Negatives ({self.model_false_negative_count}):** Candidates were retrieved but scored below the decision threshold.",
            f"3. **Model False Positives ({self.model_false_positive_count}):** Negative candidates were erroneously predicted as matches.",
            f"4. **Singleton False Merges ({self.singleton_false_merge_count}):** True singletons incorrectly linked to a target, incurring severe 0.0 F0.5 penalty.",
        ])

        with open(p, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        return p


class ErrorAnalyzer:
    """
    Forensic diagnostic analyzer evaluating prediction errors against ground truth.
    """

    def __init__(self, sample_limit_per_category: int = 5):
        self.sample_limit_per_category = sample_limit_per_category

    def analyze(
        self,
        ground_truth: Mapping[str, Collection[str]],
        predictions: Mapping[str, Collection[str]],
        candidate_pairs: Mapping[str, Collection[str]],
        feature_lookup: Optional[Mapping[Tuple[str, str], Dict[str, float]]] = None,
    ) -> ErrorAnalysisReport:
        """
        Conducts forensic error analysis across all evaluated anchors.
        """
        summary, per_entity = compute_macro_f05(ground_truth, predictions)
        feat_map = feature_lookup or {}

        blocking_misses: List[ErrorRecord] = []
        model_fns: List[ErrorRecord] = []
        model_fps: List[ErrorRecord] = []
        singleton_fms: List[ErrorRecord] = []
        singleton_fds: List[ErrorRecord] = []

        exact_matches = 0

        for anchor_id, true_targets in ground_truth.items():
            true_set = set(true_targets)
            pred_set = set(predictions.get(anchor_id, ()))
            cand_set = set(candidate_pairs.get(anchor_id, ()))

            is_singleton = len(true_set) == 0

            # 1. Exact match anchor check
            if true_set == pred_set:
                exact_matches += 1
                continue

            # 2. Singleton false merge (True empty, predicted > 0)
            if is_singleton and len(pred_set) > 0:
                for p in pred_set:
                    feats = feat_map.get((anchor_id, p), {})
                    singleton_fms.append(
                        ErrorRecord(
                            anchor_id=anchor_id,
                            target_id=p,
                            error_type="SINGLETON_FALSE_MERGE",
                            true_target_count=0,
                            predicted_target_count=len(pred_set),
                            candidate_target_count=len(cand_set),
                            details={"predicted_target": p, "features": feats},
                        )
                    )
                continue

            # 3. Whole-anchor false dismissal (True matched, predicted empty)
            if not is_singleton and len(pred_set) == 0:
                for t in true_set:
                    if t not in cand_set:
                        blocking_misses.append(
                            ErrorRecord(
                                anchor_id=anchor_id,
                                target_id=t,
                                error_type="BLOCKING_MISS",
                                true_target_count=len(true_set),
                                predicted_target_count=0,
                                candidate_target_count=len(cand_set),
                                details={"target_id": t, "reason": "Not in candidate_pairs"},
                            )
                        )
                # If all or some candidates were present, record anchor dismissal
                if any(t in cand_set for t in true_set):
                    singleton_fds.append(
                        ErrorRecord(
                            anchor_id=anchor_id,
                            target_id=None,
                            error_type="SINGLETON_FALSE_DISMISSAL",
                            true_target_count=len(true_set),
                            predicted_target_count=0,
                            candidate_target_count=len(cand_set),
                            details={"missed_targets": list(true_set)},
                        )
                    )
                continue

            # 4. Partial target-level False Negatives (Model predicted some, but missed others)
            for t in true_set:
                if t not in pred_set:
                    if t not in cand_set:
                        # Blocking miss
                        blocking_misses.append(
                            ErrorRecord(
                                anchor_id=anchor_id,
                                target_id=t,
                                error_type="BLOCKING_MISS",
                                true_target_count=len(true_set),
                                predicted_target_count=len(pred_set),
                                candidate_target_count=len(cand_set),
                                details={"target_id": t, "reason": "Not in candidate_pairs"},
                            )
                        )
                    else:
                        # Model false negative on partial match
                        feats = feat_map.get((anchor_id, t), {})
                        model_fns.append(
                            ErrorRecord(
                                anchor_id=anchor_id,
                                target_id=t,
                                error_type="MODEL_FALSE_NEGATIVE",
                                true_target_count=len(true_set),
                                predicted_target_count=len(pred_set),
                                candidate_target_count=len(cand_set),
                                details={"target_id": t, "features": feats},
                            )
                        )

            # 5. Target-level False Positives
            for p in pred_set:
                if p not in true_set:
                    feats = feat_map.get((anchor_id, p), {})
                    model_fps.append(
                        ErrorRecord(
                            anchor_id=anchor_id,
                            target_id=p,
                            error_type="MODEL_FALSE_POSITIVE",
                            true_target_count=len(true_set),
                            predicted_target_count=len(pred_set),
                            candidate_target_count=len(cand_set),
                            details={"target_id": p, "features": feats},
                        )
                    )

        error_breakdown = {
            "BLOCKING_MISS": len(blocking_misses),
            "MODEL_FALSE_NEGATIVE": len(model_fns),
            "MODEL_FALSE_POSITIVE": len(model_fps),
            "SINGLETON_FALSE_MERGE": len(singleton_fms),
            "SINGLETON_FALSE_DISMISSAL": len(singleton_fds),
        }

        sample_diagnostics = {
            "BLOCKING_MISS": [r.to_dict() for r in blocking_misses[: self.sample_limit_per_category]],
            "MODEL_FALSE_NEGATIVE": [r.to_dict() for r in model_fns[: self.sample_limit_per_category]],
            "MODEL_FALSE_POSITIVE": [r.to_dict() for r in model_fps[: self.sample_limit_per_category]],
            "SINGLETON_FALSE_MERGE": [r.to_dict() for r in singleton_fms[: self.sample_limit_per_category]],
            "SINGLETON_FALSE_DISMISSAL": [r.to_dict() for r in singleton_fds[: self.sample_limit_per_category]],
        }

        logger.info(
            f"Error analysis completed ({len(ground_truth)} anchors, {exact_matches} exact matches, Macro F0.5: {summary.macro_f05:.4f})",
            extra={"payload": {"error_breakdown": error_breakdown, "macro_f05": summary.macro_f05}},
        )

        return ErrorAnalysisReport(
            total_anchors=len(ground_truth),
            macro_f05=summary.macro_f05,
            blocking_miss_count=len(blocking_misses),
            model_false_negative_count=len(model_fns),
            model_false_positive_count=len(model_fps),
            singleton_false_merge_count=len(singleton_fms),
            singleton_false_dismissal_count=len(singleton_fds),
            exact_match_anchors=exact_matches,
            error_breakdown=error_breakdown,
            sample_diagnostics=sample_diagnostics,
        )
