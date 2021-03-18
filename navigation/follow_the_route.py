#!/usr/bin/env python3

import yaml
import rospy
from time import sleep
from std_msgs.msg import Bool
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
from move_base_msgs.msg import MoveBaseActionResult

def listener_photo_callback(data):
    global status_photo
    status_photo = data
	
def listener_robot_callback(data):
    global status
    status = data.status.status
	
def set_goal(count, pos, quat):
	
	pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
	rate = rospy.Rate(1) #10Hz
	
	#Criando o objeto para setar a pose inicial informada
	pose_msg = PoseStamped()
	pose_msg.header.frame_id = 'map'
	pose_msg.header.stamp = rospy.Time.now()
	pose_msg.pose = Pose(Point(pos['x'], pos['y'], 0.000), Quaternion(quat['x'], quat['y'], quat['z'], quat['w']))
	
	if not rospy.is_shutdown():
		rospy.loginfo("Deslocando para pose: %s", count)
		pub.publish(pose_msg)
		rate.sleep()
		pub.publish(pose_msg)
		rospy.loginfo(pose_msg)
		rate.sleep()
    
def main():
	with open("fpso_poses.yaml", 'r') as stream:
		poses = yaml.load(stream)
	
	rospy.init_node('fpso', anonymous=False) #No de controle
	
	while True:
	
		set_goal(0, poses[0]['position'], poses[0]['quaternion'])
		sleep(2)
		
		for i in range(len(poses)):
		
			#Verificando se ja cheguei no meu objetivo
			while not rospy.is_shutdown():
				rospy.Subscriber('/move_base/result', MoveBaseActionResult, listener_robot_callback)
				#rospy.Subscriber('/take_picture', Bool, listener_photo_callback)
				#if status_photo == True:
				if status == 3:
					break
					
			#Setando a pose objetivo da base movel
			set_goal(i+1, poses[i+1]['position'], poses[i+1]['quaternion'])
			sleep(2)
          
if __name__ == '__main__':
	status = 0
	#status_photo = Bool()
	main()