'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''
import time

tStart = time.clock()
i = 3

primes = [3]

# Length of primes + 2 because I have excluded the first two natural numbers (1 and 2)
while len(primes) + 2 <= 10001:

    for j in primes:       
        if i % j == 0:
            break
        if j == primes[-1]:
            primes.append(i)
    i += 2;

print(primes[-1])
tEnd = time.clock()
print(tEnd - tStart)