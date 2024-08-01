#!/usr/bin/env python3


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Returns a function the multiplies a float by multiplier"""
    return multiplier * multiplier
