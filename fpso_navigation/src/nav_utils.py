#!/usr/bin/env python3
import pathlib 
import yaml

def get_content_by_yaml(yaml_file):
    yaml_path = get_dir_yaml(yaml_file)
    with open(yaml_path, 'r') as stream:
        return yaml.safe_load(stream)

def get_dir_yaml(yaml_file):
    path = abs_path = str(pathlib.Path(__file__).parent.absolute())
    return path + "/cfg/" + yaml_file
