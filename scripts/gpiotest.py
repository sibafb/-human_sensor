#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pigpio

from time import sleep

pi = pigpio.pi()
pi.set_mode(14, pigpio.OUTPUT)

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