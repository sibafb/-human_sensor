#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
HC-SR501
data sheet https://datasheetspdf.com/pdf-file/1493309/ETC/HC-SR501/1
"""

import pigpio

HUMAN_SENSOR_SIGNAL = 18

class HumanSensor:
    def __init__(self, pin_asign = HUMAN_SENSOR_SIGNAL, IO_instance = pigpio.pi()):

        self.is_human_detect = False

        self.pin = pin_asign
        self.IO = IO_instance

        self.IO.set_mode(self.pin, pigpio.INPUT)
        self.IO.set_pull_up_down( self.pin, pigpio.PUD_UP )


        self.sensor_value = self.IO.input(self.pin)

    def cb_rising_edge(self):
        self.is_human_detect = True

    def cb_falling_edge(self):
        self.is_human_detect = False

    def is_detect(self):

        return self.s_human_detect 


if __name__ == '__main__':
    try:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        pass