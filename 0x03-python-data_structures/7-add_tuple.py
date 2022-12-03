#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        tuple_n = tuple_a[0] + tuple_b[0], 0 + tuple_b[1]
        return tuple_n
    elif len(tuple_a) == 0:
        tuple_n = 0 + tuple_b[0], 0 + tuple_b[1]
        return tuple_n
    if len(tuple_b) == 1:
        tuple_n = tuple_a[0] + tuple_b[0], tuple_a[1] + 0
        return tuple_n
    elif len(tuple_b) == 0:
        tuple_n = tuple_a[0] + 0, tuple_a[1] + 0
        return tuple_n
    else:
        tuple_n = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
        return tuple_n
