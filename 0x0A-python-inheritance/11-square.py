#!/usr/bin/python3

"""
Model inheriting from Rectangle Class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square (Rectangle):
    """
    a class Square that inherits from Rectangle (9-rectangle.py):
    """
    def __init__(self, size):
        """ Initialisation function
        """
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, self.__size, self.__size)
        self.area()

    def __str__(self):
        """
        Str function indicating what should be printed
        to the screen whwen this method is called
        """
        return f"[{Square.__name__}] {self.__size}/{self.__size}"
