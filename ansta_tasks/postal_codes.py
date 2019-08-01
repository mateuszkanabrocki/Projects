#!/usr/bin/env python3

# postal_codes.py 2019-08-01
# Author: Mateusz Kanabrocki <mateusz.kanabrocki@gmail.com>
# Copyright: This module has been placed in the public domain
# https://github.com/mateuszkanabrocki/projects

"""
# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
# przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi

usage examples:
./postal_codes.py 79-900 80-155
./postal_codes.py 80-155 79-900
"""

__docformat__ = 'restructuredtext'

import os
from sys import argv
from typing import List

# 'kody.csv' is a file containing all polish postal codes
# file download site: http://www.kody-pocztowe.dokladnie.com/okreg8.php
data_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "kody.csv")


def main(data_file: str) -> List[str]:
    try:
        first_code = int(argv[1].replace('-', ''))
        last_code = int(argv[2].replace('-', ''))
    except ValueError:
        print("Wrong input values.")
        exit(1)

    # switch arguments if given in the wrong order
    if first_code > last_code:
        first_code, last_code = last_code, first_code

    with open(data_file, 'r', encoding='utf-8', errors='ignore') as file:
        # ignore the first line in the data file (column names)
        file.readline()
        codes = [line[0:6] for line in file
                 if first_code <= int(line[0:6].replace('-', '')) <= last_code]
        # remove duplicated codes - see the 'kody.csv' file
        final_codes = sorted(list(set(codes)))
        return final_codes


print(main(data_file))
