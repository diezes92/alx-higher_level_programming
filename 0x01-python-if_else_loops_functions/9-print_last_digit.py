#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        test = number % 10
    else:
        test = number % -10
        test = test * -1
    print("{:d}".format(test), end='')
    return (test)
