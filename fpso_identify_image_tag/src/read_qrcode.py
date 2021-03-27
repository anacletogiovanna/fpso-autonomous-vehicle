#!/usr/bin/env python3
import cv2 # importando o openCV
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from image_read_code import identify_qrcode

#Gerando a janela da imagem 
def callback_camera(data):
    bridge = CvBridge()
    cv_image= bridge.imgmsg_to_cv2(data)
    img_result = identify_qrcode(cv_image)
    cv2.imshow("Turtlebot3 - Vision", img_result)
    cv2.waitKey(1)

#Pegando a imagem da camera do turtlebot no topico
def receive_message():
    rospy.init_node("identify_image_tag", anonymous=False)
    rospy.Subscriber("/camera/rgb/image_raw", Image, callback_camera)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        receive_message()
    except rospy.ROSInterruptException:
        pass


    