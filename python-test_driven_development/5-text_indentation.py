#!/usr/bin/python3
"""This module contains a function that formats text indentation."""


def text_indentation(text):
    """Prints a text with two new lines after ., ? and :.

    Args:
        text: The text to format.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = False

    for char in text:
        if char in ".?:":
            print(char)
            print()
            new_line = True
        elif char == " " and new_line:
            continue
        else:
            print(char, end="")
            new_line = False
