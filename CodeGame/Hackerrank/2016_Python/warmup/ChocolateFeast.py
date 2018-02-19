#!/usr/local/bin/python3
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
    L = readCase1().split(" ")
    N = int(L[0])
    C = int(L[1])
    M = int(L[2])

    totChocolate = int(N/C)
    wrapper = totChocolate
    while wrapper >= M:
        freeChoc = int(wrapper/M)
        totChocolate += freeChoc
        wrapper = wrapper - (freeChoc * (M - 1))

    ################
    print(totChocolate)
