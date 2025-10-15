
def rabbit_pop(n, k, i = 1):
    if n == 1:
        print(i)
    else:
        i = i + k * (i - i//k)
        return rabbit_pop(n - 1, k, i)

rabbit_pop(5, 3)
print(1//3)