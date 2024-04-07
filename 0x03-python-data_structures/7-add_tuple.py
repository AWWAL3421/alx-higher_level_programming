#!/usr/bin/python3
def add_tuple(x=(), y=()):
    if len(x) == 0:
        x = (0, 0)
    elif len(x) == 1:
        x = (x[0], 0)
    if len(y) == 0:
        y = (0, 0)
    elif len(y) == 1:
        y = (y[0], 0)

    return (x[0] + y[0], x[1] + y[1])
