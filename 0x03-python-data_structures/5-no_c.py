#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for ch in my_string:
        if ch != 'C' and ch != 'c':
            new += ch
    return(new)
