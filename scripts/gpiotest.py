#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pigpio

from time import sleep

pi = pigpio.pi()
pi.set_mode(14, pigpio.OUTPUT)

pi.set_mode(15, pigpio.INPUT)
pi.set_pull_up_down(15, pigpio.PUD_UP)

pi.set_mode(18, pigpio.INPUT)
pi.set_pull_up_down(18, pigpio.PUD_UP)

def cb_interrupt(gpio, level, tick):
    print (gpio, level, tick)
    sleep(0.2)

def cb2_interrupt(gpio, level, tick):
    print (gpio, level, tick)
    sleep(0.2)

cb = pi.callback(15, pigpio.RISING_EDGE, cb_interrupt)

cb2 = pi.callback(18, pigpio.RISING_EDGE, cb2_interrupt)

try:
    while True:
        pi.write(14,pigpio.HIGH)
        print(pi.read(14))
        sleep(0.5)
        pi.write(14,pigpio.LOW)
        print(pi.read(14))
        sleep(0.5)
except KeyboardInterrupt:
    pass   