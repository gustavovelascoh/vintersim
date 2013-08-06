#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from vintersim.srv import *

robot_pose = Odometry()
next_goal = Odometry()

robot_vel = Twist()
wander = 0
turn = 0;

# Functions
def set_goal():
	pass

def move_to():
	pass

# Services

def start_wander(req):
	global wander
	wander = 1
	rospy.loginfo("starting wander...")
	return wander

def stop_wander(req):
	global wander
	wander = 0
	rospy.loginfo("stoping wander...")
	return wander

def turn():
	global turn
	turn = 1
	rospy.loginfo("turning...")

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
		vel_pub = rospy.Publisher('/car_0/cmd_vel',Twist)
		rospy.init_node('wander')
		rospy.Subscriber("/car_0/odom", Odometry, pose_subscriber)
		rospy.Service('/car_0/start_wander', WanderCtrl, start_wander)
		rospy.Service('/car_0/stop_wander', WanderCtrl, stop_wander)
		rospy.Service('/car_0/turn', WanderCtrl, turn)
		
		while not rospy.is_shutdown():
			rospy.loginfo("my Pose is (%s,%s)" % (robot_pose.pose.pose.position.x,robot_pose.pose.pose.position.y))
			if wander:
				x_0 = robot_pose.pose.pose.position.x
				robot_vel.linear.x = 5
				vel_pub.publish(robot_vel)
			else:	
				rospy.sleep(1.0)
			
	except rospy.ROSInterruptException:
		pass
