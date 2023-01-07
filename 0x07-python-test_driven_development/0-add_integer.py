def add_integer(a, b=98):
    if isinstance(a, int) or isinstance(a, float):
        c = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, int) or isinstance(b, float):
        d = int(b)
    else:
        raise TypeError("b must be an integer")

    return c + d
