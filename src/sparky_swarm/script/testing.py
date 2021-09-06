#!/usr/bin/env python
import subprocess

class start:
    def swarmrobot(self):
        self.name="sparky"
        for i in range(int(self.num)):
            print("Hello")
            subprocess.call("/home/navid/sparky/src/sparky_swarm/script/test2lauchFile.py",1)
            

if __name__ == '__main__':
    
    robot=start()
    number_of_robots=input()
    robot.num=number_of_robots
    robot.swarmrobot()
    