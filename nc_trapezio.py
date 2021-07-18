#!/usr/bin/python3
import math

f = lambda x: math.log(x)
x0 = 5
x1 = 6
h  = x1 - x0

integral_f = h * ( (f(x0) + f(x1))) / 2

print("Resultado integral = ", integral_f)

