---
type: gene-evaluation
gene: CHMP4A
date: 2026-06-28
tags: [nuclear-envelope, ESCRT-III, membrane-remodeling, nuclear-pore, kinetochore]
status: shortlisted
---

# CHMP4A - Gene Evaluation

## 1. Basic Information

| Field | Value |
|-------|-------|
| **Gene Symbol** | CHMP4A |
| **UniProt Accession** | Q9BY43 |
| **Protein Name** | Charged multivesicular body protein 4a |
| **Protein Length** | 222 aa |
| **Molecular Function** | ESCRT-III complex component, membrane remodeling |
| **Chromosome** | 14q12 |
| **PubMed Hits** | 55 |

## 2. Nuclear Localization Scoring

| Criterion | Score | Weight | Weighted | Notes |
|-----------|-------|--------|----------|-------|
| **GO-CC: Nucleus** | ×4 | ×4 | 16 | Nuclear localization annotated |
| **GO-CC: Nuclear Envelope** | ×4 | ×5 | 20 | Direct NE association |
| **GO-CC: Nuclear Pore** | ×3 | ×1 | 3 | NPC association |
| **GO-CC: Kinetochore** | ×3 | ×3 | 9 | Mitotic chromatin attachment |
| **HPA Nuclear Evidence** | ×1 | ×3 | 3 | No HPA data available (unclassified_bare) |
| **Nuclear PPI Partners** | ×3 | ×2 | 6 | STAMBP (nuclear endosomal sorting) |
| **Literature Evidence** | ×3 | ×3 | 9 | 55 publications, ESCRT-III well-characterized |
| **Total** | | | **66** | |



| **加权总分** | | | **66.0/180** | |
| **归一化总分 (÷1.83)** | | | **36.1/100** | |
## 3. Detailed Analysis

### 3.1 Protein Function
CHMP4A is a core component of the endosomal sorting complex required for transport III (ESCRT-III). ESCRT-III mediates membrane scission in multiple cellular processes including multivesicular body (MVB) formation, cytokinesis, viral budding, and nuclear envelope resealing. CHMP4A polymerizes into spiral filaments that constrict membrane necks to drive scission.

### 3.2 Nuclear Localization Evidence
- **GO-CC terms**: Nucleus (GO:0005634), Nuclear envelope (GO:0005635), Nuclear pore (GO:0005643), Kinetochore (GO:0000776), in addition to multiple cytoplasmic/endosomal compartments
- **UniProt annotation**: "Cytoplasmic vesicle membrane; Late endosome membrane"
- ESCRT-III is critically involved in nuclear envelope resealing after mitosis
- CHMP4A localizes to the nuclear envelope during NE reformation
- CHMP4A is recruited to kinetochores during mitosis
- The protein dynamically cycles between endosomal and nuclear compartments

### 3.3 Domain Architecture
CHMP4A is a 222 aa protein of the SNF7 family within ESCRT-III. It contains:
- **N-terminal core domain**: Mediates polymerization into helical filaments
- **C-terminal autoinhibitory domain**: Regulates polymerization
- **MIT-interacting motif (MIM)**: Recruits VPS4 AAA-ATPase for filament disassembly

### 3.4 Protein-Protein Interactions
- **STAMBP (AMSH)**: Deubiquitinating enzyme that regulates ESCRT-III
- **PDCD6IP (ALIX)**: ESCRT accessory protein bridges ESCRT-I and ESCRT-III
- **SYT17**: Synaptotagmin-17, membrane trafficking
- **CHMP4B, CHMP4C**: Paralogous ESCRT-III subunits with partially overlapping functions

### 3.5 Relevance to TE Regulation
CHMP4A connects to TE regulation through nuclear envelope dynamics:
- Nuclear envelope integrity is essential for maintaining heterochromatin organization at the nuclear periphery
- TE-rich genomic regions are often localized to the nuclear lamina
- Disruption of nuclear envelope resealing (e.g., by ESCRT-III defects) can lead to chromatin organization defects
- Nuclear pore association suggests a role in nucleocytoplasmic transport that could affect TE-derived RNA trafficking
- ESCRT-III-mediated membrane remodeling at the nuclear envelope may influence lamina-associated domains where many TEs reside

## 4. Overall Assessment

**Classification: nuclear-envelope** - CHMP4A has well-documented localization to the nuclear envelope, nuclear pore, and kinetochore. While its primary function is in endosomal sorting, its nuclear envelope role during NE resealing and mitosis is distinct and physiologically important.

**Strengths**:
- Specific nuclear envelope and nuclear pore GO-CC annotations
- Well-characterized ESCRT-III pathway
- 55 publications with mechanistic studies
- Nuclear envelope function in NE resealing

**Weaknesses**:
- Nuclear localization is cell-cycle-dependent (mitotic exit)
- Primary function is cytoplasmic/endosomal
- No HPA data
- Nuclear role is structural (membrane remodeling) rather than regulatory

**Recommendation: Shortlist for TE regulation evaluation.** CHMP4A's role in nuclear envelope dynamics provides a structural connection to chromatin organization at the nuclear periphery, where TE-rich lamina-associated domains are concentrated. However, the indirect nature of this connection to TE regulation warrants lower priority than direct chromatin/RNA regulators.

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CHMP3 | STRING | 999 |
| CHMP6 | STRING | 998 |
| TSG101 | STRING | 991 |
| CHMP2B | STRING | 991 |
| CHMP7 | STRING | 984 |
| CHMP1B | STRING | 971 |
| MVB12A | STRING | 938 |
| IST1 | STRING | 928 |


### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能直接或间接参与 TE 沉默机制，值得进一步实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CHMP4A

### PubMed

**Count: 55**

| PMID | Title |
|---|---|
| 41112257 | CHMP4A in hepatocellular carcinoma: exploring its role in tumor progression, immune modulation, and potential link to TIM3 checkpoint. |
| 40909968 | Developing a prognostic model of glutamine metabolism-related genes associated with clinical features and immune status in melanoma. |
| 40152606 | ESCRT III-mediated lysosomal repair improve renal tubular cell injury in cisplatin-induced AKI. |
| 39337546 | HRS Facilitates Newcastle Disease Virus Replication in Tumor Cells by Promoting Viral Budding. |
| 39263102 | Characteristics of two different immune infiltrating pyroptosis subtypes in ischemic stroke. |


## 5. Data Sources

- UniProt: Q9BY43 (accessed 2026-06-28 via REST API)
- GO-CC: nucleus (GO:0005634), nuclear envelope (GO:0005635), nuclear pore (GO:0005643), kinetochore (GO:0000776)
- BioGRID PPI: human PPI dataset (STAMBP, PDCD6IP, SYT17 interactions)
- PubMed: 55 total hits
- HPA: unclassified_bare (no nuclear localization data)
