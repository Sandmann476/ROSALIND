from itertools import product

symbols = input().split()
n = int(input())


for p in product(symbols, repeat=n):
    print("".join(p))