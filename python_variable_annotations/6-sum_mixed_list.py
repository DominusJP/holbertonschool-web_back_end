#!/usr/bin/env python3
"""
Python - Variable Annotations

"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of the given list of integers and floats."""
    return sum(mxd_lst)