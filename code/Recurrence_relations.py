def rabbit_population(n, k):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1  # Starting with 1 pair of rabbits

    population = [0] * (n + 1)
    population[1] = 1  # First month with 1 pair
    population[2] = 1  # Second month with 1 pair
    
    for i in range(3, n + 1):
        population[i] = population[i-1] + k * population[i-2]
    
    return population[n]

n = 31  # number of months
k = 3   # Number of new pairs each mature rabbit pair produces
print(rabbit_population(n, k))
