#!/usr/bin/env python
import roslib
import rospy
import time
import wiringpi
from std_msgs.mst import String

# main
if __name__ == '__main__':
    rospy.init_node('detect_high')

    pub = rospy.Publisher('detecting', String, queue_size = 1)

    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(11, wirignpi.INPUT)
    wiringpi.pinMode(8, wiringpi.INPUT)
    rate = rospy.Rate(5)

    while not rospy.is_shutdown():
        b_str = ''
        b_str.append(str(wiringpi.digitalRead(11)))
        b_str.append(str(wiringpi.digitalRead(8)))
        pub.publish(b_str)
        rate.sleep()

    print('\rStopped')
