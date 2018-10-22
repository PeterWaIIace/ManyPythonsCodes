#!/usr/bin/python3.6

a = [1,2,12,4]
b = [2,4,2,8]
c =[]
for n in range(len(a)):
    c.append(a[n]*b[n])

print("Vectors product: {}".format(c))