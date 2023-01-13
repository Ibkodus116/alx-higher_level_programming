#!/usr/bin/python3

"""
Module handling a function that return True or False
"""


def inherits_from(obj, a_class):
    """
    a function that returns True if the object is an instance of
    a class that inherited (directly or indirectly) from the
    specified class ; otherwise False.
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
