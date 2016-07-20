#!/bin/python


# Task 
# Given an integer, , perform the following conditional actions:
#If  is odd, print Weird
#If  is even and in the inclusive range of 2 to 5, print Not Weird
#If  is even and in the inclusive range of 6 to 20, print Weird
#If  is even and greater than 20, print Not Weird

import sys

N = int(raw_input().strip())


# http://www.tutorialspoint.com/python/python_if_else.htm
if (N%2 == 0 and (N > 20 or N in range(2, 6))):
    print 'Not Weird'
else:
    print 'Weird'
