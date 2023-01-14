#!/usr/bin/python3

"""
Module handling a called BaseGeometry it defines Geometry
"""


class BaseGeometry:
    """
    A class that defines geometry
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A function that rasies an error when value
        isn't an intiger or it's not less greater than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
