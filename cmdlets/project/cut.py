#!/usr/bin/env python3.7
import argparse
from sys import exit, stdin


def parse():
    #  ./cut.py file -d ' ' -f 1,3
    #  ./cut.py file -d ',' -f 1-2
    #  ./cut.py -d ',' -f 1-2
    # , type=int, choices=range(10)
    help = "This module works like a simple cut terminal command."
    parser = argparse.ArgumentParser(description=help)
    parser.add_argument('file', type=str, help='an input file',
                        nargs='*', default=None)
    parser.add_argument('-d', type=str,
                        help='a character to separate the columns of data',
                        default='   ')
    parser.add_argument('-f', help='number of a column to be displayed')
    args = parser.parse_args()
    print(args, '\n')
    breakpoint()
    return args


def read_file(file):
    try:
        # polish signs - how to use them?
        with open(file, 'r', errors='ignore') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print('No file found.')
        exit(1)
    return lines


def display(lines, args):
    columns_num = []
    for column in args.f.split(','):
        try:
            if '-' in column:
                range_num = column.split('-')
                print(range_num)
                for i in range(int(range_num[0]), int(range_num[1])+1):
                    columns_num.append(i)
            else:
                columns_num.append(int(column))
        except (AttributeError, ValueError):
            raise SyntaxError("f-flag syntax examples: -f 1-2, -f 1,3 (only positive numbers)")
    for line in lines:
        words = line.split(args.d)
        try:
            for index in columns_num:
                print(words[index-1], end=' ')
            print()
        except IndexError:
            print()
            continue


def main():
    args = parse()
    lines = []
    if args.file:
        text = read_file(args.file)
        for line in text:
            lines.append(line.strip('\n'))
    else:
        lines = stdin.readlines()
    display(lines, args)


if __name__ == '__main__':
    main()