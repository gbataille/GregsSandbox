#!/usr/local/bin/python3
#https://www.hackerrank.com/challenges/quicksort4

import sys

qcount = 0
icount = 0

def main(argv = None):
    if argv is None:
        argv = sys.argv

    n = int(input())
    ar = list(map(int, input().split(' ')))

    global qcount
    global icount

    iar = ar[:]
    quicksort(ar)
    insertion_sort(iar)

    print(icount - qcount)
    # printIntList(ar)


def quicksort(ar):
    partition(ar, 0, len(ar)-1)

def partition(ar, begin, end):
    if begin >= end:
        return

    pivot = ar[end]
    small_index = begin - 1
    for i in range(begin, end):
        if ar[i] < pivot:
            swap(ar, i, small_index + 1)
            small_index += 1

    pivot_index = small_index + 1
    swap(ar, end, pivot_index)

    partition(ar, begin,            pivot_index - 1)
    partition(ar, pivot_index + 1,  end)


def swap(ar, i1, i2):
    global qcount
    qcount += 1

    if i1 == i2:
        return

    temp = ar[i1]
    ar[i1] = ar[i2]
    ar[i2] = temp

def insertion_sort(l):
    global icount
    for i in range(1, len(l)):
        j = i-1
        key = l[i]

        while (l[j] > key) and (j >= 0):
           icount += 1
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

def printIntList(ar):
    print(' '.join(list(map(str, ar))))

# Invoking the program entry point
if __name__ == "__main__":
    sys.exit(main())
