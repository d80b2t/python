'''
Task

Initialize your list (L = []) and follow the N commands given over N lines.

Each command will be 1 of the 8 commands given above:
The extend(L) method will not be used.


arr = [1,2,3]

1.) append(x)
Adds a single element x to the end of a list.
  arr.append(9)   
  print arr  
  # prints [1, 2, 3, 9]
  
2.) extend(L)
Merges another list L to the end.
  arr.extend([10,11])
  print arr
  # prints [1, 2, 3, 9, 10, 11]
  
3.) insert(i,x) 
Inserts element x at position i.
  arr.insert(3,7)
  print arr
  # prints [1, 2, 3, 7, 9, 10, 11]
  
4.) remove(x) 
Removes the first occurrence of element x.
  arr.remove(10)  
  arr  
  # prints [1, 2, 3, 7, 9, 11]
  
5.) pop() 
Removes the last element of a list. If an argument is passed, that index item is popped out.
  temp = arr.pop()
  print temp 
  # prints 11
  
6.) index(x) 
Returns the first index of a value in the list. Throws an error if it is not found.
  temp = arr.index(3)
  print temp
  # prints 2

7.) count(x)
Counts the number of occurrences of an element x.
  temp = arr.count(1)
  print temp
  # prints 1
  
8.) sort() 
Sorts the list.
  arr.sort()
  print arr
  # [1, 2, 3, 7, 9]
  
9.) reverse() 
Reverses the list.
  arr.reverse()
  print arr
  # [9, 7, 3, 2, 1]

Each command will have its own value(s) separated by a space.

'''


## https://www.hackerrank.com/challenges/python-lists/tutorial

# 1.) append(x)


