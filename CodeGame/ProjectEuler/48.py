#!/usr/local/bin/python3


def main():
    # brute
    tot = 0
    for i in range(1, 1001):
        power = 1
        for p in range(i):
            power = (power * i) % (10**11)

        tot += power % (10**11)

    print(tot)


if __name__ == "__main__":
    main()
