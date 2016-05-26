#!/usr/local/bin/python3
# Has extremely bad performance. indeed we need to determine the primality of
# numbers up to about 7.10**8. The computation of a sieve that big is huge
# (although it works)

# Some primality tests are suggested to be better:

#        For 32 bits integers you don't have to carry out the complete
#        Miller-Rabin to establish primality, it suffices to call the witness
#        function max. 3 times with bases resp. 2, 7 and 61. this leads to a
#        very fast primality test for numbers upto about 4.3 billion (I forgot
#        the first failure, but it's over 2^32).

from __future__ import division
from utils.prime import isPrime
from itertools import count


def diag():
    isPrime(10**9)      # Sieve init
    last = 1
    diagNumsCount = 1
    primeCountTillNow = 0
    for layer in count(1):
        sideLength = 2 * layer
        for side in range(1, 5):
            last += sideLength
            if isPrime(last):
                primeCountTillNow += 1
            diagNumsCount += 1

        ratio = primeCountTillNow / diagNumsCount

        if layer % 100 == 0:
            print("layer: ", layer, ", ratio: ", ratio, ", last: ", last,
                  ", primes: ", primeCountTillNow, ", tot: ", diagNumsCount)
        if ratio < 0.1:
            return sideLength


def main():
    print(diag() + 1)


if __name__ == "__main__":
    main()
