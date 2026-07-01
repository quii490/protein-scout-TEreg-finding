---
type: gene-evaluation
gene: CCS
date: 2026-06-28
tags: [nucleus-cytoplasm, copper-chaperone, SOD1, antioxidant, incidental-nuclear]
status: shortlisted
---

# CCS - Gene Evaluation

## 1. Basic Information

| Field | Value |
|-------|-------|
| **Gene Symbol** | CCS |
| **UniProt Accession** | O14618 |
| **Protein Name** | Copper chaperone for superoxide dismutase |
| **Protein Length** | 274 aa |
| **Molecular Function** | Copper delivery to SOD1 |
| **Chromosome** | 11q13.2 |

## 2. Nuclear Localization Scoring

| Criterion | Score | Weight | Weighted | Notes |
|-----------|-------|--------|----------|-------|
| **GO-CC: Nucleus** | ×2 | ×4 | 8 | Nuclear GO-CC present but likely incidental |
| **Primary Localization** | ×1 | ×5 | 5 | Cytosolic (primary), mitochondrial |
| **HPA Nuclear Evidence** | ×1 | ×3 | 3 | No HPA data available (unclassified_bare) |
| **Nuclear PPI Partners** | ×1 | ×2 | 2 | No strong nuclear PPI partners |
| **Literature Evidence** | ×1 | ×3 | 3 | No evidence of nuclear function |
| **Total** | | | **21** | |



| **加权总分** | | | **21.0/180** | |
| **归一化总分 (÷1.83)** | | | **11.5/100** | |
## 3. Detailed Analysis

### 3.1 Protein Function
CCS delivers copper to copper-zinc superoxide dismutase (SOD1), which is essential for SOD1 enzymatic activity. CCS is the dedicated copper chaperone for SOD1, transferring copper through a specific protein-protein interaction mechanism. SOD1 and CCS function in antioxidant defense against superoxide radicals.

### 3.2 Nuclear Localization Evidence
- **GO-CC terms**: Cytoplasm, cytosol, mitochondrion, nucleus
- **UniProt annotation**: "Cytoplasm, cytosol" - primary localization
- The nuclear GO-CC annotation likely reflects incidental detection
- No known nuclear import mechanism
- Primary functional localization is cytoplasmic and mitochondrial

### 3.3 Domain Architecture
CCS is a 274 aa protein with three domains:
- **Domain I**: Copper-binding ATX1-like domain
- **Domain II**: SOD1-like domain (structural mimicry for target recognition)
- **Domain III**: C-terminal copper delivery domain

### 3.4 Protein-Protein Interactions
- Primary interaction with SOD1 (copper delivery target)
- No nuclear PPI partners identified

### 3.5 Relevance to TE Regulation
Limited direct relevance. CCS functions in copper homeostasis and antioxidant defense. While oxidative stress can influence TE activity, CCS has no direct mechanistic connection to chromatin biology, RNA processing, or TE silencing pathways.

## 4. Overall Assessment

**Classification: nucleus-cytoplasm** - Low confidence. CCS is a well-characterized cytosolic copper chaperone. The nuclear GO-CC annotation appears incidental and likely reflects passive diffusion or high-throughput detection artifacts rather than functional nuclear localization.

**Recommendation: Low priority.** Minimal nuclear evidence and no mechanistic connection to TE regulation. Evaluate only after exhausting higher-priority candidates.

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR006121;IPR036163;IPR036423;IPR024134;IPR018152;IPR001424; |
| Pfam | PF00403;PF00080; |
| UniProt Domain | DOMAIN 11..74; /note="HMA"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00280" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SOD1 | STRING | 999 |
| ATOX1 | STRING | 973 |
| APBA1 | BioGRID | 1 |
| CCS | BioGRID | 1 |
| XIAP | BioGRID | 1 |
| GOT1 | BioGRID | 1 |
| PPIL3 | BioGRID | 1 |
| RAE1 | BioGRID | 1 |


### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能直接或间接参与 TE 沉默机制，值得进一步实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CCS

### PubMed

**Count: 24774**

| PMID | Title |
|---|---|
| 42374476 | Targeting AIF to trigger RIPKs/MLKL necroptosis: a disulfiram-based strategy to reverse paclitaxel resistance in ovarian cancer. |
| 42374436 | Compositional recalibrations of cardiolipin integrate loss of stearoyl-CoA desaturase 1 activity with mitochondrial decay in lipid-laden pancreatic β- |
| 42373542 | Democratized single-cell proteomics resolves cell state heterogeneity in skin tumors. |
| 42371830 | Can resting segmental strain identify obstructive coronary artery disease in chronic coronary syndrome patients referred to CABG? |
| 42371696 | Whole-genome sequencing of Listeria monocytogenes from maternal and neonatal clinical isolates in Kuwait. |


## 5. Data Sources

- UniProt: O14618 (accessed 2026-06-28 via REST API)
- GO-CC: cytoplasm (GO:0005737), cytosol (GO:0005829), nucleus (GO:0005634)
- BioGRID PPI: human PPI dataset
- HPA: unclassified_bare (no nuclear localization data)
