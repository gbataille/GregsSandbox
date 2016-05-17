#!/usr/local/bin/python3
from utils.prime import isPrime, primes


def main():
    ps = primes(10**6)
    biggest = 1
    for start in range(len(ps)):
        acc = 0
        nbTerms = 0

        if len(ps[start:]) < biggest:
            continue

        for p in ps[start:]:
            nbTerms += 1
            acc += p

            if acc > 10**6:
                continue

            if isPrime(acc) and nbTerms > biggest:
                biggest = nbTerms
                print("prime ", acc, " with ", nbTerms, " terms")


if __name__ == "__main__":
    main()
