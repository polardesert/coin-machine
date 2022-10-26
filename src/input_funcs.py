#!/usr/bin/env python
"""
Functions for converting string "£{pounds}-{pence}" to int of pounds * 100 + pence
"""

from typing import Tuple
from src.coin_denom import DENOM

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

    pounds = amount[0]
    pence = amount[1]
    pounds = pounds if len(pounds) else 0
    pence = pence if len(pence) else 0
    assert isint(pounds) and isint(pence)

    pounds = int(pounds)
    pence = int(pence)

    return pounds * 100 + pence, ccy_symbol


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
