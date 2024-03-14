#!/usr/bin/env python3
"""
Has a type-annotated function to_kv.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes in the two arguments and returns a tuple.
    """

    squareV: float = v ** 2

    return (k, squareV)
