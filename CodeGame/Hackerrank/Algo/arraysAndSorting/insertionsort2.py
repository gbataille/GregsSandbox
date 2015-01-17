#!/usr/local/bin/python3
#https://www.hackerrank.com/challenges/insertionsort2

import sys

def main(argv = None):
    if argv is None:
        argv = sys.argv

    s = int(input())
    l = list(map(int, input().split(' ')))

    for i in range(1, s):
        l = sortIthElmInL(i, l)
        print(' '.join(list(map(str, l))))

def sortIthElmInL(ith,l):

    value = l[ith]
    for i in range(ith-1, -1, -1):
        pivot = l[i]
        if pivot < value:
            l[i+1] = value
            break
        else:
            l[i+1] = pivot

        if i == 0:
            l[i] = value

    return l


# Invoking the program entry point
if __name__ == "__main__":
    sys.exit(main())
