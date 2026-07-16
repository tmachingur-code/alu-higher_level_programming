#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Represents a square with size validation and printing."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size: The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set and validate the size of the square.

        Args:
            value: The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the current square area.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using the # character.

        If the size is 0, an empty line is printed.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
