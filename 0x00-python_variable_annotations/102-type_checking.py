#!/usr/bin/env python3
""" type checking """

from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ return list """
    zoomed_in: List[Any] = [
        item for item in list(lst)
        for i in range(factor)
    ]
    return zoomed_in
