'''
Task

Initialize your list (L = []) and follow the N commands given over N lines.

Each command will be 1 of the 8 commands given above:
The extend(L) method will not be used.

Each command will have its own value(s) separated by a space.

Sample Input::
12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print

'''


n = eval(input())
l = []

for _ in range(n):
    s = input().split()
    ## In [53]: s = raw_input().split()
    ##          insert 0 5
    ## In [54]: s
    ## Out[54]: ['insert', '0', '5']
    cmd = s[0]
    args = s[1:]
    
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        ## this takes e.g.
        ## 'insert' and adds ( args[0] , args[1] )
        
        eval("l."+cmd)
        ## this performs the operation of what's inside the ()
        ## and as such, basically operates on l 
    else:
        print(l)

## https://www.hackerrank.com/challenges/python-lists/tutorial

# 1.) append(x)


