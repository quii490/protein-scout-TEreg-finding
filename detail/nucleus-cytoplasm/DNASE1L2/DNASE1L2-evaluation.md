---
type: gene-evaluation
gene: DNASE1L2
date: 2026-06-28
tags: [nucleus-cytoplasm, DNase, epidermal, corneocyte, secreted, incidental-nuclear]
status: shortlisted
---

# DNASE1L2 - Gene Evaluation

## 1. Basic Information

| Field | Value |
|-------|-------|
| **Gene Symbol** | DNASE1L2 |
| **UniProt Accession** | Q92874 |
| **Protein Name** | Deoxyribonuclease-1-like 2 |
| **Protein Length** | 299 aa |
| **Molecular Function** | Acid DNA endonuclease |
| **Chromosome** | 16p13.3 |

## 2. Nuclear Localization Scoring

| Criterion | Score | Weight | Weighted | Notes |
|-----------|-------|--------|----------|-------|
| **GO-CC: Nucleus** | ×2 | ×4 | 8 | Nuclear GO-CC present but functional context is extracellular |
| **Primary Localization** | ×1 | ×5 | 5 | Cytoplasm/secreted (primary) |
| **HPA Nuclear Evidence** | ×1 | ×3 | 3 | No HPA data available (unclassified_bare) |
| **Nuclear PPI Partners** | ×1 | ×2 | 2 | PHF13 (nuclear) but weak evidence |
| **Literature Evidence** | ×2 | ×3 | 6 | Known epidermal DNase, nuclear degradation during cornification |
| **Total** | | | **24** | |



| **加权总分** | | | **24.0/180** | |
| **归一化总分 (÷1.83)** | | | **13.1/100** | |
## 3. Detailed Analysis

### 3.1 Protein Function
DNASE1L2 is a divalent cation-dependent acid DNA endonuclease involved in the breakdown of the nucleus during corneocyte formation in epidermal keratinocytes. It may play an immune role by eliminating harmful DNA released into the extracellular environment by damaged epidermal cells.

### 3.2 Nuclear Localization Evidence
- **GO-CC terms**: Cytoplasm, extracellular region, nucleus
- **UniProt annotation**: "Cytoplasm; Secreted"
- The protein is involved in nuclear degradation during cornification - this is a degradative process where DNASE1L2 breaks down nuclear DNA during terminal differentiation of keratinocytes
- However, DNASE1L2 is not a functional nuclear resident - it accesses the nucleus only when the nuclear envelope breaks down during cornification
- The primary localization is cytoplasmic and secreted

### 3.3 Domain Architecture
DNASE1L2 is a 299 aa protein with:
- **Signal peptide**: N-terminal secretion signal
- **DNase I domain**: Acid-optimal endonuclease activity
- The low pH optimum is consistent with its function in the acidifying environment of differentiating keratinocytes

### 3.4 Protein-Protein Interactions
- **PHF13**: PHD finger protein 13, nuclear chromatin regulator - potential connection but evidence is weak (single Huttlin 2015 screen)
- **SLC19A2, SLC25A21**: Solute carrier proteins, likely non-specific

### 3.5 Relevance to TE Regulation
Limited relevance in steady-state cells. DNASE1L2 functions specifically during keratinocyte terminal differentiation to degrade nuclear DNA, including any TE-derived DNA. This is a specialized terminal differentiation function rather than a general TE regulatory mechanism.

## 4. Overall Assessment

**Classification: nucleus-cytoplasm** - Low confidence. DNASE1L2 accesses the nucleus only during terminal differentiation for DNA degradation. It does not function as a nuclear regulatory protein in steady-state cells. The connection to nuclear DNA is degradative and cell-type-specific.

**Recommendation: Low priority.** Specialized function in epidermal differentiation with no evidence of TE regulatory activity in physiologically relevant contexts.

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000167968-DNASE1L2

![](https://images.proteinatlas.org/44714/527_H4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44714/527_H4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/44714/522_H4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44714/522_H4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/44714/529_H4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/44714/529_H4_3_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00476; |
| InterPro | IPR018057;IPR016202;IPR033125;IPR036691;IPR005135; |
| Pfam | PF03372; |
| UniProt Domain [FT] | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| XRN2 | STRING | 854 |
| DXO | STRING | 824 |
| PHF13 | STRING | 824 |
| SPOC1 | STRING | 824 |
| TBX20 | STRING | 782 |
| RPL23 | BioGRID | 1 |
| BLVRA | BioGRID | 1 |
| PTDSS1 | BioGRID | 1 |


### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能直接或间接参与 TE 沉默机制，值得进一步实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/DNASE1L2

### PubMed

**Count: 31**

| PMID | Title |
|---|---|
| 42351650 | A Gene Feature Based on Histone Modifications Can Predict the Prognosis of Prostate Cancer. |
| 41908962 | Genome-wide assessment of runs of homozygosity and inbreeding in Inner Mongolia cashmere goats reveals candidate genes for economic traits. |
| 41612567 | Elucidating the functional dynamics of DNASE1L2 intron retention in tuberculosis progression. |
| 41407891 | Mendelian randomization and bioinformatics analysis identify the association between plasma proteins and cataract. |
| 41261583 | Plasma proteins and rheumatoid arthritis: A Mendelian randomization analysis. |


## 5. Data Sources

- UniProt: Q92874 (accessed 2026-06-28 via REST API)
- GO-CC: cytoplasm (GO:0005737), nucleus (GO:0005634), extracellular region (GO:0005576)
- BioGRID PPI: human PPI dataset (PHF13, SLC19A2, SLC25A21 interactions)
- HPA: unclassified_bare (no nuclear localization data)
