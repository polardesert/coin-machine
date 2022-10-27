#!/usr/bin/env python
"""
Functions for converting string "£{pounds}-{pence}" to int of pounds * 100 + pence
"""

from typing import Tuple
from src.denominations import DENOM

__author__ = "Usman Ahmad"
__version__ = "1.0.1"


def cnvt_str_int(str_val: str) -> Tuple[int, str]:
    """

    :param str_val:
    :return:
    """
    ccy_symbol = str_val[0]
    assert ccy_symbol in DENOM.keys()  # assert denomination symbol is correct
    assert "-" in str_val

    str_val = str_val[1:]
    amount = str_val.split("-")
    assert len(amount) == 2

    # major_denom is either e.g. Pounds or Dollar
    # minor_denom is either e.g. Pence or Cents
    major_denom = amount[0]
    minor_denom = amount[1]
    assert len(minor_denom) <= 2
    major_denom = major_denom if len(major_denom) else 0
    minor_denom = minor_denom if len(minor_denom) else 0
    assert isint(major_denom) and isint(minor_denom)

    major_denom = int(major_denom)
    minor_denom = int(minor_denom)

    return major_denom * 100 + minor_denom, ccy_symbol


def isint(in_str: str) -> bool:
    """

    :param in_str:
    :return:
    """
    try:
        int(in_str)
        return True
    except ValueError:
        return False
