# Wall-Following-Robot-using-ROS

In this project, I use topics to control a robot and my goal is to create a ROS program that makes the robot have a wall following behavior.

The wall following behavior is a behavior that makes the robot follow along the wall on its right hand side. This means that the robot must be moving forward at a 30cm distance from the wall, having the wall on its right hand side, the entire time.

To achieve this behavior in the robot, I followed two things:

--> Subscribe to the laser topic of the robot

--> Publish to the velocity topic of the robot


launched the keyboard teleop with the following command:

**rosrun teleop_twist_keyboard teleop_twist_keyboard.py**

Now used the keys to move the robot to a convenient position to test my ROS program.
