"""Evaluation metric implementations strictly adhering to the official challenge specification.

Official Metric Contract:
- Macro-averaged F_0.5 score calculated per Source 1 entity, then averaged
  across ALL Source 1 entities in the evaluation set.
- F_0.5 = (1.25 * Precision * Recall) / (0.25 * Precision + Recall)
- Singletons: A Source 1 entity with no true matches scores 1.0 when the model
  correctly predicts an empty list, and 0.0 when any match is predicted.
- Macro-average treats singletons and multi-match entities on equal footing.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Collection, Dict, Mapping, Optional, Set, Tuple


@dataclass(frozen=True)
class EntityMetricResult:
    """Per-entity precision, recall, and F_0.5 score."""

    source1_entity_id: str
    is_singleton: bool
    true_count: int
    predicted_count: int
    tp_count: int
    fp_count: int
    fn_count: int
    precision: float
    recall: float
    f05: float


@dataclass(frozen=True)
class MacroEvaluationSummary:
    """Aggregated macro-evaluation summary over an entire dataset."""

    total_entities: int
    singleton_count: int
    matched_count: int
    macro_f05: float
    mean_precision: float
    mean_recall: float
    singleton_f05: float
    matched_f05: float
    perfect_score_count: int
    zero_score_count: int

    def to_dict(self) -> Dict[str, float | int]:
        return {
            "total_entities": self.total_entities,
            "singleton_count": self.singleton_count,
            "matched_count": self.matched_count,
            "macro_f05": round(self.macro_f05, 6),
            "mean_precision": round(self.mean_precision, 6),
            "mean_recall": round(self.mean_recall, 6),
            "singleton_f05": round(self.singleton_f05, 6),
            "matched_f05": round(self.matched_f05, 6),
            "perfect_score_count": self.perfect_score_count,
            "zero_score_count": self.zero_score_count,
        }


def compute_entity_f05(
    s1_id: str,
    true_matches: Collection[str],
    predicted_matches: Collection[str],
) -> EntityMetricResult:
    """Compute official challenge F_0.5 metric for a single Source 1 entity.

    Rules:
    1. Singletons (true_matches is empty):
       - If predicted_matches is empty -> F_0.5 = 1.0, precision = 1.0, recall = 1.0
       - If predicted_matches is not empty -> F_0.5 = 0.0, precision = 0.0, recall = 0.0
    2. Non-singletons (true_matches is not empty):
       - If predicted_matches is empty -> F_0.5 = 0.0, precision = 0.0, recall = 0.0
       - If true_positives == 0 -> F_0.5 = 0.0
       - Otherwise:
         precision = TP / (TP + FP)
         recall = TP / (TP + FN)
         denom = 0.25 * precision + recall
         F_0.5 = (1.25 * precision * recall) / denom
    """
    true_set: Set[str] = set(true_matches)
    pred_set: Set[str] = set(predicted_matches)

    is_singleton = len(true_set) == 0

    if is_singleton:
        if len(pred_set) == 0:
            return EntityMetricResult(
                source1_entity_id=s1_id,
                is_singleton=True,
                true_count=0,
                predicted_count=0,
                tp_count=0,
                fp_count=0,
                fn_count=0,
                precision=1.0,
                recall=1.0,
                f05=1.0,
            )
        else:
            return EntityMetricResult(
                source1_entity_id=s1_id,
                is_singleton=True,
                true_count=0,
                predicted_count=len(pred_set),
                tp_count=0,
                fp_count=len(pred_set),
                fn_count=0,
                precision=0.0,
                recall=0.0,
                f05=0.0,
            )

    # Non-singleton entity
    if len(pred_set) == 0:
        return EntityMetricResult(
            source1_entity_id=s1_id,
            is_singleton=False,
            true_count=len(true_set),
            predicted_count=0,
            tp_count=0,
            fp_count=0,
            fn_count=len(true_set),
            precision=0.0,
            recall=0.0,
            f05=0.0,
        )

    tp_count = len(true_set & pred_set)
    fp_count = len(pred_set - true_set)
    fn_count = len(true_set - pred_set)

    if tp_count == 0:
        return EntityMetricResult(
            source1_entity_id=s1_id,
            is_singleton=False,
            true_count=len(true_set),
            predicted_count=len(pred_set),
            tp_count=0,
            fp_count=fp_count,
            fn_count=fn_count,
            precision=0.0,
            recall=0.0,
            f05=0.0,
        )

    precision = tp_count / len(pred_set)
    recall = tp_count / len(true_set)
    denominator = 0.25 * precision + recall

    if denominator <= 0.0:
        f05 = 0.0
    else:
        f05 = (1.25 * precision * recall) / denominator

    return EntityMetricResult(
        source1_entity_id=s1_id,
        is_singleton=False,
        true_count=len(true_set),
        predicted_count=len(pred_set),
        tp_count=tp_count,
        fp_count=fp_count,
        fn_count=fn_count,
        precision=precision,
        recall=recall,
        f05=f05,
    )


def compute_macro_f05(
    ground_truth: Mapping[str, Collection[str]],
    predictions: Mapping[str, Collection[str]],
) -> Tuple[MacroEvaluationSummary, Dict[str, EntityMetricResult]]:
    """Compute official challenge Macro F_0.5 across all Source 1 entities in ground truth.

    Args:
        ground_truth: Dict mapping source1_entity_id -> true matched IDs
        predictions: Dict mapping source1_entity_id -> predicted matched IDs (missing defaults to empty)

    Returns:
        Tuple of (MacroEvaluationSummary, Dict[s1_id -> EntityMetricResult])
    """
    if not ground_truth:
        return (
            MacroEvaluationSummary(
                total_entities=0,
                singleton_count=0,
                matched_count=0,
                macro_f05=0.0,
                mean_precision=0.0,
                mean_recall=0.0,
                singleton_f05=0.0,
                matched_f05=0.0,
                perfect_score_count=0,
                zero_score_count=0,
            ),
            {},
        )

    results: Dict[str, EntityMetricResult] = {}
    f05_total = 0.0
    precision_total = 0.0
    recall_total = 0.0

    singleton_f05_total = 0.0
    matched_f05_total = 0.0
    singleton_count = 0
    matched_count = 0
    perfect_count = 0
    zero_count = 0

    for s1_id, true_matches in ground_truth.items():
        pred_matches = predictions.get(s1_id, ())
        res = compute_entity_f05(s1_id, true_matches, pred_matches)
        results[s1_id] = res

        f05_total += res.f05
        precision_total += res.precision
        recall_total += res.recall

        if res.is_singleton:
            singleton_count += 1
            singleton_f05_total += res.f05
        else:
            matched_count += 1
            matched_f05_total += res.f05

        if res.f05 >= 0.999999:
            perfect_count += 1
        elif res.f05 <= 1e-6:
            zero_count += 1

    n = len(ground_truth)
    summary = MacroEvaluationSummary(
        total_entities=n,
        singleton_count=singleton_count,
        matched_count=matched_count,
        macro_f05=f05_total / n,
        mean_precision=precision_total / n,
        mean_recall=recall_total / n,
        singleton_f05=singleton_f05_total / singleton_count if singleton_count > 0 else 0.0,
        matched_f05=matched_f05_total / matched_count if matched_count > 0 else 0.0,
        perfect_score_count=perfect_count,
        zero_score_count=zero_count,
    )

    return summary, results


class MacroF05Evaluator:
    """Official Macro F_0.5 evaluation engine."""

    def __init__(self, beta: float = 0.5):
        self.beta = beta

    def evaluate(
        self,
        ground_truth: Mapping[str, Collection[str]],
        predictions: Mapping[str, Collection[str]],
    ) -> Tuple[MacroEvaluationSummary, Dict[str, EntityMetricResult]]:
        """Evaluate macro F_0.5 across all entities in ground truth."""
        return compute_macro_f05(ground_truth, predictions)

