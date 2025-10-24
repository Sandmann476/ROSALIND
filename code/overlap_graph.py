data = open("data/rosalind_grph (1).txt")

def read_fasta(data):
    fasta = {}
    label = None
    for line in data:#.strip().splitlines():
        line = line.strip()
        if line.startswith(">"):
            label = line[1:]#.strip()
            fasta[label] = ""
        else:
            fasta[label] += line#.strip()
    return fasta

def overlap_graph(fasta, k=3):
    edges = []
    labels = list(fasta.keys())
    for a in labels:
        for b in labels:
            if a != b and fasta[a].endswith(fasta[b][:k]):
                edges.append((a, b))
    return edges

fasta = read_fasta(data)
edges = overlap_graph(fasta, k=3)
for a, b in edges:
    print(a, b)