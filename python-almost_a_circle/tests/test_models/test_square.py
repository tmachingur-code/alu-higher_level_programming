#!/usr/bin/python3
"""Unit tests for Square class"""

import os
import unittest

from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test Square class"""

    def setUp(self):
        """Reset Base counter"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove generated files"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_square_size(self):
        """Test Square(size)"""
        s = Square(5)

        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

    def test_square_with_x(self):
        """Test Square(size, x)"""
        s = Square(5, 2)

        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)

    def test_square_with_y(self):
        """Test Square(size, x, y)"""
        s = Square(5, 2, 3)

        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_with_id(self):
        """Test Square(size, x, y, id)"""
        s = Square(5, 2, 3, 89)

        self.assertEqual(s.id, 89)

    def test_invalid_size_type(self):
        """Test invalid size type"""
        with self.assertRaises(TypeError):
            Square("5")

    def test_invalid_x_type(self):
        """Test invalid x type"""
        with self.assertRaises(TypeError):
            Square(5, "2")

    def test_invalid_y_type(self):
        """Test invalid y type"""
        with self.assertRaises(TypeError):
            Square(5, 2, "3")

    def test_invalid_size_value(self):
        """Test invalid size values"""
        with self.assertRaises(ValueError):
            Square(0)

        with self.assertRaises(ValueError):
            Square(-1)

    def test_invalid_x_value(self):
        """Test invalid x value"""
        with self.assertRaises(ValueError):
            Square(5, -2)

    def test_invalid_y_value(self):
        """Test invalid y value"""
        with self.assertRaises(ValueError):
            Square(5, 2, -3)

    def test_str(self):
        """Test Square string"""
        s = Square(5, 2, 1, 12)

        self.assertEqual(
            str(s),
            "[Square] (12) 2/1 - 5"
        )

    def test_area(self):
        """Test inherited area"""
        s = Square(5)

        self.assertEqual(
            s.area(),
            25
        )

    def test_size_getter(self):
        """Test size getter"""
        s = Square(5)

        self.assertEqual(
            s.size,
            5
        )

    def test_size_setter(self):
        """Test size setter"""
        s = Square(5)

        s.size = 10

        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_type(self):
        """Test size setter type"""
        s = Square(5)

        with self.assertRaises(TypeError):
            s.size = "10"

    def test_size_setter_value(self):
        """Test size setter value"""
        s = Square(5)

        with self.assertRaises(ValueError):
            s.size = 0

    def test_update_args(self):
        """Test update with args"""
        s = Square(5)

        s.update(89, 2, 3, 4)

        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """Test update with kwargs"""
        s = Square(5)

        s.update(
            id=89,
            size=2,
            x=3,
            y=4
        )

        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_to_dictionary(self):
        """Test dictionary representation"""
        s = Square(10, 2, 1, 89)

        self.assertEqual(
            s.to_dictionary(),
            {
                "id": 89,
                "size": 10,
                "x": 2,
                "y": 1
            }
        )

    def test_create(self):
        """Test create"""
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

    def test_save_to_file_none(self):
        """Test save None"""
        Square.save_to_file(None)

        with open("Square.json") as file:
            self.assertEqual(
                file.read(),
                "[]"
            )

    def test_save_to_file_empty(self):
        """Test save empty list"""
        Square.save_to_file([])

        with open("Square.json") as file:
            self.assertEqual(
                file.read(),
                "[]"
            )

    def test_save_to_file_objects(self):
        """Test save objects"""
        s = Square(1)

        Square.save_to_file([s])

        with open("Square.json") as file:
            data = file.read()

        self.assertTrue(len(data) > 0)

    def test_load_from_file_missing(self):
        """Test missing file"""
        result = Square.load_from_file()

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
