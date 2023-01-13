#!/usr/bin/python3

"""
Module that coontains a class of inheritance
"""


class MyList(list):
    """
    A Class that inherited from list
    """

    def print_sorted(self):
        """
        Function that sort and print the inherited list
        """
        l_sort = self.copy()
        l_sort.sort()
        print(l_sort)
