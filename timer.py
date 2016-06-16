#!/usr/bin/env python

from timeit import Timer
mydict = "d={"+",".join(["'%d':%d" % (i,i) for i in range(10000)])+"}"
iterations = 20000
key = "bambi"
t=Timer("if '%s' in d:\n\td['%s']+1" % (key,key), mydict)
print t.timeit(iterations)
t=Timer("try: d['%s']+1\nexcept KeyError: pass" % key, mydict)
print t.timeit(iterations)
