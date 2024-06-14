#!/usr/bin/env python3
"""
This module contains an asynchronous routine that spawns
multiple wait_random coroutines
and returns the list of delays in ascending order.
"""

from typing import List
import asyncio
import importlib

# Dynamically import wait_random from 0-basic_async_syntax
module_name = '0-basic_async_syntax'
wait_random = importlib.import_module(module_name).wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    and returns a list of delays.

    :param n: Number of times to spawn wait_random
    :param max_delay: Maximum delay value for wait_random
    :return: A list of delays in ascending order
    """

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
