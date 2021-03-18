#!/usr/bin/env python3

import yaml
import rospy
from time import sleep
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
from move_base_msgs.msg import MoveBaseActionResult

	
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
		#rate.sleep()
		rospy.sleep(5)
		pub.publish(pose_msg)
		rospy.loginfo(pose_msg)
		rate.sleep()
    
def main():
	with open("fpso_poses.yaml", 'r') as stream:
		poses = yaml.load(stream)
	rospy.init_node('fpso', anonymous=False) #No de controle
	
	while True:
		for i in range(len(poses)-1):
			#Setando a pose objetivo da base movel
			set_goal(i+1, poses[i+1]['position'], poses[i+1]['quaternion'])
			#Verificando se ja cheguei no meu objetivo
			while not rospy.is_shutdown():
				rospy.Subscriber('/move_base/result', MoveBaseActionResult, listener_robot_callback)
				if status == 3:
					break
					
if __name__ == '__main__':
	try:
		status = 0
		main()
	except rospy.ROSInterruptException:
		pass