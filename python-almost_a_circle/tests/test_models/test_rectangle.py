#!/usr/bin/python3
"""Unit tests for Rectangle class"""

import io
import os
import sys
import unittest

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle class"""

    def setUp(self):
        """Reset Base counter"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove generated files"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_rectangle_1_2(self):
        """Test Rectangle(1, 2)"""
        r = Rectangle(1, 2)

        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_rectangle_with_x(self):
        """Test Rectangle with x"""
        r = Rectangle(1, 2, 3)

        self.assertEqual(r.x, 3)

    def test_rectangle_with_x_y(self):
        """Test Rectangle with x and y"""
        r = Rectangle(1, 2, 3, 4)

        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_with_id(self):
        """Test Rectangle with id"""
        r = Rectangle(1, 2, 3, 4, 5)

        self.assertEqual(r.id, 5)

    def test_width_type(self):
        """Test width type"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_height_type(self):
        """Test height type"""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_x_type(self):
        """Test x type"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_y_type(self):
        """Test y type"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_width_value(self):
        """Test invalid width values"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_height_value(self):
        """Test invalid height values"""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_x_value(self):
        """Test invalid x values"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_y_value(self):
        """Test invalid y values"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Test area"""
        r = Rectangle(10, 12)

        self.assertEqual(r.area(), 120)

    def test_str(self):
        """Test __str__"""
        r = Rectangle(4, 6, 2, 1, 12)

        self.assertEqual(
            str(r),
            "[Rectangle] (12) 2/1 - 4/6"
        )

    def test_display(self):
        """Test display"""
        r = Rectangle(2, 3)

        output = io.StringIO()
        sys.stdout = output

        r.display()

        sys.stdout = sys.__stdout__

        self.assertEqual(
            output.getvalue(),
            "##\n##\n##\n"
        )

    def test_display_with_x_y(self):
        """Test display with x and y"""
        r = Rectangle(2, 2, 1, 1)

        output = io.StringIO()
        sys.stdout = output

        r.display()

        sys.stdout = sys.__stdout__

        self.assertEqual(
            output.getvalue(),
            "\n ##\n ##\n"
        )

    def test_update_args(self):
        """Test update args"""
        r = Rectangle(10, 10)

        r.update(89, 2, 3, 4, 5)

        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        """Test update kwargs"""
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
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_to_dictionary(self):
        """Test dictionary representation"""
        r = Rectangle(10, 2, 1, 9, 12)

        self.assertEqual(
            r.to_dictionary(),
            {
                "id": 12,
                "width": 10,
                "height": 2,
                "x": 1,
                "y": 9
            }
        )

    def test_create(self):
        """Test create"""
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

    def test_save_to_file_none(self):
        """Test save None"""
        Rectangle.save_to_file(None)

        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty(self):
        """Test save empty list"""
        Rectangle.save_to_file([])

        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_objects(self):
        """Test save objects"""
        r = Rectangle(1, 2)

        Rectangle.save_to_file([r])

        with open("Rectangle.json") as file:
            data = file.read()

        self.assertTrue(len(data) > 0)

    def test_load_from_file_missing(self):
        """Test load missing file"""
        result = Rectangle.load_from_file()

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
