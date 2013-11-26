#!/usr/bin/env python

import rospy
import math
# transforms imports
import tf
# messages
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Pose2D, PoseArray
from tf import transformations
from vinter_msgs.msg import Location
# services
from std_srvs.srv import *

class LaserBase():
    def __init__(self):
        self.name = "intersection_0"
        self.subscribers = []
        self.laser_odoms = [{} for i in range(4)]
        self.Location = Location()
        self.Pose = Pose2D()
        self.tf_broadcaster = tf.TransformBroadcaster()
        
        self.pose_configured = 0
        self.laser_rcvd = [0 for i in range(4)]
        
        self.ns = rospy.get_param('/intersection/laser_array', 'laserbase0')
        rospy.Service('get_odoms',Empty,self.get_odoms)
        rospy.Service('get_location',Empty,self.get_location)
        rospy.init_node('laser_array_controller')
        
        rate = rospy.Rate(60)
        
        try:
            
            self.getLaserNames()
            self.subscribe()
                
            while not rospy.is_shutdown():
                
                if self.pose_configured == 1:
                    
                    for i in range(len(self.laser_odoms)):
                        x = self.laser_odoms[i].pose.pose.position.x
                        y = self.laser_odoms[i].pose.pose.position.y
                        z = self.laser_odoms[i].pose.pose.position.z
                        qx = self.laser_odoms[i].pose.pose.orientation.x
                        qy = self.laser_odoms[i].pose.pose.orientation.y
                        qz = self.laser_odoms[i].pose.pose.orientation.z
                        qw = self.laser_odoms[i].pose.pose.orientation.w
                        
                        self.tf_broadcaster.sendTransform((x,y,z),
                                                          (qx,qy,qz,qw),
                                                          rospy.Time.now(),
                                                          self.laser_names[i] + "/odom",
                                                          self.name)
                    
                    self.tf_broadcaster.sendTransform((0, 0, 0),
                                tf.transformations.quaternion_from_euler(0, 0, 0),
                                rospy.Time.now(),
                                self.name,
                                "map")
                        
                rate.sleep()
        
        except rospy.ROSInterruptException:
            rospy.loginfo('EXCEPTION!!')
    
    def getLaserNames(self):
        laser_names_str = rospy.get_param('laser_names_list','base_0 base_1 base_2 base_3')
        self.laser_names = laser_names_str.split(' ')
        rospy.loginfo("Laser names: %s" % self.laser_names)
    
    def subscribe(self):
        for i in range(0,len(self.laser_names)):
            self.subscribers.append(rospy.Subscriber(self.laser_names[i] + '/base_pose_ground_truth', Odometry, self.update_odom, i))
                                    
    def update_odom(self,data,item):
        #rospy.loginfo("item # %d, len = %d" % (item,len(self.laser_odoms)))
        self.laser_odoms[item] = data
        
        if self.pose_configured is 0:
            self.laser_rcvd[item] = 1
            rospy.loginfo("laser_rcvd = %d", item)
        
            if sum(self.laser_rcvd) == 4:
                x = []
                y = []
                        
                for i in range(len(self.laser_odoms)):            
                    x.append(self.laser_odoms[i].pose.pose.position.x)
                    y.append(self.laser_odoms[i].pose.pose.position.y)
                
                self.Pose.x = sum(x)/4.0
                self.Pose.y = sum(y)/4.0
                
                self.pose_configured = 1
        
        

    def get_location(self, req):
        rospy.loginfo("my Pose ")
        rospy.loginfo(self.Pose)        
    
    
    def get_odoms(self, req):

        for i in range(len(self.laser_odoms)):
            rospy.loginfo("Odom %d:", i)
            rospy.loginfo(self.laser_odoms[i].pose.pose)            
        
            
if __name__ == '__main__':
    laser_base = LaserBase()    
#    try:
#        laser_base = LaserBase()
#        laser_base.getLaserNames()
#        laser_base.subscribe()
#        
#        
#        while not rospy.is_shutdown():
#            rospy.sleep(1.0)
#        
#    except rospy.ROSInterruptException:
#        rospy.loginfo('EXCEPTION!!')