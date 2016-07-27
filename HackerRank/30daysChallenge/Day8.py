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

n = int(eval(input()))
name_numbers = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}

while True:
    try:
        name = eval(input())
        if name in phone_book:
            print(('%s=%s' % (name, phone_book[name])))
        else:
            print('Not found')
    except:
        break



