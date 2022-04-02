#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
HC-SR501
data sheet https://datasheetspdf.com/pdf-file/1493309/ETC/HC-SR501/1
"""

import RPi.GPIO as GPIO
#import Jetson.GPIO as GPIO

HUMAN_SENSOR_SIGNAL = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup( HUMAN_SENSOR_SIGNAL , GPIO.IN )

if __name__ == '__main__':
    try:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
    