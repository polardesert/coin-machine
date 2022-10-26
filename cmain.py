#!/usr/bin/env python
"""

"""

from typing import Optional, Union, Dict
import sys
from src.coin_machine import dispense_count, dispense_odd_count, NWays

__author__ = "Usman Ahmad"
__version__ = "1.0.1"


def main(amount: str,
         nways_type: Optional[NWays] = NWays.ODD) -> Union[int, Dict[str, int]]:
    """

    :param amount:
    :param nways_type:
    :return:
    """
    num_ways = dispense_count(amount)
    if nways_type is None:
        return num_ways
    else:
        return num_ways[nways_type]


if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        args = [x.upper() if isinstance(x, str) else x for x in args]
        print(main(*args))
    else:  # calculate number of ways for 50p, £2, £10, £100
        amounts = ["£0-50", "£2-", "£10-", "£100-"]
        for amt in amounts:
            print(f"Input: {amt} \t Output: {dispense_odd_count(amt)}")
