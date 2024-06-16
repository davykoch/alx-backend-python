#!/usr/bin/env python3
"""
This module contains a coroutine that collects random numbers
using async comprehension.
"""

import asyncio
from typing import List
import importlib

# Dynamically import async_generator from 0-async_generator
module_name = '0-async_generator'
async_generator = importlib.import_module(module_name).async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension over async_generator.

    :return: A list of 10 random numbers.
    """
    return [num async for num in async_generator()]
