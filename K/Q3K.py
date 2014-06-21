'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from EulerMethods import EulerMethodsClass
import math
import time

eMethods = EulerMethodsClass()

primeFactors = []

#targetNumber = 600851475143;
targetNumber = 13195
i = 1

tStart = time.clock()
while i < math.ceil(targetNumber/2):
    if targetNumber % i == 0:
        if eMethods.isPrime(i):
            print(i)
    i += 1
        
tEnd = time.clock()

print(tEnd - tStart)


        
        
 
