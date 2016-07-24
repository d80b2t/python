'''

Task: 
Given an integer, n, and n space-separated integers as input, create a
tuple, t, of those n integers. Then compute and print the result of
hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

N.B. ALL IN PYTHON 3 NOW!!!!

'''

input()
print (hash(tuple(map(int,input().strip().split()))))

## Alternative: 
#print(       input()==0 or hash(tuple(map(int,input().strip().split()))))

## It checks if the first input is zero, then if not, it looks for
## input again, takes away the whitespace, and splits the string, then
## iterates over the list, turning all of the items into integers. It
## then turns that list into a tuple, hashes it, and prints it.




