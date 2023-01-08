#!/usr/bin/python3

"""

Module containing a function the prints a square with the character '#'

"""


def print_square(size):
    """A function that prints a square with the character '#'
    Arg:
        size: the size of our intended square

    Print:
        A square representing it with '#'

    Raise:
        TypeError: when the type of size provided isn't intigers
        ValueError: when the size given is less than 0

    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    square = ""
    if size != 0:
        for i in range(size):
            square += ("#" * size) + "\n"
        print(square[:-1])
    else:
        print()

