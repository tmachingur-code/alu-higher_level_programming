#!/usr/bin/python3
"""Module that provides a function to convert an object to JSON."""


import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object.

    Args:
        my_obj: The Python object to serialize.

    Returns:
        A JSON string representation of the object.
    """
    return json.dumps(my_obj)
