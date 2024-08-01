#!/usr/bin/env python3
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """Returns the length of an element in a list"""
    return [(i, len(i)) for i in lst]