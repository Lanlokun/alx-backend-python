#!/usr/bin/env python3
""" duck typing first element of a sequence """

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ return first element of list or None """
    if lst:
        return lst[0]
    else:
        return None
