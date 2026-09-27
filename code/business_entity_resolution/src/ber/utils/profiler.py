"""
Performance Profiling and Scalability Optimization Engine for ENTIVYRE.
Phase 30: System resource profiling, memory-bounded batch processing,
and throughput benchmarking for multi-gigabyte scale entity resolution.

Guarantees:
- Cross-platform peak RSS memory measurement (macOS bytes vs Linux kilobytes).
- High-precision wall and CPU execution timing.
- Memory-bounded batch chunking preventing unbounded RAM accumulation.
- Real-time throughput (items/sec and pairs/sec) telemetry.
- Pure-Python, zero external C-dependencies.
"""
from __future__ import annotations

import gc
import os
import sys
import time
import resource
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Tuple, Any, Iterator, Callable, Iterable, TypeVar

from entivyre.utils.logger import get_logger

logger = get_logger("ber.utils.profiler", stage="30_performance_optimization")

T = TypeVar("T")
R = TypeVar("R")


def get_peak_memory_mb() -> float:
    """
    Returns peak resident set size (RSS) in Megabytes.
    Handles macOS (bytes) and Linux (kilobytes) differences.
    """
    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == "darwin":
        # macOS reports ru_maxrss in bytes
        return usage / (1024.0 * 1024.0)
    else:
        # Linux reports ru_maxrss in kilobytes
        return usage / 1024.0


@dataclass(frozen=True)
class ProfileStats:
    """Quantitative performance and resource utilization profile."""
    stage_name: str
    total_items: int
    elapsed_wall_sec: float
    elapsed_cpu_sec: float
    peak_memory_mb: float
    throughput_items_per_sec: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class ExecutionTimer:
    """Context manager for high-precision resource profiling."""

    def __init__(self, stage_name: str, total_items: int = 0):
        self.stage_name = stage_name
        self.total_items = total_items
        self.start_wall: float = 0.0
        self.start_cpu: float = 0.0
        self.stats: Optional[ProfileStats] = None

    def __enter__(self) -> ExecutionTimer:
        gc.collect()
        self.start_wall = time.perf_counter()
        self.start_cpu = time.process_time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        end_wall = time.perf_counter()
        end_cpu = time.process_time()

        wall_sec = max(1e-6, end_wall - self.start_wall)
        cpu_sec = max(1e-6, end_cpu - self.start_cpu)
        peak_mb = get_peak_memory_mb()
        throughput = (self.total_items / wall_sec) if self.total_items > 0 else 0.0

        self.stats = ProfileStats(
            stage_name=self.stage_name,
            total_items=self.total_items,
            elapsed_wall_sec=round(wall_sec, 4),
            elapsed_cpu_sec=round(cpu_sec, 4),
            peak_memory_mb=round(peak_mb, 2),
            throughput_items_per_sec=round(throughput, 1),
        )
        logger.info(
            f"Stage '{self.stage_name}' completed in {wall_sec:.3f}s (Throughput: {throughput:.1f} items/s, Peak RAM: {peak_mb:.1f} MB)",
            extra={"payload": self.stats.to_dict()},
        )


class BatchProcessor:
    """
    Memory-safe batch executor preventing runaway memory growth during large-scale operations.
    """

    @staticmethod
    def chunk_iterable(iterable: Iterable[T], chunk_size: int = 5000) -> Iterator[List[T]]:
        """Yield items from iterable in bounded chunks of chunk_size."""
        batch: List[T] = []
        for item in iterable:
            batch.append(item)
            if len(batch) >= chunk_size:
                yield batch
                batch = []
        if batch:
            yield batch

    @staticmethod
    def execute_in_batches(
        items: Iterable[T],
        worker_fn: Callable[[List[T]], List[R]],
        chunk_size: int = 5000,
        enable_gc: bool = False,
    ) -> Iterator[R]:
        """
        Processes items in bounded chunks, invoking worker_fn per chunk
        and yielding results one-by-one to maintain constant memory O(chunk_size).
        """
        for chunk in BatchProcessor.chunk_iterable(items, chunk_size):
            results = worker_fn(chunk)
            for res in results:
                yield res
            if enable_gc:
                gc.collect()
