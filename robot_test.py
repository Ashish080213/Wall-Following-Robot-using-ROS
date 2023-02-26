#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan 
from geometry_msgs.msg import Twist

def callback(msg): 
  print ("front",msg.ranges[360])
  print ("right",msg.ranges[180])
  print ("left",msg.ranges[540])

  if msg.ranges[360] < 0.5:
      move.linear.x = 0.0
      move.angular.z = 1

  else:
    if msg.ranges[180] > 0.2 and msg.ranges[180] < 0.3:
       move.linear.x = 0.2
       move.angular.z = 0.0

    if msg.ranges[180] > 0.3:
        move.linear.x = 0.2
        move.angular.z = -0.2

    if msg.ranges[180] < 0.2: 
        move.linear.x = 0.2
        move.angular.z = 0.2
            
  print ("linear",move.linear.x)
  print ("angular",move.angular.z)
  pub.publish(move)


rospy.init_node('test_node')
sub = rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist)
move = Twist()

rospy.spin()