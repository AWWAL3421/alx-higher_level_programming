#!/usr/bin/python3
"""
Module to convert a class instance to a dictionary for JSON serialization.
"""


def class_to_json(obj):
    """Return a dictionary description of an object for JSON serialization."""
    if not isinstance(obj, object):
        raise TypeError("Argument must be an instance of a class")

    attrs = obj.__dict__
    json_dict = {}
    for key, value in attrs.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
