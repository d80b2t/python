"""
Objective:: Today we're discussing scope. Check out the Tutorial tab for learning materials and an instructional video!

The absolute difference between two integers, a and b, is written as |a-b|. The maximum absolute difference between two integers in a set of positive integers, elements, is the largest absolute difference between any two integers in elements.

The Difference class is started for you in the editor. It has a private integer array (elements) for storing N non-negative integers, and a public integer (maximumDifference) for storing the maximum absolute difference.

Task:: Complete the Difference class by writing the following:
-- A class constructor that takes an array of integers as a parameter and saves it to the  instance variable.

-- A computeDifference method that finds the maximum absolute difference between any  numbers in  and stores it in the  instance variable.

Input Format:: You are not responsible for reading any input from stdin. The locked Solution class in your editor reads in 2 lines of input; the first line contains N, and the second line describes the elements array.

Sample Input::
3
1 2 5

Sample Output::
4
"""
class Difference:
    def __init__(self, a):
        self.__elements = a
        
"""
Your constructor must save the argument passed as its integer array parameter to the integer array instance variable (). 

The computeDifference method must then access the the integer array instance variable () and find its maximum and minimum elements. Once these are found, the method must save their absolute difference to the  instance variable. 

Note: The use of Math.abs is not really necessary. Because the problem constraints stipulate that we are only dealing with positive numbers,  will always be positive. 
"""
# Add your code here
self.maximumDifference = 0        
    def computeDifference(self):
        self.maximumDifference = (max(a)-min(a))

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

