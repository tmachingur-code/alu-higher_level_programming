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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of a list of dictionaries.
        """
        import json

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of objects to a file.
        """
        filename = cls.__name__ + ".json"

        if list_objs is None:
            list_objs = []

        list_dictionary = []

        for obj in list_objs:
            list_dictionary.append(obj.to_dictionary())

        json_string = cls.to_json_string(list_dictionary)

        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list represented by a JSON string.
        """
        import json

        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set from a dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances loaded from a JSON file.
        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as file:
                json_string = file.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**dictionary) for dictionary in list_dicts]
