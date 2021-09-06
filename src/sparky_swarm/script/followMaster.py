#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PointStamped,Pose
from move_base_msgs.msg import MoveBaseAction ,MoveBaseGoal
from actionlib_msgs.msg import GoalID,GoalStatus
from nav_msgs.msg import Odometry
from std_msgs.msg import Bool
import actionlib
class multipoint(object):
    def __init__(self):
        self.x=[]
        self.y=[]
        self.count=0
       
        self.point_data=rospy.Subscriber("clicked_point", PointStamped, self.callback)
        
    def callback(self, data):
        
        if (self.count<3): 
            
            data=data.point # filtering
            self.x.append(data.x) 
            self.y.append(data.y)
            # print(self.x)
            self.count=self.count+1
        else:
            print(".....terminating......")
            self.point_data.unregister()
            print(self.x)
            print(self.y)
            print("-------Moving robot on defined path-------")

            # self.point_data=rospy.Subscriber("/sparky1/odom", Odometry, self.followcallback)
  

            self.navclient=actionlib.SimpleActionClient('sparky2/move_base', MoveBaseAction)
            self.navclient.wait_for_server()
            
            for points in range(len(self.x)):

                self.goal=MoveBaseGoal()
                self.goal.target_pose.header.frame_id="map"
                self.goal.target_pose.header.stamp=rospy.Time.now()

                self.goal.target_pose.pose.position.x=self.x[points]
                self.goal.target_pose.pose.position.y=self.y[points]

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
    mp=multipoint()
    
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
   
    
    