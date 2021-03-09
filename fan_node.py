#!/usr/bin/env python

# NOTE ON PERMISSIONS:
# Have to type the below line first for permission change to run
# sudo chmod a+rw /dev/i2c-*

# CREDITS:
# 

# IMPORT:
import time
import board
import RPi.GPIO as GPIO        # need this?
from fan_first_test22.py import fanControl
import rospy

def talker(): # MAIN PART OF PUBLISHING:
	pub = rospy.Publisher('example/fan', fanControl, queue_size=50)    # Change: pub = rospy.Publisher('name_of_component', package_used, queue_size=50)
	rospy.init_node('fan node', anonymous=True)                 # Change: rospy.init_node('name_of_node', anonymous=True)
	
	start_time = rospy.Time.now()    # TIME KEEPING:
	current_time = rospy.Time.now()
	last_time = rospy.Time.now()
	rate = rospy.Rate(10)  # 10hz while not rospy.is_shutdown(): odom = Odometry()
	
	while not rospy.is_shutdown(): # FUNCTIONS OF SPECIFIC COMPONENT:
		f = fanControl()
		pub.publish(f) # PUBLISH RESULTS:
        
# NAME THIS SECTION:
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
