#!/usr/bin/env python3
"""
Testing the utils.access_nested_map method.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, requests, memoize


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
    def test_access_nested_map_exception(self, nested_map, path, error):
        """
        Tests that the function access_nested_map raises a KeyError
        when the path parameters are not found in the nested_map.
        """
        with self.assertRaises(KeyError, msg=error):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Tests the utils.get_json method.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """
        Tests the response of get_json.
        """
        with patch.object(requests, "get") as mock_response:
            mock_response(url).json.return_value = payload
            mock_response.reset_mock()
            self.assertEqual(get_json(url), payload)
            mock_response.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """
    Tests the utils.memoize method.
    """
    def test_memoize(self):
        """
        Tests the that a function decorated with memoize is called once
        through memoization.
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_object = TestClass()

        with patch.object(test_object, "a_method",
                          side_effect=test_object.a_method) as mock:
            test_object.a_property
            test_object.a_property
            mock.assert_called_once()
