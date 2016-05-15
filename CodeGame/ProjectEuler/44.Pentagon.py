#!/usr/local/bin/python3
# Not my solution. I was forcing myself to use iterators and generators but the
# way I coded it, that meant O(n^4) I guess now that I think about it.
# This however is O(n^2) only


def main():
    # dSolution()
    def pe44():
        ps = set()
        i = 0
        while True:
            i += 1
            p = (3*i*i - i) / 2
            ps.add(p)
            for n in ps:
                if p-n in ps and p-2*n in ps:
                    return p-2*n

    print("Project Euler 44 Solution =", pe44())

if __name__ == "__main__":
    main()

# Pn = n * (3n - 1) / 2

# Pj + Pk = Pn
# Pj - Pk = Pm

# Find Pm

# P5 - P4 = D
# P4 - P3 = E
# P5 - P4 > P4 - P3
# D > E
# P5 = P4 + D
# P4 + E < P5

# D = Ps
# then s > j and s > k
