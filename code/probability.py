
def probability_dominant(k, m, n):
    total = k + m + n
    # aa x aa: always recessive
    prob_aa_aa = (n / total) * ((n - 1) / (total - 1))

    # aa x Aa or Aa x aa: 50% recessive
    prob_aa_Aa = (n / total) * (m / (total - 1)) + (m / total) * (n / (total - 1))
    prob_aa_Aa *= 0.5

    # Aa x Aa: 25% recessive
    prob_Aa_Aa = (m / total) * ((m - 1) / (total - 1)) * 0.25

    # Total probability of producing a recessive phenotype
    prob_recessive = prob_aa_aa + prob_aa_Aa + prob_Aa_Aa

    # So probability of producing a dominant phenotype:
    prob_dominant = 1 - prob_recessive

    return prob_dominant


print(probability_dominant(29, 15, 24))