#!/bin/python3

'''
Objective:: Today, we are building on our knowledge of Arrays by adding another dimension. Check out the Tutorial tab for learning materials and an instructional video!

Context 
Given a 6x6 2D Array, A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in A to be a subset of values with indices falling in this pattern in As graphical representation:

a b c
  d
e f g

There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass'' values.

Task::  
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

Sample Input::
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output::
19
'''

import sys

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

res = []
for x in range(0, 4):
    for y in range(0, 4):
        print(x,y)
        print('arr[x][y:y+3]',   arr[x][y:y+3])
        print('arr[x+1][y+1]',   arr[x+1][y+1])
        print('arr[x+2][y:y+3]', arr[x+2][y:y+3])
        s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
        res.append(s)

print(max(res))

