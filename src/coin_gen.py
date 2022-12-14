#!/usr/bin/env python
"""
Functions to dynamically create generating functions that calculate the number of
ways to sum up to a target amount using a set of coin denominations
"""
from itertools import islice
from typing import List, Generator
from src.poly_math import poly_series, poly_divide

__author__ = "Usman Ahmad"
__version__ = "1.0.1"


def coins_gen_fun(coins: List[int], gen_val: int = -1) -> Generator:
    """
    Create generating function for the number of ways to sum a particular
    amount of coins.

    The generating function is a product series of geometric power series where each
    of the exponents in the denominator are the coin denominations.

    When gen_val = -1 the coefficient of the Xth term of the power series is the
    total number of ways to sum the amount of X using the coin denominations

    When gen_val = +1 the coefficient of the Xth term of the power series is the
    alternative number of ways to sum the amount of X using the coin denominations

    :param coins: denomination of coins
    :param gen_val:
                    -1 gives usual geometric type power series 1 / ( 1 - a*x)
                    This gives all number of ways to sum coins to the target amount
                    all(x)

                    +1 gives alternating geometric type power series 1 / (1 + a*x)
                    This gives all alternating ways to sum coins to the target amount
                    alt(x)

                    In calc_coins function we calculate the ways to sum to the
                    target amount where the number of coins are odd.
    :return: generating function representing number of ways
    """
    if not coins:
        return poly_series([1])
    else:
        c = coins[0]  # head of the coins
        return poly_divide(
            # recurse through the rest of the coins
            coins_gen_fun(coins[1:], gen_val),

            # denominator
            # gen_val = -1 -> 1/(1-x^c1) * 1/(1-x^c2) * ... * 1/(1-x^cn)
            # gen_val = 1 -> 1/(1+x^c1) * 1/(1+x^c2) * ... * 1/(1+x^cn)
            [1] + [0] * (c - 1) + [gen_val]
        )


def calc_coins(coins: List[int], target: int, gen_val: int) -> int:
    """
    Calculate number of ways to sum coins to target amount
    gen = -1 -> all number of ways
    gen = 1 -> alternating number of ways

    :param coins: denomination of coins
    :param target: target amount to dispense through coins
    :param gen_val: see gen_val parameter in coins_gen_fun function docstring
    :return:
    """
    return next(islice(coins_gen_fun(coins, gen_val), target, None))
