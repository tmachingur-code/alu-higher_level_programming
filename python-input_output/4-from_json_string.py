#!/usr/bin/python3
"""Module that provides a function to deserialize a JSON string."""


import json


def from_json_string(my_str):
    """
    Return the Python object represented by a JSON string.

    Args:
        my_str: The JSON string to deserialize.

    Returns:
        The corresponding Python object.
    """
    return json.loads(my_str)
