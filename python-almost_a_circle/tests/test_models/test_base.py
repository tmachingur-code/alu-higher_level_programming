#!/usr/bin/python3
"""Unit tests for Base class"""

import os
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test Base"""

    def test_base_without_id(self):
        """Base assigns automatic id"""
        b1 = Base()
        b2 = Base()

        self.assertIsNotNone(b1.id)
        self.assertEqual(b2.id, b1.id + 1)

    def test_base_with_id(self):
        """Base saves given id"""
        b = Base(89)

        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """None returns empty JSON list"""
        self.assertEqual(
            Base.to_json_string(None),
            "[]"
        )

    def test_to_json_string_empty(self):
        """Empty list returns empty JSON list"""
        self.assertEqual(
            Base.to_json_string([]),
            "[]"
        )

    def test_to_json_string_dictionary(self):
        """Dictionary converted to JSON"""
        result = Base.to_json_string(
            [{"id": 12}]
        )

        self.assertEqual(
            result,
            '[{"id": 12}]'
        )

        self.assertIsInstance(result, str)

    def test_from_json_string_none(self):
        """None returns empty list"""
        self.assertEqual(
            Base.from_json_string(None),
            []
        )

    def test_from_json_string_empty(self):
        """Empty JSON returns empty list"""
        self.assertEqual(
            Base.from_json_string("[]"),
            []
        )

    def test_from_json_string_list(self):
        """JSON string returns list"""
        result = Base.from_json_string(
            '[{"id": 89}]'
        )

        self.assertEqual(
            result,
            [{"id": 89}]
        )

        self.assertIsInstance(result, list)

    def test_save_rectangle_file(self):
        """Save Rectangle objects"""
        r1 = Rectangle(3, 4)
        r2 = Rectangle(5, 8, 1)

        Rectangle.save_to_file([r1, r2])

        self.assertTrue(
            os.path.exists("Rectangle.json")
        )

        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                file.read(),
                "[]"
            )

    def test_save_square_file(self):
        """Save Square objects"""
        s1 = Square(2)
        s2 = Square(4, 1)

        Square.save_to_file([s1, s2])

        self.assertTrue(
            os.path.exists("Square.json")
        )

    def test_create_rectangle(self):
        """Create Rectangle from dictionary"""
        dictionary = {
            "id": 89,
            "width": 2,
            "height": 3,
            "x": 1,
            "y": 4
        }

        r = Rectangle.create(**dictionary)

        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 4)

    def test_create_square(self):
        """Create Square from dictionary"""
        dictionary = {
            "id": 89,
            "size": 5,
            "x": 1,
            "y": 2
        }

        s = Square.create(**dictionary)

        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

    def test_load_rectangle_file_not_exist(self):
        """Loading missing file returns empty list"""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

        result = Rectangle.load_from_file()

        self.assertEqual(result, [])

    def test_load_square_file_not_exist(self):
        """Loading missing file returns empty list"""
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

        result = Square.load_from_file()

        self.assertEqual(result, [])

    def test_save_square_none(self):
        """Test Square save None"""
        Square.save_to_file(None)

        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_square_empty(self):
        """Test Square save empty list"""
        Square.save_to_file([])

        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_rectangle_empty(self):
        """Test Rectangle save empty list"""
        Rectangle.save_to_file([])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    @classmethod
    def tearDownClass(cls):
        """Remove created files"""
        for filename in [
            "Rectangle.json",
            "Square.json"
        ]:
            if os.path.exists(filename):
                os.remove(filename)


if __name__ == "__main__":
    unittest.main()
