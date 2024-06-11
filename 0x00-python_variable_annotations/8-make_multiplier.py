#!/usr/bin/env python3
"""
module contains implementation of type-annotated function make_multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
Returns a function that multiplies a float by a given multiplier.

Args:
    multiplier (float): The multiplier value.

Returns:
    Callable[[float], float]: A function that takes a float and
            returns the product with the multiplier.
"""
    def multiplier_func(num: float) -> float:
        return num * multiplier
    return multiplier_func
