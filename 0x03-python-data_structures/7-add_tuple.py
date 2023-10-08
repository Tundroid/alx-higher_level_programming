#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = [0, 0]
    if len(tuple_a) == 1:
        res[0] = tuple_a[0]
    elif len(tuple_a) >= 2:
        res[0] = tuple_a[0]
        res[1] = tuple_a[1]
    if len(tuple_b) == 1:
        res[0] += tuple_b[0]
    elif len(tuple_b) >= 2:
        res[0] += tuple_b[0]
        res[1] += tuple_b[1]
    return (res[0], res[1])
