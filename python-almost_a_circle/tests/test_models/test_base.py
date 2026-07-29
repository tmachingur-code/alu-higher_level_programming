#!/usr/bin/python3
"""Unit tests for Base class."""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test Base class."""

    def setUp(self):
        """Reset Base counter."""
        Base._Base__nb_objects = 0

    def test_id_creation(self):
        """Test automatic and custom id assignment."""
        b1 = Base()
        b2 = Base()
        b3 = Base(89)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 89)

    def test_to_json_string(self):
        """Test converting list dictionaries to JSON."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

        result = Base.to_json_string([{"id": 12}])

        self.assertEqual(result, '[{"id": 12}]')
        self.assertIsInstance(result, str)

    def test_from_json_string(self):
        """Test converting JSON to list."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])

        result = Base.from_json_string('[{"id": 89}]')

        self.assertEqual(result, [{"id": 89}])
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()
