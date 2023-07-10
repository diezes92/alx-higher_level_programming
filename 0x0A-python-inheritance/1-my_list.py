#!/usr/bin/python3
"""
Class that inherits the attributes references of class list
"""


class MyList(list):
    """

    Args:
        list: class list

    """

    def print_sorted(self):
        """ Method that prints the sorted list """
        l_sort = self.copy()
        l_sort.sort()
        print(l_sort)
