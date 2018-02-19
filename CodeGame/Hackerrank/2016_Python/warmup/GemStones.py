#!/usr/local/bin/python3
import array
import copy

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
gem = []
for t in range(0, T):
    composition = readCase1()

    # first round, list everything
    if t == 0:
        for c in composition:
            if not any(g == c for g in gem):
                gem.append(c)
    else:
        # second round, discards all the chars that are not in the string
        for g in copy.deepcopy(gem):
            if not any(c == g for c in composition):
                gem.remove(g)

    # a,b = readCase2()
    # a,b,c = readCase3()

    # ai = int(a)
    # bi = int(b)
    # ci = int(c)

    ################
print(len(gem))
