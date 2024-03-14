#!/usr/bin/env python3
"""
Has annotated function element_length.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes in an iterable and returns a list of tuples
    containing the elements plus length of the element.
    """
    return [(i, len(i)) for i in lst]
