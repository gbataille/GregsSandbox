#!/usr/local/bin/python3

import sys

def main(argv = None):
    if argv is None:
        argv = sys.argv

T = int(input())
for t in range(0, T):
    N = int(input())

    # You want a maximum of 5s at the beginning of the number
    # the rest is composed for 3s

    n5 = 0
    attempt5 = N - (N % 3)
    while attempt5 > 0 and n5 == 0:
        if (N - attempt5) % 5 == 0:
            n5 = attempt5

        attempt5 -= 3

    if n5 == 0:
        if N % 5 == 0:
            num = '3' * N
        else:
            num = '-1'
    else:
        num = '5' * n5 + '3' * (N - n5)

    print(int(num))

# Invoking the program entry point
if __name__ == "__main__":
    sys.exit(main())
