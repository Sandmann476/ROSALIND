infile = open('data/rosalind_gc (3).txt', 'r')
gc_count = 0
length = 0
for line in infile:
    line = line.strip()
    if line[0] == '>':
        if length > 0:
            print((gc_count/length)*100)
            length = 0
            gc_count = 0
        print(line)
    else :
        length += len(line)
        gc_count += line.count('G') + line.count('C')
print((gc_count/length)*100)
