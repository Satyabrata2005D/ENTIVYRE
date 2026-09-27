"""
Typed, immutable configuration manager for ENTIVYRE.
Supports hierarchical YAML loading with pure-Python fallback.
"""
from __future__ import annotations
import os
import json
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


@dataclass(frozen=True)
class ProjectConfig:
    name: str = "ENTIVYRE"
    version: str = "1.0.0"
    random_seed: int = 42
    airgap_mode: bool = True


@dataclass(frozen=True)
class PathsConfig:
    dataset_root: str = "student_resource/dataset"
    train_dir: str = "student_resource/dataset/train"
    test_dir: str = "student_resource/dataset/test"
    artifacts_dir: str = "artifacts"
    output_dir: str = "output"
    logs_dir: str = "logs"


@dataclass(frozen=True)
class RuntimeConfig:
    chunk_size: int = 50000
    max_memory_mb: int = 8192
    max_workers: int = 4
    stream_buffers: bool = True
    log_level: str = "INFO"


@dataclass(frozen=True)
class ContractsConfig:
    source1_prefix: str = "S1-"
    source2_prefix: str = "S2-"
    source3_prefix: str = "S3-"
    expected_source_cols: List[str] = field(default_factory=lambda: [
        "entity_id", "business_name", "business_address", "country"
    ])
    expected_ground_truth_cols: List[str] = field(default_factory=lambda: [
        "source1_entity_id", "matched_entity_ids"
    ])
    expected_matching_cols: List[str] = field(default_factory=lambda: [
        "source1_entity_id", "matched_entity_ids"
    ])
    expected_candidate_cols: List[str] = field(default_factory=lambda: [
        "source1_entity_id", "candidate_entity_ids"
    ])


@dataclass(frozen=True)
class NormalizationConfig:
    unicode_form: str = "NFKD"
    lowercase: bool = True
    strip_accents: bool = True
    strip_punctuation: bool = True
    standardize_legal_suffixes: bool = True
    standardize_address_keywords: bool = True
    transliterate_devanagari: bool = True


@dataclass(frozen=True)
class BlockingConfig:
    max_candidates_per_anchor: int = 50
    retrieval_strategies: List[str] = field(default_factory=lambda: [
        "exact_name", "token_jaccard", "address_postal", "char_ngram_tfidf"
    ])
    min_ngram: int = 3
    max_ngram: int = 5
    tfidf_max_features: int = 100000


@dataclass(frozen=True)
class FeaturesConfig:
    enabled_groups: List[str] = field(default_factory=lambda: [
        "name_exact", "name_normalized", "name_token_jaccard", "name_levenshtein",
        "name_tfidf_cosine", "address_token_jaccard", "address_numeric_match",
        "country_exact", "country_compatibility", "cross_field_joint"
    ])


@dataclass(frozen=True)
class ModelingConfig:
    f_beta: float = 0.5
    initial_model: str = "deterministic_baseline"
    candidate_model: str = "logistic_regression"
    tree_model: str = "gradient_boosting"
    default_threshold: float = 0.55
    min_confidence_floor: float = 0.35


@dataclass(frozen=True)
class EvaluationConfig:
    metric: str = "macro_f0.5"
    singleton_handling: str = "official_zero_credit"
    validation_split_ratio: float = 0.20


@dataclass(frozen=True)
class AppConfig:
    project: ProjectConfig = field(default_factory=ProjectConfig)
    paths: PathsConfig = field(default_factory=PathsConfig)
    runtime: RuntimeConfig = field(default_factory=RuntimeConfig)
    contracts: ContractsConfig = field(default_factory=ContractsConfig)
    normalization: NormalizationConfig = field(default_factory=NormalizationConfig)
    blocking: BlockingConfig = field(default_factory=BlockingConfig)
    features: FeaturesConfig = field(default_factory=FeaturesConfig)
    modeling: ModelingConfig = field(default_factory=ModelingConfig)
    evaluation: EvaluationConfig = field(default_factory=EvaluationConfig)

    def to_dict(self) -> Dict[str, Any]:
        """Convert immutable config to dictionary."""
        import dataclasses
        return dataclasses.asdict(self)


