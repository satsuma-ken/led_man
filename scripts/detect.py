#!/usr/bin/env python
import roslib
import rospy
import time
import wiringpi
from std_msgs.msg import String

# main
if __name__ == '__main__':
    rospy.init_node('detect_high')

    pub = rospy.Publisher('detecting', String, queue_size = 1)

    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(11, 0)
    wiringpi.pinMode(8, 0)
    wiringpi.pinMode(20, 0)
    wiringpi.pinMode(21, 0)
    wiringpi.pullUpDnControl(11, 1)
    wiringpi.pullUpDnControl(8, 1)
    wiringpi.pullUpDnControl(20, 1)
    wiringpi.pullUpDnControl(21,1)
    rate = rospy.Rate(20)

    while not rospy.is_shutdown():
        b_str = ''
        b_str += str(wiringpi.digitalRead(11))
        b_str += str(wiringpi.digitalRead(8))
        b_str += str(wiringpi.digitalRead(20))
        b_str += str(wiringpi.digitalRead(21))
        pub.publish(b_str)
        rate.sleep()

    print('\rStopped')
