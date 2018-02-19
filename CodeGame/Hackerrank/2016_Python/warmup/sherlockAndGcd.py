#!/usr/local/bin/python3

import sys
from fractions import gcd

def main(argv = None):
    if argv is None:
        argv = sys.argv

T = int(input())
for t in range(0, T):
    N = int(input())
    A = list(map(int, input().split(" ")))
    trouve = False
    for i in range(0, len(A)):
        for j in range(i+1, len(A)):
            if gcd(A[i], A[j]) == 1:
                trouve = True

            if trouve:
                break

        if trouve:
            break

    if trouve:
        print("YES")
    else:
        print("NO")

# Invoking the program entry point
if __name__ == "__main__":
    sys.exit(main())
