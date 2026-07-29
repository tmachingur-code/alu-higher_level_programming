#!/usr/bin/python3
"""This module defines the Base class."""


class Base:
    """Represents the base class for all future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.

        Args:
            id (int): The identifier of the instance. If None,
            an automatic ID is assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
