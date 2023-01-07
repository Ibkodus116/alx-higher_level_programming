#!/usr/bin/python3
"""

Module containing a function that add two number

"""


def add_integer(a, b=98):
    """Function adding two numbers
    Args:
        a: First Number
        b: second Number

    Return:
        Returns the sum of arg1 and arg2

    Raises:
        TypeError: stating that a or b must be and intiger or float

    """

    if isinstance(a, int) or isinstance(a, float):
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, int) or isinstance(b, float):
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return a + b
