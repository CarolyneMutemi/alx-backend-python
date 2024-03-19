#!/usr/bin/env python3
"""
Async comprehensions.
"""
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehensing
    over async_generator and returns 10 random numbers.
    """
    random_num_list: List[float] = [num async for num in async_generator()]

    return random_num_list
