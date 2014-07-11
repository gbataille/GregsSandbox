#!/usr/local/bin/python3
# N growth cycle means
# N/2 + 1 moonsoon AND N/2 summer

# or ODD growth cycle is moonsoon
# EVEN growth cycle is summer
T = int(input())
for i in range(0, T):
    N = int(input())
    size = 1
    for c in range(1, N+1):
        if c % 2 == 0:
            size = size + 1
        else:
            size = size * 2

    print(size)
