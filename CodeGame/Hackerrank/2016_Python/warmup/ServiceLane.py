#!/usr/local/bin/python3

def maxWidth(highway, start, end):
    max = 3
    for i in range(start, end+1):
        if int(highway[i]) < max:
            max = int(highway[i])

    return max


top = input()
arr = top.split(" ")
N = int(arr[0])
T = int(arr[1])

highway = input().split(" ")

for t in range(0, T):
    troncon = input().split(" ")
    start = int(troncon[0])
    end = int(troncon[1])

    result = maxWidth(highway, start, end)
    ################
    print(result)

