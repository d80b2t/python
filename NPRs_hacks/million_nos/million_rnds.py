'''

Just a wee bit of code that I want to hack together to produce a
list of a million, non-repeating numbers, randomly sorted.

Will be good to use for e.g. comparing runtimes for various SORT algorithms (!!) 

Useful links::
http://stackoverflow.com/questions/9755538/how-do-i-create-a-list-of-unique-random-numbers
http://stackoverflow.com/questions/21744963/how-to-generate-a-range-of-random-numbers-in-python-without-repetition
http://stackoverflow.com/questions/22842289/python-generate-n-unique-random-numbers-within-a-range

http://learnpythonthehardway.org/book/ex16.html

'''
import random

size = 1000#000
lis = random.sample(range(size), size)

outfile = open('temp.dat', 'w')

for i in range(len(lis)):
    outfile.write(str(lis[i])+'\n')
    
outfile.close()
