#!/usr/bin/env python
"""
Test geometric power series generating functions based on coin denomninations.
Calculating all and alternative number of ways.
"""

import unittest
from typing import List
from parameterized import parameterized
from src.denominations import DENOM
from src.coin_gen import coins_gen_fun


__author__ = "Usman Ahmad"
__version__ = "1.0.1"


class TestCoinGenFuncs(unittest.TestCase):
    @parameterized.expand([
        # all number of ways using £ denomination coins
        [DENOM["£"], -1, 100, 4563],
        [DENOM["£"], -1, 50, 451],
        [DENOM["£"], -1, 5, 4],
        [DENOM["£"], -1, 1, 1],
        [DENOM["£"], -1, 0, 1],

        # alternative number of ways using £ denomination coins
        [DENOM["£"], +1, 100, 1],
        [DENOM["£"], +1, 99, 4],
        [DENOM["£"], +1, 97, -6],
        [DENOM["£"], +1, 50, 1],
        [DENOM["£"], +1, 25, -2],
        [DENOM["£"], +1, 17, -2],
        [DENOM["£"], +1, 15, 0],
        [DENOM["£"], +1, 5, -2],
        [DENOM["£"], +1, 1, -1],
        [DENOM["£"], +1, 0, 1],

        # all number of ways using $ denomination coins
        [DENOM["$"], -1, 100, 293],
        [DENOM["$"], -1, 50, 50],
        [DENOM["$"], -1, 5, 2],
        [DENOM["$"], -1, 1, 1],
        [DENOM["$"], -1, 0, 1],

        # alternative number of ways using $ denomination coins
        [DENOM["$"], +1, 100, 19],
        [DENOM["$"], +1, 99, -18],
        [DENOM["$"], +1, 98, 18],
        [DENOM["$"], +1, 50, 10],
        [DENOM["$"], +1, 25, -5],
        [DENOM["$"], +1, 17, -2],
        [DENOM["$"], +1, 15, -2],
        [DENOM["$"], +1, 5, -2],
        [DENOM["$"], +1, 1, -1],
        [DENOM["$"], +1, 0, 1],
    ])
    def test_coin_gen(self, coins: List[int], gen_val: int, nth_coeff: int,
                      exp_val: int):
        cgen = coins_gen_fun(coins, gen_val)
        [next(cgen) for _ in range(nth_coeff)]
        self.assertEqual(next(cgen), exp_val)
