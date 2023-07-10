#!/usr/bin/python3
"""
Function that adds a new attribute to an object
"""


def add_attribute(obj, name, value):
    """
    Args:
        obj: object
        name: attribute name
        value: attribute value

    Raises:
        TypeError: when the attribute can't be added

    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
