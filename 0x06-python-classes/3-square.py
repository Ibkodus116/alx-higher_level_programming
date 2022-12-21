#!/usr/bin/python3
"""Class Square that defines a square by: (based on 1-square.py).
"""


class Square:
    """Class Square that defines a square by: (based on 1-square.py).

    the __init__ is to initialise our Square class

    args:
        size (int): the size of the square
    """
    def __init__(self, size=0):

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """Public instance method:
        that returns the current square area
        """
        return self.__size ** 2
