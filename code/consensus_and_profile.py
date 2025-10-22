infile = open("data/consensus_and_profile.txt")
Profile = {'A': [], 'C': [], 'G': [], 'T': []}
#!/usr/bin/env python3
"""Compute consensus string and profile matrix from FASTA input.

Reads sequences from data/consensus_and_profile.txt and prints the
consensus followed by profile counts for A, C, G, T (space-separated).
"""

def parse_fasta(path):
    sequences = []
    cur = None
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                if cur is not None:
                    sequences.append(cur)
                cur = ""
            else:
                cur += line
        if cur is not None:
            sequences.append(cur)
    return sequences

def build_profile(sequences):
    if not sequences:
        return {'A': [], 'C': [], 'G': [], 'T': []}
    L = len(sequences[0])
    profile = {b: [0] * L for b in 'ACGT'}
    for s in sequences:
        for i, ch in enumerate(s):
            if ch in profile:
                profile[ch][i] += 1
            else:
                # ignore unexpected letters (could raise instead)
                pass
    return profile

def consensus_from_profile(profile):
    if not profile['A']:
        return ''
    L = len(profile['A'])
    consensus = []
    for i in range(L):
        # pick base with highest count; tie-breaking follows A, C, G, T order
        best = None
        best_count = -1
        for b in 'ACGT':
            if profile[b][i] > best_count:
                best = b
                best_count = profile[b][i]
        consensus.append(best)
    return ''.join(consensus)

def main():
    seqs = parse_fasta('data/consensus_and_profile.txt')
    profile = build_profile(seqs)
    cons = consensus_from_profile(profile)
    print(cons)
    for b in 'ACGT':
        print(f"{b}: {' '.join(str(x) for x in profile[b])}")


if __name__ == '__main__':
    main()