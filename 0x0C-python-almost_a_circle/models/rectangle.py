#!/usr/bin/python3
"""Module handling the rectangle function"""

from models.base import Base


class Rectangle(Base):
    """The rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """The initializer"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super(Rectangle, self).__init__(id)

    @property
    def width(self):
        """Width Getter"""
        return self.width

    @width.setter
    def width(self, value):
        """Setterf for width"""
        self.width = value

    @property
    def height(self):
        """height Getter"""
        return self.height

    @height.setter
    def height(self, value):
        """Setterf for height"""
        self.height = value

    @property
    def x(self):
        """Variable x Getter"""
        return self.x

    @x.setter
    def x(self, value):
        """Setterf for x"""
        self.x = value

    @property
    def y(self):
        """Variable y Getter"""
        return self.y

    @y.setter
    def y(self, value):
        """Setterf for y"""
        self.y = value
