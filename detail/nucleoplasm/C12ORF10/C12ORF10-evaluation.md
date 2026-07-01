---
type: gene-evaluation
gene: C12ORF10
date: 2026-06-28
tags: [nucleoplasm, nucleolus, RNA-exonuclease, mitochondrial, dual-localization]
status: shortlisted
---

# C12ORF10 (MYG1) - Gene Evaluation

## 1. Basic Information

| Field | Value |
|-------|-------|
| **Gene Symbol** | C12ORF10 (MYG1) |
| **UniProt Accession** | Q9HB07 |
| **Protein Name** | MYG1 exonuclease |
| **Protein Length** | 376 aa |
| **Molecular Function** | 3'-5' RNA exonuclease |
| **Chromosome** | 12q13.13 |
| **PubMed Hits** | 3 |

## 2. Nuclear Localization Scoring

| Criterion | Score | Weight | Weighted | Notes |
|-----------|-------|--------|----------|-------|
| **GO-CC: Nucleus** | ×4 | ×4 | 16 | nucleoplasm, nucleolus, nucleus all annotated |
| **GO-CC: Nucleoplasm** | ×4 | ×1 | 4 | Primary subcellular location per UniProt |
| **GO-CC: Nucleolus** | ×4 | ×5 | 20 | Ribosomal RNA processing role |
| **HPA Nuclear Evidence** | ×1 | ×3 | 3 | No HPA data available (unclassified_bare) |
| **Nuclear PPI Partners** | ×1 | ×2 | 2 | COPS5 (nuclear COP9 signalosome), DSTN |
| **Literature Evidence** | ×2 | ×3 | 6 | Published nucleo-mitochondrial crosstalk role (PMID:31081026) |
| **Total** | | | **51** | |



| **加权总分** | | | **51.0/180** | |
| **归一化总分 (÷1.83)** | | | **27.9/100** | |
## 3. Detailed Analysis

### 3.1 Protein Function
MYG1 (C12ORF10) is a 3'-5' RNA exonuclease that operates in both the nucleus and mitochondrion. It cleaves specific transcripts in situ in both organelles, functioning as a coordinator of nucleo-mitochondrial crosstalk. In the nucleolus, it processes pre-ribosomal RNA involved in ribosome assembly and alters cytoplasmic translation. In the mitochondrial matrix, it processes 3'-termini of mito-ribosomal and messenger RNAs and controls mitochondrial protein translation.

### 3.2 Nuclear Localization Evidence
- **GO-CC terms**: Nucleoplasm (primary), Nucleolus (primary), Nucleus, Mitochondrion, Mitochondrial matrix
- **UniProt annotation**: "Nucleus, nucleoplasm; Nucleus, nucleolus; Mitochondrion matrix"
- The dual nuclear-mitochondrial localization is well-established and functionally characterized

### 3.3 Domain Architecture
MYG1 contains an exonuclease domain characteristic of the DEDD superfamily of 3'-5' exonucleases. At 376 aa, it is a compact single-domain enzyme.

### 3.4 Protein-Protein Interactions
- **COPS5 (COP9 signalosome subunit 5)**: Nuclear protein involved in deneddylation, part of the COP9 signalosome complex
- **DSTN (Destrin/ADF)**: Actin-depolymerizing factor
- **DAK**: Dihydroxyacetone kinase
- Interaction with COPS5 suggests involvement in nuclear protein degradation regulation

### 3.5 Relevance to TE Regulation
MYG1's role in ribosomal RNA processing in the nucleolus makes it relevant to translational control. Its ability to process specific RNA transcripts in the nucleus could extend to TE-derived transcripts. The nucleo-mitochondrial crosstalk function suggests it may participate in organellar coordination of gene expression, which is often disrupted by TE insertions.

## 4. Overall Assessment

**Classification: nucleoplasm** - Strong nuclear localization with defined nucleoplasmic and nucleolar roles. The dual mitochondrial localization does not detract from its clear nuclear function as an RNA processing enzyme.

**Strengths**:
- Explicit nucleoplasm and nucleolus annotation
- Published functional data on nuclear RNA processing
- Compact, well-defined domain architecture

**Weaknesses**:
- Very few PubMed publications (3 total)
- No HPA immunohistochemistry data
- Limited PPI network in nuclear context

**Recommendation: Shortlist for TE regulation evaluation.** The RNA exonuclease activity in the nucleus, particularly in the nucleolus for rRNA processing, provides a plausible mechanism for TE-derived RNA surveillance.

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| COPS5 | BioGRID | 1 |
| HSP90AB1 | BioGRID | 1 |
| HSP90AA1 | BioGRID | 1 |
| DDX39A | BioGRID | 1 |
| DDX39B | BioGRID | 1 |
| RBBP7 | BioGRID | 1 |
| SUGT1 | BioGRID | 1 |
| FAM9B | BioGRID | 1 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000139637

![](https://images.proteinatlas.org/38627/591_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/38627/591_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/38627/579_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/38627/579_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/38627/581_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/38627/581_B4_2_red_green.jpg)

### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/C12ORF10

## 5. Data Sources

- UniProt: Q9HB07 (accessed 2026-06-28 via REST API)
- GO-CC: nucleoplasm (GO:0005654), nucleolus (GO:0005730), nucleus (GO:0005634)
- PubMed: 31081026 (nucleo-mitochondrial crosstalk)
- BioGRID PPI: human PPI dataset v4.4
- HPA: unclassified_bare (no nuclear localization data)
