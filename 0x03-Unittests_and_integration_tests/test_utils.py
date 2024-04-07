#!/usr/bin/env python3
"""
Testing the utils.access_nested_map method.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Testing the utils.access_nested_map method.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Tests the return value of the access_nested_map method
        given nested maps and different paths.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
        ])
    def test_access_nested_map_exception(self, nested_map, path, error_message):
        """
        Tests that the function access_nested_map raises a KeyError
        when the path parameters are not found in the nested_map.
        """
        with self.assertRaises(KeyError, msg=error_message):
            access_nested_map(nested_map, path)
