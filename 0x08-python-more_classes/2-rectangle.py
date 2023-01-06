#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by: (based on 1-rectangle.py)

"""


class Rectangle:
    """
    Class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        the intialising stage for our Class model

        args:
        Width: determines the width of our Rectangle
        Height: determines the height of our Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        A property getter that gets the the width of our Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter Method used to reasign the private variable width

        args:
        Value: the new width we are setting
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """
        A property getter that gets the the height of our Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter Method used to reasign the private variable height

        Args:
        Value- the new height we are setting
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """
        Calculate the area of our rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of our rectangle
        """
        perim = 2 * (self.__width + self.__height)

        if self.__width == 0 or self.__height == 0:
            perim = 0
        return perim
