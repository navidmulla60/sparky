#!/usr/bin/env python

import roslaunch
import subprocess

def robot(name,pos_x,count):
    path="/home/navid/sparky/src/sparky_swarm/launch/swarm_robot.launch"
    if str(count)<str(2):
          joint_publisher='joint_publisher:=true'
          
    else:
          joint_publisher='joint_publisher:=false'
    print(joint_publisher)    
    robot_name = name
    x_pos = pos_x
    print(x_pos)
    y_pos = 'y_pos:=0'
    z_pos = 'z_pos:=0'
    joint_publisher=joint_publisher

    cli_args = [path, robot_name, x_pos, y_pos, z_pos,joint_publisher]
    roslaunch_args = cli_args[1:]
    roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0], roslaunch_args)]

    uuid=roslaunch.rlutil.get_or_generate_uuid(None, False)

    roslaunch.configure_logging(uuid)
    global launch
    launch=roslaunch.parent.ROSLaunchParent(uuid,roslaunch_file)
    launch.start()
    

def nav(count,name):
  path2="/home/navid/sparky/src/sparky_swarm/launch/sparky_swarm_navigation_stack.launch"
        
  amcl_count=count
  robot_name = name
  # movebase_count=count
  cli_args = [path2, amcl_count,robot_name]
  roslaunch_args = cli_args[1:]
  roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0], roslaunch_args)]
  uuid=roslaunch.rlutil.get_or_generate_uuid(None, False)
  roslaunch.configure_logging(uuid)
  global launch
  launch=roslaunch.parent.ROSLaunchParent(uuid,roslaunch_file)
  launch.start()


print("_________________________________________________________________________")
print("       -----------------------------------------------------------")
print("_________________________________________________________________________")
print("       -----------------------------------------------------------")


number_of_robots=input("Enter the number of Robots")
print("_________________________________________________________________________")
print("       -----------------------------------------------------------")
print("_________________________________________________________________________")
for i in range(int(number_of_robots)):
    robot_name="robot_name:=sparky"+str(i+1)
    pos_x="x_pos:="+str((i+1)*2)
   
    count=str(i+1);
    robot(robot_name,pos_x,count)
    
    nav(count,robot_name)
try:
  launch.spin()
finally:
  # After Ctrl+C, stop all nodes from running
  launch.shutdown()
    