#!/usr/bin/env python3
"""
In this module we measure the runtim of
 awaitable operations
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    calculate the time to run cer6ain number of concurrent tasks

    Args:
        n (int): total number of times to run awaitable function
        max_delay (int): Maximum delay in seconds. Defaults to 10.

    Returns:
        float: time difference
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    time_diff = time.perf_counter() - s
    return time_diff/n
