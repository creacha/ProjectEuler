'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import time
import math
tStart = time.clock()
stop = False

for i in range(1,500):
    if stop:
        break
    for j in range(1,500):
        if stop:
            break
        for k in range(1,500):
            if i + j + k == 1000:
                if i < j < k:
                    if math.pow(i, 2) + math.pow(j, 2) == math.pow(k, 2):
                        print(i,j,k)
                        print(i*j*k)
                        stop = True

     
tEnd = time.clock()

print(tEnd - tStart)