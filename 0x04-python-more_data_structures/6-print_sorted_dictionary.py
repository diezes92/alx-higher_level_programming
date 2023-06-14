#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    t = sorted(a_dictionary)
    for i in range(len(t)):
        print("{}: {}".format(t[i], a_dictionary[t[i]]))
