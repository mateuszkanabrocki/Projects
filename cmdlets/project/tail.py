#!/usr/bin/env python3.6

from sys import argv, exit, stdin

# example of usage:
# history | ./tail -25
# ./tail.py -100 file.txt
# ls -l | ./tail.py -100 file.txt


# return number of lines to be tailed
def count_lines(argv):
    try:
        count = int(argv[1].strip("-"))
        return count
    except (IndexError, ValueError):
        print("Number of lines not given.")
        exit(1)


# tail lines from the stdinput and then from the given files
def search_input(argv):
    lines = []
    # check if there is some data at stdin:
    if not stdin.isatty():
        for line in stdin.readlines():
            lines.append(line)
    # check if files are given
    elif len(argv) > 2:
        try:
            for file in argv[2:]:
                with open(file, "r") as f:
                    for line in f.readlines():
                        lines.append(line)
        except FileNotFoundError:
            print(f"File '{file}' not found.")
            exit(1)
    return lines


# print given count of lines to stdout
def print_lines(lines, count):
    for line in lines[-count:]:
        print(line.strip("\n"))


def main():
    count = count_lines(argv)
    lines = search_input(argv)
    print_lines(lines, count)


if __name__ == "__main__":
    main()
