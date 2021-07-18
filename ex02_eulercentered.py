#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 01:46:06 2018

@author: jonw
"""
from math import pi,sin,e

def solve():
    f = lambda t: 1
    g = lambda x: 1 + sin(3*pi*x)
    
    a = 1/10
    dx = 1/20
    dt = 1/4
    
    ti = xi = 0
    tf = 2
    xf = 1
    
    pt = round((tf - ti)/dt)
    px = round((xf - xi)/dx)
    vt = [0 for i in range(0, pt)]
    vx = [0 for i in range(0, px)]
    vw = [[0 for j in range(0, pt)] for i in range(0, px)]
    
    vt[0] = ti
    vx[0] = xi
    
    for i in range(1, px-1):
        vw[i][0] = g(vx[i])
        vx[i] = vx[i-1] + dx
        for j in range(1, pt):
            vw[0][j] = 1
            vt[j] = vt[j-1] + dt
            
            vw[i+1][j] = vw[i][j] - a*dt/dx*(vw[i][j] - vw[i][j-1])
            print(i, j)
            
    return vt,vx,vw