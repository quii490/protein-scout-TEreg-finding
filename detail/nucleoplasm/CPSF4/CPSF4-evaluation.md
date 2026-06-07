---
type: protein-evaluation
gene: "CPSF4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 7
---

## CPSF4 (Cleavage and polyadenylation specificity factor subunit 4) -- Evaluation Report

### 1. Basic Info

| Property | Value |
|------|-----|
| **UniProt ID** | O95639 |
| **Protein Name** | Cleavage and polyadenylation specificity factor subunit 4 |
| **Aliases** | CPSF30; NAR; NEB1 |
| **Length** | 269 aa |
| **Mass** | 30.3 kDa |
| **AlphaFold mean pLDDT** | 75.9 |
| **AlphaFold pLDDT >90** | 37.2% |
| **AlphaFold pLDDT <50** | 23.4% |
| **PubMed (strict)** | 23 |
| **Function** | Component of the cleavage and polyadenylation specificity factor (CPSF) complex that play a key role in pre-mRNA 3'-end formation, recognizing the AAUAAA signal sequence and interacting with poly(A) polymerase and other factors to bring about cleavage and poly(A) addition. CPSF4 binds RNA polymers w |

### 2. Nuclear Localization Evidence

#### UniProt Subcellular Location
Nucleus

#### GO Cellular Component
- **mRNA cleavage and polyadenylation specificity factor complex** (IDA:UniProtKB)
- **nucleoplasm** (IDA:HPA)

#### HPA Subcellular Localization
- **Main location**: Nucleoplasm
- **Additional locations**: Vesicles
- **Reliability (IF)**: Supported
- **IF Display Images Available**: NO

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 23 |

**Key Papers:**
- PMID:34103682 -- CPSF4 regulates circRNA formation and microRNA mediated gene silencing in hepatocellular carcinoma. (Oncogene, 2021 Jun)
- PMID:26628108 -- CREB-binding protein regulates lung cancer growth by targeting MAPK and CPSF4 signaling pathway. (Molecular oncology, 2016 Feb)
- PMID:37629142 -- Cleavage and Polyadenylation-Specific Factor 4 (CPSF4) Expression Is Associated with Enhanced Prostate Cancer Cell Migra (International journal of molecular sciences, 2023 Aug 19)
- PMID:37542549 -- Comprehensive analysis of CPSF4-related alternative splice genes in hepatocellular carcinoma. (Journal of cancer research and clinical oncology, 2023 Nov)
- PMID:24618080 -- CPSF4 activates telomerase reverse transcriptase and predicts poor prognosis in human lung adenocarcinomas. (Molecular oncology, 2014 May)


**Research Volume Assessment**: Low (<50 papers), ample research space

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 75.9
- pLDDT >90: 37.2%, 70-90: 34.9%, 50-70: 4.5%, <50: 23.4%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| 2D9N | NMR | - | A=61-126 |
| 2RHK | X-ray | 1.95 A | C/D=61-121 |
| 6DNH | EM | 3.40 A | C=1-269 |
| 6FUW | EM | 3.07 A | C=1-178 |
| 6URG | EM | 3.00 A | C=1-269 |
| 6URO | EM | 3.60 A | C=1-269 |
| 7K95 | X-ray | 1.90 A | A=114-173 |
| 7ZYH | X-ray | 2.20 A | A/D/G/J=118-178 |
| 8E3I | EM | 2.53 A | C=1-269 |
| 8E3Q | EM | 2.68 A | C=1-269 |

**Structure Assessment**: PDB experimental structures (11 entries) + high-quality AlphaFold, very high confidence

PAE image data not yet available (local image not generated or not reliably fetched), structural assessment based on AlphaFold pLDDT statistics.

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR045348 |  |
| IPR041686 |  |
| IPR000571 |  |
| IPR036855 |  |
| IPR001878 |  |
| IPR036875 |  |

| Pfam | Description |
|------|-------------|
| PF00642 |  |
| PF15663 |  |
| PF00098 |  |

