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
    cut = int(readCase1())
    # a,b = readCase2()
    # a,b,c = readCase3()

    # ai = int(a)
    # bi = int(b)
    # ci = int(c)

    ################
    print(int(cut/2) * (cut - int(cut/2)))

