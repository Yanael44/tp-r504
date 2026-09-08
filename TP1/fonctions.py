def puissance(a, b):
    
    if not type(a) is int or not type(b) is int:
        raise TypeError   
    if a == 0:
        if b < 0:
            raise ValueError 
        return 0
    res = 1
    exp = abs(b)
    for _ in range(exp):
        res = res * a
    if b < 0:
        return 1 / res

    return res
