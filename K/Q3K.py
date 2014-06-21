'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from EulerMethods import EulerMethodsClass
import math
import time

#targetNumber = 600851475143;
tStart = time.clock()

primes = [3]

targetNumber = 600 #475143
i = 3

while i < math.ceil(targetNumber/2)+1:

    for j in primes:       
        if i % j == 0:
            break
        if j == primes[-1]:
            primes.append(i)
    i += 2;

primes.sort(key=None, reverse=True)               
for k in primes:
    if targetNumber % k == 0:
        print(k)
        break      
      
tEnd = time.clock()

print(tEnd - tStart)