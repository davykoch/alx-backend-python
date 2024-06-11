#!/usr/bin/env python3
""" module contains type annotations to the safely_get_value
function using TypeVar"""

from typing import TypeVar, Mapping, Union, Any

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary.

    Args:
        dct (Mapping[Any, Any]): A dictionary-like object.
        key (Any): The key to retrieve the value for.
        default (Union[T, None]): The default value to return if
                the key is not found.

    Returns:
        Union[Any, T]: The value associated with the key, or the default value
                if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
