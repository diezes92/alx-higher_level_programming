#!/usr/bin/python3
""" Module that contains a function that returns the number of lines
    of a text file
"""


def number_of_lines(filename=""):
    """ Function that reads from a file and prints its number of lines

    Args:
        filename: filename

    Raises
        Exception: when the file can be opened

    """
    nb = 0
    with open(filename, 'r', encoding="utf-8") as fl:
        for li in fl:
            nb += 1
    return nb
