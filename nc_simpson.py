#!/usr/bin/python3
## Using mean point as 3rd one.
## + add input from command line as argv

import math

f = lambda x: 1.0/x

x0 = 5.0
x2 = 8.0
x1 = (x2 + x0)/2
h = x2 - x1

integral_f = h * ((f(x0) + 4 * f(x1) + f(x2)) / 3)

print(x1)
print(h)
print("Integral por Simpson = ", integral_f)
