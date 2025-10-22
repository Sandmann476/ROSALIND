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
                    #!/usr/bin/env python3
                    """Consensus and profile from FASTA with configurable input file.

                    Usage:
                      python code/consensus_and_profile.py [input.fa]

                    If no input is given the default is 'data/consensus_and_profile.txt'.
                    Pass '-' to read FASTA from stdin.
                    """

                    import argparse
                    import sys


                    def parse_fasta(path):
                        """Return a list of sequences parsed from a FASTA file or stdin ('-')."""
                        sequences = []
                        cur = None
                        if path == '-':
                            iterator = (line for line in sys.stdin)
                            close_when_done = False
                        else:
                            iterator = open(path)
                            close_when_done = True

                        try:
                            for line in iterator:
                                line = line.strip()
                                if not line:
                                    continue
                                if line.startswith('>'):
                                    if cur is not None:
                                        sequences.append(cur)
                                    cur = ""
                                else:
                                    if cur is None:
                                        # handle files that start with sequence lines (not strictly FASTA)
                                        cur = ""
                                    cur += line
                            if cur is not None:
                                sequences.append(cur)
                        finally:
                            if close_when_done:
                                iterator.close()

                        return sequences


                    def build_profile(sequences):
                        if not sequences:
                            return {'A': [], 'C': [], 'G': [], 'T': []}
                        L = len(sequences[0])
                        profile = {b: [0] * L for b in 'ACGT'}
                        for s in sequences:
                            # if sequences are different lengths, we only count up to the first length
                            for i, ch in enumerate(s[:L]):
                                if ch in profile:
                                    profile[ch][i] += 1
                                else:
                                    # ignore unexpected letters
                                    pass
                        return profile


                    def consensus_from_profile(profile):
                        if not profile['A']:
                            return ''
                        L = len(profile['A'])
                        consensus = []
                        for i in range(L):
                            best = None
                            best_count = -1
                            for b in 'ACGT':
                                if profile[b][i] > best_count:
                                    best = b
                                    best_count = profile[b][i]
                            consensus.append(best)
                        return ''.join(consensus)


                    def main(argv=None):
                        parser = argparse.ArgumentParser(description='Compute consensus and profile from FASTA')
                        parser.add_argument('input', nargs='?', default='data/consensus_and_profile.txt',
                                            help="Input FASTA file (use '-' for stdin). Defaults to data/consensus_and_profile.txt")
                        args = parser.parse_args(argv)

                        try:
                            seqs = parse_fasta(args.input)
                        except FileNotFoundError:
                            print(f"Error: file not found: {args.input}", file=sys.stderr)
                            sys.exit(2)
                        except Exception as e:
                            print(f"Error reading {args.input}: {e}", file=sys.stderr)
                            sys.exit(2)

                        profile = build_profile(seqs)
                        cons = consensus_from_profile(profile)
                        print(cons)
                        for b in 'ACGT':
                            print(f"{b}: {' '.join(str(x) for x in profile[b])}")


                    if __name__ == '__main__':
                        main()