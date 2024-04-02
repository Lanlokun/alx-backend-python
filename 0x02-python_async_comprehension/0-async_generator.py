#!/usr/bin/env python3
""" Async Generator """

import asyncio
from typing import Generator
import secrets


async def async_generator() -> Generator[float, None, None]:
    """ Async Generator """
    for _ in range(10):
        await asyncio.sleep(1)
        yield secrets.SystemRandom().uniform(0, 10)
