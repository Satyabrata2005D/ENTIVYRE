"""
Unit and Integration Tests for Phase 23 & Phase 24: Supervised Learning & Tree Ensemble Models.
"""
import unittest
import tempfile
from pathlib import Path

from ber.models.logistic_regression import LogisticRegressionClassifier
from ber.models.tree_ensemble import GradientBoostedDecisionStumps


class TestSupervisedModels(unittest.TestCase):
    def setUp(self):
        # Create a synthetic dataset of 33-dimensional ER feature vectors
        # Positives: high similarities (features 0-10, 11-20 ~ 0.8-1.0, contradiction features = 0.0)
        # Negatives: low similarities or high contradictions
        self.X_train = []
        self.y_train = []

        # 20 positive pairs
        for i in range(20):
            vec = [0.85 + 0.01 * (i % 10)] * 33
            vec[28] = 0.0  # address_numeric_contradiction = 0
            vec[31] = 0.0  # country_contradiction = 0
            self.X_train.append(vec)
            self.y_train.append(1.0)

        # 30 negative pairs
        for i in range(30):
            vec = [0.15 + 0.01 * (i % 10)] * 33
            if i % 2 == 0:
                vec[28] = 1.0  # numeric contradiction
            self.X_train.append(vec)
            self.y_train.append(0.0)

    def test_logistic_regression_fit_and_predict(self):
        model = LogisticRegressionClassifier(learning_rate=0.1, max_epochs=25, seed=42)
        fit_res = model.fit(self.X_train, self.y_train)

        # Verify loss decreased
        self.assertLess(fit_res["final_loss"], fit_res["loss_history"][0])

        # Test predictions on strong positive vs strong negative
        test_pos = [0.95] * 33
        test_pos[28] = 0.0
        test_pos[31] = 0.0

        test_neg = [0.10] * 33
        test_neg[28] = 1.0

        p_pos = model.predict_proba_single(test_pos)
        p_neg = model.predict_proba_single(test_neg)

        self.assertGreater(p_pos, 0.70)
        self.assertLess(p_neg, 0.30)

        # Test save and load round-trip
        with tempfile.TemporaryDirectory() as tmpdir:
            model_path = Path(tmpdir) / "logreg_model.json"
            model.save(model_path)
            loaded_model = LogisticRegressionClassifier.load(model_path)
            self.assertEqual(loaded_model.predict_proba_single(test_pos), p_pos)
            self.assertEqual(loaded_model.predict_proba_single(test_neg), p_neg)

    def test_gradient_boosted_stumps_fit_and_predict(self):
        model = GradientBoostedDecisionStumps(n_estimators=15, learning_rate=0.15, seed=42)
        fit_res = model.fit(self.X_train, self.y_train)

        # Verify loss decreased
        self.assertLess(fit_res["final_loss"], fit_res["loss_history"][0])
        self.assertEqual(len(model.estimators), 15)

        # Test predictions on strong positive vs strong negative
        test_pos = [0.95] * 33
        test_pos[28] = 0.0
        test_pos[31] = 0.0

        test_neg = [0.10] * 33
        test_neg[28] = 1.0

        p_pos = model.predict_proba_single(test_pos)
        p_neg = model.predict_proba_single(test_neg)

        self.assertGreater(p_pos, 0.70)
        self.assertLess(p_neg, 0.30)

        # Test save and load round-trip
        with tempfile.TemporaryDirectory() as tmpdir:
            model_path = Path(tmpdir) / "boosted_stumps_model.json"
            model.save(model_path)
            loaded_model = GradientBoostedDecisionStumps.load(model_path)
            self.assertEqual(loaded_model.predict_proba_single(test_pos), p_pos)
            self.assertEqual(loaded_model.predict_proba_single(test_neg), p_neg)


if __name__ == "__main__":
    unittest.main()