def _simple_yaml_parser(text: str) -> Dict[str, Any]:
    """
    Fallback parser for basic YAML dictionaries and key-value pairs
    when PyYAML is not installed.
    """
    result: Dict[str, Any] = {}
    current_section = None
    section_dict: Dict[str, Any] = {}
    
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            parts = line.split(":", 1)
            key = parts[0].strip()
            val = parts[1].strip()
            if not val:
                # New section
                if current_section:
                    result[current_section] = section_dict
                current_section = key
                section_dict = {}
            else:
                # Handle basic primitive types
                parsed_val: Any = val
                if val.lower() == "true":
                    parsed_val = True
                elif val.lower() == "false":
                    parsed_val = False
                elif val.isdigit():
                    parsed_val = int(val)
                elif val.replace(".", "", 1).isdigit() and val.count(".") == 1:
                    parsed_val = float(val)
                elif val.startswith('"') and val.endswith('"'):
                    parsed_val = val[1:-1]
                elif val.startswith("'") and val.endswith("'"):
                    parsed_val = val[1:-1]
                elif val.startswith("[") and val.endswith("]"):
                    items = [x.strip().strip("'\"") for x in val[1:-1].split(",") if x.strip()]
                    parsed_val = items
                
                if current_section is not None:
                    section_dict[key] = parsed_val
                else:
                    result[key] = parsed_val
    if current_section:
        result[current_section] = section_dict
    return result


def load_config(config_path: Optional[str | Path] = None, overrides: Optional[Dict[str, Any]] = None) -> AppConfig:
    """
    Loads AppConfig from YAML file, merges with overrides, and enforces schema.
    """
    data: Dict[str, Any] = {}
    
    if config_path is not None:
        p = Path(config_path)
        if p.exists():
            content = p.read_text(encoding="utf-8")
            if HAS_YAML:
                data = yaml.safe_load(content) or {}
            else:
                data = _simple_yaml_parser(content)
                
    if overrides:
        # Deep merge
        for k, v in overrides.items():
            if isinstance(v, dict) and k in data and isinstance(data[k], dict):
                data[k].update(v)
            else:
                data[k] = v

    # Build sub-dataclasses with mapped values
    proj_args = data.get("project", {})
    paths_args = data.get("paths", {})
    run_args = data.get("runtime", {})
    contract_args = data.get("contracts", {})
    norm_args = data.get("normalization", {})
    block_args = data.get("blocking", {})
    feat_args = data.get("features", {})
    model_args = data.get("modeling", {})
    eval_args = data.get("evaluation", {})

    return AppConfig(
        project=ProjectConfig(**{k: v for k, v in proj_args.items() if hasattr(ProjectConfig, k)}),
        paths=PathsConfig(**{k: v for k, v in paths_args.items() if hasattr(PathsConfig, k)}),
        runtime=RuntimeConfig(**{k: v for k, v in run_args.items() if hasattr(RuntimeConfig, k)}),
        contracts=ContractsConfig(**{k: v for k, v in contract_args.items() if hasattr(ContractsConfig, k)}),
        normalization=NormalizationConfig(**{k: v for k, v in norm_args.items() if hasattr(NormalizationConfig, k)}),
        blocking=BlockingConfig(**{k: v for k, v in block_args.items() if hasattr(BlockingConfig, k)}),
        features=FeaturesConfig(**{k: v for k, v in feat_args.items() if hasattr(FeaturesConfig, k)}),
        modeling=ModelingConfig(**{k: v for k, v in model_args.items() if hasattr(ModelingConfig, k)}),
        evaluation=EvaluationConfig(**{k: v for k, v in eval_args.items() if hasattr(EvaluationConfig, k)}),
    )
