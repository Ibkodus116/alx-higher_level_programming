#!/usr/bin/python3
"""The Module Doc"""


class Student:
    """The Class Doc"""

    def __init__(self, first_name, last_name, age):
        """The Function Doc"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """The Function Doc"""
        return self.__dict__
