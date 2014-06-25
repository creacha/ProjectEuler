__author__ = 'LOVER'

'''
Couple things:
1. Ya don't need to increment i in ya loop, the loop will do it itself
2. You actually need to reset i to 2 each time you 'branch' the factor tree, to see why run it with 250 as candidate number
solution comes out as 25, because you've already passed 5 as a possible divisor by that point

3. Idea is fuckn awesome :)

'''

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
#a list of the prime factors for the candidate number
listOfPrimes = []
#also had it working fine with an int.
CANDIDATENUM = 600851475143
x = CANDIDATENUM

#candidate number will be scanned a maximum of self times. Cheated and skipped 1.
for i in range(2, x):
    #if i is a factor of the candidate number
    if x % i == 0:
        #it goes in the list of primes
        listOfPrimes.append(i)
        #candidate number is then made much smaller, just like a factor tree. I watched a video on khan academy lol.
        #you're never going to be dividing by a smaller number than the last factor you safely got out... (see after elif)
        x /= i
    #then when you get up to the largest prime x should divide out to 1.
    elif x == 1.0:
        print(listOfPrimes[-1])
        break
    #...so you can go ahead and increment.
    i += 1


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