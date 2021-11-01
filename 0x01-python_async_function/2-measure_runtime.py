#!/usr/bin/env python3
""" asynchronous coroutine """

from typing import List
import random
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """[summary]
    Args:
        n (int)
        max_delay (int)
    Returns:
        float(floating numbers)
    """

    t0 = time.time()
    asyncio.run(wait_n(n, max_delay))
    return ((time.time() - t0) / n)