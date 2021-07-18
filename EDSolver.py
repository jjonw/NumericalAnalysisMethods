# -*- coding: utf-8 -*-
"""
Created on Mon May 21 10:50:06 2018

@author: Jonata
"""
import matplotlib.pyplot as plt

def solveEuler(f, y0, a, b, t):
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
        vy[i] = vy[i-1] + h*f(vx[i-1], vy[i-1])

    return vx, vy
    

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


def solveT2Order(f, fp, y0, a, b, t):
    if(t < 1): 
        h = t
        N = int((b-a)/h)
    elif(t > 1 or t == 1):
        h = (b-a)/float(t)
        N = t
        
    #fp = [0 for i in range(0, N+1)]
    vx = [0 for i in range(0, N+1)]
    vy = [0 for i in range(0, N+1)]
    vx[0] = a
    vy[0] = y0
    
    for i in range(1, N+1):
        # fp[i] = lambda x, y: ( f(x, y) - f(x - h, y) ) / h
        vx[i] = a + i*h
        vy[i] = vy[i-1] + h*f( vx[i-1], vy[i-1] ) + h*h/2 * fp( vx[i-1], vy[i-1] )
        
    return vx, vy


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

def calcSol(f, y0, a, b, t):
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
        vx[i] = a + i*h
        vy[i] = f(vx[i])
        
    return vx, vy

def calcErro(vxMet, vyMet, vx, vy):
    dy = [0 for i in range(0, len(vy))]
    for i in range(0, len(vy)):
        dy[i] = abs(vy[i] - vyMet[i])
        
    return dy

def saveFigure(vx, vy, figName, textTitle):
    fig, ax = plt.subplots()
    fig = plt.figure(figsize=(100, 100))
    ax.plot(vx, vy)
    ax.set_title(textTitle)
    ax.set_xlabel('t')
    ax.set_ylabel('y(t)')
    fig.savefig(figName)