from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig: # the name is same as the config yaml file
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class dataValidationConfig:
    root_dir: Path
    STATUS_FILE: Path
    unzip_data_dir:Path
    all_schema:dict