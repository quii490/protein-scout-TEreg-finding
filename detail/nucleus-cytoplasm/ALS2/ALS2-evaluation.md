---
type: gene-evaluation
gene: ALS2
date: 2026-06-28
tags: [nucleus-cytoplasm, endosome, GTPase-regulator, motor-neuron, incidental-nuclear]
status: shortlisted
---

# ALS2 - Gene Evaluation

## 1. Basic Information

| Field | Value |
|-------|-------|
| **Gene Symbol** | ALS2 |
| **UniProt Accession** | Q96Q42 |
| **Protein Name** | Alsin |
| **Protein Length** | 1657 aa |
| **Molecular Function** | GTPase regulator (GEF activity) |
| **Chromosome** | 2q33.1 |

## 2. Nuclear Localization Scoring

| Criterion | Score | Weight | Weighted | Notes |
|-----------|-------|--------|----------|-------|
| **GO-CC: Nucleus** | ×2 | ×4 | 8 | Nuclear GO-CC present but likely incidental |
| **Primary Localization** | ×1 | ×5 | 5 | Endosome/cytoplasmic (primary) |
| **GO-CC: Early Endosome** | ×1 | ×1 | 1 | Primary functional compartment |
| **HPA Nuclear Evidence** | ×1 | ×3 | 3 | No HPA data available (unclassified_bare) |
| **Nuclear PPI Partners** | ×1 | ×2 | 2 | No strong nuclear PPI partners |
| **Literature Evidence** | ×1 | ×3 | 3 | Endosomal/membrane trafficking focus |
| **Total** | | | **22** | |



| **加权总分** | | | **22.0/180** | |
| **归一化总分 (÷1.83)** | | | **12.0/100** | |
## 3. Detailed Analysis

### 3.1 Protein Function
Alsin (ALS2) functions as a guanine nucleotide exchange factor (GEF) for Rab5 family GTPases, playing a role in endosomal trafficking and neurite outgrowth. Mutations in ALS2 cause juvenile amyotrophic lateral sclerosis (ALS2), infantile-onset ascending hereditary spastic paralysis, and juvenile primary lateral sclerosis.

### 3.2 Nuclear Localization Evidence
- **GO-CC terms**: Centrosome, cytoplasm, cytosol, dendrite, early endosome, glutamatergic synapse, growth cone, lamellipodium, nucleus, postsynaptic density, ruffle, vesicle
- **UniProt annotation**: No specific subcellular location annotated in the SUBCELLULAR LOCATION section
- Nuclear GO-CC is one of many annotations, suggesting incidental detection rather than functional localization
- Primary functional localization is at early endosomes and vesicular compartments
- No known nuclear import/export signals or nuclear function

### 3.3 Domain Architecture
Alsin is a large 1657 aa protein containing:
- **N-terminal RCC1-like domain (RLD)**: Beta-propeller structure
- **Central DH/PH domain tandem**: Dbl homology (DH) and pleckstrin homology (PH) domains for GEF activity
- **MORN repeats**: Membrane-targeting motifs
- **C-terminal VPS9 domain**: Rab5 GEF activity

### 3.4 Protein-Protein Interactions
- Primary interactions with Rab5 GTPases, endosomal trafficking proteins
- No significant nuclear PPI partners identified

### 3.5 Relevance to TE Regulation
Limited direct relevance. Alsin's primary function in endosomal trafficking and its association with motor neuron disease do not suggest a mechanistic role in TE regulation or nuclear biology.

## 4. Overall Assessment

**Classification: nucleus-cytoplasm** - Low confidence. Alsin is a large multi-domain protein with extensive cytoplasmic/endosomal localization. The nuclear GO-CC annotation likely reflects incidental detection in high-throughput studies rather than functional nuclear localization.

**Recommendation: Low priority.** Minimal evidence for nuclear function. The endosomal trafficking role and lack of chromatin/RNA-related activity suggest low relevance to TE regulation.

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000003393-ALS2

![](https://images.proteinatlas.org/46588/622_F2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/46588/622_F2_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/46588/616_F2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/46588/616_F2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/46588/619_F2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/46588/619_F2_5_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00698; |
| InterPro | IPR051984;IPR057248;IPR035899;IPR000219;IPR059093;IPR003409;IPR011993;IPR009091;IPR000408;IPR003123;IPR037191; |
| Pfam | PF25582;PF26202;PF02493;PF25383;PF00415;PF02204; |
| UniProt Domain [FT] | DOMAIN 690..885; /note="DH"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00062"; DOMAIN 901..1007; /note="PH"; /evidence="ECO:0000305"; DOMAIN 1513..1657; /note="VPS9"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00550" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NEK1 | STRING | 942 |
| SETX | STRING | 909 |
| SOD1 | STRING | 891 |
| TARDBP | STRING | 828 |
| FUS | STRING | 822 |
| RABGEF1 | STRING | 806 |
| DCTN1 | STRING | 794 |
| CHMP2B | STRING | 789 |


### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能直接或间接参与 TE 沉默机制，值得进一步实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/ALS2

### PubMed

**Count: 465**

| PMID | Title |
|---|---|
| 42260624 | Helicobacter pylori infection activates the HIF-1α/ALS2/Rab5 signaling axis in gastric cells. |
| 41657105 | MK4 Repositioning for IAHSP: Overcoming In Vivo Data Gaps through In Silico Refinement and In Vitro Validation. |
| 41606223 | Molecular characterization of recessively inherited ataxic and neuropathic disorders in consanguineous Pakistani families. |
| 41592170 | The genetics of autosomal recessive ALS: a review of the common forms and their phenotypes. |
| 41553447 | ALS2, encoding a plastid 50 S ribosomal protein L5, is essential for early chloroplast development in rice. |


## 5. Data Sources

- UniProt: Q96Q42 (accessed 2026-06-28 via REST API)
- GO-CC: early endosome (GO:0005769), nucleus (GO:0005634), cytoplasm (GO:0005737)
- BioGRID PPI: human PPI dataset
- HPA: unclassified_bare (no nuclear localization data)
