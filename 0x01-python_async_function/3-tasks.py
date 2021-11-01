#!/usr/bin/env python3
""" create Task """


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """[summary]
    Args:
        max_delay ([type])
    Returns:
        [type]
    """
    return asyncio.Task(wait_random(max_delay))
