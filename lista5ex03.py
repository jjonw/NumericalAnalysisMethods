#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from math import sin,pi

def solveEx3():
    b    = 1/6
    dx   = 1/20
    # dt <= (dx^2)/(2b)
    dt   = 0.1*(dx*dx/(2*b))
    tmax = 1
    xmax = 1
    
    t = np.arange(0, tmax + dt, dt)
    x = np.arange(0, xmax + dx, dx)
    tl = len(t)
    xl = len(x)
    w = np.zeros([xl, tl])

    # Necessario a inicializacao antecipada destas
    for n in range(0, tl):
        w[0, n] = 1
        w[1, n] = 0 
    for i in range(0, xl):
        w[i, 0] = 1 + sin(2*pi*x[i]*x[i])
            
    for n in range(0, tl - 1):
        for i in range(1, xl - 1):
            w[i, n+1] = w[i, n] + b*(dt/(dx)**2)*(w[i+1, n] - 2*w[i, n] + w[i-1, n])
            

    return t, x, w