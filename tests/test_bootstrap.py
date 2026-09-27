"""
Unit and integration tests for Phase 02: Repository Bootstrap and Configuration.
"""
import os
import unittest
import tempfile
from pathlib import Path

import sys
_project_root = Path(__file__).resolve().parent.parent
_ber_src = _project_root / "code" / "business_entity_resolution" / "src"
if str(_ber_src) not in sys.path:
    sys.path.insert(0, str(_ber_src))

from entivyre.config import (
    AppConfig,
    load_config,
    ProjectConfig,
    PathsConfig,
    RuntimeConfig,
    NormalizationConfig,
    BlockingConfig
)
import ber


class TestRepositoryBootstrap(unittest.TestCase):
    def setUp(self):
        self.root_dir = Path(__file__).resolve().parent.parent

    def test_directory_structure_exists(self):
        """Verify that all core project directories exist."""
        required_dirs = [
            self.root_dir / "configs",
            self.root_dir / "code" / "business_entity_resolution" / "src" / "ber",
            self.root_dir / "code" / "business_entity_resolution" / "tests",
            self.root_dir / "artifacts",
            self.root_dir / "output",
            self.root_dir / "docs",
            self.root_dir / "scripts",
        ]
        for d in required_dirs:
            self.assertTrue(d.exists(), f"Required directory missing: {d}")
            self.assertTrue(d.is_dir(), f"Path is not a directory: {d}")

    def test_default_config_loading(self):
        """Verify loading default AppConfig without file."""
        cfg = load_config()
        self.assertIsInstance(cfg, AppConfig)
        self.assertEqual(cfg.project.name, "ENTIVYRE")
        self.assertTrue(cfg.project.airgap_mode)
        self.assertEqual(cfg.blocking.max_candidates_per_anchor, 50)
        self.assertEqual(cfg.modeling.f_beta, 0.5)

    def test_yaml_config_loading(self):
        """Verify loading configs/base.yaml."""
        base_yaml = self.root_dir / "configs" / "base.yaml"
        self.assertTrue(base_yaml.exists(), "configs/base.yaml must exist")
        cfg = load_config(base_yaml)
        self.assertEqual(cfg.project.name, "ENTIVYRE")
        self.assertEqual(cfg.runtime.chunk_size, 50000)
        self.assertTrue(cfg.normalization.lowercase)
        self.assertIn("S1-", cfg.contracts.source1_prefix)

    def test_config_overrides(self):
        """Verify overriding configuration values."""
        base_yaml = self.root_dir / "configs" / "base.yaml"
        overrides = {
            "runtime": {"chunk_size": 25000},
            "project": {"random_seed": 999}
        }
        cfg = load_config(base_yaml, overrides=overrides)
        self.assertEqual(cfg.runtime.chunk_size, 25000)
        self.assertEqual(cfg.project.random_seed, 999)

    def test_ber_package_exports(self):
        """Verify official submission subpackage exports core contracts and loader."""
        self.assertTrue(hasattr(ber, "load_config"))
        self.assertTrue(hasattr(ber, "Source1Record"))
        self.assertTrue(hasattr(ber, "MacroF05Evaluator"))
        self.assertTrue(hasattr(ber, "validate_submission_files"))

    def test_immutability_of_config(self):
        """Verify that configuration dataclasses are frozen/immutable."""
        cfg = load_config()
        with self.assertRaises((AttributeError, TypeError, Exception)):
            cfg.project.name = "MutatedName"

    def test_adversarial_malformed_config(self):
        """Verify handling of empty or non-existent configuration paths."""
        cfg = load_config("/non/existent/path/config.yaml")
        # Should cleanly return defaults
        self.assertEqual(cfg.project.name, "ENTIVYRE")


if __name__ == "__main__":
    unittest.main()
