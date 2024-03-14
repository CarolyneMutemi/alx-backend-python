#!/usr/bin/env python3
"""
Has a type-annotated function make_multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Generates a multiplier function and returns it.
    """
    def made_multiplier(num: float) -> float:
        """
        Multiplies two numbers.
        """

        return num * multiplier
    return made_multiplier
