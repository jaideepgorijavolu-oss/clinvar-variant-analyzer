# Clinical Genomic Variant Analyzer (VCF)

A Python-based bioinformatics pipeline designed to parse, analyze, and visualize clinical genomic variant datasets directly from Variant Call Format (VCF) files.

## Overview
This project processes raw genomic variant data (simulating the NIH ClinVar database). It utilizes `pandas` for high-performance tabular data wrangling and Regular Expressions (`re`) to extract critical metadata (like Gene Symbols and Clinical Significance) from highly nested `INFO` columns. It handles missing data via `dropna()` and provides an interactive command-line interface.

## Features
* **VCF Parsing:** Natively reads standard tab-separated VCF genomic files.
* **Data Wrangling:** Extracts nested string data using Regular Expressions and manages missing data effectively.
* **Variant Filtering:** Identifies and isolates mutations flagged with 'Pathogenic' clinical significance.
* **CLI Implementation:** Built with `argparse` to allow users to search the dataset for specific target genes dynamically.
* **Automated Visualization:** Generates high-resolution bar charts mapping mutation distribution across key target genes using `matplotlib` and `seaborn`.

## Tech Stack
* **Language:** Python 3
* **Libraries:** `pandas`, `matplotlib`, `seaborn`, `argparse`, `re`

## How to Run
1. Clone this repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install pandas matplotlib seaborn
