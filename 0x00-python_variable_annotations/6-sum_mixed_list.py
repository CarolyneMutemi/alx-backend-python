#!/usr/bin/env python3
"""
Has a type-annotated function sum_mixed_list.
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    """
    It takes a list mxd_lst of integers and floats
    and returns their sum as a float.
    """

    total: float = 0
    for x in mxd_list:
        total += x
    return total
