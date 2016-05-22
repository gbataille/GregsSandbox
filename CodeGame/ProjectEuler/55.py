#!/usr/local/bin/python3


def countLychrel(upperbound):
    count = 0
    for n in range(0, upperbound):
        if isLychrel(n):
            count += 1

    return count


def isLychrel(num):
    """
    >>> isLychrel(47)
    False
    >>> isLychrel(349)
    False
    >>> isLychrel(196)
    True
    """

    for i in range(0, 50):
        rev = list(str(num))
        rev.reverse()
        rev = int("".join(rev))
        num = num + rev
        if isPalyndrome(num):
            return False

    return True


def isPalyndrome(num):
    """
    >>> isPalyndrome(121)
    True
    >>> isPalyndrome(1221)
    True
    >>> isPalyndrome(134)
    False
    """

    numStr = list(str(num))
    revStr = list(numStr)
    revStr.reverse()
    return numStr == revStr


def main():
    print(countLychrel(10000))


if __name__ == "__main__":
    main()
