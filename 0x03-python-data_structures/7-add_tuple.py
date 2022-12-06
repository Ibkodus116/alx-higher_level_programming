#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        a1 = 0
        a0 = tuple_a[0]
#        tuple_n = tuple_a[0] + tuple_b[0], 0 + tuple_b[1]
#        return tuple_n
    elif len(tuple_a) == 0:
        a0 = 0
        a1 = 0
    else:
        a1 = tuple_a[1]
        a0 = tuple_a[0]
#        tuple_n = 0 + tuple_b[0], 0 + tuple_b[1]
#        return tuple_n
    
    if len(tuple_b) == 1:
        b1 = 0
        b0 = tuple_b[0]
#        tuple_n = tuple_a[0] + tuple_b[0], tuple_a[1] + 0
#        return tuple_n
    elif len(tuple_b) == 0:
        b0 = 0
        b1 = 0
#        tuple_n = tuple_a[0] + 0, tuple_a[1] + 0
#        return tuple_n
    else:
        b1 = tuple_b[1]
        b0 = tuple_b[0]
#        tuple_n = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
#        return tuple_n
    return (a0 + b0, a1 + b1)
