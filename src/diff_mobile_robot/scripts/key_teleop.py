#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
 
def callback(data):
	twist = Twist()
	twist.linear.x = 4*data.axes[1]
	twist.angular.z = 4*data.axes[0]
	pub.publish(twist)
 
def joy_teleop():
	rospy.init_node('Joy_teleop')
	rospy.Subscriber("joy", Joy, callback)
	global pub
	pub = rospy.Publisher('/cmd_vel', Twist)
 
	r = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		r.sleep()
 
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
 
if __name__ == '__main__':
