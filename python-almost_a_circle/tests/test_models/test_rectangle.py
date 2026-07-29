#!/usr/bin/python3
"""Unit tests for Rectangle class."""

import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle class."""

    def setUp(self):
        """Create a Rectangle object."""
        self.r = Rectangle(10, 5, 2, 3, 1)

    def test_creation(self):
        """Test rectangle creation."""
        self.assertEqual(self.r.width, 10)
        self.assertEqual(self.r.height, 5)
        self.assertEqual(self.r.x, 2)
        self.assertEqual(self.r.y, 3)
        self.assertEqual(self.r.id, 1)

    def test_area(self):
        """Test rectangle area."""
        self.assertEqual(self.r.area(), 50)

    def test_width_setter(self):
        """Test changing width."""
        self.r.width = 20
        self.assertEqual(self.r.width, 20)

    def test_height_setter(self):
        """Test changing height."""
        self.r.height = 8
        self.assertEqual(self.r.height, 8)

    def test_invalid_width(self):
        """Test invalid width."""
        with self.assertRaises(TypeError):
            Rectangle("10", 5)

    def test_invalid_height(self):
        """Test invalid height."""
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_str(self):
        """Test string representation."""
        result = str(self.r)
        expected = "[Rectangle] (1) 2/3 - 10/5"

        self.assertEqual(result, expected)

    def test_update_args(self):
        """Test update with arguments."""
        self.r.update(89, 4, 6, 1, 2)

        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 4)
        self.assertEqual(self.r.height, 6)
        self.assertEqual(self.r.x, 1)
        self.assertEqual(self.r.y, 2)

    def test_update_kwargs(self):
        """Test update with keyword arguments."""
        self.r.update(
            id=50,
            width=7,
            height=8,
            x=4,
            y=5
        )

        self.assertEqual(self.r.id, 50)
        self.assertEqual(self.r.width, 7)
        self.assertEqual(self.r.height, 8)

    def test_dictionary(self):
        """Test dictionary conversion."""
        result = self.r.to_dictionary()

        self.assertEqual(result["width"], 10)
        self.assertEqual(result["height"], 5)
        self.assertEqual(result["x"], 2)
        self.assertEqual(result["y"], 3)


if __name__ == "__main__":
    unittest.main()
