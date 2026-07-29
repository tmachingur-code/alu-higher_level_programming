#!/usr/bin/python3
"""Unit tests for Rectangle."""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Rectangle test cases."""

    def test_constructor(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)

    def test_area(self):
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_str(self):
        r = Rectangle(4, 5, 1, 2, 99)
        self.assertEqual(str(r), "[Rectangle] (99) 1/2 - 4/5")

    def test_width_type(self):
        with self.assertRaises(TypeError):
            Rectangle("2", 3)

    def test_width_value(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 3)

    def test_height_type(self):
        with self.assertRaises(TypeError):
            Rectangle(2, "3")

    def test_height_value(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 0)

    def test_x_type(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 3, "1")

    def test_y_type(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 1, "2")

    def test_dictionary(self):
        r = Rectangle(2, 3, 1, 2, 7)
        d = r.to_dictionary()
        self.assertEqual(d["width"], 2)
        self.assertEqual(d["height"], 3)

    def test_update_args(self):
        r = Rectangle(1, 1)
        r.update(10, 5, 6, 7, 8)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 5)

    def test_update_kwargs(self):
        r = Rectangle(1, 1)
        r.update(width=7, height=8)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 8)


if __name__ == "__main__":
    unittest.main()
