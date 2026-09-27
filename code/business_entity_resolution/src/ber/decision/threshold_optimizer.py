"""
Decision Threshold Optimization Engine for ENTIVYRE.
Phase 25: Grid search and threshold calibration maximizing official challenge Macro F0.5.

Guarantees:
- Calibrates precision-favored threshold (beta = 0.5 penalizes false positives 2x harder than false negatives).
- Evaluates complete Macro F0.5 metric with full singleton credit and penalties.
- Strict entity-grouped validation evaluation (zero data leakage).
- Emits detailed threshold curve: threshold vs Macro F0.5, Precision, Recall, Singleton F0.5.
- Persists optimal threshold configuration to JSON for production inference.
"""
from __future__ import annotations

import json
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Tuple, Any, Callable, Mapping, Collection

from entivyre.contracts.metrics import (
    MacroEvaluationSummary,
    EntityMetricResult,
    compute_macro_f05,
)
from entivyre.utils.logger import get_logger

logger = get_logger("ber.decision.threshold_optimizer", stage="25_threshold_optimization")

DEFAULT_CANDIDATE_THRESHOLDS: List[float] = [
    0.30, 0.40, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95
]


@dataclass(frozen=True)
class ThresholdStepResult:
    """Metrics at a specific decision threshold."""
    threshold: float
    macro_f05: float
    mean_precision: float
    mean_recall: float
    singleton_f05: float
    matched_f05: float
    perfect_score_count: int
    zero_score_count: int

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ThresholdOptimizationResult:
    """Complete results from threshold grid search optimization."""
    best_threshold: float
    best_macro_f05: float
    best_summary: MacroEvaluationSummary
    curve: List[ThresholdStepResult]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "best_threshold": self.best_threshold,
            "best_macro_f05": round(self.best_macro_f05, 5),
            "best_summary": self.best_summary.to_dict(),
            "curve": [step.to_dict() for step in self.curve],
        }

    def save(self, filepath: Path) -> Path:
        """Persist threshold optimization result to JSON."""
        p = Path(filepath)
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2)
        return p


class ThresholdOptimizer:
    """
    Finds the optimal probability decision threshold maximizing Macro F0.5.
    """

    def __init__(
        self,
        candidate_thresholds: Optional[List[float]] = None,
    ):
        self.candidate_thresholds = candidate_thresholds or list(DEFAULT_CANDIDATE_THRESHOLDS)

    def optimize_scored_candidates(
        self,
        val_anchor_scored_candidates: Mapping[str, List[Tuple[str, float]]],
        ground_truth: Mapping[str, Collection[str]],
    ) -> ThresholdOptimizationResult:
        """
        Optimize threshold given pre-scored candidates: anchor_id -> List[(target_id, score)].
        """
        best_f05 = -1.0
        best_threshold = 0.50
        best_summary = None
        curve: List[ThresholdStepResult] = []

        for tau in self.candidate_thresholds:
            # Build predictions at threshold tau
            predictions: Dict[str, List[str]] = {}
            for anchor_id in ground_truth.keys():
                candidates = val_anchor_scored_candidates.get(anchor_id, [])
                matched_ids: List[str] = [
                    tid for tid, score in candidates if score >= tau
                ]
                predictions[anchor_id] = matched_ids

            summary, _ = compute_macro_f05(ground_truth, predictions)
            step = ThresholdStepResult(
                threshold=round(tau, 3),
                macro_f05=round(summary.macro_f05, 5),
                mean_precision=round(summary.mean_precision, 5),
                mean_recall=round(summary.mean_recall, 5),
                singleton_f05=round(summary.singleton_f05, 5),
                matched_f05=round(summary.matched_f05, 5),
                perfect_score_count=summary.perfect_score_count,
                zero_score_count=summary.zero_score_count,
            )
            curve.append(step)

            if summary.macro_f05 > best_f05:
                best_f05 = summary.macro_f05
                best_threshold = tau
                best_summary = summary

        logger.info(
            f"Optimized threshold: tau* = {best_threshold:.3f} with Macro F0.5 = {best_f05:.4f}",
            extra={"payload": {"best_threshold": best_threshold, "best_macro_f05": best_f05}},
        )

        return ThresholdOptimizationResult(
            best_threshold=best_threshold,
            best_macro_f05=best_f05,
            best_summary=best_summary,
            curve=curve,
        )
