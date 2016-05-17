#!/usr/local/bin/python3
from utils.prime import primes, isPrime
from itertools import dropwhile, permutations


def main():
    ps = dropwhile(lambda x: x < 1000, primes(10000))
    for prime in ps:
        perms = list(filter(isPrime,
                            map(int,
                                set(
                                    map("".join,
                                        permutations(str(prime)))))))

        # look for a serie
        for first in perms:
            for second in perms:
                if first >= second:
                    continue

                delta = second - first
                # looks for a potential third
                if second + delta in perms:
                    print(first, second, second + delta)

    return


if __name__ == "__main__":
    main()
