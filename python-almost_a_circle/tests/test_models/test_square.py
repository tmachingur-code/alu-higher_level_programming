#!/usr/bin/python3
"""Unit tests for Square."""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Square test cases."""

    def test_constructor(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_area(self):
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_str(self):
        s = Square(5, 1, 2, 99)
        self.assertEqual(str(s), "[Square] (99) 1/2 - 5")

    def test_size_setter(self):
        s = Square(5)
        s.size = 8
        self.assertEqual(s.size, 8)

    def test_size_type(self):
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "8"

    def test_dictionary(self):
        s = Square(4, 2, 3, 10)
        d = s.to_dictionary()
        self.assertEqual(d["size"], 4)

    def test_update_args(self):
        s = Square(5)
        s.update(1, 6, 2, 3)
        self.assertEqual(s.size, 6)

    def test_update_kwargs(self):
        s = Square(5)
        s.update(size=7, x=2)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 2)


if __name__ == "__main__":
    unittest.main()
