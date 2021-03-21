#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
from datetime import datetime

def get_dir_by_yaml(yaml_file):
    """
    Captures the directory path from the .yaml file 
    yaml_file: File with the directory 
    """    
    
    # Read information in yaml file 
    with open(yaml_file, 'r') as stream:
        yaml_dir = yaml.load(stream) [0]
        return yaml_dir['dir']


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

# def save_image(img, img_name):
#     """
#     Saves image using the OpenCV library
#     img: captured image  
#     img_name: name of image 
#     """     
    
# def take_photo(img, img_name):
#     global is_take_photo
#     tag_name = file_name_by_date(img_name)
#     tag_file_path = img_dir['dir'] + tag_name
#     cv2.imwrite(tag_file_path, img)
#     is_take_photo = False
    