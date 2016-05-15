from itertools import permutations


def pandigital():
    return map(
            "".join,
            map(lambda x: map(str, x), map(list, permutations(range(10), 10))))
