#!/usr/local/bin/python3
import sys
from itertools import takewhile


def triangleNumber():
    n = 1
    while True:
        yield n/2*(n+1)
        n = n+1


def isTriangle(x):
    total = sum(map(asciiNormalize, map(ord, list(x))))
    triangleNums = list(takewhile(lambda x: x <= total, triangleNumber()))
    return triangleNums.pop() == total


def asciiNormalize(x):
    return x - 64


def handleData(x):
    x = x.replace('"', '').strip()
    return isTriangle(x)


def main():
    f = open(sys.argv[1], 'r')
    data = f.read().split(",")
    arrayIter = map(handleData, data)
    print(len(data))
    print(len(list(filter(lambda x: x, arrayIter))))


if __name__ == "__main__":
    main()
