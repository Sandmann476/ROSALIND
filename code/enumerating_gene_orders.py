import math
from itertools import permutations

n = 5

perms = list(permutations(range(1, n+1)))

print(math.factorial(n))

for p in perms:
    print(" ".join(map(str, p)))