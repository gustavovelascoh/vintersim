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
from vinter_msgs.msg import Location

global my_int

class LaserBase():
    def __init__(self):
        self.location = Location()
        self.ns = rospy.get_param('laserbase_name', 'base0')
        self.subscriber = None
	

class Intersection():
	
	def set_type(self,type):
		self._type = type
	
	def set_location(self):
		lats = []
		longs = []
		
		for i in range(0,4):
			lats.append(self.laser_array[i].location.latitude)
			rospy.loginfo('lats = %f' % self.laser_array[i].location.latitude)
			longs.append(self.laser_array[i].location.longitude)
		
		self.location.latitude = sum(lats)/4
		self.location.longitude = sum(longs)/4
		
		rospy.loginfo('Intersection location: %f, %f' % (self.location.latitude,
														self.location.longitude))
		self.located = 1
	
	def __init__(self):
		self.located = 0
		self.id = 1
		self.location = Location()
		self.laser_array = []
		
def update_laser(data,src):
	global my_int
	
	my_int.laser_array[src].location.latitude = data.pose.pose.position.x
	my_int.laser_array[src].location.longitude = data.pose.pose.position.y
	
	#rospy.loginfo('lat %f == %f',data.pose.pose.position.x,my_int.laser_array[src].location.latitude)

if __name__ == '__main__':
	rospy.init_node('simple_intersection')
	
	my_int = intersection = Intersection()
	my_int.set_type('crossroad')
	
	laser_list_str = rospy.get_param('laser_base_list', '')
	laser_ns = laser_list_str.split(' ')
	rospy.loginfo('laser_list = %s' % laser_list_str)
	
	l0 = LaserBase()
	l0.ns = laser_ns[0]
	l0.subscriber = rospy.Subscriber(l0.ns + '/base_pose_ground_truth',Odometry,update_laser,0)
	my_int.laser_array.append(l0)
	
	l1 = LaserBase()
	l1.ns = laser_ns[1]
	l1.subscriber = rospy.Subscriber(l1.ns + '/base_pose_ground_truth',Odometry,update_laser,1)
	my_int.laser_array.append(l1)
	
	l2 = LaserBase()
	l2.ns = laser_ns[2]
	l2.subscriber = rospy.Subscriber(l2.ns + '/base_pose_ground_truth',Odometry,update_laser,2)
	my_int.laser_array.append(l2)
	
	l3 = LaserBase()
	l3.ns = laser_ns[3]
	l3.subscriber = rospy.Subscriber(l3.ns + '/base_pose_ground_truth',Odometry,update_laser,3)
	my_int.laser_array.append(l3)
		
	br0 = tf.TransformBroadcaster()
	br1 = tf.TransformBroadcaster()
	br2 = tf.TransformBroadcaster()
	br3 = tf.TransformBroadcaster()
	br4 = tf.TransformBroadcaster()
	rate = rospy.Rate(5)
	rospy.sleep(1)
	#my_int.set_location()
	
	try:
		while not rospy.is_shutdown():
			if my_int.located == 0:
				my_int.set_location()
				
			
			br0.sendTransform((1.6, 1.6, 0.4),
								tf.transformations.quaternion_from_euler(0, 0, math.pi),
								rospy.Time.now(),
								"base_0/odom",
								"intersection_0")
			br1.sendTransform((1.6, -1.6, 0.4),
								tf.transformations.quaternion_from_euler(0, 0, math.pi/2),
								rospy.Time.now(),
								"base_1/odom",
								"intersection_0")
			br2.sendTransform((-1.6, -1.6, 0.4),
								tf.transformations.quaternion_from_euler(0, 0, 0),
								rospy.Time.now(),
								"base_2/odom",
								"intersection_0")
			br3.sendTransform((-1.6, 1.6, 0.4),
								tf.transformations.quaternion_from_euler(0, 0, -math.pi/2),
								rospy.Time.now(),
								"base_3/odom",
								"intersection_0")
			br4.sendTransform((0, 0, 0),
								tf.transformations.quaternion_from_euler(0, 0, 0),
								rospy.Time.now(),
								"intersection_0",
								"map")
			rate.sleep()
	except rospy.ROSInterruptException:
			pass
