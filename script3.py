import sys

if len(sys.argv) != 3 or sys.argv[1] != "--seq":
    print("Usage: python count_fasta.py --seq file.mfa")
    sys.exit(1)

fasta_file = sys.argv[2]
count = 0

with open(fasta_file) as f:
    for line in f:
        if line.startswith(">"):
            count += 1

print(count)
