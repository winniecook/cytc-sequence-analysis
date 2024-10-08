configfile: "config.yaml"

rule all:
    input:
        "results/cytc_report.html"

rule fetch_and_analyze_cytc:
    output:
        gb="results/cytochrome_c.gb",
        fasta="results/cytochrome_c.fasta",
        json="results/cytc_analysis.json"
    params:
        protein_id=config.get("cytc_protein_id", "NP_061820.1")
    script:
        "scripts/cytc_analysis.py"

rule generate_report:
    input:
        "results/cytc_analysis.json"
    output:
        "results/cytc_report.html"
    script:
        "scripts/generate_report.py"