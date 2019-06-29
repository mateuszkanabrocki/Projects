#!/usr/bin/env python3

import argparse
from sys import exit, stdin

# ls | sort
# ls | sort -r
# ls | sort -f case
# ls | sort -g num

# ls -l | ./sort.py
# ./sort.py file.txt


def parse():
    help = "This module works like a sort cmdlet but it's much simpler and less functional."
    parser = argparse.ArgumentParser(description=help)
    parser.add_argument("file", type=str, help="input file")
    parser.add_argument("-r", action="store_true", help="reverse the sorting result")
    parser.add_argument("-f", action="store_true", help="ignore letter case")
    args = parser.parse_args()
    print(args, "\n")
    return args


def cut_standin():
    text = []
    while True:
        try:
            text.append(input())
        except EOFError:
            break
    return text


def main():
    args = parse()
    if args.file == "-":
        lines = stdin.readlines()
    else:
        try:
            with open(args.file, "r", errors="ignore") as file:
                lines = file.readlines()
        except FileExistsError:
            print("File not found.")
            exit(1)
    if args.f:
        sorted_list = sorted(
            lines, key=lambda s: s.lower(), reverse=args.r
        )  # !!for ignoring a letter case
    else:
        sorted_list = sorted(lines, reverse=args.r)
    print()
    for line in sorted_list:
        print(line)


if __name__ == "__main__":
    main()
