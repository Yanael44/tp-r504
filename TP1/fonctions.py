def puissance(a, b):
    if not type(a) is int:
        raise TypeError
    if not type(b) is int:
        raise TypeError
    if a == 0:
        if b < 0:
            raise ValueError
        if b > 0:
            return 0

    return a ** b
