import time

tStart = time.clock()

palindromes = []

for j in range(100,1000):

    for i in range(100,1000):
        
        palinCheck = j * i
    
        if palinCheck - 100000 > 0:
               
            copyTest = palinCheck
            
            digit1 = palinCheck//100000
            copyTest -= digit1*100000
            digit2 = copyTest//10000
            copyTest -= digit2*10000
            digit3 = copyTest//1000
            copyTest -= digit3*1000
            digit4 = copyTest//100
            copyTest -= digit4*100
            digit5 = copyTest//10
            copyTest -= digit5*10
            digit6 = copyTest//1
            
            if digit1 == digit6 and digit2 == digit5 and digit3 == digit4:
                palindromes.append(palinCheck)
                
palindromes.sort(key=None, reverse=True) 
print(palindromes[0])
tEnd = time.clock()
print(tEnd - tStart)

