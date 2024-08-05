#!/usr/bin/env python3
"""Async routine"""
import asyncio
from typing import List


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of the delays as floating numbers"""
    delays = await asyncio.gather(
        *list(map(lambda _: task_wait_random(max_delay), range(n)))
    )

    return sorted(delays)
