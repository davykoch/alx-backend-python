#!/usr/bin/env python3
""" module contains use of mypy"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ implented method with mypy"""
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]

    return zoomed_in


array: Tuple[int, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
