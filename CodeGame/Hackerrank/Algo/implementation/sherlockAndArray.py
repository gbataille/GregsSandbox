#!/usr/local/bin/python3
#https://www.hackerrank.com/challenges/sherlock-and-array

import sys
from functools import reduce

def main(argv = None):
    if argv is None:
        argv = sys.argv

    T = int(input())

    for t in range(0, T):
        N = int(input())
        nums = list(map(int, input().split(" ")))

        found = 0

        pivot = 0
        left = 0
        right = reduce(lambda x, y: x+y, nums[pivot+1:N+1], 0)
        found = (left == right)

        while (not found) and (pivot < N-1):
            left = left + nums[pivot]
            right = right - nums[pivot+1]
            pivot = pivot + 1
            found = (left == right)
            if found:
                break

        if found:
            print("YES")
        else:
            print("NO")


# Invoking the program entry point
if __name__ == "__main__":
    sys.exit(main())
