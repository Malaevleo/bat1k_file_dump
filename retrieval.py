import Bio
from Bio import Entrez
# in case it fails and wants to file a report
Entrez.email = "malaevleo@mail.ru"

'''with open("matrisome_proteinsref.txt") as f:
    refseq_ids = f.read().strip().replace(':', '\n').split()

with open("refseq_sequences.fasta", "w") as output_fasta:
    for refseq_id in refseq_ids:
        try:
            handle = Entrez.efetch(db="protein", id=refseq_id, rettype="fasta", retmode="text")
            fasta_data = handle.read()
            output_fasta.write(fasta_data)
            print(f"Retrieved: {refseq_id}")
        except Exception as e:
            print(f"Error retrieving {refseq_id}: {str(e)}") '''


'''with open("collagensonlyids.txt") as f:
    refseq_ids = f.read().strip().replace(':', '\n').split()

with open("homo_collagens.fasta", "w") as output_fasta:
    for refseq_id in refseq_ids:
        try:
            handle = Entrez.efetch(db="protein", id=refseq_id, rettype="fasta", retmode="text")
            fasta_data = handle.read()
            output_fasta.write(fasta_data)
            print(f"Retrieved: {refseq_id}")
        except Exception as e:
            print(f"Error retrieving {refseq_id}: {str(e)}")'''

'''
with open("glycoprotsids.txt") as f:
    refseq_ids = f.read().strip().replace(':', '\n').split()

with open("homo_glycoprots.fasta", "w") as output_fasta:
    for refseq_id in refseq_ids:
        try:
            handle = Entrez.efetch(db="protein", id=refseq_id, rettype="fasta", retmode="text")
            fasta_data = handle.read()
            output_fasta.write(fasta_data)
            print(f"Retrieved: {refseq_id}")
        except Exception as e:
            print(f"Error retrieving {refseq_id}: {str(e)}")
'''

'''with open("proteoglycansids.txt") as f:
    refseq_ids = f.read().strip().replace(':', '\n').split()

with open("homo_proteoglycans.fasta", "w") as output_fasta:
    for refseq_id in refseq_ids:
        try:
            handle = Entrez.efetch(db="protein", id=refseq_id, rettype="fasta", retmode="text")
            fasta_data = handle.read()
            output_fasta.write(fasta_data)
            print(f"Retrieved: {refseq_id}")
        except Exception as e:
            print(f"Error retrieving {refseq_id}: {str(e)}")'''

with open("secretedfactorsids.txt") as f:
    refseq_ids = f.read().strip().replace(':', '\n').split()

with open("homo_secrets.fasta", "w") as output_fasta:
    for refseq_id in refseq_ids:
        try:
            handle = Entrez.efetch(db="protein", id=refseq_id, rettype="fasta", retmode="text")
            fasta_data = handle.read()
            output_fasta.write(fasta_data)
            print(f"Retrieved: {refseq_id}")
        except Exception as e:
            print(f"Error retrieving {refseq_id}: {str(e)}")