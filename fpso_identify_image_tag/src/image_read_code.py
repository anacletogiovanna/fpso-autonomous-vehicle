#!/usr/bin/env python3
import numpy as np
from pyzbar.pyzbar import decode # importando biblioteca de decodificacao de qrCode
import ros_odometry as rosodom
import image_utils as img_utils
import cv2 # importando o openCV


#Variavel de controle para tirar a foto 
is_take_photo = True
yaml_file = "image_dir.yaml"

#tirando a foto 
def take_photo(img, img_name):

    tag_name = img_utils.file_name_with_timestamp(img_name, ".png")
    tag_file_path = img_utils.get_dir_by_yaml(yaml_file) + tag_name
    cv2.imwrite(tag_file_path, img)
    
#identificando e decodificando o qrCode       
def identify_qrcode(img):

    status_goal = rosodom.get_status_goal()
    
    global is_take_photo
    
    for barcode in decode(img):
        
        tag_info = barcode.data.decode('utf-8')
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img, [pts], True, (0,255,0),5)
        pts2 = barcode.rect
        cv2.putText(img, tag_info,(pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255,0,255), 2)

        if(status_goal == 3 and is_take_photo):
            take_photo(img, tag_info)
            rosodom.send_img_info_by_topic(tag_info)
            is_take_photo = False
        
        if(status_goal != 3):
            is_take_photo = True 

    return img