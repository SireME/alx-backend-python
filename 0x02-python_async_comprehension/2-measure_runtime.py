#!/usr/bin/env python3
"""
Measure Runtime Module

This module defines a coroutine that measures the
 total runtime of executing async_comprehension
four times in parallel using asyncio.gather.

"""

from typing import List
from time import time
from asyncio import gather
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure Runtime Coroutine

    This coroutine executes async_comprehension
      four times in parallel using asyncio.gather
    and measures the total runtime.

    Returns:
        float: The total runtime in seconds.

    """
    start_time = time()

    # Execute async_comprehension four times in parallel
    await gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension())

    end_time = time()

    return end_time - start_time
