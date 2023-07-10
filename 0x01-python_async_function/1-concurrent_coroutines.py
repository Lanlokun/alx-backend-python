#!/usr/bin/env python3

""" Let's execute multiple coroutines at the same time with async """    

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """ return list of delays in ascending order """
    delays = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
