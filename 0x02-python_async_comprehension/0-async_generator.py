#!/usr/bin/env python3
""" asynchronous generator py """


from typing import Generator
import random
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """[summary]
    async function generator
    Yields:
        Generator(floats)
    """
    for _ in range(10):
        x = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield x
