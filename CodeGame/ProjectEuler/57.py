#!/usr/local/bin/python3


# def frac(n):
#     if n == 1:
#         return 1/2
#     else:
#         return (frac(n-1) + 2) ** -1
#
#
# def sqrt2(n):
#     return 1 + frac(n)

def frac(n):
    if not hasattr(frac, 'cache'):
        frac.cache = [(1, 2)]

    if n > len(frac.cache):
        for i in range(len(frac.cache), n):
            prevNum, prevDenom = frac.cache[len(frac.cache) - 1]
            frac.cache.append((prevDenom, 2*prevDenom + prevNum))

    return frac.cache[n - 1]


def sqrt2(n):
    num, denom = frac(n)
    return (num + denom, denom)


def main():
    count = 0
    for i in range(1, 1001):
        num, denom = sqrt2(i)
        if len(list(str(num))) > len(list(str(denom))):
            count += 1

    print(count)


if __name__ == "__main__":
    main()

# n = 1393 / 985
#   = 1 + frac(n)
#   = 1 + 408 / 985
# n+1 = 1 + (408 / 985 + 2) ** -1
#     = 1 + (2378 / 985) ** -1
#     = 3363 / 2378
#
#
# sqrt1 = 1 + 1/2 = 3/2
# sqrt2 = 1 + 1/(2 + 1/2)
#       = 1 + 1/(5/2)
#       = 1 + 2/5
#       = 7/5
# sqrt3 = 1 + 1/(2 + 1/(2 + 1/2))
#       = 1 + 1/(2 + 2/5)
#       = 1 + 1/(12/5)
#       = 17/12
#
#
# sqrt2 = 1 + a/b
# sqrt3 = 1 + 1/(2 + a/b)
#       = 1 + 1/(2b + a)/b
#       = 1 + b/(2b + a)
