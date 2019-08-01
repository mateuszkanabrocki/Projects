#!/usr/bin/env python3

# missing_elements.py 2019-08-01
# Author: Mateusz Kanabrocki <mateusz.kanabrocki@gmail.com>
# Copyright: This module has been placed in the public domain
# https://github.com/mateuszkanabrocki/projects

"""
# ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n.
# NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
# 1-n = [1,2,3,4,5,...,10]
# np. n=10
# wejście: [2,3,7,4,9], 10
# wyjście: [1,5,6,8,10]

usage examples:
./missing_elements.py [2,3,7,4,9] 10
"""

__docformat__ = 'restructuredtext'


from sys import argv
from typing import List


def main() -> List[int]:

    input_list = argv[1]
    list_length = argv[2]

    if int(list_length) < 0:
        print("Value of 'list_length' should be greater than 0.")
        exit(1)

    # change input_list string into a list
    given_list = [int(item)
                  for item in input_list.strip('[').strip(']').split(',')]

    if len(given_list) > len(set(given_list)):
        print("'input_list' should have unique elements.")
        exit(1)

    missing_elements = [i for i in range(1, int(list_length)+1)]
    missing_elements = list(set(missing_elements) - set(given_list))

    return missing_elements


print(main())
