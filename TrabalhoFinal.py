# -*- coding: utf-8 -*-
import numpy as np
from math import sin,cos,e,pi
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


def solveDirichlet():
    dx   = 1/10
    dy   = 1/10
    #dt = 0.05*((dx**2 + dy**2)/(dx**2*dy**2))
    dt   = 0.5*(1/(1/dx**2 + 1/dy**2))

    tmax = 1
    xmax = 1
    ymax = 1
    
    t = np.arange(0, tmax + dt, dt)
    x = np.arange(0, xmax + dx, dx)
    y = np.arange(0, ymax + dy, dy)
    tl = len(t)
    xl = len(x)
    yl = len(y)
    
    w = np.zeros((tl, xl, yl))

    for n in range(0, tl):   
        for i in range(0, xl):            
            for j in range(0, yl):
                w[0, i, j] = cos(x[i]) + sin(y[j])
                w[n, i, 0] = cos(x[i])/e**(t[n])
                w[n, i, 1] = ( cos(x[i]) + sin(1) )/e**(t[n])
                w[n, 0, j] = ( 1 + sin(y[j]) )/e**(t[n])
                w[n, 1, j] = ( cos(1) + sin(y[j]) )/e**(t[n])
            
                
    for n in range(1, tl-1):
        for i in range(1, xl-1):    
            for j in range(1, yl-1):
                w[n+1, i, j] = w[n, i, j] \
                + (dt/(dx)**2)*( w[n, i+1, j] - 2*w[n, i, j] + w[n, i-1, j] ) \
                + (dt/(dy)**2)*( w[n, i, j+1] - 2*w[n, i, j] + w[n, i, j-1] )
                
    return t, x, y, w


def solveAnalitical():
    dx   = 1/10
    dy   = 1/10
    dt   = 0.05*(1/(1/dx**2 + 1/dy**2))

    tmax = 1
    xmax = 1
    ymax = 1
    
    ta = np.arange(0, tmax + dt, dt)
    xa = np.arange(0, xmax + dx, dx)
    ya = np.arange(0, ymax + dy, dy)
    tl = len(ta)
    xl = len(xa)
    yl = len(ya)
    print(tl);print(xl);print(yl)
    
    w = np.zeros((tl, xl, yl))
    
    for n in range(0, tl):
        for i in range(0, xl):
            for j in range(0, yl):
                w[n, i, j] = ( cos( xa[i] ) + sin( ya[j] ) )/(e**( ta[n] ))

    return ta, xa, ya, w

def plot3D(t, x, y, w, time):
    #fig = plt.figure()
    #ax = plt.axes(projection='3d')
    #ax.set_xlabel('$X$', fontsize=20)
    #ax.set_ylabel('$Y$')
    #ax.yaxis._axinfo['label']['space_factor'] = 3.0
    vx, vy = np.meshgrid(x, y)
    #vx = list(vx)
    #vy = list(vy)
    plt.pcolor(vx, vy, w[time, :, :])
    
    plt.show()