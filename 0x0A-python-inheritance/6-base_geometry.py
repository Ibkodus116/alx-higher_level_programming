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
