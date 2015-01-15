#!/usr/local/bin/python3

import sys
from time import time

def main(argv = None):
    MOD = 10**9 + 7
    LOG = 0
    start = time()

    if argv is None:
        argv = sys.argv

    I = list(map(int, input().split(" ")))
    N = I[0]
    M = I[1]

    A = list(map(int, input().split(" ")))
    B = list(map(int, input().split(" ")))
    C = list(map(int, input().split(" ")))

    if LOG:
        print("args read")
        print(time() - start)
        start = time()

    cees = {}
    for i in range(1, M+1):
        c = cees.get(B[i-1])
        if c:
            cees[B[i-1]] = ( c * C[i-1] ) % MOD
        else:
            cees[B[i-1]] = C[i-1]

    if LOG:
        print("cees done")
        print(time() - start)
        start = time()

    kays = list(cees.keys())
    kays.sort()

    for j in range(1,N+1):
        elem = A[j-1]
        # for (key, value) in cees.items():
        for k in kays:
            if k > j:
                break
            # if j % key == 0:
            if j % k == 0:
                # elem = (elem * value) % MOD
                elem = (elem * cees[k]) % MOD

        A[j-1] = elem

    if not LOG:
        print(" ".join(map(str, A)))
        # print(A[1])

    if LOG:
        print("done")
        print(time() - start)
        start = time()

# Invoking the program entry point
if __name__ == "__main__":
    sys.exit(main())
