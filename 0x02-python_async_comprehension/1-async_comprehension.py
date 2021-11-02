#!/usr/bin/env python3
"""async_comprehension py """

from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """[summary]
    Returns:
        list(float)
    Yields:
        Generator(int)
    """
    return [x async for x in async_generator()]
