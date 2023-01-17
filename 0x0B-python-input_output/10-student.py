#!/usr/bin/python3
"""The Module Doc"""


class Student:
    """The Class Doc"""

    def __init__(self, first_name, last_name, age):
        """The Function Doc"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """The Function Doc"""
        lst = []
        dct = {}
        if isinstance(attrs, list):
            for i in attrs:
                if isinstance(i, str):
                    if i in self.__dict__:
                        lst += [i]
        # print (lst)
        if lst:
            for j in lst:
                dct[j] = self.__dict__[j]
            return dct

        return self.__dict__
