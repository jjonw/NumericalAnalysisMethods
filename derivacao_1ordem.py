#!/usr/bin/python3
import math

f  = lambda x: math.log(x)
f1 = lambda x: 1.0/x

x0 = 1.8;

n = int(input("Defina o expoente maximo: "))

for i in range(1, n):
    h = 0.1**i
    print("Derivada: ", f1(x0))
    f1_num = (f(x0 + h) - f(x0)) / h
    print("Derivada num: ", f1_num)
    erro_num = abs(f1(x0) - f1_num)
    print("Erro abs: ", erro_num)
    erro_est = (h/2) * 1/x0**2
    print("Erro estimado: ", erro_est)
    print(" ")

