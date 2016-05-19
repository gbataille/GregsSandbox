#!/usr/local/bin/python3
from utils.prime import primes, isPrime
from itertools import dropwhile


def isSubMask(candidate, mask):
    """
    >>> isSubMask("1*2*", "132*")
    True
    >>> isSubMask("1**2", "13*4")
    False
    >>> isSubMask("1**2", "1*2")
    False
    >>> isSubMask("13*2", "1**2")
    False
    >>> isSubMask("13*2", "13*2")
    False
    """

    if len(candidate) != len(mask):
        return False

    if candidate == mask:
        return False

    return len(list(filter(lambda x: (x[0] == x[1]) or (x[0] == "*"),
                           zip(candidate, mask)))) == len(mask)


def isMask(number):
    """
    >>> isMask("123")
    False
    >>> isMask("1*3")
    True
    """

    return number.find("*") != -1


def maskBiggestDigit(number):
    """
    >>> maskBiggestDigit("56755")
    '*67**'
    """

    biggestItem = itemWithMaxValue(countItems(number))
    if biggestItem[1] > 1:
        return number.replace(biggestItem[0], "*")
    else:
        return number


def itemWithMaxValue(dictionnary):
    """
    >>> itemWithMaxValue({'1': 2, '2': 4, '3': 1})
    ('2', 4)
    """

    biggest = {}
    bigValue = 0
    for item in dictionnary.items():
        if item[1] > bigValue:
            biggest = item
            bigValue = item[1]

    return biggest


def countItems(x):
    """
    >>> countItems("1001") == {'0': 2, '1': 2}
    True
    >>> countItems("123") == {'1': 1, '2': 1, '3': 1}
    True
    """

    digits = {}
    for d in x:
        if d in digits.keys():
            digits[d] = digits[d] + 1
        else:
            digits[d] = 1

    return digits


def test(p):
    digits = countItems(str(p))
    dupDigits = dict(filter(lambda x: x[1] > 1, digits.items()))
    for digit in dupDigits.keys():
        serie = 0
        smallest = 0
        for i in range(10):
            pStr = str(p)
            if i == 0 and pStr[0] == digit:
                continue

            num = int(pStr.replace(digit, str(i)))
            if (isPrime(num)):
                print(num)
                serie += 1
                if smallest == 0:
                    smallest = num

        print(serie)
        if serie == 8:
            print(smallest)
            return True

    return False


def main():
    ps = primes(10**6)

    for p in dropwhile(lambda x: x <= 56003, ps):
        if test(p):
            return

    # maskWithCount = countItems(filter(isMask, map(maskBiggestDigit,
    #                                               map(str, ps))))
    # print(len(maskWithCount))
    # for m in maskWithCount.items():
    #     mask = m[0]
    #     for subm in maskWithCount.items():
    #         subMask = subm[0]
    #         if isSubMask(subMask, mask):
    #             maskWithCount[mask] = maskWithCount[mask] + 1
    # print(itemWithMaxValue(maskWithCount))


if __name__ == "__main__":
    main()
