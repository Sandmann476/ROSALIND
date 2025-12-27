rna = "CGUAUUGUGCCAGUACGUUGAGGUACGCAGUUCUUCACGGACGGACCGUUCCGUCGAAGACGGACCCUCGACGAACCG"

a_count = rna.count("A")
g_count = rna.count("G")

a_pos = 1
g_pos = 1

for i in range(a_count):
    if a_count > 0:
        a_pos *= a_count
        a_count -= 1
for i in range(g_count):
    if g_count > 0:
        g_pos *= g_count
        g_count -= 1

print(a_pos * g_pos)