**Domain Assessment**: Limited domain annotation, but AlphaFold predicts identifiable fold domains

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| CPSF3 | 0.999 | 0.961 | -- |
| FIP1L1 | 0.999 | 0.997 | -- |
| SYMPK | 0.999 | 0.975 | -- |
| WDR33 | 0.999 | 0.997 | -- |
| CPSF1 | 0.999 | 0.998 | -- |
| CPSF2 | 0.999 | 0.993 | -- |
| CSTF2 | 0.997 | 0.764 | -- |
| CSTF3 | 0.995 | 0.908 | -- |
| NUDT21 | 0.99 | 0.572 | -- |
| CPSF7 | 0.979 | 0.0 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| FIP1L1 | psi-mi:"MI:0398"(two hybrid pooling appr | pubmed:16189514|imex:IM-1 | psi-mi:"MI:0915"(physical asso | -- |
| MARK3 | psi-mi:"MI:0398"(two hybrid pooling appr | pubmed:16169070|imex:IM-1 | psi-mi:"MI:0915"(physical asso | -- |
| NS | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:2006 | psi-mi:"MI:0915"(physical asso | -- |
| CLK2 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:23602568|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:31527615|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| ARHGAP26 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:32203420|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| MID2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-2 | psi-mi:"MI:0915"(physical asso | -- |
| MYOG | psi-mi:"MI:1112"(two hybrid prey pooling | pubmed:32296183|imex:IM-2 | psi-mi:"MI:0915"(physical asso | -- |

#### UniProt Interactions
- CDC73 (3 experiments)
- FIP1L1 (5 experiments)
- MEOX2 (3 experiments)
- NS1 (5 experiments)
- NS1 (5 experiments)
- NS (4 experiments)
- MID2 (3 experiments)
- MYOG (3 experiments)

**PPI Assessment**: Sparse PPI network (15 STRING partners), possibly independent function protein

### 8. Scoring Overview

| Dimension | Score | Weight | Weighted | Summary |
|------|------|------|------|------|
| Nuclear Localization | 7/10 | x4 | 28 | Mainly nuclear localization, some cytoplasmic signal |
| Protein Size | 10/10 | x1 | 10 | Medium (269 aa), convenient for biochemical experiments |
| Research Novelty | 8/10 | x5 | 40 | Very novel (PubMed=23 papers), only limited foundational research |
| 3D Structure | 10/10 | x3 | 30 | Good quality (pLDDT 75.9), 37% high confidence, 23% disordered |
| Regulatory Domains | 6/10 | x2 | 12 | Limited domain annotation, but AlphaFold predicts identifiab |
| PPI Network | 3/10 | x3 | 9 | Sparse PPI network (15 STRING partners), possibly independen |
| **Weighted Total** | | | **132.0/180** | |
| **Normalized Total** | | | **72.1/100** | |

### 9. Final Decision

**SCORED: 72.1/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 23 papers, Extremely high research novelty
- Medium (269 aa), convenient for biochemical experiments
- Sufficient structural data (PDB experimental + AlphaFold)

**Weaknesses:**
- Nuclear localization needs further HPA confirmation
- Limited domain annotation
- Sparse PPI network

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/O95639
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CPSF4%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95639
- STRING: https://string-db.org/cgi/network?identifiers=CPSF4&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CPSF4

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000160917-CPSF4/subcellular

![](https://images.proteinatlas.org/66470/1213_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/66470/1213_F9_2_red_green.jpg)
![](https://images.proteinatlas.org/66470/1230_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/66470/1230_H11_2_red_green.jpg)
![](https://images.proteinatlas.org/66470/1235_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/66470/1235_F9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O95639 |
| SMART | SM00343;SM00356; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR045348;IPR041686;IPR000571;IPR036855;IPR001878;IPR036875; |
| Pfam | PF00642;PF15663;PF00098; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000160917-CPSF4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CPSF1 | Intact, Biogrid | true |
| FIP1L1 | Intact, Biogrid | true |
| CAPZB | Opencell | false |
| CDC73 | Intact | false |
| CPSF2 | Biogrid | false |
| CPSF3 | Biogrid | false |
| CPSF6 | Opencell | false |
| CREBBP | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
