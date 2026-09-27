"""
Unit and Integration Tests for Phase 29: Ablation Experimentation Engine.
"""
import unittest
import tempfile
from pathlib import Path

from ber.experiments.ablation_engine import AblationEngine


class TestAblationEngine(unittest.TestCase):
    def test_run_ablation_study(self):
        engine = AblationEngine(run_prefix="test_abl_")

        gt = {
            "S1-1": ("S2-1",),
            "S1-2": (), # singleton
        }

        # Candidates with features
        val_anchor_candidates = {
            "S1-1": [
                ("S2-1", 0.95, {
                    "address_numeric_contradiction": 0.0,
                    "country_contradiction": 0.0,
                    "address_token_jaccard": 0.8,
                    "in_tfidf_retriever": 1.0,
                }),
                ("S2-FALSE", 0.85, {
                    "address_numeric_contradiction": 1.0, # Building contradiction!
                    "country_contradiction": 0.0,
                    "address_token_jaccard": 0.0,
                    "in_tfidf_retriever": 1.0,
                }),
            ],
            "S1-2": [
                ("S2-CROSS_CTRY", 0.90, {
                    "address_numeric_contradiction": 0.0,
                    "country_contradiction": 1.0, # Country collision!
                    "address_token_jaccard": 0.7,
                    "in_tfidf_retriever": 1.0,
                }),
            ],
        }

        def mock_predict_fn_generator(cfg):
            def predict_fn(cands):
                matches = []
                for tid, score, feats in cands:
                    # Guard checks
                    if cfg["use_numeric_guard"] and feats.get("address_numeric_contradiction") == 1.0:
                        continue
                    if cfg["use_country_guard"] and feats.get("country_contradiction") == 1.0:
                        continue
                    if not cfg["use_address"] and feats.get("address_token_jaccard", 0.0) < 0.5:
                        pass # Ignore address
                    if not cfg["use_dual_pass"] and feats.get("in_tfidf_retriever") == 1.0 and tid == "S2-1":
                        continue # Simulate missing S2-1 without dual pass!
                    if score >= 0.70:
                        matches.append(tid)
                return matches
            return predict_fn

        results = engine.run_ablation_study(gt, val_anchor_candidates, mock_predict_fn_generator)

        self.assertEqual(len(results), 5)
        # Full system should have best score (1.0)
        self.assertEqual(results[0].ablation_name, "FULL_SYSTEM")
        self.assertEqual(results[0].macro_f05, 1.0)

        # Minus numeric guard should accept S2-FALSE on S1-1 -> lowers score
        no_num = results[2]
        self.assertEqual(no_num.ablation_name, "MINUS_NUMERIC_CONTRADICTION_GUARD")
        self.assertLess(no_num.macro_f05, 1.0)

        # Minus country guard should accept S2-CROSS_CTRY on S1-2 (singleton false merge -> 0 credit) -> lowers score
        no_ctry = results[3]
        self.assertEqual(no_ctry.ablation_name, "MINUS_COUNTRY_CONTRADICTION_GUARD")
        self.assertLess(no_ctry.macro_f05, 1.0)

        # Test export
        with tempfile.TemporaryDirectory() as tmpdir:
            json_file = Path(tmpdir) / "ablation_results.json"
            md_file = Path(tmpdir) / "ablation_results.md"

            engine.save_json(json_file)
            engine.save_markdown(md_file)

            self.assertTrue(json_file.exists())
            self.assertTrue(md_file.exists())


if __name__ == "__main__":
    unittest.main()
