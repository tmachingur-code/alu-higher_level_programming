#!/usr/bin/python3
"""Unit tests for Base class."""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base."""

    def test_auto_id(self):
        """Test automatic id assignment."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_given_id(self):
        """Test custom id."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Test None input."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        """Test JSON serialization."""
        d = [{"id": 12}]
        self.assertIsInstance(Base.to_json_string(d), str)

    def test_from_json_string_none(self):
        """Test None JSON."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test empty JSON."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string(self):
        """Test JSON deserialization."""
        result = Base.from_json_string('[{"id":89}]')
        self.assertEqual(result[0]["id"], 89)


if __name__ == "__main__":
    unittest.main()
