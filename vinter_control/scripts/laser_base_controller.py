#!/usr/bin/env python

import rospy
import math
# transforms imports
import tf
# messages
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Pose2D, PoseArray
from tf import transformations
from its_msgs.msg import Location
# services
from std_srvs.srv import *

class LaserBase():
    def __init__(self):
        self.subscribers = []
        self.laser_odoms = [{} for i in range(4)]
        self.Location = Location()
        self.ns = rospy.get_param('laserbase_name', 'base0')
        rospy.Service('get_odoms',Empty,self.get_odoms)
        rospy.init_node('laser_base_controller')
        
        try:
            
            self.getLaserNames()
            self.subscribe()
                
            while not rospy.is_shutdown():
                rospy.sleep(1.0)
        
        except rospy.ROSInterruptException:
            rospy.loginfo('EXCEPTION!!')
    
    def getLaserNames(self):
        laser_names_str = rospy.get_param('laser_names_list')
        self.laser_names = laser_names_str.split(' ')
    
    def subscribe(self):
        for i in range(0,len(self.laser_names)):
            self.subscribers.append(rospy.Subscriber(self.laser_names[i] + '/base_pose_ground_truth', Odometry, self.update_odom, i))
                                    
    def update_odom(self,data,item):
        #rospy.loginfo("item # %d, len = %d" % (item,len(self.laser_odoms)))
        self.laser_odoms[item] = data
        

    def get_location():
        pass
    
    def get_odoms(self, req):
        for i in range(len(self.laser_odoms)):
            rospy.loginfo("Odom %d:", i)
            rospy.loginfo(self.laser_odoms[i])
        
            
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