import biopython
from Bio import Entrez

# Set your email
Entrez.email = "malaevleo@mail.ru"

# Read RefSeq IDs from the file
with open("/mnt/data/matrisome_proteins.txt") as f:
    refseq_ids = f.read().strip().split()

# Fetch and save sequences to a FASTA file
with open("refseq_sequences.fasta", "w") as output_fasta:
    for refseq_id in refseq_ids:
        try:
            handle = Entrez.efetch(db="protein", id=refseq_id, rettype="fasta", retmode="text")
            fasta_data = handle.read()
            output_fasta.write(fasta_data)
            print(f"Retrieved: {refseq_id}")
        except Exception as e:
            print(f"Error retrieving {refseq_id}: {str(e)}")
