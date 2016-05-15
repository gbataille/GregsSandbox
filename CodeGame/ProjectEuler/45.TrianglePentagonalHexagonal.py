#!/usr/local/bin/python3
from itertools import islice

# Brute force it cause I want to get better with generator and memoization


def pentagonalGenerator():
    n = 1
    while True:
        yield n * (3 * n - 1) / 2
        n = n + 1


def triangleGenerator():
    n = 1
    while True:
        yield n * (n + 1) / 2
        n = n + 1


def hexagonalGenerator():
    n = 1
    while True:
        yield n * (2 * n - 1)
        n = n + 1


def triangleList():
    if not hasattr(triangleList, 'cache'):
        triangleList.cache = list(islice(triangleGenerator(), 285, 100000))
    return triangleList.cache


def pentagonalList():
    if not hasattr(pentagonalList, 'cache'):
        pentagonalList.cache = list(islice(pentagonalGenerator(), 285, 100000))
    return pentagonalList.cache


def hexagonalList():
    if not hasattr(hexagonalList, 'cache'):
        hexagonalList.cache = list(islice(hexagonalGenerator(), 285, 100000))
    return hexagonalList.cache


def main():
    for x in triangleList():
        if x in pentagonalList() and x in hexagonalList():
            print(x)
            break

if __name__ == "__main__":
    main()

# Pn = n * (3n - 1) / 2

# Pj + Pk = Pn
# Pj - Pk = Pm

# Find Pm

# P5 - P4 = D
# P4 - P3 = E
# P5 - P4 > P4 - P3
# D > E
# P5 = P4 + D
# P4 + E < P5

# D = Ps
# then s > j and s > k
