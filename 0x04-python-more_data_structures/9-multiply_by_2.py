#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    t = sorted(a_dictionary)
    for i in range(len(t)):
        a_dictionary[t[i]] = int(a_dictionary[t[i]]) * 2
    return(a_dictionary)
