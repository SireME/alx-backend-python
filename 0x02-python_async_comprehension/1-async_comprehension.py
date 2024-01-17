#!/usr/bin/env python3
"""
Async Comprehension Module

This module defines an asynchronous comprehension
 coroutine that collects 10 random numbers
using async_generator.

"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Async Comprehension Coroutine

    This coroutine collects 10 random numbers
      using async comprehensions over async_generator.

    Returns:
        List[float]: A list containing 10 random numbers.

    """
    return [i async for i in async_generator()]
