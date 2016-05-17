#!/usr/local/bin/python3
from utils.prime import sieve, primeFactors
from itertools import count


def findConseqWithProperty(n):
    sieve(10 ** 6)  # initialize the sieve
    conseq = 0

    for candidate in count(1):
        if candidate % 1000 == 0:
            print(candidate)

        if len(primeFactors(candidate)) == n:
            conseq += 1
        else:
            conseq = 0

        if conseq == n:
            print(candidate - n + 1)
            break


def main():
    findConseqWithProperty(4)


if __name__ == "__main__":
    main()
