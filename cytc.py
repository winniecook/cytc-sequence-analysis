from Bio import Entrez, SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SimpleLocation, SeqFeature

# Always tell NCBI who you are
Entrez.email = "SzQwMDM5NjhAa2NsLmFjLnVr"  # Base64 encoded email

# Fetch the cytochrome c sequence using Entrez
handle = Entrez.efetch(db="protein", id="NP_061820.1", rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
handle.close()

print("1. Basic Sequence Information:")
print(f"Sequence: {record.seq}")
print(f"Length: {len(record.seq)}")

# Demonstrate Seq object methods
print("\n2. Seq Object Methods:")
print(f"Complement: {record.seq.complement()}")
print(f"Reverse Complement: {record.seq.reverse_complement()}")

# Create a new Seq object with a modified sequence
modified_seq = Seq(str(record.seq).replace("M", "X"))
print(f"\nModified Sequence: {modified_seq}")

# Demonstrate slicing
print("\n3. Sequence Slicing:")
print(f"First 10 amino acids: {record.seq[:10]}")
print(f"Last 10 amino acids: {record.seq[-10:]}")

# Demonstrate SeqRecord attributes
print("\n4. SeqRecord Attributes:")
print(f"ID: {record.id}")
print(f"Name: {record.name}")
print(f"Description: {record.description}")

# Demonstrate annotations
print("\n5. Annotations:")
for key, value in record.annotations.items():
    print(f"{key}: {value}")

#print features of biological sequences - genes, cds, exon from genbank file
print("\n6. Features:")
for feature in record.features:
    print(f"Type: {feature.type}")
    print(f"Location: {feature.location}")
    print("Qualifiers:")
    for key, value in feature.qualifiers.items():
        print(f"  {key}: {value}")
    print()

# Create a custom feature
custom_feature = SeqFeature(
    SimpleLocation(start=10, end=20),
    type="custom_region",
    qualifiers={"note": ["This is a custom feature"]}
)
record.features.append(custom_feature)

# Demonstrate SeqRecord slicing
sub_record = record[50:100]
print("\n7. Sliced SeqRecord:")
print(f"Sequence: {sub_record.seq}")
print(f"Length: {len(sub_record)}")
print(f"Number of features: {len(sub_record.features)}")

# Demonstrate SeqRecord addition
first_half = record[:len(record)//2]
second_half = record[len(record)//2:]
reconstructed_record = first_half + second_half
print("\n8. SeqRecord Addition:")
print(f"Reconstructed sequence length: {len(reconstructed_record)}")
print(f"Is it the same as the original? {reconstructed_record.seq == record.seq}")

# Demonstrate methods on a DNA sequence
dna_seq = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print("\n9. DNA Sequence Methods:")
print(f"Original DNA: {dna_seq}")
print(f"Transcription: {dna_seq.transcribe()}")
print(f"Translation: {dna_seq.translate()}")
print(f"Reverse Complement: {dna_seq.reverse_complement()}")

# Save the modified record to a GenBank file
SeqIO.write(record, "modified_cytochrome_c.gb", "genbank")
print("\n10. Modified record saved to 'modified_cytochrome_c.gb'")