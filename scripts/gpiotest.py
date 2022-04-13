#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pigpio

from time import sleep

pi = pigpio.pi()

pi.set_mode(14, pigpio.INPUT)
pi.set_pull_up_down(14, pigpio.PUD_UP)

def cb_interrupt(gpio, level, tick):
    global callcnt
    print (gpio, level, tick)
    callcnt += 1
    pi.set_PWM_frequency(PIN, FREQ)
    pi.set_PWM_range(PIN, RANGE)
    pi.set_PWM_dutycycle(PIN, callcnt*1)

cb = pi.callback(14, pigpio.FALLING_EDGE, cb_interrupt)
 
pi = pigpio.pi()
pi.set_mode(PIN, pigpio.OUTPUT)
 

try:
    while True:
        pi.write(PIN, 1)
        sleep(0.5)
        pi.write(PIN, 0)
        sleep(0.5)
        if callcnt != 0:
            while True:
                sleep(0.5)
 
except KeyboardInterrupt:
    pass
 
pi.set_mode(PIN, pigpio.INPUT)
pi.stop()