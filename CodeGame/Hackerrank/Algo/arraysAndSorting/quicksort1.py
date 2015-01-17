#!/usr/local/bin/python3
#https://www.hackerrank.com/challenges/quicksort1

import sys

def main(argv = None):
    if argv is None:
        argv = sys.argv

n = int(input())
ar = list(map(int, input().split(' ')))

p = ar[0]
left = []
right = []
for i in range(1, len(ar)):
    if ar[i] < p:
        left.append(ar[i])
    else:
        right.append(ar[i])

left.append(p)
left.extend(right)

print(" ".join(list(map(str, left))))


# Invoking the program entry point
if __name__ == "__main__":
    sys.exit(main())
