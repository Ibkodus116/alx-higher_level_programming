#!/usr/bin/python3

"""
Model inheriting from BaseGeometry Class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """
    The rectangle class inherited from BaseGeometry
    and cheking integer validator
    """

    def __init__(self, width, height):
        """
        Init function initilising the Rectangle Class
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Function that calculate the area of a square"""
        return self.__height * self.__width

    def __str__(self):
        return f"[{Rectangle.__name__}] {self.__width}/{self.__height}"
