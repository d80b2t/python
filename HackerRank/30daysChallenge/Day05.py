'''
Objective: 
In this challenge, we are going to use loops to help us do some simple math. Check out the Tutorial tab to learn more.

Task 
Given an integer, , print its first  multiples. Each multiple  (where ) should be printed on a new line in the form: N x i = result.
'''
import sys

N = int(input().strip())

for ii in range(1, 11):
    print (N,'x', ii ,'=', N*ii)

    
