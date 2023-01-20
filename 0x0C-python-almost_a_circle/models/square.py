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

    def update(self, *args, **kwargs):
        """method to Update the Square"""
        lst_arg = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for i in range(len(args)):
                setattr(self, lst_arg[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns a Dictionary for the Square"""
        tpl_dict = ('id', 'size', 'x', 'y')
        my_dict = {}
        for key in tpl_dict:
            my_dict[key] = getattr(self, key)
        return my_dict
