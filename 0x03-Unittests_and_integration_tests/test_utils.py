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

    @parameterized.expand([
        ({}, ("a",), "a not in nested_map"),
        ({"a": 1}, ("a", "b"), "b not in {'a': 1}"),
    ])
    def test_access_nested_map_exception(self, map, path, exception_msg):
        """
        Test that accessing nested_map with invalid path
        raises KeyError with expected message
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(map, path)
            self.assertEqual(str(context.exception), exception_msg)


if __name__ == "__main__":
    unittest.main()
