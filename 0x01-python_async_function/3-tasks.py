#!/usr/bin/env python3
"""
This module contains a function that creates an
asyncio Task for the wait_random coroutine.
"""

import asyncio
import importlib

module_name = '0-basic_async_syntax'
wait_random = importlib.import_module(module_name).wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task for the wait_random coroutine with
    the given max_delay.

    :param max_delay: Maximum delay value for wait_random
    :return: An asyncio Task
    """

    return asyncio.create_task(wait_random(max_delay))
