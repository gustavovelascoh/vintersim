#!/usr/bin/env python

# standard imports
#import roslib
#roslib.load_manifest('intersection')
import rospy
import math
# transforms imports
import tf
# messages
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Pose2D, PoseArray
from tf import transformations

class Intersection():
	
	def set_type(self,type):
		self._type = type
	
	def __init__(self):
		self.pose = Pose()

if __name__ == '__main__':
	rospy.init_node('intersection')
	
	intersection = Intersection()
	intersection.set_type('crossroad')
	intersection.pose.position.x = 0
	intersection.pose.position.y = 0
	intersection.pose.orientation = tf.transformations.quaternion_from_euler(0,0,0)
	
	br0 = tf.TransformBroadcaster()
	br1 = tf.TransformBroadcaster()
	br2 = tf.TransformBroadcaster()
	br3 = tf.TransformBroadcaster()
	br4 = tf.TransformBroadcaster()
	rate = rospy.Rate(5)
	
	try:
		while not rospy.is_shutdown():
			br0.sendTransform((1.6, 1.6, 0.4),
								tf.transformations.quaternion_from_euler(0, 0, math.pi),
								rospy.Time.now(),
								"robot_0/odom",
								"intersection_0")
			br1.sendTransform((1.6, -1.6, 0.4),
								tf.transformations.quaternion_from_euler(0, 0, math.pi/2),
								rospy.Time.now(),
								"robot_1/odom",
								"intersection_0")
			br2.sendTransform((-1.6, -1.6, 0.4),
								tf.transformations.quaternion_from_euler(0, 0, 0),
								rospy.Time.now(),
								"robot_2/odom",
								"intersection_0")
			br3.sendTransform((-1.6, 1.6, 0.4),
								tf.transformations.quaternion_from_euler(0, 0, -math.pi/2),
								rospy.Time.now(),
								"robot_3/odom",
								"intersection_0")
			br4.sendTransform((0, 0, 0),
								tf.transformations.quaternion_from_euler(0, 0, 0),
								rospy.Time.now(),
								"intersection_0",
								"map")
			rate.sleep()
	except rospy.ROSInterruptException:
			pass
