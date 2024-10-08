import os
from box.exceptions import BoxValueError
import yaml
from TextSummarizerLLM.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations   #return u an error insted of execution when you place mismatch data type value in the arguments when calling the function
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml filr and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {path_to_yaml} loaded successfully')
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError('yaml is empty')
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """ Create list of directories

    Args:
        path_to_directories (list): list of path of directories to create
        ignore_log (bool, optional): ignore if multiple directories is to be created. Default to false
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'Creating directory: {path}')


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): Path of file

    Returns:
        str: size in KB
    """     
    size_in_KB = round(os.path.getsize(path)/1024)
    return f'~ {size_in_KB} KB'

