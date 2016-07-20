
#Task 
#Read two integers from STDIN and print three lines where:
#
#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.

# Enter your code here. Read input from STDIN. Print output to STDOUT

# read a line from STDIN
# a = raw_input()
a=int(input())
b=int(input())

## NPR note, you want this
##  int(input())
## command here and not the 'raw_input()' from before...

## In a one-er... 
##  a=int(input()) b=int(input()) print("{0}\n{1}\n{2}".format(a+b,a-b,a*b))

print a+b
print a-b
print a*b
