#!/usr/bin/env python3
""" module contains implentation of type-annotated function to_kv"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
Returns a tuple containing a string and the square of an integer or float.

Args:
    k (str): The string element of the tuple.
    v (Union[int, float]): The integer or float element of the tuple.

Returns:
    Tuple[str, float]: A tuple containing the string `k` and the
        square of `v` as a float.
"""
    return (k, v ** 2)
