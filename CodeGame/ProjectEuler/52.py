#!/usr/local/bin/python3
from itertools import count, permutations


def main():
    for i in count(125874):
        nums = {2*i, 3*i, 4*i, 5*i, 6*i}
        perms = set(map(int, map("".join, map(list, permutations(str(i))))))
        if nums.issubset(perms):
            print(i)
            return


if __name__ == "__main__":
    main()
