import sys

if len(sys.argv) != 3 or sys.argv[1] != "--seq":
    print("Usage: python script1.py --seq seq.fa")
    sys.exit(1)

file_path = sys.argv[2]

length = 0
with open(file_path) as f:
    for line in f:
        if not line.startswith(">"):
            length += len(line.strip())

print(length)

