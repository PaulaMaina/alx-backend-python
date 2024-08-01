#!/usr/bin/env python3
"""This function returns a tuple"""


import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    Retuns a tuple with a string as the first element
    and the square of the second element as a float
    """
    return (k, float(v * v))
