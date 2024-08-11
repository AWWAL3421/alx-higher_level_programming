#!/usr/bin/python3
"""
Module to define a student class.
"""


class Student:
    """A class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student instance."""
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        if age < 0:
            raise ValueError("age must be a positive integer")

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of a student instance."""
        attrs = self.__dict__
        json_dict = {}
        for key, value in attrs.items():
            if isinstance(value, (list, dict, str, int, bool)):
                json_dict[key] = value
        return json_dict
