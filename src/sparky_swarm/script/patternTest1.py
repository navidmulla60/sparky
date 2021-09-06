#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PointStamped,Pose
from move_base_msgs.msg import MoveBaseAction ,MoveBaseGoal
from actionlib_msgs.msg import GoalID,GoalStatus
from nav_msgs.msg import Odometry
from rospy import names
from std_msgs.msg import Bool
import actionlib
class multipoint(object):
    
    def __init__(self,name):
        self.name=name
   
            
    def move(self,x,y):
        # print(str(self.name)+"-------Moving on defined path-------")
        
        robot_name=str(self.name)+'/move_base'
        
        # print(self.x,self.y)
        self.navclient=actionlib.SimpleActionClient(robot_name, MoveBaseAction)
        self.navclient.wait_for_server()
        
        
        self.goal=MoveBaseGoal()
        self.goal.target_pose.header.frame_id="map"
        self.goal.target_pose.header.stamp=rospy.Time.now()
        self.goal.target_pose.pose.position.x=x
        self.goal.target_pose.pose.position.y=y
        self.goal.target_pose.pose.position.z=0.0
        self.goal.target_pose.pose.orientation.x=0.0
        self.goal.target_pose.pose.orientation.y=0.0
        self.goal.target_pose.pose.orientation.z=0.0
        self.goal.target_pose.pose.orientation.w=1.0
        
        self.navclient.send_goal(self.goal)
        
        self.finished=self.navclient.wait_for_result()
        if not self.finished:
            rospy.loginfo("Server not avialable")
        else:
                rospy.loginfo(self.navclient.get_result())



def main():
    rospy.init_node("multipoint_navigation", anonymous=True)
    
    sparky1=multipoint("sparky1")
    sparky1.move(0,2)
    sparky2=multipoint("sparky2")
    sparky2.move(0,1)
    
    try: 
        rospy.spin()
        if rospy.is_shutdown:
                print("----------------------path-------------------------")
                print("")
                print("TATA !!!")
    except KeyboardInterrupt:
        print("Something went wrong!!!")


if __name__ == '__main__':
  
    main()
   
    
    