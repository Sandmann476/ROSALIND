
def rabbit_pop(k,n = 0, i = 1):
    if n == 6:
        print(i)
    else:
        i = i + k * (i - n*k)
        return rabbit_pop(k, n + 1, i)

rabbit_pop(3)