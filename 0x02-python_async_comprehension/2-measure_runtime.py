#!/usr/bin/env python3
"""Measure coroutine runtime"""
import asyncio
import time


async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_time() -> float:
    """Returns the total runtime"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.time() - start

    return total_time
