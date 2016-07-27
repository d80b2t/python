'''
Objective:
Today we are expanding our knowledge of Strings and combining it with what we have already learned about loops. Check out the Tutorial tab for learning materials and an instructional video!

Task:
Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Sample Input:
2
Hacker
Rank

Sample Output:
Hce akr
Rn ak
'''

#S= eval(input())

for i in range(int(eval(input()))):
    s=eval(input())
    print((*["".join(s[::2]),"".join(s[1::2])]))

#for i in range(int(input())): s=input(); print("".join(s[::2]),"".join(s[1::2]))
