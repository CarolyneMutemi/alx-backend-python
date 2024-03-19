#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times.
    """
    lis: List[float] = [task_wait_random(max_delay) for _ in range(n)]
    result: List[float] = []

    for task in asyncio.as_completed(lis):
        result.append(await task)
    return result
