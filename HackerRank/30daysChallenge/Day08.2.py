'''
Objective 
Today, we are learning about Key-Value pair mappings using a Map or Dictionary data structure. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Given N names and phone numbers, assemble a phone book that maps friends names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for; for each name queried, print the associated entry from your phone book (in the form ) or  if there is no entry for .

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

Sample Input:
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
'''

import sys 

# Read input and assemble Phone Book
n = int(input())
phoneBook = {}
for i in range(n):
    contact = input().split(' ')
    phoneBook[contact[0]] = contact[1]

# Process Queries
lines = sys.stdin.readlines()
for i in lines:
    name = i.strip()
    if name in phoneBook:
        print(name + '=' + str( phoneBook[name] ))
    else:
        print('Not found')
