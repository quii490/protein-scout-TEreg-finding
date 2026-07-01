---
type: gene-evaluation
gene: DNASE1L1
date: 2026-06-28
tags: [nucleus-cytoplasm, DNase, ER, deoxyribonuclease, secretory]
status: shortlisted
---

# DNASE1L1 - Gene Evaluation

## 1. Basic Information

| Field | Value |
|-------|-------|
| **Gene Symbol** | DNASE1L1 |
| **UniProt Accession** | P49184 |
| **Protein Name** | Deoxyribonuclease-1-like 1 |
| **Protein Length** | 302 aa |
| **Molecular Function** | Deoxyribonuclease (predicted) |
| **Chromosome** | Xq28 |

## 2. Nuclear Localization Scoring

| Criterion | Score | Weight | Weighted | Notes |
|-----------|-------|--------|----------|-------|
| **GO-CC: Nucleus** | ×2 | ×4 | 8 | Nuclear GO-CC present but ER/secretory primary |
| **Primary Localization** | ×1 | ×5 | 5 | Endoplasmic reticulum (primary) |
| **HPA Nuclear Evidence** | ×1 | ×3 | 3 | No HPA data available (unclassified_bare) |
| **Nuclear PPI Partners** | ×1 | ×2 | 2 | No nuclear PPI partners |
| **Literature Evidence** | ×1 | ×3 | 3 | Minimal characterization, no nuclear function |
| **Total** | | | **21** | |



| **加权总分** | | | **21.0/180** | |
| **归一化总分 (÷1.83)** | | | **11.5/100** | |
## 3. Detailed Analysis

### 3.1 Protein Function
DNASE1L1 is a DNase I-like deoxyribonuclease. Despite the name suggesting DNA cleavage activity, DNASE1L1 is very poorly characterized. UniProt lists no functional annotation text, indicating minimal experimental characterization. It belongs to the DNase I family of endonucleases.

### 3.2 Nuclear Localization Evidence
- **GO-CC terms**: Endoplasmic reticulum, extracellular region, nucleus, specific granule lumen
- **UniProt annotation**: "Endoplasmic reticulum" - primary localization
- Nuclear GO-CC is present but the protein is primarily annotated to ER and secretory compartments
- The predicted signal peptide and ER localization suggest DNASE1L1 is processed through the secretory pathway
- Nuclear localization may be an artifact or incidental

### 3.3 Domain Architecture
DNASE1L1 is a 302 aa protein containing:
- **Signal peptide**: N-terminal, targeting to ER
- **DNase I domain**: Predicted endonuclease domain
- The secretory signal peptide argues against constitutive nuclear localization

### 3.4 Protein-Protein Interactions
- **GFAP (Glial fibrillary acidic protein)**: Cytoskeletal protein
- **SPCS1, SPCS2**: Signal peptidase complex subunits, ER-resident
- The SPCS interactions confirm ER localization and secretory pathway involvement
- No nuclear PPI partners

### 3.5 Relevance to TE Regulation
Limited relevance. DNASE1L1 is a poorly characterized secretory DNase. While DNases can process TE-derived DNA, the ER/secretory localization of DNASE1L1 makes nuclear DNA access unlikely under normal conditions.

## 4. Overall Assessment

**Classification: nucleus-cytoplasm** - Low confidence. DNASE1L1 is a poorly characterized secretory DNase with primary ER localization. The nuclear GO-CC annotation is contradictory to the signal peptide and ER processing evidence. Nuclear localization is unlikely to be functionally significant.

**Recommendation: Low priority.** Minimal characterization, contradictory localization evidence, and no connection to TE regulation. The secretory pathway targeting argues against meaningful nuclear function.

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00476; |
| InterPro | IPR018057;IPR016202;IPR033125;IPR036691;IPR005135; |
| Pfam | PF03372; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ESR2 | BioGRID | 1 |
| ESR1 | BioGRID | 1 |
| KIF14 | BioGRID | 1 |
| TAF5L | BioGRID | 1 |
| RPS6KA3 | BioGRID | 1 |
| RPL23 | BioGRID | 1 |
| BANP | BioGRID | 1 |
| CSPG4 | BioGRID | 1 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与核内 TE 调控过程，但目前无直接实验证据支持。需实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/DNASE1L1

### PubMed

**Count: 24**

| PMID | Title |
|---|---|
| 41688428 | cfGWAS reveal genetic basis of cell-free DNA end motifs. |
| 38907278 | Amplifications of EVX2 and HOXD9-HOXD13 on 2q31 in mature cystic teratomas of the ovary identified by array comparative genomic hybridization may expl |
| 37914307 | Utility of peripheral blood macrophage factor Apo10 and TKTL1 as markers in distinguishing malignant from benign lung nodules: a protocol for a prospe |
| 36628843 | Analysis of tafazzin and deoxyribonuclease 1 like 1 transcripts and X chromosome sequencing in the evaluation of the effect of mosaicism in the TAZ ge |
| 35725583 | Origin and significance of the human DNase repertoire. |


## 5. Data Sources

- UniProt: P49184 (accessed 2026-06-28 via REST API)
- GO-CC: endoplasmic reticulum (GO:0005783), nucleus (GO:0005634), extracellular region (GO:0005576)
- BioGRID PPI: human PPI dataset (GFAP, SPCS1, SPCS2 interactions)
- HPA: unclassified_bare (no nuclear localization data)
