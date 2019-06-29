#!/usr/bin/env python3
import argparse
import re
from sys import exit, stdin


def parse():
    help = "This module works like a simple sed cmdlet."
    parser = argparse.ArgumentParser(description=help)
    parser.add_argument('parameters', type=str,
                        help='parsing parameters e.g s/old/new/g')
    parser.add_argument('file', type=str, help='an input file',
                        nargs='*', default=None)
    args = parser.parse_args()
    # print(args, '\n')  # used for debugging
    return args


def open_files(in_file):
    lines = []
    for file in in_file:
        try:
            with open(file, 'r', errors='ignore') as text_file:             
                for line in text_file.readlines():
                    lines.append(line.strip('\n'))
        except FileNotFoundError:
            print(f'No file {file} found.')
            exit(1)
        return lines


def get_arguments(args):
    in_file = args.file
    arguments = args.parameters.strip("'").split("/")  # 's/old/new/g' or 's/old/new/'
    try:
        s_flag, old, new, g_flag = arguments[0:4]
        # print(s_flag, old, new, g_flag, in_file)
    except ValueError:
        print('Not enough parameters.\nExample: ./sed.py s/old/new/g or without g-flag: just ./sed.py s/old/new/g')
        exit(1)
    return s_flag, old, new, g_flag, in_file


def get_std_in():
    lines = []
    for line in stdin.readlines():
        lines.append(line.strip('\n'))
    return lines


def sed(args):
    s_flag, old, new, g_flag, in_file = get_arguments(args)
    # if file given
    if in_file:
        lines = open_files(in_file)
    else:
        lines = get_std_in()
    if g_flag:
        count = 0
    else:
        count = 1
    for line in lines:
        print(re.sub(old, new, line, count))


def main():
    sed(parse())


if __name__ == '__main__':
    main()
