"""
Unit and Integration Tests for Phase 31: Security & Fair-Play Hardening.
"""
import unittest
import socket
import tempfile
from pathlib import Path

from ber.security.fair_play import (
    NetworkIsolationGuard,
    NetworkBlockedException,
    FairPlayAuditor,
)


class TestFairPlay(unittest.TestCase):
    def test_network_isolation_guard(self):
        # 1. Under guard, socket connection must raise NetworkBlockedException
        with NetworkIsolationGuard(active=True):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            with self.assertRaises(NetworkBlockedException):
                sock.connect(("8.8.8.8", 53))

        # 2. Outside guard, socket connect is restored to original method
        sock_outside = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Should not raise NetworkBlockedException
        try:
            sock_outside.connect(("127.0.0.1", 65534))
        except NetworkBlockedException:
            self.fail("NetworkBlockedException raised outside of NetworkIsolationGuard!")
        except Exception:
            pass  # Normal OS connection refused is expected, but not NetworkBlockedException

    def test_codebase_fair_play_audit(self):
        # Audit real source code directory
        ber_src = Path(__file__).resolve().parent.parent / "code" / "business_entity_resolution" / "src" / "ber"
        report = FairPlayAuditor.audit_source_directory(ber_src)

        self.assertTrue(report.is_compliant)
        self.assertEqual(len(report.banned_imports_found), 0)
        self.assertEqual(len(report.banned_urls_found), 0)
        self.assertGreater(report.audited_files_count, 10)

    def test_adversarial_detection_of_banned_imports(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            bad_file = Path(tmpdir) / "illegal_crawler.py"
            bad_file.write_text(
                "import requests\nfrom geopy import Nominatim\nprint('illegal')",
                encoding="utf-8",
            )
            report = FairPlayAuditor.audit_source_directory(Path(tmpdir))
            self.assertFalse(report.is_compliant)
            self.assertGreaterEqual(len(report.banned_imports_found), 2)


if __name__ == "__main__":
    unittest.main()
