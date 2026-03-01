
infile = open("/home/flo/Desktop/code/ROSALIND/data/rosalind_lgis (2).txt", "r")
sequence = infile.read().split()
sequence = [int(x) for x in sequence]


def longest_increasing_subsequence(seq):
    #points to an index of seq which holds the smallest value that could be used
    smallest_val_idx = [None] * len(seq)
    #indicates which is the previous element of the subsequence
    previous_index = [None] * len(seq)
    #Number that gets updated while looping

    # Since we have at least one element in our list, we can start by 
    # knowing that the there's at least an increasing subsequence of length one:
    N = 1
    smallest_val_idx[0] = 0

    # Looping over the sequence starting from the second element
    for i in range(1, len(seq)):
        # With a binary search we want the largest j <= N, such that seq[smallest_val_idx[j]] < seq[i]
        lower = 0
        upper = N
        # First we look at the upper bound value
        if seq[smallest_val_idx[upper - 1]] < seq[i]:
            j = upper
        # Actual binary search loop
        else:
            while upper - lower > 1:
                middle = (upper + lower) // 2
                if seq[smallest_val_idx[middle - 1]] < seq[i]:
                    lower = middle
                else:
                    upper = middle
            j = lower
        previous_index[i] = smallest_val_idx[j - 1]

        if j == N or seq[i] < seq[smallest_val_idx[j]]:
            smallest_val_idx[j] = i
            N = max(N, j + 1)

    # Building the result
    results = []
    pos = smallest_val_idx[N - 1]
    for _ in range(N):
        results.append(seq[pos])
        pos = previous_index[pos]
    return results[::-1] #reversing

def longest_decreasing_subsequence(seq):
    #points to an index of seq which holds the smallest value that could be used
    biggest_val_idx = [None] * len(seq)
    #indicates which is the previous element of the subsequence
    previous_index = [None] * len(seq)
    #Number that gets updated while looping

    # Since we have at least one element in our list, we can start by 
    # knowing that the there's at least an increasing subsequence of length one:
    N = 1
    biggest_val_idx[0] = 0

    # Looping over the sequence starting from the second element
    for i in range(1, len(seq)):
        # With a binary search we want the largest j <= N, such that seq[smallest_val_idx[j]] < seq[i]
        lower = 0
        upper = N
        # First we look at the upper bound value
        if seq[biggest_val_idx[upper - 1]] > seq[i]:
            j = upper
        # Actual binary search loop
        else:
            while upper - lower > 1:
                middle = (upper + lower) // 2
                if seq[biggest_val_idx[middle - 1]] > seq[i]:
                    lower = middle
                else:
                    upper = middle
            j = lower
        previous_index[i] = biggest_val_idx[j - 1]

        if j == N or seq[i] > seq[biggest_val_idx[j]]:
            biggest_val_idx[j] = i
            N = max(N, j + 1)

    # Building the result
    results = []
    pos = biggest_val_idx[N - 1]
    for _ in range(N):
        results.append(seq[pos])
        pos = previous_index[pos]
    return results[::-1] #reversing

for n in longest_increasing_subsequence(sequence):
    print(n, end=" ")
print("\n")
for n in longest_decreasing_subsequence(sequence):
    print(n, end=" ")
print("\n")