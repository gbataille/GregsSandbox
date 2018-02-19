#!/usr/local/bin/python3
#https://www.hackerrank.com/challenges/countingsort1

import sys

def main(argv = None):
    if argv is None:
        argv = sys.argv

    n = int(input())
    inList = parseIntListOnStdin()

    result = [ 0 for i in range(0, 100) ]

    for i in range (0, n):
        result[ inList[i] ] += 1

    printIntList(result)

def parseIntListOnStdin():
    return list(map(int, input().split(' ')))

def printIntList(ar):
    print(' '.join(list(map(str, ar))))

# Invoking the program entry point
if __name__ == "__main__":
    sys.exit(main())
