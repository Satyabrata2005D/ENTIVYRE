"""
Unit and Integration Tests for Phase 30: Performance & Scalability Profiler.
"""
import unittest
import time

from ber.utils.profiler import (
    get_peak_memory_mb,
    ExecutionTimer,
    ProfileStats,
    BatchProcessor,
)


class TestProfiler(unittest.TestCase):
    def test_peak_memory_mb(self):
        mem = get_peak_memory_mb()
        self.assertIsInstance(mem, float)
        self.assertGreater(mem, 0.0)

    def test_execution_timer(self):
        with ExecutionTimer("test_stage", total_items=100) as timer:
            time.sleep(0.01)

        stats = timer.stats
        self.assertIsNotNone(stats)
        self.assertEqual(stats.stage_name, "test_stage")
        self.assertEqual(stats.total_items, 100)
        self.assertGreater(stats.elapsed_wall_sec, 0.005)
        self.assertGreater(stats.throughput_items_per_sec, 0.0)
        self.assertGreater(stats.peak_memory_mb, 0.0)

    def test_batch_processor_chunking(self):
        items = list(range(25))
        chunks = list(BatchProcessor.chunk_iterable(items, chunk_size=10))

        self.assertEqual(len(chunks), 3)
        self.assertEqual(chunks[0], list(range(0, 10)))
        self.assertEqual(chunks[1], list(range(10, 20)))
        self.assertEqual(chunks[2], list(range(20, 25)))

    def test_batch_processor_execution(self):
        items = list(range(20))
        # Worker doubles each item
        def worker(chunk):
            return [x * 2 for x in chunk]

        results = list(BatchProcessor.execute_in_batches(items, worker, chunk_size=5))
        expected = [x * 2 for x in range(20)]
        self.assertEqual(results, expected)


if __name__ == "__main__":
    unittest.main()
