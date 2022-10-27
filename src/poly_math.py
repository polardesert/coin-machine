#!/usr/bin/env python
"""

"""
from typing import List, Generator

__author__ = "Usman Ahmad"
__version__ = "1.0.1"


def poly_series(poly: List[int]):
    """
    Generator function to create polynomical series
    :param poly:
    :return:
    """
    yield from poly
    while True:
        yield 0


def poly_divide(func: Generator, poly: List[int]):
    """

    :param func: generator of series coefficients
    :param poly: polynomial list
    :return:
    """
    """f is a generator of series coefficients.  g is a polynomial."""

    poly = list(poly)
    numer = [next(func) for _ in range(len(poly) - 1)]
    numer.append(0)  # this is the location "bringing down" the next term of f goes

    for term in func:
        numer[-1] = term
        coeff = numer[0] // poly[0]

        # assert all terms are integers
        assert numer[0] - coeff * poly[0] == 0

        yield coeff

        for i in range(len(poly) - 1):
            numer[i] = numer[i+1] - coeff * poly[i + 1]
