#!/usr/bin/python3
"""

Module composed by a function that multiplies 2 matrices

"""


def matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication

    Raises:
        TypeError: if m_a or m_b aren't a list
        TypeError: if m_a or m_b aren't a list of a lists
        ValueError: if m_a or m_b are empty
        TypeError: if the lists of m_a or m_b don't have integers or floats
        TypeError: if the rows of m_a or m_b don't have the same size
        ValueError: if m_a and m_b can't be multiplied


    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for itm in m_a:
        if not isinstance(itm, list):
            raise TypeError("m_a must be a list of lists")

    for itm in m_b:
        if not isinstance(itm, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for lists in m_a:
        for itm in lists:
            if not type(itm) in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for lists in m_b:
        for itm in lists:
            if not type(itm) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    lgt = 0

    for itm in m_a:
        if lgt != 0 and lgt != len(elems):
            raise TypeError("each row of m_a must be of the same size")
        lgt = len(itm)

    lgt = 0

    for itm in m_b:
        if lgt != 0 and lgt != len(itm):
            raise TypeError("each row of m_b must be of the same size")
        lgt = len(itm)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    r1 = []
    i1 = 0

    for a in m_a:
        r2 = []
        i2 = 0
        num = 0
        while (i2 < len(m_b[0])):
            num += a[i1] * m_b[i1][i2]
            if i1 == len(m_b) - 1:
                i1 = 0
                i2 += 1
                r2.append(num)
                num = 0
            else:
                i1 += 1
        r1.append(r2)

    return r1
