#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
HC-SR501
data sheet https://datasheetspdf.com/pdf-file/1493309/ETC/HC-SR501/1
"""


import pigpio

from time import sleep

import rospy
from std_msgs.msg import Bool

from human_sensor.srv import PolingStart
from human_sensor.srv import PolingStop

from h_sensor import HumanSensor

class HumanSensorService:
    def __init__(self, sensor): 

        self.sensor = HumanSensor()
        
        #rospy.Service('hs_poling_start', PolingStart, self.poling_start)
        #rospy.Service('hs_poling_stop', PolingStop, self.poling_stop)

        #self.publisher = rospy.Publisher('human_detect', Bool, queue_size=5)

    def poling_start(self):
        pass

    def poling_stop(self):
        pass
    
    def poling_sens_and_publish(self):

        is_detect = self.sensor.is_detected()
        self.publisher(self.publisher)



if __name__ == '__main__':

    HUMAN_SENSOR_SIGNAL = 18

    #rospy.init_node('human_sensor_node') 

    #rate = rospy.Rate(1)#1Hz 

    h_sensor = HumanSensor( HUMAN_SENSOR_SIGNAL, GPIO )

    sensor_service = HumanSensorService( h_sensor )

    try:
        while not rospy.is_shutdown():
            #for now 
            sensor_service.poling_sens_and_publish()
            rate.sleep()
            
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
    