#!/usr/bin/python3
"""Module that contains a function that reads a file"""

def read_file(filename=""):
    with open('filename', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
