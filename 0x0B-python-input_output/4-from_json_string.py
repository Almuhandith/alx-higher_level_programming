#!/usr/bin/python3
""" Module that contains a function that returns
an object represented by a JSON string
"""
import json


def to_json_string(my_obj):
    """ Function that returns the JSON representation of an object
    Args:
        my_obj: object
    Raises:
        Exception: when the object can't be encoded
    """
    return json.load(my_obj)
