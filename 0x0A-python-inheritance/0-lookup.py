#!/usr/bin/python3
def lookup(obj):
    """
    This function takes an object as input and returns a list of all the available
    attributes and methods of the object.
    """
    return [a for a in dir(obj) if not a.startswith('__')]
