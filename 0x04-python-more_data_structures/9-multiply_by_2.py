#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    t = list(a_dictionary.keys())
    for i in range(len(t)):
        a_dictionary[t[i]] = a_dictionary[t[i]] * 2
    return(a_dictionary)
