#!/usr/bin/env python3
"""
Explicit Unit Tests for CHALLENGER_008 Rules and Constraints:
1. P01_82: High Address Overlap (addr_sim >= 0.82) + Business Name Overlap => accepted (0.585)
2. P01_82: Exception to name_sim < 0.45 floor when addr_sim >= 0.82 and token overlap >= 1 => accepted
3. P01_82 Negative Guard: addr_sim < 0.82 with name_sim < 0.45 => rejected (0.0)
4. P_POSTAL_080: Shared exact postal code (>=5 digits) + name Jaccard >= 0.80 => accepted (0.585)
5. P_POSTAL_080 Negative Guard: short postal (<5 digits) or name Jaccard < 0.80 => rejected
6. Building number contradiction veto => strictly rejected (0.0)
7. Country contradiction veto => strictly rejected (0.0)
8. Empty address guard => strictly rejected
"""
import sys
import unittest
from pathlib import Path

# Add project root to sys.path
proj_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(proj_root / "code" / "business_entity_resolution" / "src"))

from ber.inference.engine import InferenceEngine, InferenceConfig


class TestChallenger008Rules(unittest.TestCase):
    def setUp(self):
        self.engine = InferenceEngine(InferenceConfig(decision_threshold=0.58, enable_challenger_008=True))

    def test_p01_82_high_address_overlap_accepted(self):
        """Test rule P01_82: High address overlap (>=0.82) with shared name token => accepted."""
        anchor_canon = "la fontaine restaurant bar"
        anchor_toks = {"la", "fontaine", "restaurant", "bar"}
        anchor_concat = "lafontainerestaurantbar"
        anchor_addr_toks = {"12", "rue", "de", "la", "paix", "75002", "paris"}
        anchor_num_toks = {"12"}
        anchor_country = "FR"
        anchor_postal = "75002"

        # Target has near-identical address, but slightly different legal name representation
        t_canon = "fontaine gourmande"
        t_addr_toks = ("12", "rue", "de", "la", "paix", "75002", "paris")
        t_num_toks = ("12",)
        t_country = "FR"
        t_postal = "75002"
        t_name_concat = "fontainegourmande"

        score = self.engine._score_pair(
            anchor_canon, anchor_toks, anchor_concat,
            anchor_addr_toks, anchor_num_toks, anchor_country,
            t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat,
            anchor_postal,
        )
        self.assertGreaterEqual(score, 0.58, f"Expected accepted score >= 0.58 for P01_82, got {score}")

    def test_p01_82_name_sim_below_45_exception_accepted(self):
        """Test rule P01_82: Even when name Jaccard is low (<0.45), high address overlap (>=0.82) unlocks acceptance."""
        # Anchor has 4 tokens, Target has 3 tokens, overlap is only 1 token ("aurora"). Jaccard = 1/6 = 0.167 < 0.45.
        # But address is 100% identical.
        anchor_canon = "aurora global holdings corporation"
        anchor_toks = {"aurora", "global", "holdings", "corporation"}
        anchor_concat = "auroraglobalholdingscorporation"
        anchor_addr_toks = {"500", "madison", "avenue", "new", "york"}
        anchor_num_toks = {"500"}
        anchor_country = "US"
        anchor_postal = "10022"

        t_canon = "aurora capital partners"
        t_addr_toks = ("500", "madison", "avenue", "new", "york")
        t_num_toks = ("500",)
        t_country = "US"
        t_postal = "10022"
        t_name_concat = "auroracapitalpartners"

        score = self.engine._score_pair(
            anchor_canon, anchor_toks, anchor_concat,
            anchor_addr_toks, anchor_num_toks, anchor_country,
            t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat,
            anchor_postal,
        )
        self.assertGreaterEqual(score, 0.58, f"Expected accepted score >= 0.58 via P01_82 exception, got {score}")

    def test_p01_82_low_addr_sim_rejected(self):
        """Test rule P01_82 negative guard: When addr_sim < 0.82 and name_sim < 0.45, must be rejected (0.0)."""
        anchor_canon = "aurora global holdings corporation"
        anchor_toks = {"aurora", "global", "holdings", "corporation"}
        anchor_concat = "auroraglobalholdingscorporation"
        anchor_addr_toks = {"500", "madison", "avenue", "new", "york", "ny", "10022"}
        anchor_num_toks = {"500"}
        anchor_country = "US"
        anchor_postal = "10022"

        # Address has low overlap (< 0.82)
        t_canon = "aurora capital partners"
        t_addr_toks = ("500", "broadway", "suite", "10", "brooklyn")
        t_num_toks = ("500", "10")
        t_country = "US"
        t_postal = "11201"
        t_name_concat = "auroracapitalpartners"

        score = self.engine._score_pair(
            anchor_canon, anchor_toks, anchor_concat,
            anchor_addr_toks, anchor_num_toks, anchor_country,
            t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat,
            anchor_postal,
        )
        self.assertEqual(score, 0.0, f"Expected 0.0 for low addr_sim and low name_sim, got {score}")

    def test_p_postal_080_accepted(self):
        """Test rule P_POSTAL_080: Shared exact postal code (>=5 digits) + name Jaccard >= 0.80 => accepted."""
        anchor_canon = "shri krishna tech enterprises limited"
        anchor_toks = {"shri", "krishna", "tech", "enterprises", "limited"}
        anchor_concat = "shrikrishnatechenterpriseslimited"
        anchor_addr_toks = {"plot", "45", "midc", "industrial", "area"}
        anchor_num_toks = {"45"}
        anchor_country = "IN"
        anchor_postal = "400093"

        t_canon = "shri krishna tech enterprises"
        t_addr_toks = ("midc", "andheri", "east") # different street wording, but no bldg conflict
        t_num_toks = ()
        t_country = "IN"
        t_postal = "400093" # exact 6-digit postal match
        t_name_concat = "shrikrishnatechenterprises"

        score = self.engine._score_pair(
            anchor_canon, anchor_toks, anchor_concat,
            anchor_addr_toks, anchor_num_toks, anchor_country,
            t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat,
            anchor_postal,
        )
        self.assertGreaterEqual(score, 0.58, f"Expected accepted score >= 0.58 for P_POSTAL_080, got {score}")

    def test_p_postal_080_short_postal_rejected(self):
        """Test rule P_POSTAL_080 negative guard: postal code < 5 digits must NOT trigger P_POSTAL_080."""
        anchor_canon = "shri krishna enterprises limited"
        anchor_toks = {"shri", "krishna", "enterprises", "limited"}
        anchor_concat = "shrikrishnaenterpriseslimited"
        anchor_addr_toks = {"plot", "45", "midc", "industrial", "area"}
        anchor_num_toks = {"45"}
        anchor_country = "IN"
        anchor_postal = "400" # short 3-digit code

        t_canon = "shri krishna enterprises"
        t_addr_toks = ("midc", "andheri", "east")
        t_num_toks = ()
        t_country = "IN"
        t_postal = "400"
        t_name_concat = "shrikrishnaenterprises"

        score = self.engine._score_pair(
            anchor_canon, anchor_toks, anchor_concat,
            anchor_addr_toks, anchor_num_toks, anchor_country,
            t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat,
            anchor_postal,
        )
        # Should not get boosted to 0.585
        self.assertLess(score, 0.58, f"Expected rejected score for short postal code, got {score}")

    def test_building_conflict_strictly_vetoed(self):
        """Test negative veto: Building number contradiction must strictly return 0.0."""
        anchor_canon = "fontaine restaurant"
        anchor_toks = {"fontaine", "restaurant"}
        anchor_concat = "fontainerestaurant"
        anchor_addr_toks = {"12", "rue", "de", "la", "paix", "paris"}
        anchor_num_toks = {"12"} # Number 12
        anchor_country = "FR"
        anchor_postal = "75002"

        t_canon = "fontaine restaurant"
        t_addr_toks = ("99", "rue", "de", "la", "paix", "paris") # Number 99 != 12
        t_num_toks = ("99",)
        t_country = "FR"
        t_postal = "75002"
        t_name_concat = "fontainerestaurant"

        score = self.engine._score_pair(
            anchor_canon, anchor_toks, anchor_concat,
            anchor_addr_toks, anchor_num_toks, anchor_country,
            t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat,
            anchor_postal,
        )
        self.assertEqual(score, 0.0, f"Expected 0.0 for building number contradiction, got {score}")

    def test_country_conflict_strictly_vetoed(self):
        """Test negative veto: Country mismatch must strictly return 0.0."""
        anchor_canon = "global energy trading"
        anchor_toks = {"global", "energy", "trading"}
        anchor_concat = "globalenergytrading"
        anchor_addr_toks = {"100", "main", "street"}
        anchor_num_toks = {"100"}
        anchor_country = "US"
        anchor_postal = "10001"

        t_canon = "global energy trading"
        t_addr_toks = ("100", "main", "street")
        t_num_toks = ("100",)
        t_country = "GB" # Country mismatch: US vs GB
        t_postal = "10001"
        t_name_concat = "globalenergytrading"

        score = self.engine._score_pair(
            anchor_canon, anchor_toks, anchor_concat,
            anchor_addr_toks, anchor_num_toks, anchor_country,
            t_canon, t_addr_toks, t_num_toks, t_country, t_postal, t_name_concat,
            anchor_postal,
        )
        self.assertEqual(score, 0.0, f"Expected 0.0 for country mismatch, got {score}")


if __name__ == "__main__":
    unittest.main()
