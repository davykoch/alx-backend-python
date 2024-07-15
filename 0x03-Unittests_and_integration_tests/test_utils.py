#!/usr/bin/env python3
"""
Module for testing the get_json function from utils.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json


class TestGetJson(unittest.TestCase):
    """
    Test class for the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(
        self,
        test_url: str,
        test_payload: dict,
        mock_get: Mock
    ) -> None:
        """
        Test that utils.get_json returns the expected result.
        """
        # Configure the mock to return a response with json() method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function with test input
        result = get_json(test_url)

        # Check that requests.get was called once with test_url
        mock_get.assert_called_once_with(test_url)

        # Check that the output of get_json is equal to test_payload
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
