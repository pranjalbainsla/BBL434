import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from plasmid_modifier import apply_design


def test_delete_ecori():
    seq = "AAAAGAATTCTTT"
    features = ["EcoRI"]
    markers = {}

    new_seq = apply_design(seq, features, markers)

    assert "GAATTC" not in new_seq


def test_add_marker():
    seq = "AAAATTTT"
    features = ["AmpR"]
    markers = {"ampr": "GGGG"}

    new_seq = apply_design(seq, features, markers)

    assert "GGGG" in new_seq
