'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
import sys
import time

tStart = time.clock()

i = 20
while True:
    
    for j in range(1,21):
        
        if i % j != 0:
            break
        if j == 20:
            print(i)
            tEnd = time.clock()
            print(tEnd - tStart)
            sys.exit()
    i += 20