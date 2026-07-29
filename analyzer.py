import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re

def analyze_vcf(file_path, target_gene=None):
    print(f"Loading and cleaning genomic data from {file_path}...\n")
    
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    # 1. Read VCF using pandas (skipping ## metadata headers)
    try:
        df = pd.read_csv(file_path, comment='#', sep='\t', header=None, low_memory=False)
        df.columns = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO']
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # 2. Data Wrangling: Extract Gene and Clinical Significance from the messy INFO column
    print("Extracting features from INFO column...")
    df['Gene'] = df['INFO'].str.extract(r'GENEINFO=([^:;]+)')
    df['Clinical_Significance'] = df['INFO'].str.extract(r'CLNSIG=([^;]+)')

    # 3. Handle Missing Data: Drop rows with empty Gene or Significance values
    df = df.dropna(subset=['Gene', 'Clinical_Significance'])

    # 4. Filter for Pathogenic variants
    pathogenic_df = df[df['Clinical_Significance'].str.contains('Pathogenic', na=False, case=False)]
    
    # 5. Filter by specific gene if user requested it via command line
    if target_gene:
        target_gene = target_gene.upper()
        pathogenic_df = pathogenic_df[pathogenic_df['Gene'].str.upper() == target_gene]
        print(f"--- Results for Gene: {target_gene} ---")
        if pathogenic_df.empty:
            print(f"No pathogenic variants found for {target_gene}.")
            return
    else:
        print(f"--- Overall Analysis Results ---")

    print(f"Total variants analyzed: {len(df)}")
    print(f"Pathogenic variants identified: {len(pathogenic_df)}\n")
    
    # Count the top genes
    top_genes = pathogenic_df['Gene'].value_counts().head(10)
    print("Top Genes with Pathogenic Variants:")
    print(top_genes.to_string())
    
    # 6. Generate Visualization (Only if not searching a single gene)
    if not target_gene:
        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_genes.values, y=top_genes.index, hue=top_genes.index, palette="mako", legend=False)
        
        plt.title("Frequency of Pathogenic Variants by Gene")
        plt.xlabel("Number of Pathogenic Mutations")
        plt.ylabel("Gene Symbol")
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()
        
        output_filename = "pathogenic_genes_distribution.png"
        plt.savefig(output_filename, dpi=300)
        print(f"\nSuccess! Data visualization saved locally as '{output_filename}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse and analyze ClinVar VCF files.")
    parser.add_argument('--file', type=str, default='clinvar_sample.vcf', help='Path to the VCF file')
    parser.add_argument('--gene', type=str, help='Specific gene to filter by (e.g., BRCA1)', default=None)
    
    args = parser.parse_args()
    analyze_vcf(args.file, args.gene)
