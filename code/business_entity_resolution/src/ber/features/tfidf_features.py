"""
TF-IDF and Character N-Gram Feature Extraction Engine for ENTIVYRE.
Phase 18: Extraction of sub-word character n-gram cosine similarities for names
and addresses, word-level token TF-IDF, and retrieval score alignment.

Guarantees:
- Pairwise cosine similarities in [0.0, 1.0].
- Safe handling of missing addresses and names.
- Conforms strictly with FeatureRegistry schema contracts.
"""
from __future__ import annotations

import math
from collections import Counter
from typing import Dict, Iterable, Optional, Set, Tuple, Any

from ber.normalization.name_normalizer import NormalizedName, compute_char_ngrams
from ber.normalization.address_normalizer import NormalizedAddress
from ber.retrieval.tfidf_retriever import SparseCharTfidfRetriever


class TfidfFeatureExtractor:
    """
    Computes TF-IDF cosine similarity features across names and addresses.
    """

    def __init__(self, char_retriever: Optional[SparseCharTfidfRetriever] = None):
        self.char_retriever = (
            char_retriever if char_retriever is not None
            else SparseCharTfidfRetriever(ngram_size=3)
        )

    def compute_cosine(self, text1: str, text2: str) -> float:
        """Compute character n-gram cosine similarity between two text strings."""
        if not text1 or not text2:
            return 0.0
        return self.char_retriever.compute_cosine_similarity(text1, text2)

    def extract_features(
        self,
        anchor_name: NormalizedName,
        candidate_name: NormalizedName,
        anchor_addr: NormalizedAddress,
        candidate_addr: NormalizedAddress,
        tfidf_retrieval_score: float = 0.0,
    ) -> Dict[str, float]:
        """
        Extract TF-IDF cosine features for a pair.
        """
        # Name character n-gram cosine
        name_sim = self.compute_cosine(anchor_name.canonical, candidate_name.canonical)

        # Address character n-gram cosine
        if anchor_addr.is_empty or candidate_addr.is_empty:
            addr_sim = 0.0
        else:
            addr_sim = self.compute_cosine(anchor_addr.canonical, candidate_addr.canonical)

        return {
            "name_char_ngram_cosine": round(name_sim, 4),
            "address_char_ngram_cosine": round(addr_sim, 4),
            "tfidf_retrieval_score": round(float(tfidf_retrieval_score), 4),
        }
