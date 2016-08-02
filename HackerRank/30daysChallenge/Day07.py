#!/bin/python3

'''
Objective
Today, we are learning about the Array data structure. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Given an array, A, of N integers, print A''s elements in reverse order as a single line of space-separated numbers.

http://docs.scipy.org/doc/numpy/reference/routines.array-manipulation.html
http://www.scipy-lectures.org/intro/numpy/numpy.html
'''

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

# print(arr[::-1])
print(" ".join(map(str, arr[::-1])))

#for _ in range(n):
    
