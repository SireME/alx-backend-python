#!/usr/bin/env python3
"""
In this module we execute multiple
 coroutines at the same time with async
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run several asyncronous coroutines.

    Args:
        n (int): total number of times to run awaitable function
        max_delay (int): Maximum delay in seconds. Defaults to 10.

    Returns:
        float: Random delay.
    """
    run_list: List[float] = []
    for _ in range(n):
        vl = await wait_random(max_delay)
        run_list.append(vl)
    return sorted(run_list)
