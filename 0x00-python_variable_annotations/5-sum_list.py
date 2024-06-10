#!/usr/bin/env python3
""" module contains implentation of type-annotated function sum_list"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
Calculates the sum of a list of floats.

Args:
    input_list (List[float]): A list of float numbers.

Returns:
    float: The sum of the floats in the list.
"""
    result = 0.0
    for num in input_list:
        result += num
    return result
