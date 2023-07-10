#!/usr/bin/env python3

""" execute multiple coroutines at the same time with async """

import asyncio
import heapq

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    delays = []

    async def wait_and_append_delay():
        delay = await wait_random(max_delay)
        heapq.heappush(delays, delay)

    tasks = [wait_and_append_delay() for _ in range(n)]
    await asyncio.gather(*tasks)

    sorted_delays = []
    while delays:
        sorted_delays.append(heapq.heappop(delays))

    return sorted_delays
