#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Represents a square with size and position validation."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square.

        Args:
            size: The size of the square.
            position: The coordinates of the square.

        Raises:
            TypeError: If size or position has an invalid type.
            ValueError: If size or position has an invalid value.
        """
        self.size = size
        self.position = position

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
            TypeError: If value is not an integer.
            ValueError: If value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square.

        Returns:
            The position coordinates.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set and validate the position of the square.

        Args:
            value: The position coordinates.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )

        self.__position = value

    def area(self):
        """Return the current square area.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using # characters with its position.

        If size is 0, an empty line is printed.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
