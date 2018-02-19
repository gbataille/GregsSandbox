#!/usr/local/bin/python3
#https://www.hackerrank.com/challenges/lonely-integer

import sys

def main(argv = None):
    if argv is None:
        argv = sys.argv

    N = int(input())
    A = parseIntListOnStdin()

    h = {}
    for elem in A:
        if h.get(elem) == None:
            h[elem] = 1
        else:
            h[elem] = 2

    for (key, value) in h.items():
        if value == 1:
            print (key)
            break


def parseIntListOnStdin():
    return list(map(int, input().split(' ')))

def printIntList(ar):
    print(' '.join(list(map(str, ar))))

# Invoking the program entry point
if __name__ == "__main__":
    sys.exit(main())
