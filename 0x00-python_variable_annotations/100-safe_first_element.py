#!/usr/bin/env python3
""" Duck """
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ first """
    if lst:
        return lst[0]
    else:
        return None
