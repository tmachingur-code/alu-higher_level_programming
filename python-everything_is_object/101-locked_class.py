#!/usr/bin/python3
"""LockedClass module."""


class LockedClass:
    """Prevent dynamic creation of instance attributes except first_name."""
    __slots__ = ["first_name"]
