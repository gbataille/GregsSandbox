#!/usr/local/bin/python3

import sys

def main(argv = None):
    if argv is None:
        argv = sys.argv

average = 0.0
[N, M] = map(int, input().split(" "))
for m in range(0, M):
    [a,b,k] = map(int, input().split(" "))
    average += ((b - a + 1) * k) / N

print(int(average))

# Invoking the program entry point
if __name__ == "__main__":
    sys.exit(main())
