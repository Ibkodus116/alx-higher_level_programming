#!/usr/bin/python3
"""

Module containing a function that divdes all element in a matrix

"""


def matrix_divided(matrix, div):
    """Function that divdes all element in a matrix
    Args:
        matrix: a List of List
        div: a divisable number

    Return:
        a new matrix divded by div

    Raise:
        ZeroDivisionError: if div is equal to 0
        TypeError: if matrix isnt't list of lists and the value
        aren't integers/floats
        TypeError: if each row in matrix ain't same size i.e lenght
    """

    int_msg = "matrix must be a matrix (list of lists) of integers/floats"
    size_msg = "Each row of the matrix must have the same size"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(int_msg)

    for i in matrix:
        if not i or not isinstance(i, list):
            raise TypeError(int_msg)
        len_l = len(matrix[0])
        if len_l != len(i):
            raise TypeError(size_msg)
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(int_msg)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    ma = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))

    return ma
