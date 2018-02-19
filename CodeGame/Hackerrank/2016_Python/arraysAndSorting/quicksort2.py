#!/usr/local/bin/python3
#https://www.hackerrank.com/challenges/quicksort2

import sys

def main(argv = None):
    if argv is None:
        argv = sys.argv

    n = int(input())
    ar = list(map(int, input().split(' ')))

    quicksort(ar)

def quicksort(ar):
    if len(ar) == 0:
        return []
    else:
        pivot = ar[0]
        ar_sub = ar[1:len(ar)]
        result = concat( quicksort(left(ar_sub, pivot)), pivot, quicksort(right(ar_sub, pivot)) )
        if len(result) > 1: printIntList(result)
        return result


def left(ar, pivot):
    left = []
    for i in range(0, len(ar)):
        if ar[i] < pivot:
            left.append(ar[i])

    return left

def right(ar, pivot):
    right = []
    for i in range(0, len(ar)):
        if ar[i] >= pivot:
            right.append(ar[i])

    return right

def quicksort_sub(ar):
    pivot = ar[0]
    left = []
    right = []
    for i in range(1, len(ar)):
        if ar[i] < pivot:
            left.append(ar[i])
        else:
            right.append(ar[i])

    return (pivot, left, right)

def concat(left, pivot, right):
    result = []
    result.extend(left)
    result.append(pivot)
    result.extend(right)
    return result

def printIntList(ar):
    print(' '.join(list(map(str, ar))))

# Invoking the program entry point
if __name__ == "__main__":
    sys.exit(main())
