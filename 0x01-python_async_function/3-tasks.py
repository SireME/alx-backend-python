#!/usr/bin/env python3
"""
In this module we return an async task from a regular function
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    create and return an asyncio Task

    Args:
        max_delay (int): Maximum delay in seconds. Defaults to 10.

    Returns:
        asyncio.Task class
    """
    return asyncio.ensure_future(wait_random(max_delay))