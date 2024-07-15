#!/usr/bin/env python3
"""
Module for testing the access_nested_map function from utils.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: dict,
            path: tuple,
            expected: any
    ) -> None:
        """
        Test that access_nested_map returns the expected
        result for given inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: dict,
            path: tuple,
            expected_exception_msg: str
    ) -> None:
        """
        Test that access_nested_map raises KeyError with correct message
        for invalid inputs.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), f"'{expected_exception_msg}'")


if __name__ == '__main__':
    unittest.main()