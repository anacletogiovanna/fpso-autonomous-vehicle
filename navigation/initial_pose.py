#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped, Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler

def set_initial_pose(pose):
    rospy.init_node('set_initial_pose', anonymous=False) #Nome do nó de controle
    pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=10)
    rate = rospy.Rate(1) #10Hz

    #Criando o objeto para setar a pose inicial informada
	quat = quaternion_from_euler(0, 0, pose['z'])
    initpose_msg = PoseWithCovarianceStamped()
    initpose_msg.header.frame_id = 'map'
	initpose_msg.header.stamp = rospy.Time.now()
	initpose_msg.pose = Pose(Point(pose['x'], pose['y'], 0.000), Quaternion(quat[0], quat[1], quat[2], quat[3]))
	
	if not rospy.is_shutdown():
		pub.publish(initpose_msg)
		rate.sleep()
		pub.publish(initpose_msg)
		rospy.loginfo("Setando pose inicial da base movel.")
		rate.sleep()
    
def main():
	#Lendo a posoção e orientação da pose inicial no arquivo 
	with open("initial_pose.yaml", 'r') as stream:
		initial_pose = yaml.load(stream)
		
	#Setando a pose inicial do robô
	set_initial_pose(initial_pose[pose])
          
if __name__ == '__main__':
    main()