#!/usr/bin/env python3
""" module contains implentation of type-annotated function sum_mixed_list"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
Calculates the sum of a list of integers and floats.

Args:
    mxd_lst (List[Union[int, float]]): A list of integers and floats.

Returns:
    float: The sum of the elements in the list.
"""
    result = 0.0
    for num in mxd_lst:
        result += num
    return result
