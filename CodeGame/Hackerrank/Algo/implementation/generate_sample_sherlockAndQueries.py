import random
import sys

random.seed(0)

n = int(sys.argv[1])
m = int(sys.argv[2])

print(n, m)

# A
print(' '.join(str(103) #random.randint(1, 10 ** 5))
               for i in range(n)))
# B
if 1:
    # any value
    print(' '.join(str(random.randint(1, n))
                   for i in range(m)))
else:
    # only 1
    print(' '.join(str(1)
                   for i in range(m)))
# C
print(' '.join(str(random.randint(1, 10 ** 5))
               for i in range(m)))
