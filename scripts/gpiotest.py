#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pigpio

from time import sleep

pi = pigpio.pi()
pi.set_mode(14, pigpio.OUTPUT)

try:
    while True:
        pi.write(14,pigpio.HIGH)
        print(pi.read(17))
        sleep(0.5)
        pi.write(14, pigpio.LOW)
        sleep(0.5)
except KeyboardInterrupt:
    pass   