#!/usr/bin/env python3
""" more involved type annotations """

from typing import Mapping, Any, Union, TypeVar


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[TypeVar('T'), None]) -> Union[Any, TypeVar('T')]:
    """ return value of key or default """
    if key in dct:
        return dct[key]
    else:
        return default
