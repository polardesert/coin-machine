#!/usr/bin/env python
"""

"""

import unittest
from parameterized import parameterized
from typing import Generator, List
from itertools import islice
from src.poly_math import poly_divide, poly_series

__author__ = "Usman Ahmad"
__version__ = "1.0.1"


def geometric_series(a: int, gen_val: int):
    """

    :param a:
    :param gen_val:
    :return:
                gen_val = -1 then 1/(1-ax)
                gen_val = +1 then 1/(1+ax)
    """
    return poly_divide(poly_series([1]), [1, gen_val * a])


def geometric_power_series(a: int, n: int, gen_val: int):
    """

    :param a:
    :param n:
    :param gen_val:
    :return:
                gen_val = -1 then 1/(1-ax^n)
                gen_val = +1 then 1/(1+ax^n)
    """
    """return 1/(1-ax^n)"""
    return poly_divide(poly_series([1]), [1] + [0] * (n-1) + [gen_val * a])


def fibonacci_series():
    """

    :return:
    """
    return poly_divide(poly_series([1]), [1, -1, -1])


class TestMathFuncs(unittest.TestCase):
    @parameterized.expand(
        [
            [
                geometric_series(2, -1),
                [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]],
            [
                geometric_series(2, +1),
                [1, -2, 4, -8, 16, -32, 64, -128, 256, -512, 1024]],
            [
                geometric_power_series(3, 2, -1),
                [1, 0, 3, 0, 9, 0, 27, 0, 81, 0, 243]],
            [
                geometric_power_series(3, 2, +1),
                [1, 0, -3, 0, 9, 0, -27, 0, 81, 0, -243]],
            [
                fibonacci_series(),
                [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]]
        ]
    )
    def test_series(
            self, in_poly_series: Generator,
            out_vals: List[List[int]]
    ):
        nth_order = 10
        self.assertEqual(list(islice(in_poly_series, 0, nth_order + 1)), out_vals)
