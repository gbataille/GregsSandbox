#!/usr/local/bin/python3
from functools import reduce


def maxDigitalSum():
    maximum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            num = a ** b
            digitalSum = reduce(
                lambda x, y: x + y,
                map(int, list(str(num))))
            maximum = max(maximum, digitalSum)

    return maximum


def main():
    print(maxDigitalSum())


if __name__ == "__main__":
    main()
