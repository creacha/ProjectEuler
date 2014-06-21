'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
def sum35below1000():
    sum35 = 0
    for i in range (1,1000):
        if i % 5 == 0 or i % 3 == 0:
            sum35 = sum35 + i
    return sum35
     
print(sum35below1000())
 