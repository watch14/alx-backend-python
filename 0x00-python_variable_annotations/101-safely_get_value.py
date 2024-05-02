#!/usr/bin/env python3
""" annotatuion """
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, T], key: Any, default: Union[T, None] = None
        ) -> Union[T, None]:
    """annotation"""
    if key in dct:
        return dct[key]
    else:
        return default
