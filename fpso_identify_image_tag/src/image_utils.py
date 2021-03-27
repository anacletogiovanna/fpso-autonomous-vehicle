#!/usr/bin/env python3
import yaml
import pathlib
from datetime import datetime

def get_dir_by_yaml(yaml_file):
    """
    Captures the directory path from the .yaml file 
    yaml_file: File with the directory 
    """    
    # Read information in yaml file 
    yaml_dir = get_dir_yaml_file(yaml_file)
    with open(yaml_dir, 'r') as stream:
        yaml_image_dir = yaml.safe_load(stream)[0]
        return yaml_image_dir['dir']


def file_name_with_timestamp(name, file_extension):
    """
    Create an file with timestamp 
    name: first name of file
    file_extension: extension of file name
    """    
    date_time = datetime.now() # Capturing datetime 
    timestamp = date_time.strftime("%Y%m%d%H%M%S") # formating datetime 
    file_name = name + "_" + timestamp + file_extension # mounting file name 
    return file_name

def get_dir_yaml_file(yaml_file):
    path = abs_path = str(pathlib.Path(__file__).parent.absolute())
    return path + "/" + yaml_file