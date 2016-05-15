#!/usr/local/bin/python3
from utils.pandigital import pandigital
from itertools import islice


def subDivisibility(numStr, start, divider):
    num = int(numStr[start-1:start+2])
    return (num % divider) == 0


def checkProperty(x):
    return (subDivisibility(x, 2, 2) and
            subDivisibility(x, 3, 3) and
            subDivisibility(x, 4, 5) and
            subDivisibility(x, 5, 7) and
            subDivisibility(x, 6, 11) and
            subDivisibility(x, 7, 13) and
            subDivisibility(x, 8, 17))


def main():
    print(list(islice(pandigital(), 3)))
    print(checkProperty('1406357289'))
    print(sum(map(int, filter(checkProperty, pandigital()))))


if __name__ == "__main__":
    main()
