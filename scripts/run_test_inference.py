#!/usr/bin/env python3
"""
CLI runner for ENTIVYRE Full Test Inference Pipeline.
Executes high-throughput streaming candidate retrieval and matching over test dataset.
"""
import sys
import time
import argparse
from pathlib import Path

# Add project source to path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code" / "business_entity_resolution" / "src"))

from ber.inference.engine import InferenceEngine, InferenceConfig
from ber.validation.official_validator import OfficialValidatorBridge
from ber.outputs.serializer import OutputSerializer


def main():
    parser = argparse.ArgumentParser(description="Run ENTIVYRE Full Test Inference Pipeline.")
    parser.add_argument("--test-dir", default="student_resource/dataset/test", help="Test source directory")
    parser.add_argument("--output-dir", default="output", help="Directory where TSV outputs are written")
    parser.add_argument("--limit-s1", type=int, default=None, help="Optional limit on Source 1 records (for dry runs)")
    parser.add_argument("--limit-targets", type=int, default=None, help="Optional limit on target records indexed")
    parser.add_argument("--partitioned", action="store_true", default=True, help="Use partitioned streaming to minimize RAM (recommended for full dataset)")
    parser.add_argument("--no-partitioned", dest="partitioned", action="store_false", help="Disable partitioned streaming (load both S2 and S3 into RAM simultaneously)")
    parser.add_argument("--validate", action="store_true", default=True, help="Run official validator after inference")
    parser.add_argument("--no-validate", dest="validate", action="store_false", help="Skip official validator after inference")

    args = parser.parse_args()

    test_dir = Path(args.test_dir)
    s1_path = test_dir / "test_source1.tsv"
    s2_path = test_dir / "test_source2.tsv"
    s3_path = test_dir / "test_source3.tsv"

    out_dir = Path(args.output_dir)
    matching_path = out_dir / "matching_results.tsv"
    candidate_path = out_dir / "candidate_pairs.tsv"

    print("==================================================")
    print("ENTIVYRE — FULL TEST INFERENCE PIPELINE")
    print("==================================================")
    print(f"Test Directory: {test_dir}")
    print(f"Output Directory: {out_dir}")
    print(f"Limit S1: {args.limit_s1 or 'FULL DATASET'}")
    print(f"Limit Targets: {args.limit_targets or 'FULL TARGET SOURCES'}")
    print(f"Execution Mode: {'PARTITIONED STREAMING (bounded RAM)' if args.partitioned else 'JOINT IN-MEMORY'}")
    print("--------------------------------------------------")

    if args.partitioned:
        import gc
        temp_dir = Path("artifacts/temp_inference")
        temp_dir.mkdir(parents=True, exist_ok=True)
        t_s2 = temp_dir / "intermed_s2.tsv"
        t_s3 = temp_dir / "intermed_s3.tsv"

        start_all = time.time()
        print("[1/3] Indexing Source 2 targets and streaming Source 1...")
        engine_s2 = InferenceEngine(InferenceConfig())
        engine_s2.index_target_file(s2_path, limit=args.limit_targets)
        engine_s2.run_single_source_inference(s1_path, t_s2, limit=args.limit_s1)
        del engine_s2
        gc.collect()

        print("[2/3] Indexing Source 3 targets and streaming Source 1...")
        engine_s3 = InferenceEngine(InferenceConfig())
        engine_s3.index_target_file(s3_path, limit=args.limit_targets)
        engine_s3.run_single_source_inference(s1_path, t_s3, limit=args.limit_s1)
        del engine_s3
        gc.collect()

        print("[3/3] Merging multi-source candidates and matches...")
        cfg = InferenceConfig()
        stats = InferenceEngine.merge_partitioned_outputs(
            intermed_paths=[t_s2, t_s3],
            matching_output_path=matching_path,
            candidate_output_path=candidate_path,
            max_matches_per_anchor=cfg.max_matches_per_anchor,
            start_time=start_all,
        )

        if t_s2.is_file():
            t_s2.unlink()
        if t_s3.is_file():
            t_s3.unlink()
    else:
        engine = InferenceEngine(InferenceConfig())

        print("[1/3] Indexing Source 2 targets...")
        engine.index_target_file(s2_path, limit=args.limit_targets)

        print("[2/3] Indexing Source 3 targets...")
        engine.index_target_file(s3_path, limit=args.limit_targets)

        print("[3/3] Running streaming inference over Source 1...")
        stats = engine.run_streaming_inference(
            source1_tsv_path=s1_path,
            matching_output_path=matching_path,
            candidate_output_path=candidate_path,
            limit=args.limit_s1,
        )


    print("\n--------------------------------------------------")
    print("INFERENCE SUMMARY:")
    print(f"  Total S1 Processed:       {stats.total_anchors:,}")
    print(f"  Singletons (Empty list):  {stats.singleton_count:,} ({stats.singleton_ratio:.1%})")
    print(f"  Matched S1 Entities:      {stats.matched_count:,}")
    print(f"  Total Candidates:         {stats.total_candidate_pairs:,} (avg {stats.mean_candidates_per_anchor:.2f}/anchor)")
    print(f"  Total Match Links:        {stats.total_matches:,} (avg {stats.mean_matches_per_anchor:.2f}/anchor)")
    print(f"  Elapsed Time:             {stats.elapsed_seconds:.2f}s")
    print(f"  Throughput:               {stats.throughput_anchors_per_sec:.1f} anchors/sec")
    print(f"  Peak Memory (RSS):        {stats.peak_memory_mb:.1f} MB")
    print("--------------------------------------------------")

    if args.validate:
        print("\nValidating generated submission files...")
        bridge = OfficialValidatorBridge()
        res = bridge.run_validation(
            matching_path=matching_path,
            candidate_path=candidate_path,
            test_dir=test_dir,
            check_ids=False,
        )
        print(res.stdout)
        if not res.success:
            print("Validation FAILED!", file=sys.stderr)
            sys.exit(res.returncode)

    print("\nDone. Submission files ready at:")
    print(f"  - {matching_path}")
    print(f"  - {candidate_path}")


if __name__ == "__main__":
    main()
