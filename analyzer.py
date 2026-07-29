import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_variants(file_path):
    print(f"Loading genomic data from {file_path}...\n")
    
    # Check if file exists to prevent errors
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found. Please ensure the data file is in the same folder.")
        return

    # Load data
    df = pd.read_csv(file_path)
    
    # Filter for pathogenic variants
    pathogenic_df = df[df['Clinical_Significance'].str.contains('Pathogenic', na=False)]
    
    print(f"--- Analysis Results ---")
    print(f"Total variants analyzed: {len(df)}")
    print(f"Pathogenic variants identified: {len(pathogenic_df)}\n")
    
    # Count the top genes
    top_genes = pathogenic_df['Gene_Symbol'].value_counts()
    print("Top Genes with Pathogenic Variants:")
    print(top_genes.to_string())
    
    # Generate Visualization
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_genes.values, y=top_genes.index, hue=top_genes.index, palette="mako", legend=False)
    
    plt.title("Frequency of Pathogenic Variants by Gene")
    plt.xlabel("Number of Pathogenic Mutations")
    plt.ylabel("Gene Symbol")
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Save output
    output_filename = "pathogenic_genes_distribution.png"
    plt.savefig(output_filename, dpi=300)
    print(f"\nSuccess! Data visualization saved locally as '{output_filename}'.")

if __name__ == "__main__":
    analyze_variants("sample_clinvar.csv")
