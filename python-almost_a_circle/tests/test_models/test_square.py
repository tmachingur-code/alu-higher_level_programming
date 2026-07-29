#!/usr/bin/python3
"""Unit tests for Square class"""

import unittest

from models.square import Square


class TestSquare(unittest.TestCase):
    """Test Square"""

    def test_square_creation(self):
        """Test creating Square"""
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_with_x(self):
        """Test Square with x"""
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_square_with_x_y(self):
        """Test Square with x and y"""
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_square_with_id(self):
        """Test Square with id"""
        s = Square(1, 2, 3, 89)
        self.assertEqual(s.id, 89)

    def test_size_string(self):
        """Size must be integer"""
        with self.assertRaises(TypeError):
            Square("1")

    def test_x_string(self):
        """X must be integer"""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_y_string(self):
        """Y must be integer"""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_negative_size(self):
        """Size cannot be negative"""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_negative_x(self):
        """X cannot be negative"""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_negative_y(self):
        """Y cannot be negative"""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_zero_size(self):
        """Size cannot be zero"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        """Test string representation"""
        s = Square(5, 2, 1, 12)

        self.assertEqual(
            str(s),
            "[Square] (12) 2/1 - 5"
        )

    def test_area(self):
        """Test area"""
        s = Square(5)

        self.assertEqual(s.area(), 25)

    def test_display(self):
        """Test display"""
        s = Square(2)

        self.assertIsNone(s.display())

    def test_size_getter_setter(self):
        """Test size getter and setter"""
        s = Square(5)

        self.assertEqual(s.size, 5)

        s.size = 10

        self.assertEqual(s.size, 10)

    def test_size_setter_type_error(self):
        """Setter type validation"""
        s = Square(5)

        with self.assertRaises(TypeError):
            s.size = "9"

    def test_update_args(self):
        """Test update with args"""
        s = Square(5)

        s.update(89, 6, 2, 3)

        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_update_kwargs(self):
        """Test update with kwargs"""
        s = Square(5)

        s.update(
            id=89,
            size=8,
            x=3,
            y=4
        )

        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_to_dictionary(self):
        """Test dictionary conversion"""
        s = Square(10, 2, 1)

        dictionary = s.to_dictionary()

        self.assertEqual(dictionary["id"], s.id)
        self.assertEqual(dictionary["size"], 10)
        self.assertEqual(dictionary["x"], 2)
        self.assertEqual(dictionary["y"], 1)


if __name__ == "__main__":
    unittest.main()
