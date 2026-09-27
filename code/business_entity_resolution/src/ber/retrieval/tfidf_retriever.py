"""
Sparse Character N-Gram TF-IDF Retrieval Engine for ENTIVYRE.
Phase 13: Sub-word character n-gram inverted index with TF-IDF weighting and
cosine similarity nearest-neighbor candidate retrieval.

Guarantees:
- Pure-Python, zero external C-dependencies (100% reproducible and air-gapped).
- Sub-word typo tolerance: matches OCR errors, spelling variants, and missing hyphens.
- Inverted index dot product: only computes cosine similarity for records sharing n-grams.
- Threshold filtering and Top-K bounding.
- High throughput and low memory footprint using compact tuples and posting arrays.
"""
from __future__ import annotations

import math
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from typing import Dict, Iterable, List, Optional, Set, Tuple, Any

from entivyre.utils.logger import get_logger
from ber.normalization.name_normalizer import compute_char_ngrams

logger = get_logger("ber.retrieval.tfidf_retriever", stage="13_char_ngram_retrieval")


@dataclass(frozen=True)
class RetrievalCandidate:
    """A retrieved candidate target with its TF-IDF cosine similarity score."""
    target_id: str
    similarity_score: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class SparseCharTfidfRetriever:
    """
    High-performance inverted index character n-gram TF-IDF retrieval engine.
    Computes exact sparse cosine similarity across candidate targets.
    """

    def __init__(
        self,
        ngram_size: int = 3,
        min_df: int = 1,
        max_df_ratio: float = 0.80,
    ):
        self.ngram_size = ngram_size
        self.min_df = min_df
        self.max_df_ratio = max_df_ratio

        # State after indexing
        self._doc_ids: List[str] = []
        self._idf: Dict[str, float] = {}
        # Inverted index: ngram -> list of (doc_idx, unit_weight)
        self._postings: Dict[str, List[Tuple[int, float]]] = defaultdict(list)
        self._is_indexed: bool = False

    @property
    def total_indexed_docs(self) -> int:
        return len(self._doc_ids)

    @property
    def vocabulary_size(self) -> int:
        return len(self._idf)

    def fit_and_index(self, records: List[Tuple[str, str]]) -> None:
        """
        Fit IDF and construct inverted index from target records (entity_id, text).
        """
        n_docs = len(records)
        if n_docs == 0:
            logger.warning("Empty records passed to fit_and_index")
            return

        self._doc_ids = []
        doc_term_freqs: List[Counter[str]] = []
        df_counts: Counter[str] = Counter()

        # Step 1: Collect document frequencies and term frequencies
        for entity_id, text in records:
            self._doc_ids.append(entity_id)
            ngrams = compute_char_ngrams(text, n=self.ngram_size)
            tf = Counter(ngrams)
            doc_term_freqs.append(tf)
            for ngram in tf.keys():
                df_counts[ngram] += 1

        # Step 2: Compute smooth IDF with min_df and max_df filtering
        max_df = int(n_docs * self.max_df_ratio) if n_docs > 10 else n_docs + 1
        self._idf = {}

        for ngram, df in df_counts.items():
            if df >= self.min_df and df <= max_df:
                # Standard smooth IDF formula: log((1 + N) / (1 + df)) + 1
                self._idf[ngram] = math.log((1.0 + n_docs) / (1.0 + df)) + 1.0

        # Step 3: Compute unit-norm weights and build inverted index
        self._postings = defaultdict(list)

        for doc_idx, tf in enumerate(doc_term_freqs):
            # Compute squared Euclidean norm of document vector
            sum_sq = 0.0
            doc_weights: Dict[str, float] = {}

            for ngram, count in tf.items():
                idf_val = self._idf.get(ngram)
                if idf_val is not None:
                    # Sublinear TF scaling: 1 + log(tf)
                    weight = (1.0 + math.log(count)) * idf_val
                    doc_weights[ngram] = weight
                    sum_sq += weight * weight

            norm = math.sqrt(sum_sq)
            if norm > 0.0:
                inv_norm = 1.0 / norm
                for ngram, weight in doc_weights.items():
                    unit_weight = weight * inv_norm
                    self._postings[ngram].append((doc_idx, unit_weight))

        self._is_indexed = True
        logger.info(
            f"Indexed {n_docs} documents with vocabulary of {len(self._idf)} n-grams",
            extra={"payload": {"total_docs": n_docs, "vocab_size": len(self._idf)}},
        )

    def retrieve_top_k(
        self,
        query_text: str,
        k: int = 20,
        min_similarity: float = 0.35,
    ) -> List[RetrievalCandidate]:
        """
        Retrieve Top-K candidates for a query text by cosine similarity.
        Only considers documents sharing at least one character n-gram.
        """
        if not self._is_indexed or not query_text:
            return []

        # 1. Compute query TF-IDF vector
        q_ngrams = compute_char_ngrams(query_text, n=self.ngram_size)
        q_tf = Counter(q_ngrams)

        q_weights: Dict[str, float] = {}
        sum_sq = 0.0

        for ngram, count in q_tf.items():
            idf_val = self._idf.get(ngram)
            if idf_val is not None:
                w = (1.0 + math.log(count)) * idf_val
                q_weights[ngram] = w
                sum_sq += w * w

        q_norm = math.sqrt(sum_sq)
        if q_norm == 0.0:
            return []

        inv_q_norm = 1.0 / q_norm

        # 2. Accumulate dot products across inverted posting lists
        scores: Dict[int, float] = defaultdict(float)

        for ngram, w in q_weights.items():
            query_unit_w = w * inv_q_norm
            postings = self._postings.get(ngram)
            if postings:
                for doc_idx, doc_unit_w in postings:
                    scores[doc_idx] += query_unit_w * doc_unit_w

        # 3. Filter by min_similarity threshold and select Top-K
        candidates: List[RetrievalCandidate] = []
        for doc_idx, score in scores.items():
            if score >= min_similarity:
                candidates.append(
                    RetrievalCandidate(
                        target_id=self._doc_ids[doc_idx],
                        similarity_score=round(score, 4),
                    )
                )

        # Sort descending by similarity score, then ascending by target_id for determinism
        candidates.sort(key=lambda c: (-c.similarity_score, c.target_id))
        return candidates[:k]

    def compute_cosine_similarity(self, text1: str, text2: str) -> float:
        """
        Compute cosine similarity between two strings using the fitted IDF model.
        Returns float in [0.0, 1.0].
        """
        if not text1 or not text2:
            return 0.0

        # Identical strings
        if text1 == text2:
            return 1.0

        tf1 = Counter(compute_char_ngrams(text1, n=self.ngram_size))
        tf2 = Counter(compute_char_ngrams(text2, n=self.ngram_size))

        shared_terms = set(tf1.keys()) & set(tf2.keys())
        if not shared_terms:
            return 0.0

        dot_product = 0.0
        norm1_sq = 0.0
        norm2_sq = 0.0

        for term, cnt in tf1.items():
            idf_val = self._idf.get(term, 1.0)
            w = (1.0 + math.log(cnt)) * idf_val
            norm1_sq += w * w
            if term in tf2:
                w2 = (1.0 + math.log(tf2[term])) * idf_val
                dot_product += w * w2

        for term, cnt in tf2.items():
            idf_val = self._idf.get(term, 1.0)
            w = (1.0 + math.log(cnt)) * idf_val
            norm2_sq += w * w

        norm1 = math.sqrt(norm1_sq)
        norm2 = math.sqrt(norm2_sq)

        if norm1 == 0.0 or norm2 == 0.0:
            return 0.0

        return min(1.0, max(0.0, dot_product / (norm1 * norm2)))
