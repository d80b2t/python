'''
Sample Challenge:: 
This is a simple challenge to get things started. Given a sorted array () and a number (), can you print the index location of  in the array?
'''

v = int(eval(input()))
n = int(eval(input()))

for a0 in range(n):
        a = list(map(int,input().strip().split(' ')))
        
for index, item in enumerate(a, start=0):
    if item == v:
        print(index)
      
