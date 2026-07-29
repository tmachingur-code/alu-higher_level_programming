#!/usr/bin/python3
"""Base class"""

import json
import csv


class Base:
    """Base class for all models"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON representation of list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON representation of objects to file"""
        filename = cls.__name__ + ".json"

        list_dictionary = []

        if list_objs is not None:
            for obj in list_objs:
                list_dictionary.append(obj.to_dictionary())

        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_dictionary))

    @staticmethod
    def from_json_string(json_string):
        """Return list from JSON string"""
        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set"""

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)

        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """Load objects from JSON file"""

        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as file:
                list_dictionary = cls.from_json_string(file.read())

            objects = []

            for dictionary in list_dictionary:
                objects.append(cls.create(**dictionary))

            return objects

        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save objects to CSV file"""

        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            if list_objs is None:
                return

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([
                        obj.id,
                        obj.width,
                        obj.height,
                        obj.x,
                        obj.y
                    ])

                elif cls.__name__ == "Square":
                    writer.writerow([
                        obj.id,
                        obj.size,
                        obj.x,
                        obj.y
                    ])

    @classmethod
    def load_from_file_csv(cls):
        """Load objects from CSV file"""

        filename = cls.__name__ + ".csv"

        objects = []

        try:
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)

                for row in reader:

                    if cls.__name__ == "Rectangle":
                        dictionary = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                        }

                    elif cls.__name__ == "Square":
                        dictionary = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                        }

                    objects.append(cls.create(**dictionary))

        except FileNotFoundError:
            return []

        return objects
