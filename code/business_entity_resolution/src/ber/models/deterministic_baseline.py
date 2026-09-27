"""
Deterministic Rule-Based Baseline Model for ENTIVYRE.
Phase 21: High-precision, deterministic business entity resolution baseline.

Guarantees:
- Interpretable, auditable decision rules with explicit rule provenance.
- Strict contradiction rejection (country conflict, numeric building contradiction).
- Full singleton credit: correctly emits empty matches when evidence is insufficient.
- Multi-match support: resolves multiple valid matches per Source 1 entity.
- Candidate contract enforcement: every predicted match is guaranteed to be a subset of candidate_pairs.
- Evaluates official challenge metric: Macro F0.5 with singleton handling.
- Pure-Python, zero external C-dependencies.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Tuple, Any, Mapping, Collection

from entivyre.contracts.metrics import (
    MacroEvaluationSummary,
    EntityMetricResult,
    compute_macro_f05,
)
from entivyre.utils.logger import get_logger

logger = get_logger("ber.models.deterministic_baseline", stage="21_deterministic_baseline")


@dataclass(frozen=True)
class DecisionResult:
    """Detailed decision explanation for an entity pair."""
    is_match: bool
    confidence: float
    rule_name: str
    target_id: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class DeterministicBaseline:
    """
    Production-grade rule-based matcher serving as the baseline for ENTIVYRE.
    Uses multi-field evidence and contradiction guards to make deterministic predictions.
    """

    def __init__(
        self,
        high_sim_threshold: float = 0.85,
        min_name_jaccard: float = 0.70,
        min_address_jaccard: float = 0.20,
        allow_missing_address_exact_name: bool = True,
    ):
        self.high_sim_threshold = high_sim_threshold
        self.min_name_jaccard = min_name_jaccard
        self.min_address_jaccard = min_address_jaccard
        self.allow_missing_address_exact_name = allow_missing_address_exact_name

    def classify_pair(
        self,
        features: Dict[str, float],
        target_id: str = "",
    ) -> DecisionResult:
        """
        Classifies an entity pair using deterministic rules.
        """
        # Hard Negatives & Contradictions (Rule 0: Rejection Guards)
        country_contra = features.get("country_contradiction", 0.0) == 1.0
        addr_contra = features.get("address_numeric_contradiction", 0.0) == 1.0

        if country_contra:
            return DecisionResult(
                is_match=False,
                confidence=0.0,
                rule_name="REJECT_COUNTRY_CONTRADICTION",
                target_id=target_id,
            )

        if addr_contra:
            return DecisionResult(
                is_match=False,
                confidence=0.0,
                rule_name="REJECT_ADDRESS_NUMERIC_CONTRADICTION",
                target_id=target_id,
            )

        # Rule 1: Exact Canonical Name Match + Compatible Address
        name_exact = (
            features.get("name_canonical_exact_match", 0.0) == 1.0
            or features.get("name_clean_exact_match", 0.0) == 1.0
        )
        addr_missing = features.get("address_is_missing", 0.0) == 1.0
        addr_compatible = (
            features.get("address_canonical_exact_match", 0.0) == 1.0
            or features.get("address_postal_code_match", 0.0) == 1.0
            or features.get("address_token_jaccard", 0.0) >= self.min_address_jaccard
            or features.get("address_levenshtein_sim", 0.0) >= 0.50
        )

        if name_exact and (addr_compatible or (addr_missing and self.allow_missing_address_exact_name)):
            return DecisionResult(
                is_match=True,
                confidence=0.96 if addr_compatible else 0.88,
                rule_name="RULE_EXACT_CANONICAL_WITH_COMPATIBLE_ADDRESS",
                target_id=target_id,
            )

        # Rule 2: High Joint Name & Address Similarity
        if features.get("name_and_address_high_sim", 0.0) == 1.0:
            return DecisionResult(
                is_match=True,
                confidence=0.92,
                rule_name="RULE_NAME_AND_ADDRESS_HIGH_SIM",
                target_id=target_id,
            )

        # Rule 3: High Overall Composite Similarity
        composite_sim = features.get("overall_composite_similarity", 0.0)
        if composite_sim >= self.high_sim_threshold:
            return DecisionResult(
                is_match=True,
                confidence=composite_sim,
                rule_name="RULE_HIGH_COMPOSITE_SCORE",
                target_id=target_id,
            )

        # Fallback: Insufficient evidence
        return DecisionResult(
            is_match=False,
            confidence=composite_sim,
            rule_name="INSUFFICIENT_EVIDENCE",
            target_id=target_id,
        )

    def predict_anchor_candidates(
        self,
        anchor_id: str,
        candidates_with_features: List[Tuple[str, Dict[str, float]]],
    ) -> List[str]:
        """
        Evaluate candidate pairs for a single anchor and return matching target IDs.
        Returns empty list [] for singletons or if no candidate satisfies matching rules.
        """
        matches: List[Tuple[str, float]] = []

        for target_id, feats in candidates_with_features:
            decision = self.classify_pair(feats, target_id=target_id)
            if decision.is_match:
                matches.append((target_id, decision.confidence))

        # Sort matches by confidence descending
        matches.sort(key=lambda x: x[1], reverse=True)

        # Deduplicate while preserving order
        seen = set()
        matched_ids: List[str] = []
        for tid, _ in matches:
            if tid not in seen:
                seen.add(tid)
                matched_ids.append(tid)

        return matched_ids

    def evaluate(
        self,
        ground_truth: Mapping[str, Collection[str]],
        predictions: Mapping[str, Collection[str]],
    ) -> Tuple[MacroEvaluationSummary, Dict[str, EntityMetricResult]]:
        """
        Evaluate predictions using the official challenge Macro F0.5 evaluator.
        """
        return compute_macro_f05(ground_truth, predictions)
