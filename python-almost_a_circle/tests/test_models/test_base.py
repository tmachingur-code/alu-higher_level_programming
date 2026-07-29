#!/usr/bin/python3
"""Unit tests for Base class"""

import os
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test Base class"""

    def setUp(self):
        """Reset ID counter"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove created files"""
        for filename in ["Rectangle.json", "Square.json"]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_base_no_id(self):
        """Test automatic id assignment"""
        b1 = Base()
        b2 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_with_id(self):
        """Test id assignment"""
        b = Base(89)

        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Test None JSON conversion"""
        self.assertEqual(
            Base.to_json_string(None),
            "[]"
        )

    def test_to_json_string_empty(self):
        """Test empty list JSON conversion"""
        self.assertEqual(
            Base.to_json_string([]),
            "[]"
        )

    def test_to_json_string_list(self):
        """Test dictionary list conversion"""
        data = [{"id": 12}]

        result = Base.to_json_string(data)

        self.assertEqual(
            result,
            '[{"id": 12}]'
        )

        self.assertIsInstance(result, str)

    def test_from_json_string_none(self):
        """Test None conversion"""
        self.assertEqual(
            Base.from_json_string(None),
            []
        )

    def test_from_json_string_empty(self):
        """Test empty conversion"""
        self.assertEqual(
            Base.from_json_string("[]"),
            []
        )

    def test_from_json_string_list(self):
        """Test JSON string conversion"""
        result = Base.from_json_string(
            '[{"id": 89}]'
        )

        self.assertEqual(
            result,
            [{"id": 89}]
        )

        self.assertIsInstance(result, list)

    def test_save_rectangle_none(self):
        """Test Rectangle save None"""
        Rectangle.save_to_file(None)

        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_rectangle_empty(self):
        """Test Rectangle save empty list"""
        Rectangle.save_to_file([])

        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_rectangle_objects(self):
        """Test Rectangle save objects"""
        r1 = Rectangle(1, 2)

        Rectangle.save_to_file([r1])

        with open("Rectangle.json") as file:
            data = file.read()

        self.assertTrue(len(data) > 0)

    def test_save_square_none(self):
        """Test Square save None"""
        Square.save_to_file(None)

        with open("Square.json") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_square_empty(self):
        """Test Square save empty"""
        Square.save_to_file([])

        with open("Square.json") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_square_objects(self):
        """Test Square save objects"""
        s1 = Square(1)

        Square.save_to_file([s1])

        with open("Square.json") as file:
            data = file.read()

        self.assertTrue(len(data) > 0)

    def test_create_rectangle(self):
        """Test Rectangle create"""
        r = Rectangle.create(
            id=89,
            width=1,
            height=2,
            x=3,
            y=4
        )

        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_create_square(self):
        """Test Square create"""
        s = Square.create(
            id=89,
            size=5,
            x=2,
            y=3
        )

        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)


if __name__ == "__main__":
    unittest.main()
