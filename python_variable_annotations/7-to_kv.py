#!/usr/bin/env python3
"""
Python - Variable Annotations

"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with the first element as string k and the second element as the square of int/float v (annotated as float)."""
    return (k, v ** 2)