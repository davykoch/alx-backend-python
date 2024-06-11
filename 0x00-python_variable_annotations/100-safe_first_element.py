#!/usr/bin/env python3
""" module contains duck-typed annotations"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence or None if the sequence is empty.

    Args:
        lst (Sequence[Any]): A sequence containing elements of any type.

    Returns:
        Union[Any, None]: The first element of the sequence if it exists,
                otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
