#!/bin/python3

'''
Objective 
In this challenge, we are getting started with conditional statements. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Given an integer, , perform the following conditional actions:

If n  is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.

'''

import sys

N = int(input().strip())

condition = 'Not Weird' 

if N % 2 !=  0:
    condition = 'Weird'
elif N % 2 ==  0 and (N >= 6 and N <= 20):
    condition = 'Weird'
else:
    condition = 'Not Weird' 

print(condition)        

    
