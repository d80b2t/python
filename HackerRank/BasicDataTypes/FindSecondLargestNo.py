'''
You are given N numbers. Store them in a list and find the second largest number.

Input Format:
The first line contains N. The second line contains an array A[] of N integers each separated by a space.

Sample Input:
5
2 3 6 6 5
'''

i = int(eval(input()))

lis = list(map(int,input().strip().split()))[:i]
z = max(lis)

while max(lis) == z:
    print((z, max(lis)))
    ##
    lis.remove(max(lis))

print((max(lis)))
