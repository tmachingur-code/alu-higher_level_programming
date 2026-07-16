#!/usr/bin/python3
"""This module defines a singly linked list implementation."""


class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new node.

        Args:
            data: The data stored in the node.
            next_node: The next node in the linked list.

        Raises:
            TypeError: If data or next_node has an invalid type.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data stored in the node.

        Returns:
            The node data.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Set and validate the node data.

        Args:
            value: The data value.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node.

        Returns:
            The next node or None.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set and validate the next node.

        Args:
            value: The next node.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """Return the string representation of the linked list.

        Returns:
            A string containing each node's data on a new line.
        """
        values = []
        current = self.__head

        while current:
            values.append(str(current.data))
            current = current.next_node

        return "\n".join(values)

    def sorted_insert(self, value):
        """Insert a new node into the correct sorted position.

        Args:
            value: The integer value to insert.
        """
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head

        while (current.next_node is not None and
               current.next_node.data < value):
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
