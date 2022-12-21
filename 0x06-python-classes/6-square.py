#!/usr/bin/python3
"""Class Square that defines a square by: (based on 1-square.py).
"""


class Square:
    """Class Square that defines a square by: (based on 1-square.py).

    the __init__ is to initialise our Square class

    args:
        size (int): the size of the square
    """
    def __init__(self, size=0, position=(0, 0)):

        self.__position = position

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """The property getter to retrieve size
        """
        return self.__size

    @property
    def position(self):
        """The property getter to retrieve position
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """The property setter to set Position
        """

        if type(value) is tuple:
            if len(value) == 2:
                if type(value[0]) is int and type(value[1]) is int:
                    if value[0] > 0 or value[1] > 0:
                        self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
        zero = self.__position[0]
        one = self.__position[1]
        box = "#" * self.__size
        space = " " * zero
        if self.__size == 0:
            print()
        while num < self.__size:
            # if one > 0:
            #     print(box)
            # else:
            print(space+box)
            num += 1
