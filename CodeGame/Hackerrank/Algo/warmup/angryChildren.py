#!/usr/local/bin/python3

import sys

def main(argv = None):
    if argv is None:
        argv = sys.argv

# Tant qu'on a trop de paquets; on calcule la moyenne, le min et le max.
# On enlève soit le min, soit le max (celui le plus loin de la moyenne) et 
# on recommence

N = int(input())
K = int(input())
candies = []
for n in range(0, N):
    candies.append(int(input()))

candies.sort()

mini = candies[len(candies) - 1] - candies[0]

for i in range(0, len(candies) - 1 - K):
    minsub = candies[i+K-1] - candies[i]
    if minsub < mini:
        mini = minsub

print(mini)

# Invoking the program entry point
if __name__ == "__main__":
    sys.exit(main())
