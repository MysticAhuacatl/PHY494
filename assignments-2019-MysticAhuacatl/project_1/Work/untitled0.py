#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 20:29:34 2019

@author: Martin
"""

import matplotlib.pyplot as plt
import numpy as np
import math

a = -3  # vehicle decceleration (m/s^2)
v0 = 15.2778  # vehicle velocity (m/s)
tau = 3  # green to red (s)
d = 0.8  # reaction time (s)
w = 30  # intersection width (m)

def eqbrake(xi, time):
    t = list(range(0 , time + 0.1 , 0.1))
    x = []
    for q in t:
        while q <= d:
            q = xi + v0*q
            x.append(q)
    print(x)

eqbrake(-30, 7)
#def eqbrake(xinitial, time):