

def get_enzyme_database():
    return {
        "ecori": "GAATTC",
        "bamhi": "GGATCC",
        "hindiii": "AAGCTT",
        "psti": "CTGCAG",
        "sphi": "GCATGC",
        "sali": "GTCGAC",
        "xbai": "TCTAGA",
        "kpni": "GGTACC",
        "saci": "GAGCTC",
        "smai": "CCCGGG",
    }


def load_markers(marker_file):
    markers = {}
    with open(marker_file, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                markers[parts[0].lower()] = parts[1].upper()
    return markers


def parse_design(design_file):
    features = []
    with open(design_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("**"):
                continue
            parts = [x.strip() for x in line.split(",")]
            if len(parts) == 2:
                features.append(parts[1])
    return features


def apply_design(sequence, features, markers):
    enzyme_db = get_enzyme_database()

    for feature in features:
        f = feature.lower()

        if f in enzyme_db:
            site = enzyme_db[f]
            sequence = sequence.replace(site, "")

        elif f in markers:
            sequence += markers[f]

    return sequence


def insert_ori_and_replication(plasmid_seq, ori_seq):
    # Simple insertion strategy:
    # Prepend ORI + default replication gene

    default_rep_gene = "ATGCGTACGTAGCTAGCTAGCTAGCTAGCTA"  # placeholder replication gene

    return ori_seq + default_rep_gene + plasmid_seq
