#!/usr/bin/env python
import roslib
import rospy
import time
import wiringpi
# main
if __name__ == '__main__':
    rospy.init_node('ledflash')

    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(11, 1)
    wiringpi.pinMode(8, 1)

    while not rospy.is_shutdown():
        wiringpi.digitalWrite(11, 1)
        wiringpi.digitalWrite(8, 0)
        time.sleep(1)
        wiringpi.digitalWrite(11, 0)
        wiringpi.digitalWrite(8, 1)
        time.sleep(1)

    wiringpi.digitalWrite(11, 0)
    wiringpi.digitalWrite(8, 0)
    print('\rStopped')
