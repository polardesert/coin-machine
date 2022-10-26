#!/usr/bin/env python
"""Functions to calculate number of ways to dispense coins given a target amount.

coins_gen_fun creates a generating function to represent the number of ways to
sum up coins to the target amount.

calc_coins calculates the number of ways to sum up coins to the target amount.

Both functions employ gen_val (-1, +1) parameter to determine calculating either:
all(x) where gen_val = -1 which gives all sum combinations
alt(x) where gen_val = +1 which gives alternating sum combinations
"""

from typing import List, Dict
from bisect import bisect
from enum import Enum
from src.input_funcs import cnvt_str_int
from src.coin_gen import calc_coins
from src.coin_denom import DENOM

__author__ = "Usman Ahmad"
__version__ = "1.0.1"


class NWays(str, Enum):
    ALL = 'ALL'
    ODD = 'ODD'
    EVEN = 'EVEN'


def calc_number_coins(value: int, in_coins: List[int]) -> Dict[str, int]:
    """

    :param value:
    :param in_coins:
    :return:
    """
    bval = bisect(in_coins, value)
    all_x = calc_coins(in_coins[0:bval], value, -1)
    alt_x = calc_coins(in_coins[0:bval], value, 1)
    even_num = (all_x + alt_x) / 2
    # assert the number of even number ways is an integer
    assert even_num - round(even_num) == 0
    even_num = int(even_num)
    odd_num = all_x - even_num

    return {NWays.ALL: all_x, NWays.ODD: odd_num, NWays.EVEN: even_num}


def dispense_count(amount: str) -> Dict[str, int]:
    """
    Count ALL, ODD, EVEN number of ways to sum denomination coins to target amount
    :param amount: input string of e.g. "£{pounds}-{pence}"
    :return: number of ways to sum the amount using denomination coins
             returning for ALL, ODD and EVEN number of ways
    """
    amount_val, ccy_symbol = cnvt_str_int(amount)
    return calc_number_coins(amount_val, DENOM[ccy_symbol])


def dispense_odd_count(amount: str) -> int:
    """
    Count ODD number of ways to sum denomination coins to target amount
    :param amount: input string of e.g. "£{pounds}-{pence}"
    :return: ODD number of ways to sum the amount using denomination coins
    """
    return dispense_count(amount)[NWays.ODD]


def dispense_even_count(amount: str) -> int:
    """
    Count EVEN number of ways to sum denomination coins to target amount
    :param amount: input string of e.g. "£{pounds}-{pence}"
    :return: EVEN number of ways to sum the amount using denomination coins
    """
    return dispense_count(amount)[NWays.EVEN]


def dispense_all_count(amount: str) -> int:
    """
    Count ALL number of ways to sum denomination coins to target amount
    :param amount: input string of e.g. "£{pounds}-{pence}"
    :return: ALL number of ways to sum the amount using denomination coins
    """
    return dispense_count(amount)[NWays.ALL]
