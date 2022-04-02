#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
HC-SR501
data sheet https://datasheetspdf.com/pdf-file/1493309/ETC/HC-SR501/1
"""

import RPi.GPIO as GPIO
#import Jetson.GPIO as GPIO

HUMAN_SENSOR_SIGNAL = 18

class HumanSenosr:
    def __init__(self, pin_asign = HUMAN_SENSOR_SIGNAL, IO_instance = GPIO):
        self.pin = pin_asign
        self.IO = IO_instance

        self.IO.setup( self.pin ,  IO_instance.IN )

        self.sensor_value = self.IO.input(self.pin)

    def value(self):
        self.sensor_value = self.IO.input(self.pin)

        return self.sensor_value
    
    def is_detected(self):
        self.sensor_value = self.IO.input(self.pin)

        if self.sensor_value == GPIO.HIGH:
            return True
        return False

    def is_just_detected(self):
        if self.sensor_value != self.IO.input(self.pin):
            self.sensor_value = self.IO.input(self.pin)
            return True
        else:
            return False
        

        


if __name__ == '__main__':
    try:
        IO .setmode( GPIO.BCM )
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
    