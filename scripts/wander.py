#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

robot_pose = Odometry()
next_goal = Odometry()

robot_vel = Twist()

# Functions
def set_goal():
	pass

def move_to():
	pass

# Services

def start_wander():
	pass

def stop_wander():
	pass

# Subscriber callback
def pose_subscriber(data):
	global robot_pose
	
	robot_pose = data
	
# Publishers
def talker():
    pub = rospy.Publisher('chatter', String)
    rospy.init_node('talker')
    while not rospy.is_shutdown():
        str = "hello world %s" % rospy.get_time()
        rospy.loginfo(str)
        pub.publish(String(str))
        rospy.sleep(1.0)


if __name__ == '__main__':
	try:
		vel_pub = rospy.Publisher('/robot_2/cmd_vel',Twist);
		rospy.init_node('wander')
		rospy.Subscriber("/robot_2/odom", Odometry, pose_subscriber)
		while not rospy.is_shutdown():
			rospy.loginfo("my Pose is (%s,%s)" % (robot_pose.pose.pose.position.x,robot_pose.pose.pose.position.y))
			rospy.sleep(1.0)
	except rospy.ROSInterruptException:
		pass
