#!/usr/bin/env python3
"""
Has a type-annotated function sum_list.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    It takes a list input_list of floats as argument
    and returns their sum as a float.
    """

    total: float = 0
    for x in input_list:
        total += x

    return total
