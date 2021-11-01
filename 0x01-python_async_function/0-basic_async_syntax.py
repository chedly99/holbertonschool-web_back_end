#!/usr/bin/env python3
""" asynchronous coroutine python """

import random
import asyncio


async def wait_random(max_delay: int = 10 ) -> float:
    delay = random(0, max_delay)
    await asyncio.sleep(delay)
    return delay