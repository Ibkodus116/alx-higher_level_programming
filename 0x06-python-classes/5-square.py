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
            self.__size = size

    def area(self):
        """Public instance method:
        that returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #
            But if size is equal to 0, it prints an empty line
        """
        num = 0
        if self.__size == 0:
            print()
        while num < self.__size:
            print("#" * self.__size)
            num += 1

    @property
    def size(self):
        """The property getter to retrieve size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """The property setter to set size
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
