#!/usr/bin/python3
"""This module defines the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.
            x (int): The horizontal position.
            y (int): The vertical position.
            id (int): The identifier of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return the string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )

    @property
    def size(self):
        """
        Get the size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        """
        self.width = value
        self.height = value
