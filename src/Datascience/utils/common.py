import os
import yaml
from src.Datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    read the yaml file and returns
    args:
    path_to_yaml(str) : path like input
    
    Raises:
    ValueError : if yaml file is empty
    e : empty yaml file

    return : 
    configbox : configBox type

    Read YAML file and return it as a ConfigBox.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise BoxValueError(f"yaml file is empty: {path_to_yaml}")


    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    """
    create the directories
    args:
    path_to_directories(list) : list of paths to be created
    verbose(bool) : if True, log the creation of directories

    Raises:
    ValueError : if path_to_directories is not a list

    return :
    None

    Create directories.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    """
    Save the json data
    Args:
    path(Path): path like input
    data(dict): data to be saved

    Returns:
    None
    """
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"Json file: {path} saved successfully")

@ensure_annotations
def load_json(path:Path)->ConfigBox:
    """
    read the json file and returns
    args:
    path(Path) : path like input

    Raises:
    ValueError : if json file is empty
    e : empty json file

    Returns:
    ConfigBox : ConfigBox type
    """
    try:
        with open(path,"r") as f:
            data = json.load(f)
            logger.info(f"Json file: {path} loaded successfully")
            return data
    except BoxValueError as e:
        raise BoxValueError(f"Json file is empty: {path}")
    except Exception as e:
        raise e
        
@ensure_annotations
def save_bin(data:Any,path:Path):
    """
    Save the bin data
    Args:
    data(Any): data to be saved
    path(Path): path like input

    Returns:
    None
    """
    joblib.dump(value =data,filename=path)
    logger.info(f"Bin file: {path} saved successfully")

@ensure_annotations    
def load_bin(path:Path)->ConfigBox:
    """
    read the bin file and returns
    args:
    path(Path) : path like input

    Raises:
    ValueError : if bin file is empty
    e : empty bin file

    Returns:
    ConfigBox : ConfigBox type
    """
    try:
            data = joblib.load(path)
            logger.info(f"Bin file: {path} loaded successfully")
            return data
    except BoxValueError as e:
        raise BoxValueError(f"Bin file is empty: {path}")
    except Exception as e:
        raise e
        
    