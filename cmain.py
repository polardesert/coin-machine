#!/usr/bin/env python
"""coin-machine program, by Usman Ahmad
Executions on how to run cmain.py in Anaconda Command prompt (Python 3.x):

To compute the number of odd ways to sum to £0-50, £2-, £10-, £100-
RUN: python cmain.py
After calculating the number of ways for these amounts, an interpreter will be
opened allowing the following types of executions:
e.g. <cmain> £123-45            # calculate odd number of ways
e.g. <cmain> £123-45 odd        # calculate odd number of ways
e.g. <cmain> £123-45 even       # calculate even number of ways
e.g. <cmain> £123-45 all        # calculate all number of ways
e.g. <cmain> help               # show this help screen
e.g. <cmain> quit               # exit the program

Generally, to compute the number of odd ways to sum £{pounds}-{pence}
RUN: python cmain.py £{pounds}-{pence}
e.g. python cmain.py £123-45
e.g. python cmain.py £123-
e.g. python cmain.py £123-45 odd
e.g. python cmain.py £123-45 even
e.g. python cmain.py £123-45 all
e.g. python cmain.py £1000-

NOTEs:
- for "£1000-" elapsed time is ~15 secs on a 32GB RAM i7 2.60Ghz SSD machine
- all upper and lower case strings are handled on the "odd", "even", "all" params
- US Dollar denominations are handled via $ symbol e.g. $123-45 (see coin_denom.py)
"""


from typing import Optional, Union, Dict
import sys
import traceback
from src.coin_machine import dispense_count, dispense_odd_count, NWays


__author__ = "Usman Ahmad"
__version__ = "1.0.1"
DOCS = __doc__


def main_coin_calc(in_amt: str,
                   nways_type: Optional[NWays] = NWays.ODD
                   ) -> Union[int, Dict[str, int]]:
    """

    :param in_amt:
    :param nways_type:
    :return:
    """
    num_ways = dispense_count(in_amt)
    if nways_type is None:
        return num_ways
    else:
        return num_ways[nways_type]


def run_inter():
    """

    :return:
    """
    in_args = ""
    print("\npress ENTER / RETURN key to continue...")
    input()
    print(DOCS)
    while not (in_args == "QUIT"):
        in_args = input("<cmain> ").upper()
        gen_commands = ["HELP", "QUIT"]
        if in_args.upper() not in gen_commands:
            try:
                print(main_coin_calc(*in_args.split(chr(32))))
            except (AssertionError, TypeError):
                print("Error: ",
                      "\n".join(traceback.format_exc().splitlines()[-2:]),
                      "\nPlease type 'help' for guidance.\n")

        else:
            if in_args == "HELP":
                print(DOCS)
    print("coin-machine program ending.")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        if args[0].upper() == "HELP":
            print(DOCS)
        else:
            args = [x.upper() if isinstance(x, str) else x for x in args]
            print(main_coin_calc(*args))
    else:  # calculate number of ways for 50p, £2, £10, £100
        amounts = ["£0-50", "£2-", "£10-", "£100-"]
        print("Computing odd number of ways to sum the following amounts:")
        for amt in amounts:
            print(f"Input: {amt} \t Output: {dispense_odd_count(amt)}")
        run_inter()
