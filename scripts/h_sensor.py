#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
HC-SR501
data sheet https://datasheetspdf.com/pdf-file/1493309/ETC/HC-SR501/1
"""

import pigpio
import rospy
from std_msgs.msg import Bool

HUMAN_SENSOR_SIGNAL = 18

class HumanSensor:
    def __init__(self, pin_asign = HUMAN_SENSOR_SIGNAL, IO_instance = pigpio.pi(), Topic_name = 'human_detect'):

        self.is_human_detect = False

        self.pin = pin_asign
        self.IO = IO_instance

        self.IO.set_mode(self.pin, pigpio.INPUT)
        self.IO.set_pull_up_down( self.pin, pigpio.PUD_UP )


        self.sensor_value = self.IO.read(self.pin)

        self.publisher = rospy.Publisher( Topic_name, Bool, queue_size=5)

        self.IO.callback(self.pin, pigpio.RISING_EDGE, self.cb_rising_edge)
        self.IO.callback(self.pin, pigpio.FALLING_EDGE, self.cb_falling_edge)

    def cb_rising_edge(self, gpio, level, tick):
        self.is_human_detect = True
        self.publisher.publish(self.is_human_detect)
        rospy.loginfo("rising")

    def cb_falling_edge(self, gpio, level, tick):
        self.is_human_detect = False
        self.publisher.publish(self.is_human_detect)
        rospy.loginfo("falling")

    def is_detect(self):
        return self.s_human_detect 


if __name__ == '__main__':

    rospy.init_node('human_sensor', anonymous=True)

    human_sensor = HumanSensor()

    rate = rospy.Rate(50)
    try:
        while not rospy.is_shutdown():
            #for now 
            rate.sleep()
    except KeyboardInterrupt:
        pass
    finally:
        pass