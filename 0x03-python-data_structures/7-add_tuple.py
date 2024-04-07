#!/usr/bin/python3
def add_tuple(tuple_b=(), tuple_c=()):
    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    if len(tuple_c) == 0:
        tuple_c = (0, 0)
    elif len(tuple_c) == 1:
        tuple_c = (tuple_c[0], 0)

    return (tuple_b[0] + tuple_c[0], tuple_c[1] + tuple_c[1])
