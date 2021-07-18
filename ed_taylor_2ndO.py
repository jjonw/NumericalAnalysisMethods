#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 21:31:46 2018

@author: jonw
f -> funcao
fp -> derivada da funcao
y0 -> valor inicial
[a, b] -> calculo dos valores
t -> se t < 1 entao h = t senao N = t
"""

def solveT2Order(f, fp, y0, a, b, t):
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
        vy[i] = vy[i-1] + h*f(vx[i-1], vy[i-1]) + h*h/2 * fp(vx[i-1], vy[i-1])
        
    return vx, vy

