#!/usr/local/bin/python3


def fact(n):
    """
    >>> fact(1)
    1
    >>> fact(3)
    6
    >>> fact(10)
    3628800
    """

    if not hasattr(fact, 'upper'):
        fact.upper = 0
        fact.cache = {0: 1}

    if n > fact.upper:
        for i in range(fact.upper + 1, n + 1):
            fact.cache[i] = fact.cache[i-1] * i

    return fact.cache[n]


def comb(n, p):
    """
    >>> comb(5, 1)
    5
    >>> comb(5, 3)
    10
    >>> comb(5,5)
    1
    """
    return int(fact(n) / (fact(p) * fact(n - p)))


def brute():
    counter = 0
    for n in range(23, 101):
        for r in range(0, n):
            if comb(n, r) > 10**6:
                counter += 1

    print(counter)


def main():
    brute()


if __name__ == "__main__":
    main()

# C(n,r) = n! / (r! * (n - r)!)
# for fixed n, C(n,r) when r grows
