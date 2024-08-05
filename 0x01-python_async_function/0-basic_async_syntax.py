#!/usr/bin/env python3
"""Asynchronous coroutine wait_random"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Returns the amount of time waited"""
    wait_amount: float = random.random() * max_delay
    await asyncio.sleep(wait_amount)

    return wait_amount
