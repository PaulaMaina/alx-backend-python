#!/usr/bin/env python3
"""This function a function that multiplies a float by multiplier"""


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Returns a function the multiplies a float by multiplier"""
    return lambda num: num * multiplier
