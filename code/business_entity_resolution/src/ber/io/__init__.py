"""
BER I/O subpackage: Manifest generation, discovery, streaming ingestion.
"""
from ber.io.manifest import (
    FileManifest,
    DatasetManifest,
    profile_single_file,
    generate_dataset_manifest,
    verify_dataset_integrity,
)
from ber.io.ingestion import (
    stream_source_chunks,
    stream_ground_truth_chunks,
    load_ground_truth_map,
    clean_field_text,
    QuarantineManager,
    IngestionStats,
    MalformedRowRecord,
)

__all__ = [
    "FileManifest",
    "DatasetManifest",
    "profile_single_file",
    "generate_dataset_manifest",
    "verify_dataset_integrity",
    "stream_source_chunks",
    "stream_ground_truth_chunks",
    "load_ground_truth_map",
    "clean_field_text",
    "QuarantineManager",
    "IngestionStats",
    "MalformedRowRecord",
]
