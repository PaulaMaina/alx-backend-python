#!/usr/bin/env python3
"""Async_generator Coroutine"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """Loops 10 times and yields a random number between 0 and 10"""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.random() * 10
