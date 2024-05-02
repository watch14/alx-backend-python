#!/usr/bin/env python3
""" multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ multiplies a float by multiplier."""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
