#!/usr/bin/env python3

""" 0. The basics of async """

import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ return random delay """
    random_float = __import__('random').uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
