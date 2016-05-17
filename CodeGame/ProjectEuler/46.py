#!/usr/local/bin/python3
from utils.prime import primes, sieve
import math


def bruteIt():
    limit = 10000
    s = sieve(limit)
    # Only odds numbers
    for candidate in range(3, limit, 2):
        # Only composite
        if not s[candidate]:
            # Brute : test all the primes smaller than candidate and check the
            # property of the substraction
            isGoldbach = False
            for p in primes(candidate):
                delta = candidate - p
                if (int(math.sqrt(delta/2)) == math.sqrt(delta/2)):
                    isGoldbach = True
                    break

            if not isGoldbach:
                print(candidate)
                break


def main():
    bruteIt()


if __name__ == "__main__":
    main()
