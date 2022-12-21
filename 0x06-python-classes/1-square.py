#!/usr/bin/python3
"""Class Square that defines a square by: (based on 0-square.py).
"""


class Square:
    """Class Square that defines a square by: (based on 0-square.py).

    the __init__ is to initialise our Square class

    args:
        size (int): the size of the square
    """
    def __init__(self, size) -> None:
        self.__size = size
