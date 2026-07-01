---
type: gene-evaluation
gene: DNPEP
date: 2026-06-28
tags: [nucleus-cytoplasm, aminopeptidase, aspartyl, proteolysis, incidental-nuclear]
status: shortlisted
---

# DNPEP - Gene Evaluation

## 1. Basic Information

| Field | Value |
|-------|-------|
| **Gene Symbol** | DNPEP |
| **UniProt Accession** | Q9ULA0 |
| **Protein Name** | Aspartyl aminopeptidase |
| **Protein Length** | 485 aa |
| **Molecular Function** | Aminopeptidase (acidic N-terminal specificity) |
| **Chromosome** | 2q35 |

## 2. Nuclear Localization Scoring

| Criterion | Score | Weight | Weighted | Notes |
|-----------|-------|--------|----------|-------|
| **GO-CC: Nucleus** | ×2 | ×4 | 8 | Nuclear GO-CC present but cytoplasmic primary |
| **Primary Localization** | ×1 | ×5 | 5 | Cytosol/cytoplasm (primary) |
| **HPA Nuclear Evidence** | ×1 | ×3 | 3 | No HPA data available (unclassified_bare) |
| **Nuclear PPI Partners** | ×1 | ×2 | 2 | No strong nuclear PPI partners |
| **Literature Evidence** | ×1 | ×3 | 3 | Proteolysis focus, no nuclear function |
| **Total** | | | **21** | |



| **加权总分** | | | **21.0/180** | |
| **归一化总分 (÷1.83)** | | | **11.5/100** | |
## 3. Detailed Analysis

### 3.1 Protein Function
DNPEP (aspartyl aminopeptidase) is an aminopeptidase with specificity towards acidic amino acids (aspartate, glutamate) at the N-terminus of peptide substrates. It likely plays a role in intracellular protein and peptide metabolism, participating in the terminal stages of protein turnover and peptide processing.

### 3.2 Nuclear Localization Evidence
- **GO-CC terms**: Blood microparticle, cytoplasm, cytosol, nucleus
- **UniProt annotation**: "Cytoplasm" - primary localization
- Nuclear GO-CC is one of several annotations and likely reflects incidental detection
- No known nuclear import signal or nuclear function
- The protein functions in general intracellular proteolysis, primarily cytosolic

### 3.3 Domain Architecture
DNPEP is a 485 aa protein:
- **Peptidase M18 family domain**: Aminopeptidase catalytic domain
- **Zinc metallopeptidase**: Requires zinc for catalysis
- Forms a dodecameric assembly (12 subunits) typical of the M18 family

### 3.4 Protein-Protein Interactions
- **SAT1 (Spermidine/spermine N1-acetyltransferase 1)**: Polyamine metabolism
- **ADAMTSL4**: Extracellular matrix protein
- **MDFI (MyoD family inhibitor)**: Transcriptional regulator, nuclear - potential weak nuclear connection
- No strong nuclear functional PPI network

### 3.5 Relevance to TE Regulation
Limited direct relevance. DNPEP is a general intracellular aminopeptidase. While proteolytic processing is involved in many cellular pathways including chromatin regulation, there is no evidence that DNPEP specifically processes nuclear or TE-related substrates.

## 4. Overall Assessment

**Classification: nucleus-cytoplasm** - Low confidence. DNPEP is a cytoplasmic aminopeptidase. The nuclear GO-CC annotation is likely incidental. No evidence supports a specific nuclear function or role in TE biology.

**Recommendation: Low priority.** General protease with no specific connection to nuclear biology or TE regulation.

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR001948;IPR023358; |
| Pfam | PF02127; |
| UniProt Domain | 未检出 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000123992-DNPEP

![](https://images.proteinatlas.org/44860/1700_E6_1_cr57ed01f7d151c_blue_red_green.jpg)
![](https://images.proteinatlas.org/44860/1700_E6_27_cr57ed01ff4667d_blue_red_green.jpg)
![](https://images.proteinatlas.org/44860/1704_F5_11_cr57f4beb611623_blue_red_green.jpg)
![](https://images.proteinatlas.org/44860/1704_F5_26_cr57f4bec017160_blue_red_green.jpg)
![](https://images.proteinatlas.org/44860/529_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44860/529_H1_2_blue_red_green.jpg)

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| LAP3 | STRING | 727 |
| KIF4A | BioGRID | 1 |
| NELFCD | BioGRID | 1 |
| UGP2 | BioGRID | 1 |
| PTPN12 | BioGRID | 1 |
| DGCR6 | BioGRID | 1 |
| DNPEP | BioGRID | 1 |
| TPI1 | BioGRID | 1 |


### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能直接或间接参与 TE 沉默机制，值得进一步实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/DNPEP

### PubMed

**Count: 28**

| PMID | Title |
|---|---|
| 42180904 | DNPEP promotes the growth, metastasis, and cisplatin resistance of tongue squamous cell carcinoma through RACK1/ERK signaling pathway. |
| 41864094 | Mixture risk assessment of nine reproductive toxic chemicals affecting male sperm quality in a representative sample of children and adolescents livin |
| 41142432 | Detection of aspartyl aminopeptidase in atherosclerosis mice and clinical sample using an optical probe. |
| 39675269 | A novel directed enzymolysis strategy for the preparation of umami peptides in Stropharia rugosoannulata and its mechanism of taste perception. |
| 38134227 | FBXO3 stabilizes USP4 and Twist1 to promote PI3K-mediated breast cancer metastasis. |


## 5. Data Sources

- UniProt: Q9ULA0 (accessed 2026-06-28 via REST API)
- GO-CC: cytoplasm (GO:0005737), cytosol (GO:0005829), nucleus (GO:0005634)
- BioGRID PPI: human PPI dataset (SAT1, ADAMTSL4, MDFI interactions)
- HPA: unclassified_bare (no nuclear localization data)
