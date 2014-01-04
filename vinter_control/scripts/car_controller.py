#!/usr/bin/env python

import rospy
import math
import random
# message imports
from tf import transformations
from move_base_msgs.msg import MoveBaseActionGoal
from geometry_msgs.msg import Point, Pose, Pose2D, PoseArray, Quaternion
from vinter_control.srv import *

class CarController():
    def __init__(self):
        rospy.init_node('car_controller')
        
        rospy.loginfo('Starting car_controller node!!')
        self.init_vars()
        self.goal_pub = rospy.Publisher('/car_0/move_base/goal',MoveBaseActionGoal)
        self.publish = 0
        rospy.Service('/car_0/set_goal',Char,self.set_goal)
        rospy.Service('/car_0/set_goal_list',GoalList,self.set_goal_list)        
        
        rate = rospy.Rate(10)
        
        try:
            rospy.loginfo('Ready')            
            while not rospy.is_shutdown():
                if self.publish == 1:
                    self.goal_pub.publish(self.next_goal)
                    self.publish = 0
            
                rate.sleep()
        
        except rospy.ROSInterruptException:
            rospy.loginfo('EXCEPTION!!')
    
    def set_goal_list(self,req):
        rospy.loginfo("setting goal list from '%s' with %d items" % (req.first_goal, req.length))
        
        self.goal_list = []
        ng = req.first_goal
        
        for i in range(req.length):
            rospy.loginfo(ng)
            self.goal_list.append(ng)
            ind = self.keys.index(ng)
        
            ng_l = len(self.next_s[ind])
            
            if (ng_l == 1):
                ng = self.next_s[ind][0]
            else:
                ri = random.randint(0,1)
                ng = self.next_s[ind][ri]        
                     
        return self.goal_list
     
    def set_goal(self,req):
        
        resp = "setting goal to %s" % req.item
        rospy.loginfo(resp)
        self.next_goal = self.goals[req.item]
        self.publish = 1
        #self.goal_pub.publish(self.goals[req.item])
        return resp
        
        
    def init_vars(self):
        rospy.loginfo('Generating goals...')
        self.goals = {}
        self.goals_next = {}
        I = 0.4
        Q = 1.6
        H = 11.5
        W = 21.5
        PI = math.pi        
        
        self.keys = ['As','Aw','Bn','Bw','Cn','Ce','Ds','De',
                'E','F','G','H','I','J','K','L','M','N',
                'O','P','Q','R','S','T','U','V','W','X']
        x_s = [-I,-I,I,I,I,I,-I,-I,
               -I,I,Q,Q,I,-I,-Q,-Q,-I,I,
               W,W,W,W,I,-I,-W,-W,-W,-W]
        y_s = [I,I,I,I,-I,-I,-I,-I,
               Q,Q,I,-I,-Q,-Q,-I,I,H,H,
               H,I,-I,-H,-H,-H,-H,-I,I,H]
        th_s = [-PI/2,PI,PI/2,PI,PI/2,0,PI/2,0,
                -PI/2,PI/2,PI,0,PI/2,-PI/2,0,PI,-PI/2,0,
                -PI/2,PI,-PI/2,PI,PI/2,PI,PI/2,0,PI/2,0]
        self.next_s = (['Ce','Ds'],['L'],['F'],['Aw','Ds'],['Aw','Bn'],['H'],['J'],
                  ['Bn','Ce'],['As','L'],['N'],['Bw','F'],['Q'],['CnChar','H'],['T'],
                  ['De','J'],['W'],['E'],['O'],['P'],['G'],['R'],
                  ['S'],['I'],['U'],['V'],['K'],['X'],['M'])
        cnt = 0
        for i in self.keys:
            self.goals[i] = MoveBaseActionGoal()
            self.goals[i].goal.target_pose.header.frame_id = 'map'
            self.goals[i].goal.target_pose.pose.position.x = x_s[cnt]
            self.goals[i].goal.target_pose.pose.position.y = y_s[cnt]
            self.goals[i].goal.target_pose.pose.orientation = self.quat_from_euler(0.0, 0.0, th_s[cnt])
            cnt = cnt +1
        
        rospy.loginfo('Done!!')        
    
    def quat_from_euler(self,r, p, y):
          quat_g = Quaternion()
          quat_tf = transformations.quaternion_from_euler(r,p,y)
          
          quat_g.x = quat_tf[0]
          quat_g.y = quat_tf[1]
          quat_g.z = quat_tf[2]
          quat_g.w = quat_tf[3]
          
          return quat_g
          
          
    
if __name__ == '__main__':
    car_controller = CarController()    