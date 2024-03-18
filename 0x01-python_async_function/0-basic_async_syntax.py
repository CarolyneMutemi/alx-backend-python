#!/usr/bin/env python3

"""
The basics of async.
"""
import asyncio
import random


async def wait_random(max_delay: float = 10):
    """
    Waits for a random delay.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay