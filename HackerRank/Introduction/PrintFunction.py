'''
   Task:
   Read an integer N.
   Without using any string methods, try to print the following:
      123...N
   Note that ... represents the values in between.
'''

#
# from __future__ import print_function
# N = int(raw_input())
# for i in range(1, N+1):
#    print(i, end="")


# in one line...
print "".join([str(i+1) for i in range(input())])

print (''.join(str(e) for e in map(None,range(1,int(raw_input())+1))))

# l=range(5)
# print l
# ''.join(str(i) for i in l)


'''
 map(function, iterable, ...)
Apply function to every item of iterable and return a list of the results. If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. If one iterable is shorter than another it is assumed to be extended with None items. If function is None, the identity function is assumed; if there are multiple arguments, map() returns a list consisting of tuples containing the corresponding items from all iterables (a kind of transpose operation). The iterable arguments may be a sequence or any iterable object; the result is always a list.
'''


'''
 print(*range(1, int(input())+1), sep='')
 # Pretty sure the '*', aka identifier, is a Python 3 thing...
 # See:
 # https://docs.python.org/3/reference/expressions.html
'''


