---
type: gene-evaluation
gene: C1ORF146
date: 2026-06-28
tags: [chromatin, chromosome, meiosis, synaptonemal-complex, recombination]
status: shortlisted
---

# C1ORF146 (SPO16) - Gene Evaluation

## 1. Basic Information

| Field | Value |
|-------|-------|
| **Gene Symbol** | C1ORF146 (SPO16) |
| **UniProt Accession** | Q5VVC0 |
| **Protein Name** | Protein SPO16 homolog |
| **Protein Length** | 180 aa |
| **Molecular Function** | Synaptonemal complex stabilization |
| **Chromosome** | 1p34.3 |
| **PubMed Hits** | 0 (no Gene-indexed publications) |

## 2. Nuclear Localization Scoring

| Criterion | Score | Weight | Weighted | Notes |
|-----------|-------|--------|----------|-------|
| **GO-CC: Chromosome** | ×4 | ×4 | 16 | Direct chromosomal association |
| **GO-CC: Nucleus (implicit)** | ×3 | ×4 | 12 | Synaptonemal complex = nuclear |
| **Meiotic Function** | ×3 | ×5 | 15 | SC stabilization and recombination |
| **HPA Nuclear Evidence** | ×1 | ×3 | 3 | No HPA data available (unclassified_bare) |
| **Nuclear PPI Partners** | ×2 | ×2 | 4 | LMO1 (nuclear transcription factor) |
| **Literature Evidence** | ×1 | ×3 | 3 | No direct PubMed publications |
| **Total** | | | **53** | |



| **加权总分** | | | **53.0/180** | |
| **归一化总分 (÷1.83)** | | | **29.0/100** | |
## 3. Detailed Analysis

### 3.1 Protein Function
SPO16 (C1ORF146) plays a key role in reinforcing the integrity of the central element of the synaptonemal complex (SC), stabilizing SC and ensuring progression of meiotic prophase I in male and female germ cells. It promotes homologous recombination and crossing-over in meiotic prophase I via its association with SHOC1. It is required for the localization of TEX11 and MSH4 to recombination intermediates.

### 3.2 Nuclear Localization Evidence
- **GO-CC terms**: Chromosome (GO:0005694) - sole cellular compartment annotation
- **UniProt annotation**: "Chromosome"
- The synaptonemal complex is a meiosis-specific nuclear structure that assembles between homologous chromosomes
- SPO16 localizes to the central element of the SC

### 3.3 Domain Architecture
SPO16 is a small protein of 180 aa. It contains regions mediating interaction with SHOC1 and other SC components. The compact size suggests it functions primarily as a structural adaptor or stabilizer within the SC central element.

### 3.4 Protein-Protein Interactions
- **CST8 (Cystatin 8)**: Protease inhibitor, testis-specific
- **LMO1 (LIM domain only 1)**: Nuclear transcription factor involved in development
- **CDSN (Corneodesmosin)**: Epidermal adhesion protein (likely non-physiological)
- The interaction with LMO1 suggests potential nuclear regulatory connections

### 3.5 Relevance to TE Regulation
SPO16 connects to TE regulation through meiotic genome defense:
- The synaptonemal complex is crucial for proper chromosome segregation during meiosis
- Meiotic recombination provides a surveillance mechanism against TE insertions
- The piRNA pathway in the germline targets TEs during meiosis
- SC components interact with DNA damage response pathways that recognize TE-induced lesions

## 4. Overall Assessment

**Classification: chromatin** - Chromosome-associated protein functioning in the synaptonemal complex during meiosis.

**Strengths**:
- Direct chromatin/chromosome localization
- Essential role in meiotic chromosome dynamics
- Connection to recombination machinery (SHOC1, TEX11, MSH4)

**Weaknesses**:
- Zero PubMed publications indexed by gene
- Function inferred primarily from orthology (By similarity evidence codes)
- Germline-specific expression
- Very small protein (180 aa) with limited domain information
- No HPA data

**Recommendation: Shortlist with caution.** SPO16 has clear nuclear/chromosomal localization through its role in the synaptonemal complex. However, the lack of direct human studies and germline-restricted expression limit its priority for TE regulation evaluation.

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HFM1 | STRING | 885 |
| MSH4 | STRING | 863 |
| G7 | STRING | 810 |
| MSH5-SAPCD1 | STRING | 810 |
| MSH5 | STRING | 810 |
| LMO1 | BioGRID | 1 |
| TSC22D4 | BioGRID | 1 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000203910-C1orf146

![](https://images.proteinatlas.org/74051/2036_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/74051/2036_H2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/74051/1943_A8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/74051/1943_A8_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000203910-C1orf146

![](https://images.proteinatlas.org/74051/2036_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/74051/2036_H2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/74051/1943_A8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/74051/1943_A8_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000203910-C1orf146

![](https://images.proteinatlas.org/74051/2036_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/74051/2036_H2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/74051/1943_A8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/74051/1943_A8_3_blue_red_green.jpg)

### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能参与 TE 沉默。需实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/C1ORF146

## 5. Data Sources

- UniProt: Q5VVC0 (accessed 2026-06-28 via REST API)
- GO-CC: chromosome (GO:0005694)
- BioGRID PPI: human PPI dataset (CST8, LMO1, CDSN interactions)
- HPA: unclassified_bare (no nuclear localization data)
- Note: All functional annotations are by similarity (ECO:0000250)
