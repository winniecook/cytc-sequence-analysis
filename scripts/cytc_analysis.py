# cytc_analysis.py
from Bio import Entrez, SeqIO
from Bio.Seq import Seq
import json

def main(snakemake):
    Entrez.email = "your@email.com"  # Replace with your email

    # Fetch the cytochrome c sequence using Entrez
    handle = Entrez.efetch(db="protein", id=snakemake.params.protein_id, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()

    # Save GenBank and FASTA files
    SeqIO.write(record, snakemake.output.gb, "genbank")
    SeqIO.write(record, snakemake.output.fasta, "fasta")

    # Perform analysis
    analysis_results = {
        "id": record.id,
        "name": record.name,
        "description": record.description,
        "length": len(record.seq),
        "molecular_weight": record.annotations.get("molecular_weight", "N/A"),
        "first_10_aa": str(record.seq[:10]),
        "last_10_aa": str(record.seq[-10:]),
        "num_features": len(record.features)
    }

    # Save analysis results
    with open(snakemake.output.json, "w") as f:
        json.dump(analysis_results, f, indent=2)

if __name__ == "__main__":
    main(snakemake)
