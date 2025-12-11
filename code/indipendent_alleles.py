from math import comb

# Genotypes (A-locus × B-locus)
A_types = ['AA','Aa','aa']
B_types = ['BB','Bb','bb']
genotypes = [a + ' ' + b for a in A_types for b in B_types]
idx = {g:i for i,g in enumerate(genotypes)}

def locus_probs(parent):
    # parent is one of 'AA','Aa','aa' or 'BB','Bb','bb'
    # mate is heterozygous at that locus ('Aa' or 'Bb'), so probabilities:
    if parent in ('AA','BB'):
        if parent[0]=='A':
            return {'AA':0.5,'Aa':0.5,'aa':0.0}
        else:
            return {'BB':0.5,'Bb':0.5,'bb':0.0}
    if parent in ('Aa','Bb'):
        if parent[0]=='A':
            return {'AA':0.25,'Aa':0.5,'aa':0.25}
        else:
            return {'BB':0.25,'Bb':0.5,'bb':0.25}
    if parent in ('aa','bb'):
        if parent[0].upper()=='A':
            return {'AA':0.0,'Aa':0.5,'aa':0.5}
        else:
            return {'BB':0.0,'Bb':0.5,'bb':0.5}
    raise ValueError(parent)

# per-parent-type -> child genotype (one child) probabilities
p = [[0.0]*9 for _ in range(9)]
for i,g in enumerate(genotypes):
    a_parent, b_parent = g.split()
    probsA = locus_probs(a_parent)
    probsB = locus_probs(b_parent)
    for j,g2 in enumerate(genotypes):
        a_child, b_child = g2.split()
        p[i][j] = probsA[a_child] * probsB[b_child]

# polynomial helpers
def poly_mul(a,b):
    res = [0.0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):
            res[i+j]+=ai*bj
    return res

def poly_compose_sum_weighted(weights, polys):
    res = [0.0]
    for w,poly in zip(weights, polys):
        if w==0: continue
        if len(poly) > len(res):
            res += [0.0]*(len(poly)-len(res))
        for i,v in enumerate(poly):
            res[i]+= w*v
    return res

def compute_pmf_for_generation(k):
    r = idx['Aa Bb']
    # H_j^{(0)}(x)
    H = []
    for j in range(9):
        H.append([0.0, 1.0] if j==r else [1.0])
    for level in range(1, k+1):
        newH = []
        for i in range(9):
            S = poly_compose_sum_weighted(p[i], H)
            Sq = poly_mul(S, S)
            newH.append(Sq)
        H = newH
    pmf = H[r]
    # correct tiny negatives and normalize
    pmf = [max(0.0, v) for v in pmf]
    s = sum(pmf)
    if s>0:
        pmf = [v/s for v in pmf]
    return pmf

def prob_at_least_N(k, N):
    pmf = compute_pmf_for_generation(k)
    total = sum(pmf[N:]) if N < len(pmf) else 0.0
    return total

# Example (sample dataset):
if __name__ == "__main__":
    k, N = 5, 7
    p = prob_at_least_N(k, N)
    print(p)           # full-precision
    print(f"{p:.3f}")  # rounded to 3 decimal places
