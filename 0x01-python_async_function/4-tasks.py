#!/usr/bin/env python3
"""
This module contains a function that spawns multiple asyncio
tasks using task_wait_random.
"""

from typing import List
import asyncio
import importlib

module_name = '3-tasks'
task_wait_random = importlib.import_module(module_name).task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns a list of delays.

    :param n: Number of times to spawn task_wait_random
    :param max_delay: Maximum delay value for task_wait_random
    :return: A list of delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)  # Sort the delays in ascending order
