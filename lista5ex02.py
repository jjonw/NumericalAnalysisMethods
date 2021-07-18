#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from math import sin,pi

def solveEx2():
    a    = 1/10
    dx   = 1/20
    # dt <= dx/a
    dt   = 0.1*(dx/a)
    tmax = 2
    xmax = 1
    
    t = np.arange(0, tmax + dt, dt)
    x = np.arange(0, xmax + dx, dx)
    tl = len(t)
    xl = len(x)
    w = np.zeros([xl, tl])
    
    for n in range(0, tl-1):
        w[0, n] = 1
    for i in range(1, xl-1):
        w[i, 0] = 1 + sin(3 * pi * x[i])

   # w[0, tl-1] = 1     # nao iniciliza no loop
   # se nao utilizar o meshgrid ocorre um erro para a ultima posicao do vetor
   # para que isso nao ocorra desconsiderar o ultimo
    for n in range(0, tl-1):
        #w[0, n] = 1
        for i in range(1, xl-1):
           # w[i, 0] = 1 + sin(3 * pi * x[i])
            w[i, n+1] = w[i, n] - a*(dt/dx)*(w[i, n] - w[i-1, n])
            
    return t, x, w
