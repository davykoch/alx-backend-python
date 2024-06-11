#!/usr/bin/env python3
""" module contains implentation of typed annotated functiom element_length"""

from typing import Sequence, Iterable, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains a sequence
    and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing
            sequences (e.g., strings, lists, tuples).

     Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple
            contains a sequence from the input iterable and the
            length of that sequence.
    """
    return [(i, len(i)) for i in lst]
