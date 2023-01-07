#!/usr/bin/python3
"""

Module containing a function that prints First name and last name

"""


def say_my_name(first_name, last_name=""):
    """A function that prints My name is <first name> <last name>

    Args:
        first_name: the first name
        last_name: the last name

    Prints:
        My name is <first name> <last name>

    Raise:
        TypeError: raised a type error
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
