#!/usr/bin/env python
"""

"""

import unittest
from typing import List, Tuple, Dict
from itertools import combinations_with_replacement
from parameterized import parameterized
from bisect import bisect
from src.denominations import DENOM
from src.coin_machine import NWays
from src.coin_gen import calc_coins
from src.coin_machine import calc_number_coins, dispense_odd_count

__author__ = "Usman Ahmad"
__version__ = "1.0.1"


def find_coin_combination(amount: int, coins: List[int]) -> List[Tuple[int, ...]]:
    """
    Compute all lists of denominations which sum up to the target amount in a
    brute force manner

    e.g. amount = 5, coins = DENOM["£"]
    Result: [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (5,)]

    :param amount:
    :param coins:
    :return:
    """
    combinations = []
    for i in range(amount, -1, -1):
        for j in range(amount, -1, -1):
            in_arr = coins[0:bisect(coins, i)]
            for in_combo in combinations_with_replacement(in_arr, j):
                combo_sum = sum(in_combo)
                if (combo_sum == amount) and (in_combo not in combinations):
                    combinations.append(in_combo)
    print(f" Result: {amount} can be summed in the following ways: {combinations}")
    return combinations


def calc_combo_num_coins(amount: int, coins: List[int]) -> Dict[str, int]:
    combo = find_coin_combination(amount, coins)
    odd, even = [], []
    for coin_set in combo:
        if len(coin_set) % 2 == 1:
            odd.append(coin_set)
        elif len(coin_set) % 2 == 0:
            even.append(coin_set)
    return {NWays.ODD: len(odd), NWays.EVEN: len(even), NWays.ALL: len(combo)}


class TestCoinCalc(unittest.TestCase):
    @parameterized.expand([["£0-", 0], ["£-0", 0], ["£0-5", 3], ["£-1", 1],
                           ["£0-50", 225], ["£2-", 36840], ["£10-", 160667940],
                           ["£10-", 160667940], ["£100-", 566936652323775]])
    def test_dispense_odd_count_vs_vals(self, str_amt: str, exp_val: int):
        """

        :param str_amt:
        :param exp_val:
        :return:
        """
        self.assertEqual(dispense_odd_count(str_amt), exp_val)

    @parameterized.expand([[c, sym, DENOM[sym]]
                           for c in range(20) for sym in ("£", "$")])
    def test_dispense_odd_count_vs_combo(
            self, amount: int, sym: str, coins: List[int]):
        """
        Testing dispense_odd_count

        :param amount:
        :param sym:
        :param coins:
        :return:
        """
        # convert int amount to str e.g. 555 --> £5.55
        str_amt = f"{sym}{amount // 100}-{amount % 100}"
        self.assertEqual(dispense_odd_count(str_amt),
                         calc_combo_num_coins(amount, coins)[NWays.ODD])

    @parameterized.expand([[c, DENOM[sym]] for c in range(20) for sym in ("£", "$")])
    def test_calc_number_coins(self, amount: int, coins: List[int]):
        """
        Testing calc_number_coins for odd number of coins

        :param amount:
        :param coins:
        :return:
        """
        self.assertEqual(calc_number_coins(amount, coins)[NWays.ODD],
                         calc_combo_num_coins(amount, coins)[NWays.ODD])

    @parameterized.expand([[c, DENOM[sym]] for c in range(20) for sym in ("£", "$")])
    def test_coin_gen_val(self, amount: int, coins: List[int]):
        """
        Testing calc_coins for all number of coins

        :param amount:
        :param coins:
        :return:
        """
        self.assertEqual(calc_coins(coins, amount, -1),
                         calc_combo_num_coins(amount, coins)[NWays.ALL])

    @parameterized.expand(
        [
            [0, DENOM["£"], [()]],
            [1, DENOM["£"], [(1,)]],
            [2, DENOM["£"], [(1, 1), (2,)]],
            [3, DENOM["£"], [(1, 1, 1), (1, 2)]],
            [4, DENOM["£"], [(1, 1, 1, 1), (1, 1, 2), (2, 2)]],
            [5, DENOM["£"], [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (5,)]],
            [6, DENOM["£"], [(1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 2), (1, 1, 2, 2),
                             (2, 2, 2), (1, 5)]],
            [7, DENOM["£"], [(1, 1, 1, 1, 1, 1, 1),
                             (1, 1, 1, 1, 1, 2),
                             (1, 1, 1, 2, 2),
                             (1, 2, 2, 2),
                             (1, 1, 5),
                             (2, 5)]],
            [10, DENOM["£"], [(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                              (1, 1, 1, 1, 1, 1, 1, 1, 2),
                              (1, 1, 1, 1, 1, 1, 2, 2),
                              (1, 1, 1, 1, 2, 2, 2),
                              (1, 1, 1, 1, 1, 5),
                              (1, 1, 2, 2, 2, 2),
                              (1, 1, 1, 2, 5),
                              (2, 2, 2, 2, 2),
                              (1, 2, 2, 5),
                              (5, 5),
                              (10,)]],
            [19, DENOM["£"],
             [(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
              (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2),
              (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2),
              (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2),
              (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5),
              (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2),
              (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 5),
              (1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2),
              (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 5),
              (1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2),
              (1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 5),
              (1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2),
              (1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5),
              (1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 5),
              (1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2),
              (1, 1, 1, 1, 1, 1, 1, 1, 1, 10),
              (1, 1, 1, 1, 1, 1, 1, 2, 5, 5),
              (1, 1, 1, 1, 2, 2, 2, 2, 2, 5),
              (1, 2, 2, 2, 2, 2, 2, 2, 2, 2),
              (1, 1, 1, 1, 1, 1, 1, 2, 10),
              (1, 1, 1, 1, 1, 2, 2, 5, 5),
              (1, 1, 2, 2, 2, 2, 2, 2, 5),
              (1, 1, 1, 1, 1, 2, 2, 10),
              (1, 1, 1, 2, 2, 2, 5, 5),
              (2, 2, 2, 2, 2, 2, 2, 5),
              (1, 1, 1, 1, 5, 5, 5),
              (1, 1, 1, 2, 2, 2, 10),
              (1, 2, 2, 2, 2, 5, 5),
              (1, 1, 1, 1, 5, 10),
              (1, 1, 2, 5, 5, 5),
              (1, 2, 2, 2, 2, 10),
              (1, 1, 2, 5, 10),
              (2, 2, 5, 5, 5),
              (2, 2, 5, 10)]]
        ]
    )
    def test_find_coin_combo(
            self, amount: int, coins: List[int],
            exp_val: List[Tuple[int, ...]]
    ):
        """
        Testing find_coin_combination i.e. testing the function we will use to test
        coins_gen_fun.

        This will generate all possible combinations to give the target amount
        using the denomination coins

        :param amount:
        :param coins:
        :param exp_val:
        :return:
        """
        self.assertEqual(find_coin_combination(amount, coins), exp_val)
