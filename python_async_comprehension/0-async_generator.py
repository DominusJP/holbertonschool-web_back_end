#!/usr/bin/env python3
"""python_async_comprehension coroutine"""
from asyncio import sleep
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async_generator"""
    for _ in range(10):
        await sleep(1)
        yield random.uniform(0, 10)