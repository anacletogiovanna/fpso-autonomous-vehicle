#!/usr/bin/env python3

import yaml
import rospy
from datetime import datetime
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
from move_base_msgs.msg import MoveBaseActionResult

GOAL_REACHED = 3
	
def listener_robot_callback(data):
    global status
    status = data.status.status
	
def set_goal(count, pose):
	pos = pose['position']
	quat = pose['quaternion']
	local = pose['local']
	pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
	rate = rospy.Rate(1) #10Hz
	pose_msg = PoseStamped()
	pose_msg.header.frame_id = 'map'
	pose_msg.header.stamp = rospy.Time.now()
	pose_msg.pose = Pose(Point(pos['x'], pos['y'], 0.000), Quaternion(quat['x'], quat['y'], quat['z'], quat['w']))
	if not rospy.is_shutdown():
		dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		rospy.loginfo("Deslocando para pose: %s - %s em %s", count, local, dt)
		pub.publish(pose_msg)
		rospy.sleep(1)
		#rospy.loginfo(pose_msg)
		pub.publish(pose_msg)
		rospy.sleep(1)
    
def main():
	with open("fpso_poses.yaml", 'r') as stream:
		poses = yaml.load(stream)
	rospy.init_node('fpso', anonymous=False)
	
	while True:
		for i in range(len(poses)-1):
			set_goal(i+1, poses[i+1])
			while not rospy.is_shutdown():
				rospy.Subscriber('/move_base/result', MoveBaseActionResult, listener_robot_callback)
				if status == GOAL_REACHED:
					rospy.sleep(3)
					break
					
if __name__ == '__main__':
	try:
		status = 0
		main()
	except KeyboardInterrupt:
		rospy.is_shutdown("Bye!")
	except rospy.ROSInterruptException:
		pass