
import cv2 # importando o openCV
import rospy
from datetime import datetime
import time
import image_utils as img_utils
from sensor_msgs.msg import Image
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from move_base_msgs.msg import MoveBaseActionResult
from cv_bridge import CvBridge
import numpy as np
from pyzbar.pyzbar import decode # importando biblioteca de decodificacao de qrCode

#Variavel de controle para tirar a foto 
is_take_photo = True

odom = Odometry()
status_goal = 0

yaml_file = "image_dir.yaml"

def callback_status_goal(data):
    global status_goal
    status_goal = data.status.status

def get_status_goal():
    rospy.Subscriber("/move_base/result", MoveBaseActionResult, callback_status_goal)

#mandando as informacoes sobre a imagem para um topico 
def callback_pose(data):
    global odom
    odom = data
       
def send_img_info_by_topic(tag_name):

    global odom 

    date = datetime.now().strftime("%Y%m%d%H%M%S")
    
    rospy.Subscriber("/odom", Odometry, callback_pose)
    odom_x = odom.pose.pose.position.x
    odom_y = odom.pose.pose.position.y  

    img_info = "tag: {}, pose: [x: {}, y:{}], timstamp:{} ".format(tag_name, odom_x, odom_y, date)

    pub = rospy.Publisher("/image_info_tag", String, queue_size=10)

    pub.publish(img_info)
    

#tirando a foto 
def take_photo(img, img_name):

    tag_name = img_utils.file_name_with_timestamp(img_name, ".png")

    tag_file_path = img_utils.get_dir_by_yaml(yaml_file) + tag_name
    cv2.imwrite(tag_file_path, img)
    
    
#identificando e decodificando o qrCode       
def identify_qrcode(img):
    get_status_goal()
    global is_take_photo
    
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img, [pts], True, (0,255,0),5)
        pts2 = barcode.rect
        cv2.putText(img, myData,(pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255,0,255), 2)

        
        if(status_goal == 3 and is_take_photo):
            take_photo(img, myData)
            print(myData)
            send_img_info_by_topic(myData)
            is_take_photo = False
        
        if(status_goal != 3):
            is_take_photo = True 

    return img

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


    