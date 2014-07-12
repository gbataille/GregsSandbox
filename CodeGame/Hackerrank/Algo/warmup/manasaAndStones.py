#!/usr/local/bin/python3

import sys

def main(argv = None):
    if argv is None:
        argv = sys.argv

T = int(input())
for t in range(0,T):
    nbStone = int(input())
    incA    = int(input())
    incB    = int(input())

    solutions = set([0])
    for i in range(1, nbStone):
        newSolution = set()
        for val in solutions:
            newSolution.add(val+incA)
            newSolution.add(val+incB)

        solutions = newSolution

    print(" ".join(map(str,sorted(solutions))))


# Invoking the program entry point
if __name__ == "__main__":
    sys.exit(main())
