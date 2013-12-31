#!/usr/bin/env python

import rospy
import math
# message imports
from tf import transformations
from move_base_msgs.msg import MoveBaseActionGoal
from geometry_msgs.msg import Point, Pose, Pose2D, PoseArray
from vinter_control.srv import *

class CarController():
    def __init__(self):
        self.init_vars()
        self.goal_pub = rospy.Publisher('/car_0/move_base/goal',MoveBaseActionGoal)
        self.publish = 0
        rospy.Service('set_goal',Char,self.set_goal)
        
        rospy.init_node('car_controller')
        rate = rospy.Rate(10)
        
        try:            
            while not rospy.is_shutdown():
                if self.publish == 1:
                    self.goal_pub.publish(self.next_goal)
                    self.publish = 0
            
                rate.sleep()
        
        except rospy.ROSInterruptException:
            rospy.loginfo('EXCEPTION!!')
        
    def set_goal(self,req):
        
        rospy.loginfo("setting goal to %s",req.item)
        self.next_goal = self.goals[req.item]
        self.publish = 1
        #self.goal_pub.publish(self.goals[req.item])
        return
        
        
    def init_vars(self):
        self.goals = {}
        
        self.goals['Q'] = MoveBaseActionGoal()
        self.goals['Q'].goal.target_pose.header.frame_id = 'map'
        self.goals['Q'].goal.target_pose.pose.position.x = 21.5
        self.goals['Q'].goal.target_pose.pose.position.y = -0.4
        self.goals['Q'].goal.target_pose.pose.orientation.w = 1
        
        self.goals['R'] = MoveBaseActionGoal()
        self.goals['R'].goal.target_pose.header.frame_id = 'map'
        self.goals['R'].goal.target_pose.pose.position.x = 21.5
        self.goals['R'].goal.target_pose.pose.position.y = -11.5
        quaternion = transformations.quaternion_from_euler(0.0,0.0,math.pi)
        #type(pose) = geometry_msgs.msg.Pose
        self.goals['R'].goal.target_pose.pose.orientation.x = quaternion[0]
        self.goals['R'].goal.target_pose.pose.orientation.y = quaternion[1]
        self.goals['R'].goal.target_pose.pose.orientation.z = quaternion[2]
        self.goals['R'].goal.target_pose.pose.orientation.w = quaternion[3]
        #self.goals['R'].goal.target_pose.pose.orientation.w = math.sqrt(2.0)/2.0
        #self.goals['R'].goal.target_pose.pose.orientation.y = math.sqrt(2.0)/2.0#,0.0,math.sqrt(2)/2,0.0)#transformations.quaternion_from_euler(5.0*math.pi/4.0, 0, 0)
        
        self.goals['S'] = MoveBaseActionGoal()
        self.goals['S'].goal.target_pose.header.frame_id = 'map'
        self.goals['S'].goal.target_pose.pose.position.x = 0.4
        self.goals['S'].goal.target_pose.pose.position.y = -11.5
        quaternion = transformations.quaternion_from_euler(0.0,0.0,math.pi/2.0)
        #type(pose) = geometry_msgs.msg.Pose
        self.goals['S'].goal.target_pose.pose.orientation.x = quaternion[0]
        self.goals['S'].goal.target_pose.pose.orientation.y = quaternion[1]
        self.goals['S'].goal.target_pose.pose.orientation.z = quaternion[2]
        self.goals['S'].goal.target_pose.pose.orientation.w = quaternion[3]
        #self.goals['S'].goal.target_pose.pose.orientation.w = math.sqrt(2.0)/2.0
        #self.goals['S'].goal.target_pose.pose.orientation.y = -math.sqrt(2.0)/2.0#,0.0,-math.sqrt(2)/2,0.0)#transformations.quaternion_from_euler(math.pi/2.0, 0, 0)
        #self.goals['Q'].goal.target_pose.pose.orientation.y = -0.866    
    
if __name__ == '__main__':
    car_controller = CarController()    