#!/usr/local/bin/python3
from math import sqrt, pow, fabs

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

maxxor = 0

for i in range(L, R+1):
    for j in range(L,R+1):
        if i^j > maxxor:
            maxxor = i^j

################
print(int(maxxor))
