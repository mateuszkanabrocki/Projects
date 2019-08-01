#!/usr/bin/env python3

# list.py 2019-08-01
# Author: Mateusz Kanabrocki <mateusz.kanabrocki@gmail.com>
# Copyright: This module has been placed in the public domain
# https://github.com/mateuszkanabrocki/projects

"""
# ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5,
# DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.

usage examples:
./list.py
./list.py 1 10 0.25
"""

__docformat__ = 'restructuredtext'

import decimal


def drange(start=2, stop=5, step=0.5, precision=None):
    """drange generates a set of Decimal values over the
    range [start, stop) with given step"""

    # set precision
    if precision is not None:
        decimal.getcontext().prec = precision
    # convert values to decimals
    start = decimal.Decimal(start)
    stop = decimal.Decimal(stop)
    step = decimal.Decimal(step)
    # create a generator expression for the index values
    numbers_list = []
    i = start
    while i <= stop:
        numbers_list.append(i)
        i += step
    return numbers_list


print(drange())
# print(drange(1, 10, 0.25))
