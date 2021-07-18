#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 20:26:44 2018

@author: jonw
"""

def solveRK4(f, y0, a, b, t):
    if(t < 1): 
        h = t
        N = int((b-a)/h)
    elif(t > 1 or t == 1):
        h = (b-a)/float(t)
        N = t
        

    vx = [0 for i in range(0, N+1)]
    vy = [0 for i in range(0, N+1)]
    vx[0] = a;
    vy[0] = y0;
    
    for i in range(1, N+1):
        k1 = f(vx[i-1], vy[i-1])
        k2 = f(vx[i-1] + h/2, vy[i-1] + (1/2)*h*k1)
        k3 = f(vx[i-1] + h/2, vy[i-1] + (1/2)*h*k2)
        k4 = f(vx[i-1] + h,   vy[i-1] + h*k3)
        vx[i] = a + i*h
        vy[i] = vy[i-1] + (h/6)*(k1 + 2*k2 + 2*k3 + k4) 
        
    return vx, vy

        