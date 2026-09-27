#!/usr/bin/env python3
"""
Explicit Unit Tests for CHALLENGER_007 Rules and Constraints:
1. score 0.56-0.58 + address Jaccard >= 0.15 => accepted
2. score 0.56-0.58 + empty address => rejected
3. shared building number + same postal + >=2 name tokens => accepted
4. exact canonical name + same postal => accepted
5. token permutation + same postal => accepted
6. contradictory building number => rejected
"""
import sys
import unittest
from pathlib import Path

# Add project root to sys.path
proj_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(proj_root / "code" / "business_entity_resolution" / "src"))

from ber.inference.engine import InferenceEngine, InferenceConfig


class TestChallenger007Rules(unittest.TestCase):
    def setUp(self):
        self.engine = InferenceEngine(InferenceConfig(decision_threshold=0.58, enable_challenger_007=True))

    def test_score_056_058_with_address_jaccard_015_accepted(self):
        """Test rule P20: score 0.56-0.58 + address Jaccard >= 0.15 => accepted."""
        # Anchor and target have moderate name match (Jaccard ~0.67) and moderate address overlap (Jaccard ~0.33)
        # yielding base score ~0.56-0.57. With non-empty target address, it must be accepted (score >= 0.58).
        anchor_canon = "phoenix energy services"
        anchor_toks = {"phoenix", "energy", "services"}
        anchor_concat = "phoenixenergyservices"
        anchor_addr_toks = {"100", "industrial", "parkway", "suite", "200"}
        anchor_num_toks = {"100", "200"}
        anchor_country = "US"
        anchor_postal = "77001"

        t_canon = "phoenix energy"
        t_addr_toks = ("100", "industrial", "way")
        t_num_toks = ("100",)
        t_country = "US"
        t_postal = "77002"
        t_name_concat = "phoenixenergy"

        score = self.engine._score_pair(
            anchor_canon, anchor_toks, anchor_concat,
            anchor_addr_toks, anchor_num_toks, anchor_country,
            t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat,
            anchor_postal,
        )
        self.assertGreaterEqual(score, 0.58, f"Expected accepted score >= 0.58 for P20, got {score}")

    def test_score_056_058_with_empty_address_rejected(self):
        """Test rule P20 negative guard: score 0.56-0.58 + empty address => rejected."""
        # Same anchor, but target address is completely empty.
        # Must NOT trigger P20, score must remain below 0.58 (or 0.0).
        anchor_canon = "phoenix energy services"
        anchor_toks = {"phoenix", "energy", "services"}
        anchor_concat = "phoenixenergyservices"
        anchor_addr_toks = {"100", "industrial", "parkway", "suite", "200"}
        anchor_num_toks = {"100", "200"}
        anchor_country = "US"
        anchor_postal = "77001"

        t_canon = "phoenix energy"
        t_addr_toks = () # EMPTY ADDRESS
        t_num_toks = ()
        t_country = "US"
        t_postal = ""
        t_name_concat = "phoenixenergy"

        score = self.engine._score_pair(
            anchor_canon, anchor_toks, anchor_concat,
            anchor_addr_toks, anchor_num_toks, anchor_country,
            t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat,
            anchor_postal,
        )
        self.assertLess(score, 0.58, f"Expected rejected score < 0.58 for empty target address, got {score}")

    def test_shared_building_same_postal_containment_accepted(self):
        """Test rule P02: shared building number + same postal + >=2 name tokens => accepted."""
        anchor_canon = "apex global logistics limited"
        anchor_toks = {"apex", "global", "logistics", "limited"}
        anchor_concat = "apexgloballogisticslimited"
        anchor_addr_toks = {"45", "harbor", "blvd", "suite", "400"}
        anchor_num_toks = {"45", "400"}
        anchor_country = "US"
        anchor_postal = "98101"

        t_canon = "apex global logistics"
        t_addr_toks = ("45", "harbor", "boulevard")
        t_num_toks = ("45",)
        t_country = "US"
        t_postal = "98101" # IDENTICAL POSTAL
        t_name_concat = "apexgloballogistics"

        score = self.engine._score_pair(
            anchor_canon, anchor_toks, anchor_concat,
            anchor_addr_toks, anchor_num_toks, anchor_country,
            t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat,
            anchor_postal,
        )
        self.assertGreaterEqual(score, 0.58, f"Expected accepted score >= 0.58 for P02, got {score}")

    def test_exact_canonical_name_same_postal_accepted(self):
        """Test rule P04: exact canonical name (>=10c) + same postal (>=5c) => accepted."""
        anchor_canon = "international dynamics corporation"
        anchor_toks = {"international", "dynamics", "corporation"}
        anchor_concat = "internationaldynamicscorporation"
        anchor_addr_toks = {"777", "broadway", "fl", "12"}
        anchor_num_toks = {"777", "12"}
        anchor_country = "US"
        anchor_postal = "10003"

        t_canon = "international dynamics corporation" # EXACT CANONICAL NAME >= 10 chars
        t_addr_toks = ("po", "box", "1234") # Different street tokens
        t_num_toks = ("1234",)
        # Note: no building number on target street to conflict with 777
        t_country = "US"
        t_postal = "10003" # EXACT POSTAL >= 5 chars
        t_name_concat = "internationaldynamicscorporation"

        # Neutralize building number for PO box target so no bldg conflict
        score = self.engine._score_pair(
            anchor_canon, anchor_toks, anchor_concat,
            anchor_addr_toks, set(), anchor_country,
            t_canon, t_addr_toks, (), t_country, t_postal, t_name_concat,
            anchor_postal,
        )
        self.assertGreaterEqual(score, 0.58, f"Expected accepted score >= 0.58 for P04, got {score}")

    def test_token_permutation_same_postal_accepted(self):
        """Test rule P16: exact token permutation (>=3 tokens) + same postal => accepted."""
        anchor_canon = "delta cloud systems"
        anchor_toks = {"delta", "cloud", "systems"}
        anchor_concat = "deltacloudsystems"
        anchor_addr_toks = {"500", "tech", "ridge"}
        anchor_num_toks = {"500"}
        anchor_country = "US"
        anchor_postal = "78758"

        t_canon = "systems cloud delta" # PERMUTATION OF EXACT 3 TOKENS
        t_addr_toks = ("suite", "a")
        t_num_toks = ()
        t_country = "US"
        t_postal = "78758" # SAME POSTAL
        t_name_concat = "systemsclouddelta"

        score = self.engine._score_pair(
            anchor_canon, anchor_toks, anchor_concat,
            anchor_addr_toks, anchor_num_toks, anchor_country,
            t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat,
            anchor_postal,
        )
        self.assertGreaterEqual(score, 0.58, f"Expected accepted score >= 0.58 for P16, got {score}")

    def test_contradictory_building_number_rejected(self):
        """Test negative constraint A: contradictory building number => rejected (score = 0.0)."""
        anchor_canon = "apex global logistics limited"
        anchor_toks = {"apex", "global", "logistics", "limited"}
        anchor_concat = "apexgloballogisticslimited"
        anchor_addr_toks = {"45", "harbor", "blvd"}
        anchor_num_toks = {"45"} # Building 45
        anchor_country = "US"
        anchor_postal = "98101"

        t_canon = "apex global logistics limited" # Even with EXACT name
        t_addr_toks = ("99", "harbor", "blvd")
        t_num_toks = ("99",) # Building 99 -> CONFLICT!
        t_country = "US"
        t_postal = "98101"
        t_name_concat = "apexgloballogisticslimited"

        score = self.engine._score_pair(
            anchor_canon, anchor_toks, anchor_concat,
            anchor_addr_toks, anchor_num_toks, anchor_country,
            t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat,
            anchor_postal,
        )
        self.assertEqual(score, 0.0, f"Expected 0.0 for building conflict veto, got {score}")


if __name__ == "__main__":
    unittest.main()
