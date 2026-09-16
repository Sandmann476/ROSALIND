import scipy

n, k = open("/home/florian-gruber/Programming/ROSALIND/data/rosalind_pper.txt", "r").read().split(" ")

print(scipy.special.perm(int(n), int(k)) % 1000000)
