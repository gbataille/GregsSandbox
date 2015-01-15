#!/usr/local/bin/python3
#https://www.hackerrank.com/challenges/cut-the-sticks

import sys

def main(argv = None):
    if argv is None:
        argv = sys.argv

    N = int(input())
    sticks = list(map(int, input().split(" ")))

    done = 0
    while not done:
        sticks.sort()
        shortest = sticks[0]
        sticks = list(map(lambda x: x - shortest, sticks))
        print(len(sticks))
        sticks = list(filter(lambda x: x != 0, sticks))

        if len(sticks) == 0:
            done = 1 



# Invoking the program entry point
if __name__ == "__main__":
    sys.exit(main())
