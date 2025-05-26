with open("matrisome_proteins.txt", "r") as input_file:
    data = input_file.read()

# Split the IDs by ":" and save them to a new file with one ID per line
ids = data.split(":")
with open("split_uniprot_ids.txt", "w") as output_file:
    for id_ in ids:
        output_file.write(id_.strip() + "\n")
