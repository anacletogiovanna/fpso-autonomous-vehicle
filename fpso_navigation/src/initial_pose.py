#!/usr/bin/env python3

import os
import yaml
import rospy
import nav_utils as nav_utils
from geometry_msgs.msg import PoseWithCovarianceStamped, Pose, Point, Quaternion

def set_initial_pose(pos, quat):
	rospy.init_node('fpso', anonymous=False) #No de controle
	pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=10)
	rate = rospy.Rate(1) #10Hz
	
	#Criando o objeto para setar a pose inicial informada
	initpose_msg = PoseWithCovarianceStamped()
	initpose_msg.header.frame_id = 'map'
	initpose_msg.header.stamp = rospy.Time.now()
	initpose_msg.pose.pose = Pose(Point(pos['x'], pos['y'], 0.000), Quaternion(quat['x'], quat['y'], quat['z'], quat['w']))
	
	if not rospy.is_shutdown():
		rospy.loginfo("Setando pose inicial da base movel.")
		pub.publish(initpose_msg)
		rate.sleep()
		pub.publish(initpose_msg)
		rate.sleep()
    
def main():
	
	initial_pose = nav_utils.get_content_by_yaml(YAML_FILE)[0]
	set_initial_pose(initial_pose['position'], initial_pose['quaternion'])

if __name__ == '__main__':
	try:
		YAML_FILE = "fpso_poses.yaml"
		main()
	except KeyboardInterrupt:
		rospy.is_shutdown("Bye!")
	except rospy.ROSInterruptException:
		pass