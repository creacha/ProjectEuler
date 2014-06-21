'''
Created on 21/06/2014

@author: Karl
'''

class EulerMethodsClass(object):
    
    def isPrime(self, numberIn, primes):
        prime = True
        count = 1
        if numberIn in primes:
            return prime
        for i in range(2,10):       
            if numberIn % i == 0:
                prime = False
            else:
                primes[count] = numberIn
                
        return prime

    def __init__(self):
        '''
        Constructor
        '''
        