#!/usr/local/bin/python3

import sys

def main(argv = None):
    if argv is None:
        argv = sys.argv

    fibo   = [1,1]
    length = 2
    while fibo[length - 1] < pow(10,10):
        fibo.append(fibo[length - 1] + fibo[length - 2])
        length += 1

    T = int(input())
    for t in range(0, T):
        N = int(input())
        if N in fibo:
            print("IsFibo")
        else:
            print("IsNotFibo")

# Invoking the program entry point
if __name__ == "__main__":
    sys.exit(main())
