---
type: gene-evaluation
gene: CLIP4
date: 2026-06-28
tags: [nucleus-cytoplasm, microtubule, CAP-Gly, cytoskeleton, incidental-nuclear]
status: shortlisted
---

# CLIP4 - Gene Evaluation

## 1. Basic Information

| Field | Value |
|-------|-------|
| **Gene Symbol** | CLIP4 |
| **UniProt Accession** | Q8N3C7 |
| **Protein Name** | CAP-Gly domain-containing linker protein 4 |
| **Protein Length** | 705 aa |
| **Molecular Function** | Microtubule plus-end binding |
| **Chromosome** | 2p23.2 |

## 2. Nuclear Localization Scoring

| Criterion | Score | Weight | Weighted | Notes |
|-----------|-------|--------|----------|-------|
| **GO-CC: Nucleus** | ×2 | ×4 | 8 | Nuclear GO-CC present but likely incidental |
| **Primary Localization** | ×1 | ×5 | 5 | Cell cortex/microtubule (primary) |
| **GO-CC: MT Plus-End** | ×1 | ×1 | 1 | Primary functional localization |
| **HPA Nuclear Evidence** | ×1 | ×3 | 3 | No HPA data available (unclassified_bare) |
| **Nuclear PPI Partners** | ×1 | ×2 | 2 | No strong nuclear PPI partners |
| **Literature Evidence** | ×1 | ×3 | 3 | No evidence of nuclear function |
| **Total** | | | **22** | |



| **加权总分** | | | **22.0/180** | |
| **归一化总分 (÷1.83)** | | | **12.0/100** | |
## 3. Detailed Analysis

### 3.1 Protein Function
CLIP4 is a CAP-Gly domain-containing linker protein that localizes to microtubule plus-ends. CAP-Gly (cytoskeleton-associated protein glycine-rich) domains bind to microtubules and regulate microtubule dynamics. CLIP4 likely functions in microtubule stabilization and cargo transport along microtubules.

### 3.2 Nuclear Localization Evidence
- **GO-CC terms**: Cell cortex, microtubule plus-end, nucleus
- **UniProt annotation**: No specific subcellular location annotation
- Nuclear GO-CC is the weakest annotation among three compartments
- Primary localization is at the cell cortex and microtubule plus-ends
- No known nuclear import mechanism
- The CAP-Gly domain is a cytoskeletal targeting domain, not a nuclear localization signal

### 3.3 Domain Architecture
CLIP4 is a 705 aa protein containing:
- **CAP-Gly domain(s)**: Microtubule-binding
- **Coiled-coil regions**: Protein-protein interaction and dimerization
- **Zinc finger motif(s)**: Potential nucleic acid or protein binding

### 3.4 Protein-Protein Interactions
- **KIFC3**: Kinesin motor protein, microtubule-dependent transport
- **MAGEA12**: Cancer/testis antigen, nuclear/cytoplasmic
- **APP**: Amyloid precursor protein (likely non-specific)
- No convincing nuclear functional PPI partners

### 3.5 Relevance to TE Regulation
Limited direct relevance. CLIP4 functions in microtubule dynamics at the cell cortex. While microtubules participate in nuclear positioning and mitotic spindle formation, CLIP4 has no known role in chromatin biology, RNA processing, or TE silencing.

## 4. Overall Assessment

**Classification: nucleus-cytoplasm** - Low confidence. CLIP4 is a microtubule-associated protein with primary function at the cell cortex and microtubule plus-ends. The nuclear GO-CC annotation is likely incidental, possibly reflecting detection during mitosis when nuclear envelope breaks down.

**Recommendation: Low priority.** Minimal nuclear evidence and cytoskeletal primary function suggest low relevance to TE regulation.

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00248;SM01052; |
| InterPro | IPR002110;IPR036770;IPR036859;IPR000938; |
| Pfam | PF12796;PF01302; |
| UniProt Domain | DOMAIN 303..345; /note="CAP-Gly 1"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00045"; DOMAIN 505..547; /note="CAP-Gly 2"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00045"; DOMAIN 644..686; /note="CAP-Gly 3"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00045" |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000115295-CLIP4

![](https://images.proteinatlas.org/43366/547_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43366/547_H1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43366/496_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43366/496_H1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43366/532_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43366/532_H1_2_blue_red_green.jpg)

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ZNF114 | STRING | 777 |
| EGFR | STRING | 758 |
| APP | BioGRID | 1 |
| MAGEA12 | BioGRID | 1 |
| TRIP13 | BioGRID | 1 |
| MEOX2 | BioGRID | 1 |
| HSF2BP | BioGRID | 1 |
| SIX2 | BioGRID | 1 |


### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能直接或间接参与 TE 沉默机制，值得进一步实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CLIP4

### PubMed

**Count: 73**

| PMID | Title |
|---|---|
| 42054806 | Prenatal metal exposure moderates the effect of CRH-related DNA methylation in the placenta on infant communication outcomes at 2 months of age. |
| 40879392 | Unculturable bacteria exploit a secretory protein to antagonize insect melanization for persistent infection. |
| 40707988 | Exploring UBASH3A: from immune regulation to autoimmune diseases. |
| 39920578 | Endoplasmic reticulum stress-related CLIP4 plays a procarcinogenic role in hepatocellular carcinoma: an integrated analysis. |
| 39482662 | The signature of SARS-CoV-2-related genes predicts the immune therapeutic response and prognosis in breast cancer. |


## 5. Data Sources

- UniProt: Q8N3C7 (accessed 2026-06-28 via REST API)
- GO-CC: cell cortex (GO:0005938), microtubule plus-end (GO:0035371), nucleus (GO:0005634)
- BioGRID PPI: human PPI dataset (KIFC3, MAGEA12, APP interactions)
- HPA: unclassified_bare (no nuclear localization data)
