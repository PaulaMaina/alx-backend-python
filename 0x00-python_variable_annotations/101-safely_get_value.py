#!/usr/bin/env python3
"""Safely get value function"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')
result = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """Returns the value using a key"""
    if key in dct:
        return dct[key]
    else:
        return default
