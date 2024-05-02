#!/usr/bin/env python3
""" tuple """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ convert """
    return k, float(v) ** 2
