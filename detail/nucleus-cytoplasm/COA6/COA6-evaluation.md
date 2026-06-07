---
type: protein-evaluation
gene: "COA6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 4
---

## COA6 (Cytochrome c oxidase assembly factor 6 homolog) -- Evaluation Report

### 1. Basic Info

| Property | Value |
|------|-----|
| **UniProt ID** | Q5JTJ3 |
| **Protein Name** | Cytochrome c oxidase assembly factor 6 homolog |
| **Aliases** | C1orf31 |
| **Length** | 125 aa |
| **Mass** | 14.1 kDa |
| **AlphaFold mean pLDDT** | 77.2 |
| **AlphaFold pLDDT >90** | 46.4% |
| **AlphaFold pLDDT <50** | 0.8% |
| **PubMed (strict)** | 30 |
| **Function** | Involved in the maturation of the mitochondrial respiratory chain complex IV subunit MT-CO2/COX2. Thereby, may regulate early steps of complex IV assembly. Mitochondrial respiratory chain complex IV or cytochrome c oxidase is the component of the respiratory chain that catalyzes the transfer of elec |

### 2. Nuclear Localization Evidence

#### UniProt Subcellular Location
Mitochondrion intermembrane space

#### GO Cellular Component
- **mitochondrial intermembrane space** (IDA:UniProtKB)
- **mitochondrion** (IDA:HPA)
- **nucleoplasm** (IDA:HPA)

#### HPA Subcellular Localization
- **Main location**: Mitochondria
- **Additional locations**: Nucleoplasm
- **Reliability (IF)**: Supported
- **IF Display Images Available**: YES

HPA IF display images available, reliability: Supported.

### 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF display images available, reliability: Supported.

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 30 |

**Key Papers:**
- PMID:26425749 -- Nuclear Gene-Encoded Leigh Syndrome Spectrum Overview. (, 1993)
- PMID:37303286 -- Nitric oxide regulates mitochondrial biogenesis in plants. (Plant, cell & environment, 2023 Aug)
- PMID:32977416 -- What Role Does COA6 Play in Cytochrome C Oxidase Biogenesis: A Metallochaperone or Thiol Oxidoreductase, or Both? (International journal of molecular sciences, 2020 Sep 23)
- PMID:39472746 -- Oxidative phosphorylation related gene COA6 is a novel indicator for the prognosis and immune response in lung adenocarc (Scientific reports, 2024 Oct 29)
- PMID:37215201 -- Cuproptosis-Related Genes CDK1 and COA6 Involved in the Prognosis Prediction of Liver Hepatocellular Carcinoma. (Disease markers, 2023)


**Research Volume Assessment**: Low (<50 papers), ample research space

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 77.2
- pLDDT >90: 46.4%, 70-90: 8.0%, 50-70: 44.8%, <50: 0.8%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| 6NL3 | NMR | - | A=47-125 |
| 6PCE | X-ray | 1.65 A | A/B=50-119 |
| 6PCF | X-ray | 2.20 A | A/B/C/D=49-113 |

**Structure Assessment**: High-quality AlphaFold prediction (pLDDT 77.2), fold confidence high, PDB 3 entries verified

PAE image data not yet available (local image not generated or not reliably fetched), structural assessment based on AlphaFold pLDDT statistics.

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR042289 |  |
| IPR048280 |  |
| IPR036549 |  |

| Pfam | Description |
|------|-------------|
| PF02297 |  |

**Domain Assessment**: Limited domain annotation, but AlphaFold predicts identifiable fold domains

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| COX7C | 0.985 | 0.682 | -- |
| COX5A | 0.983 | 0.748 | -- |
| UQCRB | 0.974 | 0.747 | -- |
| MT-CO2 | 0.97 | 0.811 | -- |
| UQCRQ | 0.967 | 0.744 | -- |
| UQCR10 | 0.963 | 0.748 | -- |
| CYC1 | 0.949 | 0.749 | -- |
| UQCRFS1 | 0.949 | 0.748 | -- |
| COX5B | 0.947 | 0.516 | -- |
| SCO1 | 0.946 | 0.399 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:20562859|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| adgA | psi-mi:"MI:0398"(two hybrid pooling appr | imex:IM-13779|pubmed:2071 | psi-mi:"MI:0915"(physical asso | -- |
| COX14 | psi-mi:"MI:1314"(proximity-dependent bio | pubmed:29568061|imex:IM-2 | psi-mi:"MI:2364"(proximity) | -- |
| PLGRKT | psi-mi:"MI:1314"(proximity-dependent bio | pubmed:29568061|imex:IM-2 | psi-mi:"MI:2364"(proximity) | -- |
| COX4I1 | psi-mi:"MI:1314"(proximity-dependent bio | pubmed:29568061|imex:IM-2 | psi-mi:"MI:2364"(proximity) | -- |
| SCO1 | psi-mi:"MI:1314"(proximity-dependent bio | pubmed:29568061|imex:IM-2 | psi-mi:"MI:2364"(proximity) | -- |
| SFXN1 | psi-mi:"MI:1314"(proximity-dependent bio | pubmed:29568061|imex:IM-2 | psi-mi:"MI:2364"(proximity) | -- |
| CABP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-2 | psi-mi:"MI:0915"(physical asso | -- |

#### UniProt Interactions
- CABP2 (3 experiments)
- DTX2 (3 experiments)
- TTC19 (3 experiments)

**PPI Assessment**: Sparse PPI network (15 STRING partners), possibly independent function protein

### 8. Scoring Overview

| Dimension | Score | Weight | Weighted | Summary |
|------|------|------|------|------|
| Nuclear Localization | 4/10 | x4 | 16 | Weak nuclear localization evidence |
| Protein Size | 8/10 | x1 | 8 | Small (125 aa), suitable for structural studies |
| Research Novelty | 8/10 | x5 | 40 | Very novel (PubMed=30 papers), only limited foundational research |
| 3D Structure | 9/10 | x3 | 27 | Good quality (pLDDT 77.2), 46% high confidence, 0% disordered |
| Regulatory Domains | 6/10 | x2 | 12 | Limited domain annotation, but AlphaFold predicts identifiab |
| PPI Network | 3/10 | x3 | 9 | Sparse PPI network (15 STRING partners), possibly independen |
| **Weighted Total** | | | **115.0/180** | |
| **Normalized Total** | | | **62.8/100** | |

### 9. Final Decision

**SCORED: 62.8/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 30 papers, Extremely high research novelty
- Small (125 aa), suitable for structural studies
- Sufficient structural data (PDB experimental + AlphaFold)

**Weaknesses:**
- Nuclear localization evidence weak, HPA IF validation needed
- Limited domain annotation
- Sparse PPI network

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q5JTJ3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22COA6%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JTJ3
- STRING: https://string-db.org/cgi/network?identifiers=COA6&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/COA6

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (supported)。来源: https://www.proteinatlas.org/ENSG00000168275-COA6/subcellular

![](https://images.proteinatlas.org/28588/281_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28588/281_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/28588/282_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28588/282_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/28588/283_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28588/283_A7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5JTJ3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 55..98; /note="CHCH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01150" |
| InterPro | IPR042289;IPR048280;IPR036549; |
| Pfam | PF02297; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168275-COA6/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CABP2 | Intact | false |
| DTX2 | Intact | false |
| TTC19 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
