#!/usr/bin/env python3
"""
    python_async_comprehension
    
"""
import random
import asyncio


async def async_generator():
    """0-async_generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)