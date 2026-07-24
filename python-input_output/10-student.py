#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name: Student's first name.
            last_name: Student's last name.
            age: Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of a Student instance.

        Args:
            attrs: List of attribute names to retrieve.

        Returns:
            Dictionary containing selected or all attributes.
        """
        if isinstance(attrs, list):
            return {
                key: getattr(self, key)
                for key in attrs
                if hasattr(self, key)
            }

        return self.__dict__
