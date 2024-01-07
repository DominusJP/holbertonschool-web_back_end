#!/usr/bin/env python3
"""
Python - Variable Annotations

"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing elements from lst and their respective lengths."""
    return [(i, len(i)) for i in lst]