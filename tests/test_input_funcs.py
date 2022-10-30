#!/usr/bin/env python
"""
Test input functions converting string to int
i.e. £{pounds}-{pence} --> pounds * 100 + pence
"""

import unittest
from parameterized import parameterized
from src.input_funcs import cnvt_str_int

__author__ = "Usman Ahmad"
__version__ = "1.0.1"


class TestInputFuncs(unittest.TestCase):
    @parameterized.expand([
        ["£-", 0], ["£0-", 0], ["£-0", 0], ["£1234567-98", 123456798],
        ["£1000-23", 100023], ["£4-5", 405], ["£4-05", 405], ["£4-50", 450],
        ["£0-43", 43], ["£0-3", 3]
    ])
    def test_pound_input_funcs(self, in_str_val: str, out_exp_val: int):
        int_val, ccy_symbol = cnvt_str_int(in_str_val)
        self.assertEqual(int_val, out_exp_val)
        self.assertEqual(ccy_symbol, "£")

    @parameterized.expand([
        ["$-", 0], ["$0-", 0], ["$-0", 0], ["$1234567-98", 123456798],
        ["$1000-23", 100023], ["$4-5", 405], ["$4-05", 405], ["$4-50", 450],
        ["$0-43", 43], ["$0-3", 3]
    ])
    def test_dollar_input_funcs(self, in_str_val: str, out_exp_val: int):
        int_val, ccy_symbol = cnvt_str_int(in_str_val)
        self.assertEqual(int_val, out_exp_val)
        self.assertEqual(ccy_symbol, "$")
