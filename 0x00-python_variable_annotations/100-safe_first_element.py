#!/usr/bin/env python3
"""
Has annotated function safe_first_element.
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Takes in a sequence and returns the first element or None.
    """
    if lst:
        return lst[0]
    else:
        return None
