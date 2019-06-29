#!/usr/bin/env python3


def generator():
    for x in range(100):
        yield x
        x = x - 1
        print(x)


a = generator()
next(a)
next(a)
next(a)
