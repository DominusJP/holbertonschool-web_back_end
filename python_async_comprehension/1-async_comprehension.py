#!/usr/bin/env python3
"""
    python_async_comprehension
"""
import asyncio


async_generator = __import__('0-async_generator').async_generator
async def async_comprehension():
    """01_async_comprehension"""
    return [i async for i in async_generator()]