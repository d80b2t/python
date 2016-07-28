'''

http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html

'''

import timeit


def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


## http://pythoncentral.io/time-a-python-function/
#def wrapper(func, *args, **kwargs):
#    def wrapped():
#        return func(*args, **kwargs)
#    return wrapped

#alist = [54,26,93,17,77,31,44,55,20]

#with open('million_nos.dat') as f:
with open('thousand_nos.dat') as f:
    lines = f.read().splitlines()

alist = lines
#timeit.timeit(bubbleSort(alist))
#timeit.Timer(bubbleSort(alist))
(bubbleSort(alist))


print(alist)
#print('Timed at...', t)
