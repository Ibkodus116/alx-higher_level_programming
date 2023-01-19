#!/usr/bin/python3
"""Module handling the Square Class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """The Sqaure Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """The initialise method"""
        super(Square, self).__init__(size, size, x, y, id)

    def __str__(self):
        """Str method that handles printing to stdout"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """Square getter method"""
        return self.width

    @size.setter
    def size(self, value):
        """Square setter method"""
        self.width = value
        self.height = value
