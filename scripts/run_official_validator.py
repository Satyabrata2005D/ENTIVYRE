#!/usr/bin/env python3
"""
CLI runner for validating ENTIVYRE output submissions against the official Amazon ML Challenge validator.
"""
import sys
import argparse
from pathlib import Path

# Add project source to path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code" / "business_entity_resolution" / "src"))

from ber.validation.official_validator import OfficialValidatorBridge


def main():
    parser = argparse.ArgumentParser(description="Run official Amazon ML Challenge submission validator.")
    parser.add_argument("--matching", "-m", default="output/matching_results.tsv", help="Path to matching_results.tsv")
    parser.add_argument("--candidate", "-c", default="output/candidate_pairs.tsv", help="Path to candidate_pairs.tsv")
    parser.add_argument("--test-dir", "-t", default="student_resource/dataset/test", help="Test source directory")
    parser.add_argument("--check-ids", action="store_true", help="Perform full ID existence check against test sources")

    args = parser.parse_args()

    bridge = OfficialValidatorBridge()
    result = bridge.run_validation(
        matching_path=Path(args.matching),
        candidate_path=Path(args.candidate) if args.candidate else None,
        test_dir=Path(args.test_dir),
        check_ids=args.check_ids,
    )

    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
