#!/usr/bin/env python3
"""
Module containing unit tests for utils module
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    class to test the nested_map funxtion
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, map, path, result):
        """method to test the nested_map funxtion"""
        self.assertEqual(access_nested_map(map, path), result)


if __name__ == "__main__":
    unittest.main()
