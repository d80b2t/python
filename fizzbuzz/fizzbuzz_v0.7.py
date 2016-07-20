## http://codereview.stackexchange.com/questions/9751/ultra-beginner-python-fizzbuzz-am-i-missing-something
count = 0
while (count < 101):
    if (count % 5) == 0 and (count % 3) == 0:
        print "FizzBuzz"
        count = count +1
    elif (count % 3) == 0:
        print "Fizz"
        count = count + 1
    elif (count % 5) == 0:
        print "Buzz"
        count = count +1
    else:
        print count
        count = count + 1
