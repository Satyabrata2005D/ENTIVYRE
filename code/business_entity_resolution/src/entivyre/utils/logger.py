"""Structured logging utilities for ENTIVYRE.

Produces JSON-lines structured log records suitable for automated parsing,
traceability, and reproducible auditing across all pipeline phases.
"""

from __future__ import annotations

import json
import logging
import os
import sys
import time
from typing import Any, Dict, Optional


class StructuredFormatter(logging.Formatter):
    """Custom logging formatter outputting JSON objects with consistent schema."""

    def __init__(self, run_id: Optional[str] = None, stage: Optional[str] = None):
        super().__init__()
        self.run_id = run_id or os.environ.get("ENTIVYRE_RUN_ID", "default_run")
        self.stage = stage or os.environ.get("ENTIVYRE_STAGE", "01_contracts")

    def format(self, record: logging.LogRecord) -> str:
        log_entry: Dict[str, Any] = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(record.created)),
            "time_epoch_ms": int(record.created * 1000),
            "level": record.levelname,
            "logger": record.name,
            "stage": getattr(record, "stage", self.stage),
            "run_id": getattr(record, "run_id", self.run_id),
            "event": getattr(record, "event", record.funcName or "log_event"),
            "message": record.getMessage(),
        }

        # Include structured payload if attached
        if hasattr(record, "payload") and isinstance(record.payload, dict):
            log_entry["data"] = record.payload

        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_entry, default=str)


def get_logger(name: str, stage: str = "01_contracts", run_id: Optional[str] = None) -> logging.Logger:
    """Obtain or configure a structured JSON logger for an ENTIVYRE module."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid adding duplicate handlers if logger already initialized
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(StructuredFormatter(run_id=run_id, stage=stage))
        logger.addHandler(handler)

    logger.propagate = False
    return logger


def configure_logging(level: int = logging.INFO, log_file: Optional[str] = None) -> None:
    """Configure global logging level and optional file output."""
    root = logging.getLogger("entivyre")
    root.setLevel(level)
    if log_file:
        os.makedirs(os.path.dirname(os.path.abspath(log_file)), exist_ok=True)
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(StructuredFormatter())
        root.addHandler(file_handler)

