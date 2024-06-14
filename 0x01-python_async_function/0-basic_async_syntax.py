#!/usr/bin/env python3
""" This module contains asynchronous coroutine definition that
waits for random delay. """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (inclusive)
    seconds and returns the delay.

    :param max_delay: Maximum number of seconds to wait (default is 10)
    :return: The amount of time waited as a float
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
