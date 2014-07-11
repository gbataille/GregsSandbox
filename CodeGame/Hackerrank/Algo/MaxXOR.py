#!/usr/local/bin/python3
from math import sqrt, pow

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

L = int(input())
R = int(input())

nbits = int(sqrt(R)) + 1
maxxor = pow(2, nbits) - 1

################
print(int(maxxor))
