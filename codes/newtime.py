import time

t = time.clock()
for n in range(50000):
    c =n

t2 = time.clock()
print(t,t2)
t3 = t2 - t
print(t3)