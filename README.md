# SCENIC-Based Gene Regulatory Network Analysis of Human PBMCs

## 1. Project Overview

This project applies **SCENIC (Single-Cell Regulatory Network Inference and Clustering)** to a human Peripheral Blood Mononuclear Cell (PBMC) single-cell RNA sequencing dataset.

The objective is to infer transcription factor (TF)-target gene relationships, identify regulons using motif enrichment, and quantify transcription factor activity across individual cells using AUCell.

## 2. Dataset

- **Dataset:** 10x Genomics PBMC 3k
- **Organism:** Homo sapiens
- **Initial dataset:** 2,700 cells and 32,738 genes
- **After quality filtering:** 2,689 cells and 13,665 genes

## 3. Methodology

The analysis followed the three main stages of the SCENIC workflow:

### Step 1: Data preprocessing
- Loaded the 10x Genomics expression matrix.
- Evaluated total counts, detected genes and mitochondrial gene percentage.
- Applied quality filtering to remove low-quality cells and genes.

### Step 2: Gene regulatory network inference
- Used **GRNBoost2** to infer TF-target relationships.
- Generated an adjacency table containing transcription factors, target genes and importance scores.

### Step 3: Regulon identification
- Used **cisTarget motif enrichment** to identify motif-supported TF-target relationships.
- Identified significant motif enrichment results using an NES threshold of 3.0.
- Generated regulon target gene sets.

### Step 4: Regulon activity scoring
- Used **AUCell** to calculate regulon activity scores for individual cells.
- Generated a cell-by-regulon activity matrix.

## 4. Results

The analysis produced:

- **252 regulons**
- **30,661 TF-target relationships** in the extracted regulon target sets
- AUCell activity scores for **2,689 cells**
- A final AUCell matrix containing **252 regulons**

The top regulons by mean AUCell activity included JUNB, ZNF564, JUN, MYC and ZNF384.

## 5. Visualizations

The following figures summarize the results:

1. `Top 15 Regulons.png` – Top regulons ranked by mean AUCell activity.
2. `Regulon Activity Heatmap.png` – Regulon activity across individual PBMC cells.
3. `Top 15 TF Target Interactions.png` – Highest-importance predicted TF-target interactions from GRNBoost2.

## 6. Tools and Technologies

- Python
- pySCENIC
- GRNBoost2
- cisTarget
- AUCell
- Pandas
- NumPy
- Matplotlib
- Google Colab

## 7. Limitations

- The inferred TF-target relationships are computational predictions and do not establish direct physical binding or causal regulation.
- Motif enrichment provides supporting evidence for regulatory relationships but does not experimentally validate them.
- The analysis uses a single PBMC dataset, so the inferred regulatory patterns may not generalize to all cell types or biological conditions.
- AUCell scores represent relative regulon activity and should not be interpreted as direct measurements of transcription factor protein abundance.

## 8. Repository Structure

```text
SCENIC-PBMC-Analysis/
│
├── Data Preprocessing.ipynb
├── SCENIC PBMC Analysis.ipynb
├── Top 15 Regulons.png
├── Regulon Activity Heatmap.png
├── Top 15 TF Target Interactions.png
└── README.md
```

## 9. References

Aibar et al. (2017). SCENIC: Single-cell regulatory network inference and clustering. *Nature Methods*, 14, 1083–1086.

10x Genomics. PBMC 3k dataset.
