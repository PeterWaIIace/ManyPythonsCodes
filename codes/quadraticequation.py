#!/usr/bin/python3.6

import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
print("a = {}, b = {}, c = {}".format(a,b,c))
delta = b**2-4*a*c
x1, x2 = 0,0
sqrtdelta = delta**(1/2)
if b < 0:
    x2 = (-b + sqrtdelta) /(2*a)
    x1 = c/(x2*a)
else:
    x1 = (-b - sqrtdelta) /(2*a)
    x2 = c/(x1*a)

print("Quadratic equation roots:\nx1={} \nx2={}".format(x1,x2))