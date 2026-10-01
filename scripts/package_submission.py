#!/usr/bin/env python3
"""
Official Submission Packaging Script for ENTIVYRE.
Phase 38: Assembles and validates the competition submission ZIP archive.

Conforms strictly to the official challenge structure:
<team_name>_submission.zip
├── output/
│   ├── matching_results.tsv
│   └── candidate_pairs.tsv
├── code/
│   └── business_entity_resolution/
│       ├── src/
│       ├── README.md
│       └── requirements.txt
└── Documentation_template.md
"""
import os
import sys
import zipfile
import argparse
from pathlib import Path

# Add project source to path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code" / "business_entity_resolution" / "src"))

from ber.outputs.serializer import OutputSerializer
from ber.validation.official_validator import OfficialValidatorBridge


def package_submission(
    team_name: str = "UNPAID_ENGINEERS",
    output_dir: Path = Path("output"),
    code_dir: Path = Path("code/business_entity_resolution"),
    doc_path: Path = Path("Documentation_template.md"),
    target_zip_dir: Path = Path("submission"),
) -> Path:
    target_zip_dir.mkdir(parents=True, exist_ok=True)
    zip_filename = f"{team_name}_submission.zip"
    zip_path = target_zip_dir / zip_filename

    print(f"Creating submission package: {zip_path}")

    # Validate output files exist
    m_tsv = output_dir / "matching_results.tsv"
    c_tsv = output_dir / "candidate_pairs.tsv"

    if not m_tsv.is_file():
        raise FileNotFoundError(f"Missing {m_tsv}! Run test inference first.")
    if not c_tsv.is_file():
        raise FileNotFoundError(f"Missing {c_tsv}! Run test inference first.")
    if not doc_path.is_file():
        raise FileNotFoundError(f"Missing {doc_path}!")

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        # 1. output/
        zf.write(m_tsv, arcname="output/matching_results.tsv")
        zf.write(c_tsv, arcname="output/candidate_pairs.tsv")

        # 2. code/business_entity_resolution/
        for root, dirs, files in os.walk(code_dir):
            # Exclude pycache, git, bytecodes
            dirs[:] = [d for d in dirs if d not in {"__pycache__", ".git", ".pytest_cache"}]
            for f in files:
                if f.endswith((".pyc", ".pyo", ".DS_Store")):
                    continue
                file_path = Path(root) / f
                rel_path = file_path.relative_to(code_dir.parent)
                arc_name = Path("code") / rel_path
                zf.write(file_path, arcname=str(arc_name))

        # 3. requirements.txt at root (matches official screenshot specification)
        req_path = Path("requirements.txt")
        if req_path.is_file():
            zf.write(req_path, arcname="requirements.txt")

        # 4. Documentation_template.md
        zf.write(doc_path, arcname="Documentation_template.md")

    print(f"Package created successfully: {zip_path} ({zip_path.stat().st_size / (1024 * 1024):.2f} MB)")
    return zip_path


def main():
    parser = argparse.ArgumentParser(description="Package ENTIVYRE official challenge submission ZIP.")
    parser.add_argument("--team-name", default="UNPAID_ENGINEERS", help="Team name prefix for ZIP file")
    parser.add_argument("--output-dir", default="output", help="Directory containing TSV files")
    parser.add_argument("--dest", default="submission", help="Target destination directory for ZIP")

    args = parser.parse_args()

    zip_path = package_submission(
        team_name=args.team_name,
        output_dir=Path(args.output_dir),
        target_zip_dir=Path(args.dest),
    )
    print(f"\nReady for submission: {zip_path}")


if __name__ == "__main__":
    main()
