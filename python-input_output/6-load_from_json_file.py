#!/usr/bin/python3
"""Module that provides a function to create objects from JSON files."""


import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename: The name of the JSON file to read.

    Returns:
        The Python object represented by the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
