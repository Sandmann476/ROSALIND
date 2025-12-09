def wabbit_population(n, m):
    if n <= 0:
        return 0
    if m <= 0:
        raise ValueError("lifespan m must be >= 1")

    # ages[i] = number of pairs of age i months (0..m-1)
    ages = [0] * m
    ages[0] = 1  # start with one newborn pair in month 1

    for month in range(1, n):
        # newborns are produced by all rabbits of age >= 1 (they reproduce from month 2)
        newborns = sum(ages[1:])
        # age everyone by one month; oldest die (dropped)
        ages = [newborns] + ages[:-1]

    return sum(ages)


print(wabbit_population(86, 19))