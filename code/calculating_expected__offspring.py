parents_genotype = [17765, 19755, 16352, 17898, 18101, 16553]
dom_phentype_offspring = 0

for i in range(len(parents_genotype)):
    if i <= 2:
        dom_phentype_offspring += parents_genotype[i] * 2
    elif i == 3:
        dom_phentype_offspring += parents_genotype[i] * 1.5
    elif i == 4:
        dom_phentype_offspring += parents_genotype[i] * 1
    else:
        dom_phentype_offspring += parents_genotype[i] * 0

print(dom_phentype_offspring)
