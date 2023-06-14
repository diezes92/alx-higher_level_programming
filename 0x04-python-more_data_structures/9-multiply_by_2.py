#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    t = list(a_dictionary.keys())
    new = a_dictionary.copy()
    for i in range(len(t)):
        new[t[i]] = a_dictionary[t[i]] * 2
    return(new)
