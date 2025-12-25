import bisect

infile = open("/home/florian/Downloads/rosalind_lgis(2).txt", "r")
arr = list(map(int, infile.read().split()))

def longest_increasing_subsequence(arr):
    n = len(arr)
    tails = []
    tails_idx = []
    prev = [-1] * n

    for i, x in enumerate(arr):
        pos = bisect.bisect_left(tails, x)
        if pos == len(tails):
            tails.append(x)
            tails_idx.append(i)
        else:
            tails[pos] = x
            tails_idx[pos] = i

        if pos > 0:
            prev[i] = tails_idx[pos - 1]

    # Reconstruct LIS
    lis = []
    idx = tails_idx[-1]
    while idx != -1:
        lis.append(arr[idx])
        idx = prev[idx]

    return lis[::-1]


def longest_decreasing_subsequence(arr):
    neg = [-x for x in arr]
    lds_neg = longest_increasing_subsequence(neg)
    return [-x for x in lds_neg]



lis = longest_increasing_subsequence(arr)
lds = longest_decreasing_subsequence(arr)

print(" ".join(map(str, lis)))
print(" ".join(map(str, lds)))

