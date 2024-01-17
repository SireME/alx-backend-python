#!/usr/bin/env python3
"""
Async Generator Module

This module defines an asynchronous generator
 coroutine that yields random numbers
between 0 and 10 after waiting for 1 second asynchronously.

"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Async Generator Coroutine

    This coroutine loops 10 times, waits asynchronously
      for 1 second in each iteration,
    and yields a random number between 0 and 10.

    Yields:
        float: A random float between 0 and 10.

    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
