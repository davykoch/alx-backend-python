#!/usr/bin/env python3
"""
This module contains a coroutine that measures the total runtime of running
async_comprehension four times in parallel.
"""

import asyncio
import time
import importlib

# Import async_comprehension from 1-async_comprehension
module_name = '1-async_comprehension'
async_comprehension = importlib.import_module(module_name).async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel and measures the
    total runtime.

    :return: Total runtime in seconds
    """
    start_time = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    return end_time - start_time
