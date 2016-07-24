#!/usr/bin/python3

from collections import deque

class test:
    
    def do_someting(self,value):
        print(value)
        return value

    def fun1(self):
        #map(self.do_someting,range(10))
        list(map(self.do_someting,range(10)))
        deque(map(self.do_someting, range(10)))
   
if __name__=="__main__":
    t = test()
    t.fun1()

#deque(map(self.do_someting, range(10)))

for i in range(10):
    self.do_someting(i)
