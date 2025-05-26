import Bio
from Bio import SeqIO

input_dir = "msa_outputs"
output_dir = "phylip_files"

import os
os.makedirs(output_dir, exist_ok=True)

for fasta_file in os.listdir(input_dir):
    if fasta_file.endswith("_aligned.fasta"):
        input_path = os.path.join(input_dir, fasta_file)
        output_path = os.path.join(output_dir, fasta_file.replace("_aligned.fasta", ".phy"))
        
        records = list(SeqIO.parse(input_path, "fasta"))
        SeqIO.write(records, output_path, "phylip")
        print(f"Converted: {fasta_file} -> {output_path}")
