---
type: protein-evaluation
gene: "COPS7B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 7
---

## COPS7B (COP9 signalosome complex subunit 7b) -- Evaluation Report

### 1. Basic Info

| Property | Value |
|------|-----|
| **UniProt ID** | Q9H9Q2 |
| **Protein Name** | COP9 signalosome complex subunit 7b |
| **Aliases** | CSN7B |
| **Length** | 264 aa |
| **Mass** | 29.6 kDa |
| **AlphaFold mean pLDDT** | 84.8 |
| **AlphaFold pLDDT >90** | 65.2% |
| **AlphaFold pLDDT <50** | 12.1% |
| **PubMed (strict)** | 13 |
| **Function** | Component of the COP9 signalosome complex (CSN), a complex involved in various cellular and developmental processes. The CSN complex is an essential regulator of the ubiquitin (Ubl) conjugation pathway by mediating the deneddylation of the cullin subunits of SCF-type E3 ligase complexes, leading to  |

### 2. Nuclear Localization Evidence

#### UniProt Subcellular Location
Cytoplasm; Nucleus

#### GO Cellular Component
- **COP9 signalosome** (IDA:UniProtKB)
- **cytoplasm** (ISS:ComplexPortal)
- **cytosol** (TAS:Reactome)
- **nucleoplasm** (IDA:HPA)
- **nucleus** (ISS:ComplexPortal)

#### HPA Subcellular Localization
- **Main location**: Nucleoplasm
- **Additional locations**: None
- **Reliability (IF)**: Supported
- **IF Display Images Available**: NO

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 13 |

**Key Papers:**
- PMID:29928389 -- Novel insights into biomarkers associated with renal cell carcinoma. (Oncology letters, 2018 Jul)
- PMID:37560971 -- The IGF2BP3-COPS7B Axis Facilitates mRNA Translation to Drive Colorectal Cancer Progression. (Cancer research, 2023 Nov 1)
- PMID:35954157 -- Kidney Cancer Biomarker Selection Using Regularized Survival Models. (Cells, 2022 Jul 27)
- PMID:35741748 -- Genome-Wide Association Study of Potential Meat Quality Trait Loci in Ducks. (Genes, 2022 May 31)
- PMID:41920966 -- Uncovering BAP1 deubiquitination landscape enhances mechanism elucidation and therapeutic precision for BAP1-deficient p (Science translational medicine, 2026 Apr)


**Research Volume Assessment**: Low (<50 papers), ample research space

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 84.8
- pLDDT >90: 65.2%, 70-90: 19.3%, 50-70: 3.4%, <50: 12.1%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| 6R6H | EM | 8.40 A | G=9-214 |
| 6R7F | EM | 8.20 A | G=8-215 |
| 6R7H | EM | 8.80 A | G=8-215 |
| 6R7I | EM | 5.90 A | G=1-215 |
| 6R7N | EM | 6.50 A | G=1-215 |
| 8H38 | EM | 4.25 A | G=1-264 |
| 8H3A | EM | 7.51 A | G=1-264 |
| 8H3F | EM | 6.73 A | G=1-220 |

**Structure Assessment**: PDB experimental structures (8 entries) + high-quality AlphaFold, very high confidence

PAE image data not yet available (local image not generated or not reliably fetched), structural assessment based on AlphaFold pLDDT statistics.

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR045237 |  |
| IPR041481 |  |
| IPR000717 |  |

| Pfam | Description |
|------|-------------|
| PF22061 |  |
| PF18392 |  |
| PF01399 |  |

**Domain Assessment**: Limited domain annotation, but AlphaFold predicts identifiable fold domains

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| GPS1 | 0.999 | 0.987 | -- |
| COPS3 | 0.999 | 0.994 | -- |
| COPS2 | 0.999 | 0.995 | -- |
| COPS6 | 0.999 | 0.994 | -- |
| COPS8 | 0.999 | 0.992 | -- |
| COPS4 | 0.999 | 0.998 | -- |
| COPS5 | 0.999 | 0.993 | -- |
| COPS7A | 0.987 | 0.8 | -- |
| COPS9 | 0.961 | 0.482 | -- |
| NEDD8 | 0.958 | 0.808 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| COPS5 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:18850735|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecip | imex:IM-12079|pubmed:1961 | psi-mi:"MI:0914"(association) | -- |
| Ddb1 | psi-mi:"MI:0676"(tandem affinity purific | imex:IM-11719|pubmed:2036 | psi-mi:"MI:0915"(physical asso | -- |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| CUL2 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| CUL1 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| NEDD8 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| EBI-1257123 | psi-mi:"MI:0096"(pull down) | pubmed:19367725|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |

#### UniProt Interactions
- BEX5 (3 experiments)
- CCT5 (3 experiments)
- COPS2 (4 experiments)
- COPS4 (4 experiments)
- COPS5 (12 experiments)
- COPS6 (10 experiments)
- COPS8 (5 experiments)
- DCAF11 (4 experiments)
- HSPB1 (3 experiments)
- NMI (9 experiments)

**PPI Assessment**: Sparse PPI network (15 STRING partners), possibly independent function protein

### 8. Scoring Overview

| Dimension | Score | Weight | Weighted | Summary |
|------|------|------|------|------|
| Nuclear Localization | 7/10 | x4 | 28 | Mainly nuclear localization, some cytoplasmic signal |
| Protein Size | 10/10 | x1 | 10 | Medium (264 aa), convenient for biochemical experiments |
| Research Novelty | 10/10 | x5 | 50 | Extremely novel (PubMed=13 papers), nearly unstudied, huge exploration space |
| 3D Structure | 10/10 | x3 | 30 | High quality (pLDDT 84.8), 65% high confidence, 12% disordered |
| Regulatory Domains | 6/10 | x2 | 12 | Limited domain annotation, but AlphaFold predicts identifiab |
| PPI Network | 3/10 | x3 | 9 | Sparse PPI network (15 STRING partners), possibly independen |
| **Weighted Total** | | | **142.0/180** | |
| **Normalized Total** | | | **77.6/100** | |

### 9. Final Decision

**SCORED: 77.6/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 13 papers, Extremely high research novelty
- Medium (264 aa), convenient for biochemical experiments
- Sufficient structural data (PDB experimental + AlphaFold)

**Weaknesses:**
- Nuclear localization needs further HPA confirmation
- Limited domain annotation
- Sparse PPI network

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9H9Q2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22COPS7B%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H9Q2
- STRING: https://string-db.org/cgi/network?identifiers=COPS7B&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/COPS7B

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000144524-COPS7B/subcellular

![](https://images.proteinatlas.org/34676/574_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/34676/574_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/34676/580_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/34676/580_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/34676/590_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/34676/590_H8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H9Q2 |
| SMART | SM00088; |
| UniProt Domain [FT] | DOMAIN 2..159; /note="PCI"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01185" |
| InterPro | IPR045237;IPR041481;IPR000717; |
| Pfam | PF22061;PF18392;PF01399; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000144524-COPS7B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| COPS2 | Intact, Biogrid | true |
| COPS3 | Biogrid, Bioplex | true |
| COPS4 | Intact, Biogrid, Bioplex | true |
| COPS5 | Intact, Biogrid, Bioplex | true |
| COPS6 | Intact, Biogrid, Bioplex | true |
| COPS7A | Biogrid, Bioplex | true |
| COPS8 | Intact, Biogrid, Bioplex | true |
| CUL2 | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
