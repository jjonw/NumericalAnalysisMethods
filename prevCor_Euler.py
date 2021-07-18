#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solvePrevCorrEuler(f, y0, a, b, t, rep):
    if(t < 1): 
        h = t
        N = int((b-a)/h)
    elif(t > 1 or t == 1):
        h = (b-a)/float(t)
        N = t
    
    vy_precor = [0 for i in range(0, rep+1)]
    vx = [0 for i in range(0, N+1)]
    vy = [0 for i in range(0, N+1)]
    vx[0] = a
    vy[0] = y0
    
    for i in range(1, N+1):
        vx[i] = a + i*h
        vy[i] = vy[i-1] + h*f(vx[i-1], vy[i-1])
        vy_precor[0] = vy[i-1] + h*f(vx[i], vy[i])
        
        for j in range(1, rep+1):
            vy_precor[j] = vy[i-1] + h*f(vx[i], vy_precor[j-1])
  
        vy[i] = vy_precor[rep]
        
    return vx, vy