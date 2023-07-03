#!/usr/bin/python3
"""

This module is composed by a function that adds two numbers

"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first integer or float.
        b (int or float, optional): The second integer.

    Returns:
        int: The addition of a and b, casted to an integer.

    Raises:
        TypeError: If a or b is not an integer or float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
