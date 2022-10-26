#!/usr/bin/env python
"""Functions to calculate number of ways to dispense coins given a target amount.

coins_gen_fun creates a generating function to represent the number of ways to
sum up coins to the target amount.

calc_coins calculates the number of ways to sum up coins to the target amount.

Both functions employ gen_val (-1, +1) parameter to determine calculating either:
all(x) where gen_val = -1 which gives all sum combinations
alt(x) where gen_val = +1 which gives alternating sum combinations
"""

from typing import List, Optional, Dict
from bisect import bisect
from src.cfuncs import calc_coins

__author__ = "Usman Ahmad"
__version__ = "1.0.1"


class NWays(str):
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
    print(f"output: {odd_num}, all(x) = {all_x}, alt(x) = {alt_x}")
    return {NWays.ALL: all_x, NWays.ODD: odd_num, NWays.EVEN: even_num}


class CoinMachine(object):
    def __init__(self, coins: Optional[List[int]] = None):
        """

        :param coins: list of coins denomination
        """
        if coins is None:
            self.coins = [1, 2, 5, 10, 20, 50, 100, 200]

    def dispense_count(self, amount: int) -> Dict[str, int]:
        return calc_number_coins(amount, self.coins)


if __name__ == "__main__":
    cm = CoinMachine()
    ways = cm.dispense_count(33)
    print(ways)
