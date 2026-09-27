#!/usr/bin/env python3
"""
CLI script to generate the official Dataset Manifest.
Executes Phase 03: file checksums, sizes, row counts, and schema verification.
Outputs machine-readable artifacts/dataset_manifest.json.
"""
import sys
import json
import time
from pathlib import Path

# Add ber to path
_root = Path(__file__).resolve().parent.parent
_ber_src = _root / "code" / "business_entity_resolution" / "src"
if str(_ber_src) not in sys.path:
    sys.path.insert(0, str(_ber_src))

from ber.io.manifest import generate_dataset_manifest, verify_dataset_integrity
from entivyre.config import load_config

def main():
    cfg = load_config()
    dataset_root = _root / cfg.paths.dataset_root
    out_dir = _root / cfg.paths.artifacts_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = out_dir / "dataset_manifest.json"

    print(f"=== ENTIVYRE: Phase 03 Dataset Manifest Generator ===")
    print(f"Dataset root: {dataset_root}")
    t0 = time.perf_counter()

    manifest = generate_dataset_manifest(dataset_root)
    manifest_dict = manifest.to_dict()

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_dict, f, indent=2)

    elapsed = time.perf_counter() - t0
    print(f"\nManifest successfully created in {elapsed:.2f}s:")
    print(f"Total Files: {manifest.total_files}")
    print(f"Total Size: {manifest.total_bytes / (1024**3):.2f} GB ({manifest.total_bytes:,} bytes)")
    print(f"Total Records: {manifest.total_records:,}")
    print(f"All Files Present: {manifest.all_files_present}")
    print(f"All Schemas Valid: {manifest.all_schemas_valid}")
    print(f"All Prefixes Valid: {manifest.all_prefixes_valid}")
    print(f"Saved to: {manifest_path}")

    # Verify integrity immediately
    is_valid, errors = verify_dataset_integrity(manifest_path, dataset_root, verify_hashes=False)
    if not is_valid:
        print(f"ERROR: Integrity verification failed: {errors}")
        sys.exit(1)

    print("Integrity verification: PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
