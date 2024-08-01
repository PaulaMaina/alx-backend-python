#!/usr/bin/env python3
"""This function takes a list of numbers and returns their sum as a float"""


def sum_list(input_list: list[float]) -> float:
    """Takes a list of floats and returns their sum"""
    total = 0.0

    for num in input_list:
        total += num
    return total
