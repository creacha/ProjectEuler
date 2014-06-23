'''

'''
import time
import math
tStart = time.clock()

cutOff = 2000000
tfList = cutOff * [True]
index = 2
k = 0


for i in range(2,math.ceil(math.sqrt(cutOff))):
    if tfList[i-1] == True:       
        while index <= cutOff:  
            tfList[index-1] = False
            index = int(math.pow(i,2) + k*i)
            k += 1
        index = 2 
        k = 0
for i in range(len(tfList)):
    if tfList[i] == True:
        print(i+1)

tEnd = time.clock()

print(tEnd - tStart)

