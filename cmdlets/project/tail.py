#! /usr/bin/env python3

from sys import argv, exit, stdin
# history | ./tail -25


def arguments(argv):
    try:
        lines_num = int(argv[1].strip('-'))
        return lines_num
    except IndexError:
        print('Number of lines not gien.')
        exit(1)


def main():
    count = arguments(argv)
    if len(argv) > 2:
        try:
            lines = []
            for file in argv[2:]:
                with open(file, 'r') as f:
                    for line in f.readlines():
                        lines.append(line)
        except FileNotFoundError:
            print('File not found.')
            exit(1)
    else:
        lines = stdin.readlines()

    result_lines = lines[-count:]
    for line in result_lines:
        print(line.strip('\n'))


if __name__ == '__main__':
    main()
