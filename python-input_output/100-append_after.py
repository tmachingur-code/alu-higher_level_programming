#!/usr/bin/python3
"""Module that provides a function to append text after matching lines."""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a string after each line containing a specific string.

    Args:
        filename: Name of the file to modify.
        search_string: String to search for in each line.
        new_string: String to insert after matching lines.
    """
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    new_lines = []

    for line in lines:
        new_lines.append(line)

        if search_string in line:
            new_lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(new_lines)
