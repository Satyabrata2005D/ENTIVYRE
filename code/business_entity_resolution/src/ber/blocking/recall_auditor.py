"""
Candidate Recall and Blocking Quality Auditor for ENTIVYRE.
Phase 15: Rigorous evaluation of candidate generation recall upper bounds,
multiplicity breakdowns, country diagnostics, candidate volume distributions,
reduction ratios, and missed-match forensic logging.

Guarantees:
- Audits mathematical upper bound on final recall: Final Recall <= Candidate Recall.
- Breaks down recall across sources (S2 vs S3), countries (US vs India vs open-set), and multiplicity.
- Evaluates candidate volume distribution (mean, median, p90, max).
- Extracts diagnostic samples of missed true matches to identify edge cases.
- Produces structured JSON audit reports.
"""
from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple, Any

from entivyre.utils.logger import get_logger
from ber.labels.ground_truth import GroundTruthStore

logger = get_logger("ber.blocking.recall_auditor", stage="15_candidate_recall_audit")


@dataclass(frozen=True)
class RecallAuditReport:
    """Comprehensive candidate recall and quality audit report."""
    total_anchors: int
    matched_anchors: int
    singleton_anchors: int
    total_true_targets: int
    total_found_targets: int
    global_target_recall: float
    anchor_full_recall_rate: float
    anchor_partial_recall_rate: float
    anchor_zero_recall_rate: float
    source2_target_recall: float
    source3_target_recall: float
    country_recall: Dict[str, float]
    candidate_volume: Dict[str, float]
    reduction_ratio: float
    missed_matches_sample: List[Dict[str, Any]]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class CandidateRecallAuditor:
    """
    Evaluator and forensic auditor for candidate generation pipelines.
    """

    def audit(
        self,
        candidate_pairs_map: Dict[str, List[str]],
        ground_truth: GroundTruthStore,
        anchor_countries: Optional[Dict[str, str]] = None,
        total_target_population: int = 10_000_000,
        max_missed_samples: int = 50,
    ) -> RecallAuditReport:
        """
        Audit candidate recall across anchors and ground truth.
        """
        total_anchors = len(candidate_pairs_map)
        matched_anchors = 0
        singleton_anchors = 0

        total_true_targets = 0
        total_found_targets = 0

        full_recall_count = 0
        partial_recall_count = 0
        zero_recall_count = 0

        s2_true = 0
        s2_found = 0
        s3_true = 0
        s3_found = 0

        country_true: Dict[str, int] = defaultdict(int)
        country_found: Dict[str, int] = defaultdict(int)

        candidate_counts: List[int] = []
        missed_samples: List[Dict[str, Any]] = []

        total_candidate_pairs = 0

        for aid, cands in candidate_pairs_map.items():
            n_cands = len(cands)
            candidate_counts.append(n_cands)
            total_candidate_pairs += n_cands

            cand_set = set(cands)
            true_targets = ground_truth.get_target_set(aid)
            n_true = len(true_targets)

            if n_true == 0:
                singleton_anchors += 1
                continue

            matched_anchors += 1
            total_true_targets += n_true

            # Intersect with candidates
            found = true_targets & cand_set
            n_found = len(found)
            total_found_targets += n_found

            # Anchor-level recall category
            if n_found == n_true:
                full_recall_count += 1
            elif n_found > 0:
                partial_recall_count += 1
            else:
                zero_recall_count += 1

            # Source breakdowns
            for tid in true_targets:
                is_s2 = tid.startswith("S2-") or "source2" in tid
                is_s3 = tid.startswith("S3-") or "source3" in tid

                if is_s2:
                    s2_true += 1
                    if tid in cand_set:
                        s2_found += 1
                elif is_s3:
                    s3_true += 1
                    if tid in cand_set:
                        s3_found += 1

            # Country breakdowns
            ctry = (anchor_countries.get(aid, "UNKNOWN") if anchor_countries else "ALL")
            country_true[ctry] += n_true
            country_found[ctry] += n_found

            # Forensic sampling of missed targets
            missed = true_targets - cand_set
            if missed and len(missed_samples) < max_missed_samples:
                missed_samples.append({
                    "anchor_id": aid,
                    "country": ctry,
                    "total_true": n_true,
                    "found_count": n_found,
                    "missed_targets": list(missed),
                    "candidate_sample": cands[:5],
                })

        # Calculations
        global_recall = (total_found_targets / total_true_targets) if total_true_targets > 0 else 1.0
        full_rec_rate = (full_recall_count / matched_anchors) if matched_anchors > 0 else 1.0
        part_rec_rate = (partial_recall_count / matched_anchors) if matched_anchors > 0 else 0.0
        zero_rec_rate = (zero_recall_count / matched_anchors) if matched_anchors > 0 else 0.0

        s2_rec = (s2_found / s2_true) if s2_true > 0 else 1.0
        s3_rec = (s3_found / s3_true) if s3_true > 0 else 1.0

        country_rec: Dict[str, float] = {}
        for c, t_cnt in country_true.items():
            f_cnt = country_found[c]
            country_rec[c] = round(f_cnt / t_cnt, 4) if t_cnt > 0 else 1.0

        # Volume percentiles
        candidate_counts.sort()
        mean_cands = (total_candidate_pairs / total_anchors) if total_anchors > 0 else 0.0
        med_cands = candidate_counts[len(candidate_counts) // 2] if candidate_counts else 0
        p90_idx = int(len(candidate_counts) * 0.90)
        p90_cands = candidate_counts[p90_idx] if candidate_counts else 0
        max_cands = candidate_counts[-1] if candidate_counts else 0

        # Reduction ratio: 1 - (total_candidate_pairs / (total_anchors * total_target_population))
        total_possible = total_anchors * total_target_population
        red_ratio = 1.0 - (total_candidate_pairs / total_possible) if total_possible > 0 else 1.0

        report = RecallAuditReport(
            total_anchors=total_anchors,
            matched_anchors=matched_anchors,
            singleton_anchors=singleton_anchors,
            total_true_targets=total_true_targets,
            total_found_targets=total_found_targets,
            global_target_recall=round(global_recall, 4),
            anchor_full_recall_rate=round(full_rec_rate, 4),
            anchor_partial_recall_rate=round(part_rec_rate, 4),
            anchor_zero_recall_rate=round(zero_rec_rate, 4),
            source2_target_recall=round(s2_rec, 4),
            source3_target_recall=round(s3_rec, 4),
            country_recall=country_rec,
            candidate_volume={
                "mean": round(mean_cands, 2),
                "median": float(med_cands),
                "p90": float(p90_cands),
                "max": float(max_cands),
            },
            reduction_ratio=round(red_ratio, 6),
            missed_matches_sample=missed_samples,
        )

        logger.info(
            f"Candidate recall audit completed: global_recall={report.global_target_recall}, full_recall_rate={report.anchor_full_recall_rate}",
            extra={"payload": report.to_dict()},
        )
        return report

    @staticmethod
    def save_report(report: RecallAuditReport, output_path: Path) -> Path:
        """Persist recall audit report to JSON."""
        p = Path(output_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(report.to_dict(), f, indent=2)
        return p
