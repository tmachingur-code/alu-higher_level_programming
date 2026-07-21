#!/usr/bin/python3
"""Module that defines the MyInt class."""


class MyInt(int):
    """A rebel integer class with inverted comparison operators."""

    def __eq__(self, other):
        """Return False when values are equal."""
        return int(self) != other

    def __ne__(self, other):
        """Return True when values are equal."""
        return int(self) == other
