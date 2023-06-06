#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    test = test = number % 10
else:
    test = number % -10
print("Last digit of {} is {} and is ".format(number, test), end='')
if test > 5:
    print("greater than 5")
elif test < 6 and test != 0:
    print("less than 6 and not 0")
elif test == 0:
    print("0")
