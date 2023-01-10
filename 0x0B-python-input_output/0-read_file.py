#!/usr/bin/python3
"""Module that contains a function that reads a file"""

def read_file(filename=""):
     """ Function that reads from a file
    Args:
        filename: filename
    Raises
        Exception: when the file can be opened
    """

    with open('filename', 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")