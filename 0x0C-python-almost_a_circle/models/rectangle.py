#!/usr/bin/python3
"""Module handling the rectangle function"""

from models.base import Base


class Rectangle(Base):
    """The rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """The initializer"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super(Rectangle, self).__init__(id)

    @property
    def width(self):
        """Width Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setterf for width"""
        self.__width = value

    @property
    def height(self):
        """height Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setterf for height"""
        self.__height = value

    @property
    def x(self):
        """Variable x Getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setterf for x"""
        self.__x = value

    @property
    def y(self):
        """Variable y Getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setterf for y"""
        self.__y = value
