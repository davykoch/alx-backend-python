#!/usr/bin/env python3
""" module contains implentation of typed annotated functiom element_length"""

from typing import Sequence, Iterable, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
