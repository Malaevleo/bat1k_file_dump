from Bio import SeqIO
import pandas as pd


matrisome_fasta_file = "refseq_sequences.fasta"
bat_fasta_file = "myotis_protein.faa"
blast_results_file = "blastp_lowpid_myotis_data.txt"
output_file = "paired_lowpid_myotis_sequences.fasta"

def load_fasta_with_duplicates(fasta_file):
    sequences = {}
    for record in SeqIO.parse(fasta_file, "fasta"):
        if record.id not in sequences:
            sequences[record.id] = record
        else:
            print(f"Duplicate ID found: {record.id}, ignoring this entry.")
    return sequences

matrisome_sequences = load_fasta_with_duplicates(matrisome_fasta_file)
bat_sequences = load_fasta_with_duplicates(bat_fasta_file)


blast_df = pd.read_csv(blast_results_file, sep="\t")

with open(output_file, "w") as output_fasta:
    for index, row in blast_df.iterrows():
        qseqid = row["qseqid"]
        sseqid = row["sseqid"]

        # Get the qseqid sequence from the human matrisome
        if qseqid in matrisome_sequences:
            qseq = matrisome_sequences[qseqid].seq
            qdesc = matrisome_sequences[qseqid].description
        else:
            print(f"QseqID {qseqid} not found in human matrisome.")
            continue

        # Get the sseqid sequence from the bat proteome
        if sseqid in bat_sequences:
            sseq = bat_sequences[sseqid].seq
            sdesc = bat_sequences[sseqid].description
        else:
            print(f"SseqID {sseqid} not found in bat proteome.")
            continue

        # Write the sequences to the output file in FASTA format, paired by query/subject
        output_fasta.write(f">{qseqid} {qdesc}\n{qseq}\n")
        output_fasta.write(f">{sseqid} {sdesc}\n{sseq}\n")

print(f"Paired sequences written to {output_file}")