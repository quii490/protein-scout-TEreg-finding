---
type: gene-evaluation
gene: C19ORF57
date: 2026-06-28
tags: [chromatin, chromosome, meiosis, recombination, double-strand-break-repair]
status: shortlisted
---

# C19ORF57 (BRME1) - Gene Evaluation

## 1. Basic Information

| Field | Value |
|-------|-------|
| **Gene Symbol** | C19ORF57 (BRME1) |
| **UniProt Accession** | Q0VDD7 |
| **Protein Name** | Break repair meiotic recombinase recruitment factor 1 |
| **Protein Length** | 668 aa |
| **Molecular Function** | Meiotic recombination factor, DSB repair |
| **Chromosome** | 19p13.2 |
| **PubMed Hits** | 7 |

## 2. Nuclear Localization Scoring

| Criterion | Score | Weight | Weighted | Notes |
|-----------|-------|--------|----------|-------|
| **GO-CC: Chromosome** | ×4 | ×4 | 16 | Direct chromosomal association |
| **GO-CC: Nucleus (implicit)** | ×3 | ×4 | 12 | Meiotic chromosome = nuclear context |
| **Meiotic Recombination** | ×4 | ×5 | 20 | Direct role in DNA repair on chromatin |
| **HPA Nuclear Evidence** | ×1 | ×3 | 3 | No HPA data available (unclassified_bare) |
| **Nuclear PPI Partners** | ×3 | ×2 | 6 | BRCA2 pathway, HSF2BP complex |
| **Literature Evidence** | ×3 | ×3 | 9 | Known meiotic recombination factor |
| **Total** | | | **66** | |



| **加权总分** | | | **66.0/180** | |
| **归一化总分 (÷1.83)** | | | **36.1/100** | |
## 3. Detailed Analysis

### 3.1 Protein Function
BRME1 (C19ORF57) is a meiotic recombination factor that modulates the localization of recombinases DMC1 and RAD51 to meiotic double-strand break (DSB) sites. It does this through interaction with and stabilization of the BRCA2:HSF2BP complex during meiotic recombination. BRME1 is indispensable for DSB repair, homologous synapsis, and crossover formation needed for progression past metaphase I. It is essential for spermatogenesis and male fertility.

### 3.2 Nuclear Localization Evidence
- **GO-CC terms**: Chromosome (GO:0005694) - sole cellular compartment annotation
- **UniProt annotation**: "Chromosome"
- Meiotic chromosomes are exclusively nuclear structures
- Functions at sites of meiotic double-strand breaks on chromatin

### 3.3 Domain Architecture
BRME1 is a 668 aa protein. It contains regions that mediate interaction with the BRCA2:HSF2BP complex. The protein has predicted coiled-coil regions that may facilitate protein-protein interactions in the recombination machinery.

### 3.4 Protein-Protein Interactions
- **C19orf25**: Putative interaction partner
- **RABL6 (RBEL1)**: GTPase involved in cell cycle regulation
- **GPS2**: G protein pathway suppressor 2, involved in transcriptional regulation
- Primary functional interactions are with BRCA2 and HSF2BP (meiotic recombination complex)

### 3.5 Relevance to TE Regulation
BRME1 is relevant to TE regulation through its role in meiotic recombination and genome stability:
- Meiotic recombination machinery is a primary defense against TE expansion in the germline
- The BRCA2/RAD51 pathway that BRME1 regulates is essential for homologous recombination repair, which can process TE-induced DNA damage
- Piwi-piRNA pathway components interface with meiotic recombination factors in the germline
- Defects in meiotic recombination factors can lead to TE mobilization

## 4. Overall Assessment

**Classification: chromatin** - Direct chromosomal association with a clear role in DNA repair and recombination on chromatin.

**Strengths**:
- Direct chromatin localization
- Essential role in DNA repair and genome integrity
- Mechanistic connection to germline genome defense
- Good functional characterization

**Weaknesses**:
- Germline-specific expression limits broader relevance
- Only 7 PubMed publications
- No HPA data
- Function may be restricted to meiotic cells

**Recommendation: Shortlist for TE regulation evaluation.** BRME1's role in meiotic recombination and genome defense in the germline directly connects to TE suppression. Its function in the BRCA2/RAD51 pathway positions it within the germline genome defense network.

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HSF2BP | STRING | 793 |
| RABL6 | BioGRID | 1 |
| GPS2 | BioGRID | 1 |
| TRIM23 | BioGRID | 1 |
| RUNX1T1 | BioGRID | 1 |
| EWSR1 | BioGRID | 1 |
| COPS4 | BioGRID | 1 |
| C19ORF57 | BioGRID | 1 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000132016

![](https://images.proteinatlas.org/54615/1011_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/54615/1011_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/54615/1179_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/54615/1179_F5_2_red_green.jpg)
![](https://images.proteinatlas.org/54615/1006_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/54615/1006_E1_2_red_green.jpg)

### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能参与 TE 沉默。需实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/C19ORF57

## 5. Data Sources

- UniProt: Q0VDD7 (accessed 2026-06-28 via REST API)
- GO-CC: chromosome (GO:0005694)
- BioGRID PPI: human PPI dataset (C19orf25, RABL6, GPS2 interactions)
- HPA: unclassified_bare (no nuclear localization data)
