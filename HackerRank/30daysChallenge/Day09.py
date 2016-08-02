'''
Objective:: Today, we are learning and practicing an algorithmic concept called Recursion. Check out the Tutorial tab for learning materials and an instructional video!

Task:: Write a factorial function that takes a positive integer, N, as a parameter and prints the result of N! 

Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.

Input Format: A single integer, N (the argument to pass to factorial).

'''

#N = int(input())

#def factorial(n)

#for i in range(n):
    

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print((factorial  (int(eval(input())))))
