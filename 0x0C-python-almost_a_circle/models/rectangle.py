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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """height Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setterf for height"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Variable x Getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setterf for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Variable y Getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setterf for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Method that returns the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Method that returns the area of a rectangle"""
        print_width = "#" * self.width
        print_x = " " * self.x
        print_y = "\n" * self.y
        rectangle = print_y
        for i in range(self.height):
            rectangle += print_x
            rectangle += print_width + "\n"
        print(rectangle, end="")

    def __str__(self):
        """The str method which print to stdout"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
            )

    def update(self, *args, **kwargs):
        """Update method"""
        lst_attr = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) > 0:
            for i in range(len(args)):
                setattr(self, lst_attr[i], args[i])
        else:
            for key, values in kwargs.items():
                setattr(self, key, values)

    def to_dictionary(self):
        """Returns a Dictionary"""
        lst_attr = ("id", "width", "height", "x", "y")
        rec_dict = {}
        for i in lst_attr:
            rec_dict[i] = getattr(self, i)
        return rec_dict
