#!/usr/bin/env python3
"""
Measure the runtime.
"""
import time
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time fot coroutine wait_n.
    """
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.time()

    elapsed_time: float = end - start
    return elapsed_time
