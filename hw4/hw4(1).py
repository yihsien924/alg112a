from numpy import arange
import math

def f(x) :
    return x * x - 3 * x + 1

for x in arange(-100, 100, 0.001):
    if abs(f(x)) < 0.001:                #abs為絕對值
        print("x=", x, " f(x)=", f(x)) 