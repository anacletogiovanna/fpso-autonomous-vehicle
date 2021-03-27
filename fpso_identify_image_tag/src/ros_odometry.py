#!/usr/bin/env python3
import rospy
import time
from datetime import datetime
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from move_base_msgs.msg import MoveBaseActionResult

pose_x = pose_y = 0.0
status_goal = 0

def callback_status_goal(data):
    global status_goal
    status_goal =  data.status.status

def get_status_move_base():
    rospy.Subscriber("/move_base/result", MoveBaseActionResult, callback_status_goal)

def get_status_goal():
    global status_goal
    get_status_move_base()
    return status_goal

def callback_pose(data):
    global pose_x, pose_y
    pose_x = round(data.pose.pose.position.x,5)
    pose_y = round(data.pose.pose.position.y,5)
       
def get_odometry():
    rospy.Subscriber("/odom", Odometry, callback_pose)
    time.sleep(0.25)

def send_img_info_by_topic(tag_name):
    global pose_x, pose_y
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    get_odometry()
    img_info = "tag: {}, pose: [x: {}, y:{}], timstamp:{} ".format(tag_name, pose_x, pose_y, date)
    pub = rospy.Publisher("/image_info_tag", String, queue_size=10)
    time.sleep(0.25)
    pub.publish(img_info)
    rospy.loginfo(img_info)   