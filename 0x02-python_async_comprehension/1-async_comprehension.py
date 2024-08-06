#!/usr/bin/env python3
"""Async comprehensions"""
from typing import List


async_generator = __import__("0-async_genereator").async_generator


async def async_comprehension() -> List[float]:
    """Returns 10 random numbers"""
    return [result async for result in async_generator()]
