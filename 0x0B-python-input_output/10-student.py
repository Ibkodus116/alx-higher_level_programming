#!/usr/bin/python3
"""The Module Doc"""


class Student:
    """
    This class represents a student with a first name, last name and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.
        :param first_name: The first name of the student.
        :param last_name: The last name of the student.
        :param age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """
        Returns a dictionary representation of the student object.
        :param attrs: A list of attributes to include in the
                returned dictionary.
        :return: A dictionary representation of the student object.
        """

        lst = []
        dct = {}
        obj = self.__dict__.copy()

        if isinstance(attrs, list):
            for i in attrs:
                if isinstance(i, str):
                    if i in obj:
                        lst += [i]

            for j in lst:
                dct[j] = self.__dict__[j]
            return dct

        return obj
