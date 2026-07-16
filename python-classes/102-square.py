#!/usr/bin/python3
"""This module defines a Square class with comparison support."""


class Square:
    """Represents a square with size validation and comparisons."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size: The size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than zero.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set and validate the size of the square.

        Args:
            value: The size value.

        Raises:
            TypeError: If value is not an integer or float.
            ValueError: If value is less than zero.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the area of the square.

        Returns:
            The square area.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Compare if two squares have equal areas.

        Args:
            other: Another Square instance.

        Returns:
            True if areas are equal, otherwise False.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if two squares have different areas.

        Args:
            other: Another Square instance.

        Returns:
            True if areas are different, otherwise False.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare if this square area is smaller.

        Args:
            other: Another Square instance.

        Returns:
            True if this area is smaller.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if this square area is smaller or equal.

        Args:
            other: Another Square instance.

        Returns:
            True if this area is smaller or equal.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare if this square area is larger.

        Args:
            other: Another Square instance.

        Returns:
            True if this area is larger.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if this square area is larger or equal.

        Args:
            other: Another Square instance.

        Returns:
            True if this area is larger or equal.
        """
        return self.area() >= other.area()
