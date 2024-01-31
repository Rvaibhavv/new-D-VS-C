from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_destination: Path
    local_data_file: Path
    unzip_dir: Path

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    batch_size: int
    image_width: int
    image_height: int
    inner_activation: str
    epoch_val: int
    loss_func: str
    optimizer: str
    neurons_no: list

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    batch_size: int
    model_path: Path
    mlflow_uri: str
    all_params: dict
    image_width: int
    image_height: int
    metric_file_name: Path
    model_path: Path
    