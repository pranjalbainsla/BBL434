import sys

def read_fasta_length(file_path):
    sequence = ""

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line.startswith(">"):   # Ignore header
                sequence += line

    print(f"Sequence Length: {len(sequence)}")


def main():
    if len(sys.argv) != 3 or sys.argv[1] != "--seq":
        print("Usage: python script1.py --seq <fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[2]
    read_fasta_length(fasta_file)


if __name__ == "__main__":
    main()
