#!/usr/local/bin/python3
#https://www.hackerrank.com/challenges/cavity-map

import sys

def main(argv = None):
    if argv is None:
        argv = sys.argv

    N = int(input())

    map = []
    for i in range(0, N):
        map.append(list(input()))

    t = []
    for a in range(1, N-1):
        for b in range(1, N-1):
            current = int(map[a][b])

            if (current > int(map[a-1][b])) \
                    and (current > int(map[a+1][b])) \
                    and (current > int(map[a][b-1])) \
                    and (current > int(map[a][b+1])):
                t.append( (a,b) )

    for (a, b) in t:
        map[a][b] = '0'

    for i in range(0, N):
        print("".join(map[i]).replace("0", "X"))

# Invoking the program entry point
if __name__ == "__main__":
    sys.exit(main())
