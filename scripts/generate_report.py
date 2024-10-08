
import json

def main(snakemake):
    with open(snakemake.input[0], "r") as f:
        analysis_results = json.load(f)

    html_content = f"""
    <html>
    <body>
    <h1>Cytochrome C Analysis Report</h1>
    <ul>
        <li>ID: {analysis_results['id']}</li>
        <li>Name: {analysis_results['name']}</li>
        <li>Description: {analysis_results['description']}</li>
        <li>Length: {analysis_results['length']}</li>
        <li>Molecular Weight: {analysis_results['molecular_weight']}</li>
        <li>First 10 amino acids: {analysis_results['first_10_aa']}</li>
        <li>Last 10 amino acids: {analysis_results['last_10_aa']}</li>
        <li>Number of features: {analysis_results['num_features']}</li>
    </ul>
    </body>
    </html>
    """

    with open(snakemake.output[0], "w") as f:
        f.write(html_content)

if __name__ == "__main__":
    main(snakemake)