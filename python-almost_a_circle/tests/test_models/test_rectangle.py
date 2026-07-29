#!/usr/bin/python3
"""Unit tests for Rectangle class"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle"""

    def test_rectangle_creation(self):
        """Test creating Rectangle"""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_with_x(self):
        """Test Rectangle with x"""
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_rectangle_with_x_y(self):
        """Test Rectangle with x and y"""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_rectangle_with_id(self):
        """Test Rectangle with id"""
        r = Rectangle(1, 2, 3, 4, 89)
        self.assertEqual(r.id, 89)

    def test_width_type_error(self):
        """Width must be integer"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_height_type_error(self):
        """Height must be integer"""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_x_type_error(self):
        """X must be integer"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_y_type_error(self):
        """Y must be integer"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_width_value_error(self):
        """Width cannot be <= 0"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_height_value_error(self):
        """Height cannot be <= 0"""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_width_zero(self):
        """Width cannot be zero"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_zero(self):
        """Height cannot be zero"""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_x_negative(self):
        """X cannot be negative"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1)

    def test_y_negative(self):
        """Y cannot be negative"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 0, -1)

    def test_area(self):
        """Test area"""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        """Test string representation"""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(
            str(r),
            "[Rectangle] (12) 2/1 - 4/6"
        )

    def test_display(self):
        """Test display method"""
        r = Rectangle(2, 2)
        self.assertIsNone(r.display())

    def test_update_args(self):
        """Test update with args"""
        r = Rectangle(10, 10)

        r.update(89, 2, 3, 4, 5)

        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        """Test update with kwargs"""
        r = Rectangle(10, 10)

        r.update(
            id=89,
            width=2,
            height=3,
            x=4,
            y=5
        )

        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)

    def test_to_dictionary(self):
        """Test dictionary conversion"""
        r = Rectangle(10, 2, 1, 9)

        dictionary = r.to_dictionary()

        self.assertEqual(dictionary["id"], r.id)
        self.assertEqual(dictionary["width"], 10)
        self.assertEqual(dictionary["height"], 2)
        self.assertEqual(dictionary["x"], 1)
        self.assertEqual(dictionary["y"], 9)

    def test_display_without_xy(self):
        """Test display without x and y"""
        r = Rectangle(2, 3)

        self.assertIsNone(r.display())

    def test_display_with_x(self):
        """Test display with x"""
        r = Rectangle(2, 3, 1)

        self.assertIsNone(r.display())

    def test_display_with_x_y(self):
        """Test display with x and y"""
        r = Rectangle(2, 3, 1, 2)

        self.assertIsNone(r.display())


if __name__ == "__main__":
    unittest.main()
