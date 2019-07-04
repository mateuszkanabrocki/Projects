#!/usr/bin/env python3.7
import argparse
from sys import exit, stdin

#  ./cut.py file -d ' ' -f 1,3
#  ./cut.py file -d ',' -f 1-2
#  ./cut.py -d ',' -f 1-2
#  ls -l | ./tail.py -5 | sed 's/  \+/ /g' | ./cut.py -d " " -f 1,9


def parse():
    help = "This module works like a simple cut shell command."
    parser = argparse.ArgumentParser(description=help)
    parser.add_argument(
        "file",
        type=str,
        help="an input file",
        nargs="*", default=None
    )
    parser.add_argument(
        "-d",
        type=str,
        help="a character to separate the columns of data",
        default="   "
    )
    parser.add_argument("-f", help="number of a columns to be displayed")
    args = parser.parse_args()
    print(args, "\n")
    return args


def read_file(files):
    for file in files:
        try:
            with open(file, "r", errors="ignore") as f:
                lines = [line.strip('\n') for line in f.readlines()]
        except FileNotFoundError:
            print("No file found.")
            exit(1)
    return lines


def display(lines, args):
    columns_num = []
    for column in args.f.split(","):
        try:
            if "-" in column:
                range_num = column.split("-")
                print(range_num)
                for i in range(int(range_num[0]), int(range_num[1]) + 1):
                    columns_num.append(i)
            else:
                columns_num.append(int(column))
        except (AttributeError, ValueError):
            raise SyntaxError(
                "f-flag syntax examples: -f 1-2, -f 1,3 (only positive numbers)"
            )
    print()
    for line in lines:
        words = line.split(args.d)
        try:
            for index in columns_num:
                print(words[index - 1], end=" ")
        except IndexError:
            continue
        print()
    print()


def main():
    args = parse()
    lines = []
    if args.file:
        lines = read_file(args.file)
    else:
        lines = [line.strip('\n') for line in stdin.readlines()]
    display(lines, args)


if __name__ == "__main__":
    main()
