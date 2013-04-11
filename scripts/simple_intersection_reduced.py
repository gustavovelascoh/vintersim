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

if __name__ == '__main__':
	rospy.init_node('intersection')
	br = tf.TransformBroadcaster()
	br1 = tf.TransformBroadcaster()
	rate = rospy.Rate(1.0)
	
	while not rospy.is_shutdown():
		br.sendTransform((1.6, 1.6, 0.4),
							tf.transformations.quaternion_from_euler(0, 0, math.pi),
#							(0.0, 0.0, 0.0, math.pi*3/4),
							rospy.Time.now(),
							#"map",
							"robot_0/odom",
							"map")
		br1.sendTransform((-1.6, -1.6, 0.4),
							tf.transformations.quaternion_from_euler(0, 0, 0),
#							(math.pi/4, 0.0, 0.0, 0.0),
							rospy.Time.now(),
							"robot_1/odom",
							"map")
		rate.sleep()
