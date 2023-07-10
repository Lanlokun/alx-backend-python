#!/usr/bin/env python3
""" Measure the runtime """

from asyncio import run
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime """
    start = perf_counter()
    run(wait_n(n, max_delay))
    end = perf_counter()
    return (end - start) / n
