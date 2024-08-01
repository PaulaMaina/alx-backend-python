#!/usr/bin/env python3


def sum_list(input_list: list[float]) -> float:
    """Takes a list of floats and returns their sum"""
    total = 0.0

    for num in input_list:
        total += num
    return total
