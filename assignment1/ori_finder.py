# ori_finder.py

from collections import defaultdict


def read_fasta(file_path):
    sequence = []
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(">"):
                continue
            sequence.append(line.upper())
    return "".join(sequence)


def cumulative_gc_skew(sequence):
    skew = 0
    skew_list = [0]

    for base in sequence:
        if base == "G":
            skew += 1
        elif base == "C":
            skew -= 1
        skew_list.append(skew)

    return skew_list


def find_ori(sequence, flank=250):
    skew = cumulative_gc_skew(sequence)
    min_index = skew.index(min(skew))

    start = max(0, min_index - flank)
    end = min(len(sequence), min_index + flank)

    return sequence[start:end], min_index
