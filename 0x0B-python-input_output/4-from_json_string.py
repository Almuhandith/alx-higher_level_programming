#!/usr/bin/python3
""" Module that contains a function that returns the JSON
representation of an object
"""
import json


def to_json_string(my_obj):
    """ Function that returns the object represented by a JSON string
    Args:
        my_obj: object
    Raises:
        Exception: when the object can't be encoded
    """
    return json.loads(my_obj)
