# Cytochrome C Analysis Project

This project uses Snakemake to create a workflow for analyzing the cytochrome c protein sequence.

## Prerequisites

- Python 3.9+
- Conda
- Snakemake
- Biopython

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/cytochrome_c_project.git
   cd cytochrome_c_project
   ```

2. Create and activate the Conda environment:
   ```
   conda env create -f environment.yml
   conda activate cytc_analysis
   ```

## Usage

Run the Snakemake workflow:

```
snakemake --cores all
```

This will:
1. Fetch the cytochrome c sequence from NCBI
2. Analyze the sequence
3. Generate a JSON file with analysis results
4. Create an HTML report

Results will be in the `results/` directory.

## Project Structure

- `Snakefile`: Defines the workflow
- `config.yaml`: Configuration file for the project
- `scripts/`: Contains Python scripts for analysis and report generation
- `results/`: Output directory (created when the workflow runs)

### Scripts

- `scripts/cytc_analysis.py`: This script fetches the cytochrome c sequence from NCBI, performs basic sequence analysis (length, molecular weight, etc.), and saves the results in JSON format.

- `scripts/generate_report.py`: This script takes the JSON output from the analysis script and generates an HTML report, presenting the results in a more readable format.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
