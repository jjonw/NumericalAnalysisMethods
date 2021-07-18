#!/usr/bin/python3
import math

# Define the function
f = lambda x : x*math.log(x)

a = 1.0   # from 
b = 2.0   # to
n = 4     # number of points -1
h = (b - a) / n
odd_sum  = 0.0
even_sum = 0.0
    
# Summing the f(x_{2j}), ie the even j numbers
for j in range(2, n-1, 2):
    even_sum += f(a + j*h)

# Summing the f(x_{2j - 1}), ie the odd j numbers
for j in range(1, n, 2):
    odd_sum += f(a + j*h)
    
integral = (h/3)*(f(a) + 2*even_sum + 4*odd_sum + f(b))

print("Integral = ", integral)
