#!/usr/bin/python3

def write_file(filename="", text=""):

    """function that writes a string to a file and returns the count of characters"""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
