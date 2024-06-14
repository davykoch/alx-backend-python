#!/usr/bin/env python3
"""
This module contains a function to measure the average runtime of wait_n.
"""

import time
import asyncio
import importlib

# Dynamically import wait_n from 1-concurrent_coroutines
module_name = '1-concurrent_coroutines'
wait_n = importlib.import_module(module_name).wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    :param n: Number of times to spawn wait_random
    :param max_delay: Maximum delay value for wait_random
    :return: The average time per wait_random call
    """

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
