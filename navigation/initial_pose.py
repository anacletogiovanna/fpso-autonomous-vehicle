#!/usr/bin/env python3
import yaml
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped, Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler

def set_initial_pose(pos, quat):
	rospy.init_node('set_initial_pose', anonymous=False) #Nome do no de controle
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
		rospy.loginfo(initpose_msg)
		rate.sleep()
    
def main():
	#Lendo a posicao e orientacao da pose inicial no arquivo 
	with open("fpso_poses.yaml", 'r') as stream:
		initial_pose = yaml.load(stream)[0]
		
	#Setando a pose inicial da base movel
	set_initial_pose(initial_pose['position'], initial_pose['quaternion'])
          
if __name__ == '__main__':
    main()