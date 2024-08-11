#!/usr/bin/python3
"""
Module to load an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """Create an object from a JSON file."""
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
