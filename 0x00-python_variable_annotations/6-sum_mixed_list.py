#!/usr/bin/env python3
"""This function returns the sum of a list elements as a float"""


import typing


def sum_mixed_list(mxd_list: typing.List[typing.Union[int, float]]) -> float:
    """Returns the sum of a mixed list as a float"""
    total = 0.0

    for num in mxd_list:
        total += float(num)

    return total
