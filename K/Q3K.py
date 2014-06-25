'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import time
import math
tStart = time.clock()
#a list of the prime factors for the candidate number
cutOff = math.ceil(math.sqrt(600851475143))
tfList = cutOff * [True]
index = 1
k = 0

for i in range(2,cutOff//2):
    if tfList[i-1] == True:       
        while index <= cutOff:  
            tfList[index-1] = False
            index = int(math.pow(i,2) + k*i)
            k += 1
        index = 1
        k = 0

processing = True
CANDIDATENUM = 600851475143
x = CANDIDATENUM
divisorList = []
k = 0

while processing:
    k += 1
    if tfList[k-1] == True:
        if x % k == 0:
            divisorList.append(k)
            x /= k
            k = 1
        if x == 1.0:
            print(divisorList[-1])
            processing = False

tEnd = time.clock()

print(tEnd - tStart)

"""
http://www.khanacademy.org/math/pre-algebra/factors-multiples/prime_factorization/v/prime-factorization

it was a visual thing!

600851475143
    /   \
  71  8462696833
          /   \
         839  10086647
                /  \
              1471 6857

you're only ever iterating through the (rapidly-shrinking) right hand side.
"""