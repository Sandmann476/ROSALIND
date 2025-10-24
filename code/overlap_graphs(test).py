import networkx as nx

def parse_fasta(fasta_str):
    sequences = []
    seq_names = []
    current_seq = []
    for line in fasta_str.strip().splitlines():
        if line.startswith('>'):
            seq_names.append(line[1:].strip())
            if current_seq:
                sequences.append(''.join(current_seq))
                current_seq = []
        else:
            current_seq.append(line.strip())
    if current_seq:
        sequences.append(''.join(current_seq))
    return zip(seq_names, sequences)

def similarity(a, b):
    matches = sum(x == y for x, y in zip(a, b))
    return matches / len(a)

def build_graph(strands, threshold = 0.7):
    G = nx.Graph()
    for i, strand1 in strands:
        G.add_node(i, sequence=strand1)
        for j, strand2 in strands:
            if i < j:
                sim = similarity(strand1, strand2)
                if sim >= threshold:
                    G.add_edge(i, j, weight=sim)
    return G

def find_clusters(G):
    visited = set()
    clusters = []

    for node in G.nodes():
        if node not in visited:
            cluster = list(nx.bfs_tree(G, node))
            visited.update(cluster)
            clusters.append(cluster)
    return clusters

def most_similar_path(G, source, target):
    path = nx.dijkstra_path(G, source, target, weight = lambda u, v, d: 1 - d['weight'])
    return path

G = build_graph(parse_fasta(open('data/rosalind_cons.txt').read()), threshold=0.6)
clusters = find_clusters(G)
print("Clusters:", clusters)

path = most_similar_path(G, 0, 3)
print("Most similar path:", path)