#!/usr/bin/python3
"""Module that defines a function to check an object's exact class."""


def is_same_class(obj, a_class):
    """Check whether an object is exactly an instance of a class."""
    return type(obj) is a_class
