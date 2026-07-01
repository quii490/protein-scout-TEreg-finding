---
type: gene-evaluation
gene: ALAD
date: 2026-06-28
tags: [nucleus-cytoplasm, heme-biosynthesis, cytosolic, incidental-nuclear]
status: shortlisted
---

# ALAD - Gene Evaluation

## 1. Basic Information

| Field | Value |
|-------|-------|
| **Gene Symbol** | ALAD |
| **UniProt Accession** | P13716 |
| **Protein Name** | Delta-aminolevulinic acid dehydratase |
| **Protein Length** | 330 aa |
| **Molecular Function** | Porphobilinogen synthase, heme biosynthesis |
| **Chromosome** | 9q32 |

## 2. Nuclear Localization Scoring

| Criterion | Score | Weight | Weighted | Notes |
|-----------|-------|--------|----------|-------|
| **GO-CC: Nucleus** | ×2 | ×4 | 8 | Nuclear GO-CC present but likely incidental |
| **Primary Localization** | ×1 | ×5 | 5 | Cytosolic (primary) |
| **HPA Nuclear Evidence** | ×1 | ×3 | 3 | No HPA data available (unclassified_bare) |
| **Nuclear PPI Partners** | ×1 | ×2 | 2 | No strong nuclear PPI partners detected |
| **Literature Evidence** | ×1 | ×3 | 3 | No evidence of nuclear function |
| **Total** | | | **21** | |



| **加权总分** | | | **21.0/180** | |
| **归一化总分 (÷1.83)** | | | **11.5/100** | |
## 3. Detailed Analysis

### 3.1 Protein Function
ALAD catalyzes the second step in heme biosynthesis, condensing two molecules of 5-aminolevulinate to form porphobilinogen. This reaction occurs in the cytosol. ALAD is a zinc-dependent enzyme and a target of lead poisoning (lead displaces zinc, inactivating the enzyme).

### 3.2 Nuclear Localization Evidence
- **GO-CC terms**: Cytosol, extracellular exosome, ficolin-1-rich granule lumen, nucleus, secretory granule lumen
- **UniProt annotation**: "Cytoplasm, cytosol" - no nuclear annotation
- The nuclear GO-CC annotation likely reflects incidental detection in high-throughput studies rather than functional nuclear localization
- No known nuclear import mechanism or nuclear function

### 3.3 Domain Architecture
330 aa with a TIM barrel fold. Contains an octameric assembly with zinc-binding sites at subunit interfaces. Well-characterized structural biology.

### 3.4 Protein-Protein Interactions
No strong nuclear PPI partners identified in BioGRID data. XPO5 interaction noted but not ALAD-specific.

### 3.5 Relevance to TE Regulation
Limited direct relevance. Heme biosynthesis is a cytosolic/metabolic process. No mechanistic connection to TE regulation, chromatin biology, or RNA processing.

## 4. Overall Assessment

**Classification: nucleus-cytoplasm** - Low confidence. The nuclear GO-CC annotation appears incidental. ALAD is a well-characterized cytosolic enzyme in heme biosynthesis with no evidence of nuclear function.

**Recommendation: Low priority.** The minimal nuclear evidence and lack of mechanistic connection to TE biology suggest ALAD is unlikely to be a significant TE regulator. Evaluate only if all higher-priority candidates are exhausted.

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM01004; |
| InterPro | IPR001731;IPR030656;IPR013785; |
| Pfam | PF00490; |
| UniProt Domain | 未检出 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000148218-ALAD

![](https://images.proteinatlas.org/21023/2070_G3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21023/2070_G3_7_blue_red_green.jpg)
![](https://images.proteinatlas.org/21023/2037_E4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21023/2037_E4_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/21023/182_B3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21023/182_B3_2_blue_red_green.jpg)

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HMBS | STRING | 999 |
| UROS | STRING | 997 |
| ALAS1 | STRING | 991 |
| UROD | STRING | 985 |
| FAS | STRING | 814 |
| FASN | STRING | 814 |
| AGFG1 | BioGRID | 1 |
| ACTR2 | BioGRID | 1 |


### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能直接或间接参与 TE 沉默机制，值得进一步实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/ALAD

### PubMed

**Count: 1236**

| PMID | Title |
|---|---|
| 42371508 | Identification of Bone Marrow and Peripheral Blood Plasma Extracellular Vesicle Protein Biomarker Signatures for Multiple Myeloma Diagnosis and Stagin |
| 42246965 | Risk factors for conversion to total hip arthroplasty after hip arthroscopy for femoroacetabular impingement: a five-year analysis in a large cohort. |
| 42236077 | A Perspective Summary of the ISHLT Consensus Statement on Acute Lung Allograft Dysfunction (ALAD). |
| 42223356 | In-Depth Plasma Proteomics Identifies SNCA as a Discriminating Biomarker of PDAC. |
| 42196211 | A Direct ALAD-SSUII Interaction Implies a Potential Link Between Tetrapyrrole and Terpenoid Pathways Toward Chlorophyll Biosynthesis in Plants. |


## 5. Data Sources

- UniProt: P13716 (accessed 2026-06-28 via REST API)
- GO-CC: cytosol (GO:0005829), nucleus (GO:0005634)
- BioGRID PPI: human PPI dataset
- HPA: unclassified_bare (no nuclear localization data)
