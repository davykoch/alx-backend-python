#!/usr/bin/env python3
"""
Module for testing the memoize decorator from utils.
"""

import unittest
from unittest.mock import patch, Mock
from utils import memoize


class TestMemoize(unittest.TestCase):
    """
    Test class for the memoize decorator.
    """

    def test_memoize(self) -> None:
        """
        Test that the memoize decorator works as expected.
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
            TestClass,
            'a_method',
            return_value=42
        ) as mock_method:
            test_obj = TestClass()

            # Call a_property twice
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            # Check that the results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Check that a_method was only called once
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
