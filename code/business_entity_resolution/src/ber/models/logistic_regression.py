"""
Supervised Logistic Regression Classifier for ENTIVYRE.
Phase 23: Supervised linear model with L2 regularization, feature standardization,
and numerical stability guarantees for business entity pair scoring.

Guarantees:
- Pure-Python, zero external C-dependencies (100% portable on Python 3.10+ / 3.14).
- Numerically stable sigmoid function preventing overflow/underflow.
- Feature standardization (z-score scaling) fitted on training data.
- L2 weight regularization preventing overfitting.
- Mini-batch SGD optimization with learning rate decay.
- Calibrated probability output P(match | x) in [0.0, 1.0].
- Deterministic JSON model weights serialization and deserialization.
"""
from __future__ import annotations

import json
import math
import random
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Tuple, Any

from entivyre.utils.logger import get_logger

logger = get_logger("ber.models.logistic_regression", stage="23_logistic_regression")


def _stable_sigmoid(z: float) -> float:
    """Numerically stable sigmoid function."""
    if z >= 0.0:
        ez = math.exp(-z)
        return 1.0 / (1.0 + ez)
    else:
        ez = math.exp(z)
        return ez / (1.0 + ez)


class LogisticRegressionClassifier:
    """
    Production-grade Logistic Regression model for entity pair classification.
    """

    def __init__(
        self,
        learning_rate: float = 0.05,
        l2_reg: float = 0.001,
        max_epochs: int = 50,
        batch_size: int = 32,
        seed: int = 42,
    ):
        self.learning_rate = learning_rate
        self.l2_reg = l2_reg
        self.max_epochs = max_epochs
        self.batch_size = batch_size
        self.seed = seed

        self.weights: List[float] = []
        self.bias: float = 0.0
        self.means: List[float] = []
        self.stds: List[float] = []
        self.is_fitted: bool = False

    def _compute_scaling(self, X: List[List[float]]) -> None:
        """Compute mean and standard deviation for feature standardization."""
        n_samples = len(X)
        n_features = len(X[0])
        self.means = [0.0] * n_features
        self.stds = [1.0] * n_features

        if n_samples == 0:
            return

        for col in range(n_features):
            col_vals = [X[row][col] for row in range(n_samples)]
            mean = sum(col_vals) / n_samples
            var = sum((v - mean) ** 2 for v in col_vals) / n_samples
            std = math.sqrt(var) if var > 1e-12 else 1.0

            self.means[col] = mean
            self.stds[col] = std

    def _scale_vector(self, x: List[float]) -> List[float]:
        """Apply standardization to a single feature vector."""
        return [
            (val - m) / s
            for val, m, s in zip(x, self.means, self.stds)
        ]

    def fit(self, X: List[List[float]], y: List[float]) -> Dict[str, Any]:
        """
        Train logistic regression model using mini-batch SGD with L2 regularization.
        """
        n_samples = len(X)
        if n_samples == 0:
            raise ValueError("Training dataset X cannot be empty.")
        n_features = len(X[0])

        self._compute_scaling(X)
        scaled_X = [self._scale_vector(x) for x in X]

        rng = random.Random(self.seed)
        # Xavier-like initial weights
        bound = 1.0 / math.sqrt(n_features) if n_features > 0 else 0.1
        self.weights = [rng.uniform(-bound, bound) for _ in range(n_features)]
        self.bias = 0.0

        indices = list(range(n_samples))
        loss_history: List[float] = []

        for epoch in range(self.max_epochs):
            rng.shuffle(indices)
            epoch_loss = 0.0
            lr = self.learning_rate / (1.0 + 0.02 * epoch)

            for start_idx in range(0, n_samples, self.batch_size):
                batch_indices = indices[start_idx : start_idx + self.batch_size]
                bs = len(batch_indices)

                grad_w = [0.0] * n_features
                grad_b = 0.0

                for idx in batch_indices:
                    xi = scaled_X[idx]
                    yi = y[idx]

                    # Linear dot product
                    z = self.bias + sum(w * f for w, f in zip(self.weights, xi))
                    p = _stable_sigmoid(z)

                    # Binary cross-entropy loss contribution
                    p_clipped = max(1e-15, min(1.0 - 1e-15, p))
                    loss = -(yi * math.log(p_clipped) + (1.0 - yi) * math.log(1.0 - p_clipped))
                    epoch_loss += loss

                    # Gradient of log-loss w.r.t linear logit: (p - y)
                    error = p - yi
                    grad_b += error
                    for col in range(n_features):
                        grad_w[col] += error * xi[col]

                # Update parameters with L2 weight decay
                self.bias -= lr * (grad_b / bs)
                for col in range(n_features):
                    decay = self.l2_reg * self.weights[col]
                    self.weights[col] -= lr * ((grad_w[col] / bs) + decay)

            mean_loss = epoch_loss / n_samples
            loss_history.append(round(mean_loss, 5))

        self.is_fitted = True
        logger.info(
            f"Trained LogisticRegressionClassifier ({n_samples} samples, {n_features} features, final loss: {loss_history[-1]})",
            extra={"payload": {"samples": n_samples, "features": n_features, "final_loss": loss_history[-1]}},
        )

        return {
            "n_samples": n_samples,
            "n_features": n_features,
            "epochs": self.max_epochs,
            "final_loss": loss_history[-1],
            "loss_history": loss_history,
        }

    def predict_proba_single(self, x: List[float]) -> float:
        """Predict match probability for a single unscaled feature vector."""
        if not self.is_fitted:
            raise RuntimeError("Model is not fitted. Call fit() before predict_proba.")
        scaled_x = self._scale_vector(x)
        z = self.bias + sum(w * f for w, f in zip(self.weights, scaled_x))
        return round(_stable_sigmoid(z), 4)

    def predict_proba(self, X: List[List[float]]) -> List[float]:
        """Predict match probabilities for a batch of unscaled feature vectors."""
        return [self.predict_proba_single(x) for x in X]

    def to_dict(self) -> Dict[str, Any]:
        """Serialize model weights and scaling parameters to a dictionary."""
        return {
            "model_type": "LogisticRegressionClassifier",
            "is_fitted": self.is_fitted,
            "weights": self.weights,
            "bias": self.bias,
            "means": self.means,
            "stds": self.stds,
            "learning_rate": self.learning_rate,
            "l2_reg": self.l2_reg,
        }

    def save(self, filepath: Path) -> Path:
        """Persist model to JSON."""
        p = Path(filepath)
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2)
        return p

    @classmethod
    def load(cls, filepath: Path) -> LogisticRegressionClassifier:
        """Load model from JSON file."""
        p = Path(filepath)
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
        model = cls(
            learning_rate=data.get("learning_rate", 0.05),
            l2_reg=data.get("l2_reg", 0.001),
        )
        model.weights = data["weights"]
        model.bias = data["bias"]
        model.means = data["means"]
        model.stds = data["stds"]
        model.is_fitted = data["is_fitted"]
        return model
