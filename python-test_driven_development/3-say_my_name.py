#!/usr/bin/python3
"""This module contains a function that prints a person's full name."""


def say_my_name(first_name, last_name=""):
    """Prints My name is followed by first name and last name.

    Args:
        first_name: The first name as a string.
        last_name: The last name as a string, default is empty.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
