#!/usr/bin/python3
"""Unit tests for Square class."""

import unittest

from models.square import Square


class TestSquare(unittest.TestCase):
    """Test Square class."""

    def setUp(self):
        """Create Square object."""
        self.s = Square(5, 2, 3, 1)

    def test_creation(self):
        """Test square creation."""
        self.assertEqual(self.s.size, 5)
        self.assertEqual(self.s.width, 5)
        self.assertEqual(self.s.height, 5)
        self.assertEqual(self.s.x, 2)
        self.assertEqual(self.s.y, 3)
        self.assertEqual(self.s.id, 1)

    def test_area(self):
        """Test square area."""
        self.assertEqual(self.s.area(), 25)

    def test_size_setter(self):
        """Test changing size."""
        self.s.size = 10

        self.assertEqual(self.s.size, 10)
        self.assertEqual(self.s.width, 10)
        self.assertEqual(self.s.height, 10)

    def test_invalid_size(self):
        """Test invalid size."""
        with self.assertRaises(TypeError):
            self.s.size = "5"

    def test_str(self):
        """Test square string representation."""
        result = str(self.s)
        expected = "[Square] (1) 2/3 - 5"

        self.assertEqual(result, expected)

    def test_update_args(self):
        """Test update with arguments."""
        self.s.update(89, 8, 4, 5)

        self.assertEqual(self.s.id, 89)
        self.assertEqual(self.s.size, 8)
        self.assertEqual(self.s.x, 4)
        self.assertEqual(self.s.y, 5)

    def test_update_kwargs(self):
        """Test update with keyword arguments."""
        self.s.update(
            id=20,
            size=7,
            x=1,
            y=2
        )

        self.assertEqual(self.s.id, 20)
        self.assertEqual(self.s.size, 7)
        self.assertEqual(self.s.x, 1)
        self.assertEqual(self.s.y, 2)

    def test_dictionary(self):
        """Test dictionary conversion."""
        result = self.s.to_dictionary()

        self.assertEqual(result["id"], 1)
        self.assertEqual(result["size"], 5)
        self.assertEqual(result["x"], 2)
        self.assertEqual(result["y"], 3)


if __name__ == "__main__":
    unittest.main()
