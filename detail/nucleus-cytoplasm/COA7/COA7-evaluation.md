---
type: protein-evaluation
gene: "COA7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 4
---

## COA7 (Cytochrome c oxidase assembly factor 7) -- Evaluation Report

### 1. Basic Info

| Property | Value |
|------|-----|
| **UniProt ID** | Q96BR5 |
| **Protein Name** | Cytochrome c oxidase assembly factor 7 |
| **Aliases** | C1orf163; RESA1; SELRC1 |
| **Length** | 231 aa |
| **Mass** | 25.7 kDa |
| **AlphaFold mean pLDDT** | 95.3 |
| **AlphaFold pLDDT >90** | 93.1% |
| **AlphaFold pLDDT <50** | 0.4% |
| **PubMed (strict)** | 11 |
| **Function** | Required for assembly of mitochondrial respiratory chain complex I and complex IV |

### 2. Nuclear Localization Evidence

#### UniProt Subcellular Location
Mitochondrion intermembrane space

#### GO Cellular Component
- **mitochondrial intermembrane space** (IDA:UniProtKB)
- **mitochondrion** (IDA:HPA)
- **nucleoplasm** (IDA:HPA)

#### HPA Subcellular Localization
- **Main location**: Nucleoplasm; Mitochondria
- **Additional locations**: None
- **Reliability (IF)**: Approved
- **IF Display Images Available**: NO

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 11 |

**Key Papers:**
- PMID:35304567 -- Clinical genetics of Charcot-Marie-Tooth disease. (Journal of human genetics, 2023 Mar)
- PMID:37750949 -- Dystonia and Parkinsonism in COA7-related disorders: expanding the phenotypic spectrum. (Journal of neurology, 2024 Jan)
- PMID:39811936 -- A Mitochondria-Related Signature in Diffuse Large B-Cell Lymphoma: Prognosis, Immune and Therapeutic Features. (Cancer medicine, 2025 Jan)
- PMID:37838251 -- Quantitative proteomics reveals the neurotoxicity of trimethyltin chloride on mitochondria in the hippocampus of mice. (Neurotoxicology, 2023 Dec)
- PMID:30885959 -- Inhibition of proteasome rescues a pathogenic variant of respiratory chain assembly factor COA7. (EMBO molecular medicine, 2019 May)


**Research Volume Assessment**: Low (<50 papers), ample research space

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 95.3
- pLDDT >90: 93.1%, 70-90: 4.3%, 50-70: 2.2%, <50: 0.4%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| 7MQZ | X-ray | 2.39 A | A=1-231 |

**Structure Assessment**: High-quality AlphaFold prediction (pLDDT 95.3), fold confidence high, PDB 1 entries verified

PAE image data not yet available (local image not generated or not reliably fetched), structural assessment based on AlphaFold pLDDT statistics.

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR040239 |  |
| IPR006597 |  |
| IPR011990 |  |

| Pfam | Description |
|------|-------------|
| PF08238 |  |

**Domain Assessment**: Limited domain annotation, but AlphaFold predicts identifiable fold domains

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| CHCHD4 | 0.739 | 0.361 | -- |
| SCO1 | 0.707 | 0.227 | -- |
| COA4 | 0.648 | 0.0 | -- |
| SYVN1 | 0.647 | 0.246 | -- |
| COX6B1 | 0.629 | 0.227 | -- |
| COA6 | 0.625 | 0.0 | -- |
| COA5 | 0.602 | 0.0 | -- |
| COX17 | 0.6 | 0.0 | -- |
| SAMM50 | 0.59 | 0.0 | -- |
| SETX | 0.582 | 0.0 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| Amacr | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-1 | psi-mi:"MI:0915"(physical asso | -- |
| - | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-1 | psi-mi:"MI:0915"(physical asso | -- |
| P/V | psi-mi:"MI:0096"(pull down) | pubmed:21911578|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| CCN2 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:28514442|doi:10.10 | psi-mi:"MI:0914"(association) | -- |
| AIFM1 | psi-mi:"MI:1314"(proximity-dependent bio | pubmed:29568061|imex:IM-2 | psi-mi:"MI:2364"(proximity) | -- |
| PLGRKT | psi-mi:"MI:1314"(proximity-dependent bio | pubmed:29568061|imex:IM-2 | psi-mi:"MI:2364"(proximity) | -- |
| COX14 | psi-mi:"MI:1314"(proximity-dependent bio | pubmed:29568061|imex:IM-2 | psi-mi:"MI:2364"(proximity) | -- |
| COX4I1 | psi-mi:"MI:1314"(proximity-dependent bio | pubmed:29568061|imex:IM-2 | psi-mi:"MI:2364"(proximity) | -- |

#### UniProt Interactions
- ACOT8 (2 experiments)
- C11orf54 (2 experiments)
- CASP6 (3 experiments)
- CYCS (3 experiments)
- DMWD (3 experiments)
- DPP8 (2 experiments)
- ENKD1 (3 experiments)
- FGFR3 (3 experiments)
- GPSM3 (3 experiments)
- GSN (3 experiments)

**PPI Assessment**: Sparse PPI network (15 STRING partners), possibly independent function protein

### 8. Scoring Overview

| Dimension | Score | Weight | Weighted | Summary |
|------|------|------|------|------|
| Nuclear Localization | 4/10 | x4 | 16 | Weak nuclear localization evidence |
| Protein Size | 10/10 | x1 | 10 | Medium (231 aa), convenient for biochemical experiments |
| Research Novelty | 10/10 | x5 | 50 | Extremely novel (PubMed=11 papers), nearly unstudied, huge exploration space |
| 3D Structure | 8/10 | x3 | 24 | High quality (pLDDT 95.3), 93% high confidence, 0% disordered |
| Regulatory Domains | 6/10 | x2 | 12 | Limited domain annotation, but AlphaFold predicts identifiab |
| PPI Network | 3/10 | x3 | 9 | Sparse PPI network (15 STRING partners), possibly independen |
| **Weighted Total** | | | **123.0/180** | |
| **Normalized Total** | | | **67.2/100** | |

### 9. Final Decision

**SCORED: 67.2/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 11 papers, Extremely high research novelty
- Medium (231 aa), convenient for biochemical experiments
- Sufficient structural data (PDB experimental + AlphaFold)

**Weaknesses:**
- Nuclear localization evidence weak, HPA IF validation needed
- Limited domain annotation
- Sparse PPI network

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q96BR5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22COA7%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96BR5
- STRING: https://string-db.org/cgi/network?identifiers=COA7&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/COA7

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000162377-COA7/subcellular

![](https://images.proteinatlas.org/29926/402_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/29926/402_E7_4_red_green.jpg)
![](https://images.proteinatlas.org/29926/405_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/29926/405_E7_2_red_green.jpg)
![](https://images.proteinatlas.org/29926/409_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/29926/409_E7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96BR5 |
| SMART | SM00671; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR040239;IPR006597;IPR011990; |
| Pfam | PF08238; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000162377-COA7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACOT8 | Intact, Bioplex | false |
| AIFM1 | Biogrid | false |
| B3GNT3 | Bioplex | false |
| B4GALT3 | Bioplex | false |
| C11orf54 | Intact | false |
| CASP6 | Intact | false |
| CKMT2 | Bioplex | false |
| COX11 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
