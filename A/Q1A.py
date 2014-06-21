__author__ = 'LOVER'

"""
written in Python 3.4.
First problem, good look back at python. First had a go at basic command line stuff a few years ago.
"""

a = 0

# Reminder for loop sytax: all based on colons and indentation.
while a < 1000:
    if a % 3 == 0 or a % 5 == 0:
        print(a)
    # Got errors trying to increment using a++, a = a++ etc.
    a += 1
    
'''
Old boy comments:
Use of while loop good, conciser than for loop in this case
Actually I changed my mind, for loop conciser as ya don't have to increment manually
Prints all the multiples of 3 and 5 but doesn't sum them
'''