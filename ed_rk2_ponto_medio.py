#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solvePM(f, y0, a, b, t):
    if(t < 1): 
        h = t
        N = int((b-a)/h)
    elif(t > 1 or t == 1):
        h = (b-a)/float(t)
        N = t
        
    vx = [0 for i in range(0, N+1)]
    vy = [0 for i in range(0, N+1)]
    vx[0] = a
    vy[0] = y0
    
    for i in range(1, N+1):
        vx[i] = a + i*h
        vy[i] = vy[i-1] + h * f(vx[i-1] + h/2, vy[i-1] + (h/2)*f(vx[i-1], vy[i-1]))
    
    return vx, vy