#!/usr/bin/env python3
import argparse
from sys import exit, stdin


def parse():
    help = "This module works like a cut cmdlet but it's much simpler and less functional."
    parser = argparse.ArgumentParser(description=help)
    parser.add_argument('file', type=str, help='an input file', nargs='*', default=None)
    parser.add_argument('-d', type=str, help='a character to separate columns of data', default='   ')
    parser.add_argument('-f', help='number of column to be displayed')
    args = parser.parse_args()
    # print(args, '\n')
    return args


def read_file(file):
    try:
        with open(file, 'r', errors='ignore') as f:  # polish signs how to use them
            lines = f.readlines()
    except FileNotFoundError:
        print('No file found.')
        exit(1)
    return lines


def display(lines, args):
    columns_num = []
    for column in args.f.split(','):
        if '-' in column:
            range_num = column.split('-')
            for i in range(int(range_num[0]), int(range_num[1])+1):
                columns_num.append(i)
        else:
            columns_num.append(int(column))
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
    if args.file == '-':
        lines = stdin.readlines()
    else:
        text = read_file(args.file)
        for line in text:
            lines.append(line.strip('\n'))
    display(lines, args)


if __name__ == '__main__':
    main()