#!/usr/bin/env python3
""" complex type-annotated to mixed list """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ return sum of list of floats and ints """
    return sum(mxd_lst)
