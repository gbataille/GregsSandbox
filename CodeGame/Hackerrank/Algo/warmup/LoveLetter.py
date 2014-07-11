#!/usr/local/bin/python3
from math import fabs

def readCase1():
    a = input()
    return a
def readCase2():
    a = input()
    b = input()
    return a, b
def readCase3():
    a = input()
    b = input()
    c = input()
    return a,b,c

T = int(input())
for t in range(0, T):
    word = list(readCase1())
    moves = 0
    while len(word) > 1:
        first = word.pop(0)
        last = word.pop(len(word) - 1)
        moves += fabs(ord(first) - ord(last))

    ################
    print(int(moves))
