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
CANDIDATENUM = 41
x = CANDIDATENUM

#candidate number will be scanned a maximum of self times.
for i in range(1, x):
    print(i)
    #if i is a factor of the candidate number
    if x % i == 0 and i != 1:
        print("factor found")
        if len(listOfPrimes) == 0:
            print("length of list was zero")
            listOfPrimes.append(i)
            print("first factor added")
            print(listOfPrimes)
            x //= i
            print("divided x by first factor")
            print(x)
            i += 1
            print("incremented from first factor if")
            print(i)
        elif len(listOfPrimes) != 0:
            print("length of list was longer than zero")
            for scanner in range(0, len(listOfPrimes)):
                print("began scanning list")
                print(scanner)
                print(i)
                print(listOfPrimes[scanner])
                #I'm convinced there's no 'returning' to 2. WHILE x is divisible by 2, continue to divide by 2 then increment.
                while i % listOfPrimes[scanner] == 0:
                    print("found a factor of list member")
                    i //= listOfPrimes[scanner]
                    x //= listOfPrimes[scanner]
                    print("divided x by list member")
            print("finished scanning list")
            #experimenting...
            if i != 1:
                listOfPrimes.append(i)
            print("another factor added")
            print(listOfPrimes)
            i += 1
            print("incremented from first elif")
    if x == 1:
        print(listOfPrimes)
        break


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