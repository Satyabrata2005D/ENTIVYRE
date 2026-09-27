"""
Official Challenge Validator Integration Wrapper.
Phase 33: Bridges ENTIVYRE outputs directly to the official Amazon ML Challenge
submission validator (student_resource/utils/validate_submission.py).

Provides:
- Direct programmatic invocation of the official validation logic.
- Exit code, error list, and warning list extraction.
- Automatic verification of matching_results.tsv and candidate_pairs.tsv.
"""
from __future__ import annotations

import sys
import subprocess
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Any, Tuple

from entivyre.utils.logger import get_logger

logger = get_logger("ber.validation.official_validator", stage="33_official_validator")


@dataclass
class OfficialValidationResult:
    """Structured result from running the official submission validator."""
    success: bool
    returncode: int
    matching_path: str
    candidate_path: Optional[str]
    test_dir: str
    errors: List[str]
    warnings: List[str]
    stdout: str
    stderr: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class OfficialValidatorBridge:
    """
    Executes and reports on the official student_resource/utils/validate_submission.py tool.
    """

    def __init__(self, script_path: Optional[Path] = None):
        if script_path is None:
            # Default location in project root
            self.script_path = Path(__file__).resolve().parents[5] / "student_resource" / "utils" / "validate_submission.py"
        else:
            self.script_path = Path(script_path)

        if not self.script_path.is_file():
            # Fallback search
            cwd_script = Path.cwd() / "student_resource" / "utils" / "validate_submission.py"
            if cwd_script.is_file():
                self.script_path = cwd_script

    def run_validation(
        self,
        matching_path: Path,
        candidate_path: Optional[Path] = None,
        test_dir: Optional[Path] = None,
        check_ids: bool = False,
    ) -> OfficialValidationResult:
        """
        Execute the official submission validator via subprocess.
        """
        m_path = Path(matching_path).resolve()
        c_path = Path(candidate_path).resolve() if candidate_path else None
        t_dir = Path(test_dir).resolve() if test_dir else Path.cwd() / "student_resource" / "dataset" / "test"

        if not self.script_path.is_file():
            return OfficialValidationResult(
                success=False,
                returncode=-1,
                matching_path=str(m_path),
                candidate_path=str(c_path) if c_path else None,
                test_dir=str(t_dir),
                errors=[f"Official validation script not found at {self.script_path}"],
                warnings=[],
                stdout="",
                stderr="Script not found",
            )

        cmd = [
            sys.executable,
            str(self.script_path),
            "--matching",
            str(m_path),
            "--test-dir",
            str(t_dir),
        ]
        if c_path is not None and c_path.exists():
            cmd.extend(["--candidate", str(c_path)])
        if check_ids:
            cmd.append("--check-ids")

        logger.info(f"Running official submission validator: {' '.join(cmd)}")

        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
        )

        stdout = proc.stdout
        stderr = proc.stderr
        success = (proc.returncode == 0)

        # Parse errors and warnings from stdout
        errors: List[str] = []
        warnings: List[str] = []
        in_fail_section = False

        for line in stdout.splitlines():
            line_str = line.strip()
            if line_str.startswith("WARNING:"):
                warnings.append(line_str.replace("WARNING:", "").strip())
            elif line_str.startswith("FAIL —"):
                in_fail_section = True
            elif in_fail_section and line_str and line_str[0].isdigit() and "." in line_str:
                # e.g. "  1. Some error message"
                msg = line_str.split(".", 1)[1].strip()
                errors.append(msg)

        if not success and not errors:
            errors.append(f"Validator failed with exit code {proc.returncode}: {stderr.strip() or stdout.strip()}")

        result = OfficialValidationResult(
            success=success,
            returncode=proc.returncode,
            matching_path=str(m_path),
            candidate_path=str(c_path) if c_path else None,
            test_dir=str(t_dir),
            errors=errors,
            warnings=warnings,
            stdout=stdout,
            stderr=stderr,
        )

        logger.info(
            f"Official validation finished (success: {success}, returncode: {proc.returncode}, errors: {len(errors)}, warnings: {len(warnings)})",
            extra={"payload": result.to_dict()},
        )
        return result
