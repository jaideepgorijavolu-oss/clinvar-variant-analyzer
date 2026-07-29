# Clinical Genomic Variant Analyzer

A Python-based bioinformatics pipeline designed to parse, analyze, and visualize clinical genomic variant datasets. 

## Overview
This project simulates a workflow for processing genomic variant data (similar to NIH ClinVar). It utilizes `pandas` for high-performance tabular data wrangling to isolate pathogenic mutations and maps disease-associated phenotypes. 

## Features
* **Data Ingestion:** Reads standard comma-separated genomic variant data.
* **Variant Filtering:** Identifies and isolates mutations flagged with 'Pathogenic' clinical significance.
* **Automated Visualization:** Generates high-resolution bar charts mapping mutation distribution across key target genes using `matplotlib` and `seaborn`.

## Tech Stack
* **Language:** Python 3
* **Libraries:** `pandas`, `matplotlib`, `seaborn`
