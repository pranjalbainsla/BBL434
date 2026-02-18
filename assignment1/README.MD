Plasmid Maker Pipeline

- Reads genome (Input.fa) and detects ORI using cumulative GC skew.

- Extracts ORI region from genome.

- Inserts ORI + default replication gene into plasmid backbone.

- Parses Design.txt:

- Removes listed restriction enzyme sites.

- Adds requested markers from markers.tab.

Outputs modified plasmid as Output.fa.

How to Run ->
python main.py <Input.fa> <Plasmid.fa> <Design_pUC19.txt> <markers.tab> <Output.fa>


Example:

python main.py Input.fa pUC19.fa Design_pUC19.txt markers.tab Output.fa

Run Tests ->
python -m pytest
