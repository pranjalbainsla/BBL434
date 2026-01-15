import sys

if len(sys.argv) != 5 or sys.argv[1] != "--seq" or sys.argv[3] != "-k":
    print("Usage: python kmer_count.py --seq seq.fa -k 3")
    sys.exit(1)

fasta_file = sys.argv[2]
k = int(sys.argv[4])

# Read sequence (ignore FASTA headers)
sequence = ""
with open(fasta_file) as f:
    for line in f:
        if not line.startswith(">"):
            sequence += line.strip()

kmer_dict = {}

for i in range(len(sequence) - k + 1):
    kmer = sequence[i:i+k]
    kmer_dict[kmer] = kmer_dict.get(kmer, 0) + 1

print(kmer_dict)
