#!/usr/bin/env python3
""" more involved type annotations """

from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[None, T] = None) -> Union[Any, T]:
    """return value of key if it exists, otherwise return default """
    if key in dct:
        return dct[key]
    else:
        return default
