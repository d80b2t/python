'''
Baby code for how to do a if..elif..else codechunk
'''

N = int(input().strip())
condition = 'Not Weird' 

if N % 2 !=  0:
    condition = 'Weird'
elif N % 2 ==  0 and (N >= 6 and N <= 20):
    condition = 'Weird'
else:
    condition = 'Not Weird' 

print(condition)        
