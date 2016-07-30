'''
Objective::
Today, we are working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

Task:: Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-1- integer denoting the maximum number of consecutive 1''s in n''s binary representation.
'''

## http://stackoverflow.com/questions/3528146/convert-decimal-to-binary-in-python
## Code to work/return binary Nos. 
def dec_to_bin(x):
    return int(bin(x)[2:])
"{0:b}".format(int)

n = int(input('enter a number: '))
print '{0:b}'.format(n)


bin(11111113)
# '0b101010011000101011001001'

bin(11111113)[2:]
# '101010011000101011001001'

bin(11111113)[2:].split()
# ['101010011000101011001001']

bin(11111113)[2:].split('0')
# ['1', '1', '1', '', '11', '', '', '1', '1', '11', '', '1', '', '1']

max(bin(11111113)[2:].split('0'))
# '11'

#len(max(bin(11111113)[2:].split('0')))


print(len(max(              bin(int(input().strip()))[2:].split('0'))))
print(len(max(re.split("0+",bin(int(input().strip()))[2:])))) 

## X = 633825300114114700748351602687


'''
For sake of explanation im going to replace input() with 13 and break the code down.

1- int(input().strip()) ==> int(13.strip()) takes the input of the number and strips any spaces on either side, then converts it from a string to an interger. the result is the interger 13.

2- bin(13)[2:].split('0') ==> the bin() method takes a number and converts it to binary. in this case when you enter bin(13) it returns '0b1101'. the [2:] allows us to omit the '0b' at the beginning of the string. which leaves us with '1101'.split('0'). This string method takes 1101 and splits it into a list. We end up with ['11','1'].

3-len(max(['11','1'])) ==> the max() method is simply going to look for the biggest value. In this case the biggest one is '11'. '11' is passed to the len() method which just returns the length of the object in it. In this case the object is the string '11' which has two characters, so len('11') returns 2. Which in turn is also the longest consecutive amount of ones.

'''
