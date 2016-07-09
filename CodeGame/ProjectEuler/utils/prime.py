from __future__ import division
from itertools import islice, repeat


def primes(n, DEBUG=False):
    """ Get all primes smaller than n
    >>> primes(10)
    [2, 3, 5, 7]
    """

    return [x[0] for x in enumerate(_sieve(n, DEBUG=DEBUG)[0:n+1]) if x[1]]


def _sieve(n, resetCache=False, DEBUG=False):
    """
    >>> _sieve(10, resetCache=True)
    [False, False, True, True, False, True, False, True, False, False, False]
    """

    # Sieve : whether a number N is prime or not is stored at index N
    if not hasattr(_sieve, 'cache') or resetCache:
        _sieve.cache = [False, False]

    previousSieveLen = len(_sieve.cache)

    # n+1 to account for 0 taking 1 space
    if previousSieveLen < n + 1:
        if DEBUG:
            print("prime._sieve - cache miss for n = ", n)

        _sieve.cache.extend(islice(repeat(True), n - previousSieveLen + 1))
        for num in range(2, n):
            # Take all the numbers. If they are prime (still True), remove
            # (mark as False) all their multiples in the extension
            if _sieve.cache[num]:
                # smallest multiple of num in the extension. Disallow 1 since
                # it would mark num itself as not prime
                smallest = (int((previousSieveLen - 1)/num) + 1) * num
                smallest = max(smallest, 2 * num)

                for multiple in range(smallest, n + 1, num):
                    _sieve.cache[multiple] = False

        if DEBUG:
            print("prime._sieve - DONE")

    return _sieve.cache


def isPrimeMillerRabin(n, DEBUG=False):
    return False


def isPrime(n, DEBUG=False):
    """
    >>> isPrime(0)
    False
    >>> isPrime(1)
    False
    >>> isPrime(2)
    True
    >>> isPrime(3)
    True
    >>> isPrime(11)
    True
    >>> isPrime(15)
    False
    >>> isPrime(4)
    False
    """
    if n < 2:
        return False
    else:
        return _sieve(n, DEBUG=DEBUG)[n]


def primeFactors(n):
    """
    Prime factor decomposition in the form of a dict with the keys being the
    prime factors and the values their respective power

    >>> primeFactors(2)
    {2: 1}
    >>> primeFactors(4)
    {2: 2}
    >>> primeFactors(20)
    {2: 2, 5: 1}
    """

    ps = primes(n)
    rest = n
    factors = {}
    for p in ps:
        if rest == 1:
            break

        if p ** 2 > n:
            if len(factors.keys()) > 0:
                factors[p] = 1
            else:
                factors[n] = 1
            break

        power = 0
        while rest % p == 0:
            power += 1
            rest = rest / p

        if power > 0:
            factors[p] = power

    return factors
