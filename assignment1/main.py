

import sys
from ori_finder import read_fasta, find_ori
from plasmid_modifier import (
    load_markers,
    parse_design,
    apply_design,
    insert_ori_and_replication,
)


def write_fasta(output_path, sequence):
    with open(output_path, "w") as f:
        f.write(">Universal_Plasmid\n")
        for i in range(0, len(sequence), 70):
            f.write(sequence[i:i+70] + "\n")


def main():

    if len(sys.argv) != 6:
        print("\nUsage:")
        print("python universal_plasmid_maker.py <Input_genome.fa> <plasmid.fa> <Design.txt> <markers.tab> <Output.fa>\n")
        sys.exit(1)

    genome_file = sys.argv[1]
    plasmid_file = sys.argv[2]
    design_file = sys.argv[3]
    marker_file = sys.argv[4]
    output_file = sys.argv[5]

    print("\n--- Universal Plasmid Maker ---\n")

    # 1️⃣ Find ORI from genome
    genome_seq = read_fasta(genome_file)
    ori_seq, ori_position = find_ori(genome_seq)

    print(f"[INFO] ORI found at position: {ori_position}")
    print(f"[INFO] ORI length: {len(ori_seq)} bp")

    # 2️⃣ Read plasmid backbone
    plasmid_seq = read_fasta(plasmid_file)

    # 3️⃣ Insert ORI + replication genes
    plasmid_seq = insert_ori_and_replication(plasmid_seq, ori_seq)

    # 4️⃣ Parse design file
    features = parse_design(design_file)

    # 5️⃣ Load markers
    markers = load_markers(marker_file)

    # 6️⃣ Apply design modifications
    plasmid_seq = apply_design(plasmid_seq, features, markers)

    # 7️⃣ Write output
    write_fasta(output_file, plasmid_seq)

    print(f"[SUCCESS] Output written to {output_file}\n")


if __name__ == "__main__":
    main()
