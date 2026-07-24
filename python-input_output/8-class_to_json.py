#!/usr/bin/python3
"""Module that provides a function to convert a class instance to JSON."""


def class_to_json(obj):
    """
    Return the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary containing the object's attributes.
    """
    return obj.__dict__
