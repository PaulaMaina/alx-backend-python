#!/usr/bin/env python3
"""This function returns elements and their lengths as a tuple"""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns the length of an element in a list"""
    return [(i, len(i)) for i in lst]
