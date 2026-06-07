---
type: protein-evaluation
gene: "CYB5R3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 4
---

## CYB5R3 (NADH-cytochrome b5 reductase 3) -- Evaluation Report

### 1. Basic Info

| Property | Value |
|------|-----|
| **UniProt ID** | P00387 |
| **Protein Name** | NADH-cytochrome b5 reductase 3 |
| **Aliases** | DIA1 |
| **Length** | 301 aa |
| **Mass** | 34.2 kDa |
| **AlphaFold mean pLDDT** | 93.8 |
| **AlphaFold pLDDT >90** | 89.0% |
| **AlphaFold pLDDT <50** | 3.0% |
| **PubMed (strict)** | 88 |
| **Function** | Catalyzes the reduction of two molecules of cytochrome b5 using NADH as the electron donor |

### 2. Nuclear Localization Evidence

#### UniProt Subcellular Location
Endoplasmic reticulum membrane; Mitochondrion outer membrane; Cytoplasm

#### GO Cellular Component
- **azurophil granule lumen** (TAS:Reactome)
- **cytoplasm** (TAS:ProtInc)
- **cytosol** (IDA:UniProtKB)
- **endoplasmic reticulum** (IDA:HPA)
- **endoplasmic reticulum membrane** (IDA:UniProtKB)
- **extracellular region** (TAS:Reactome)
- **hemoglobin complex** (TAS:ProtInc)
- **lipid droplet** (IDA:UniProtKB)

#### HPA Subcellular Localization
- **Main location**: Endoplasmic reticulum
- **Additional locations**: Perinuclear theca; Calyx; Connecting piece; Mid piece; Principal piece
- **Reliability (IF)**: Supported
- **IF Display Images Available**: YES

HPA IF display images available, reliability: Supported.

### 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF display images available, reliability: Supported.

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 88 |

**Key Papers:**
- PMID:34467556 -- Recommendations for diagnosis and treatment of methemoglobinemia. (American journal of hematology, 2021 Dec 1)
- PMID:36543799 -- The UFM1 system regulates ER-phagy through the ufmylation of CYB5R3. (Nature communications, 2022 Dec 21)
- PMID:38762759 -- VCP/p97 UFMylation stabilizes BECN1 and facilitates the initiation of autophagy. (Autophagy, 2024 Sep)
- PMID:40470795 -- Lipid Droplet-Organized MDM2-Mediated P53 Degradation: A Metabolic Switch Governing Diet-Driven Tumor Progression. (Advanced science (Weinheim, Baden-Wurttemberg, Germany), 2025 Aug)
- PMID:40453108 -- Erythrocytes enhance oxygen-carrying capacity through self-regulation. (Frontiers in physiology, 2025)


**Research Volume Assessment**: Moderate (<100 papers), some research foundation but unexplored niches remain

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 93.8
- pLDDT >90: 89.0%, 70-90: 4.3%, 50-70: 3.7%, <50: 3.0%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| 1UMK | X-ray | 1.75 A | A=27-301 |
| 7THG | X-ray | 2.90 A | A=28-301 |
| 7TNV | X-ray | 1.93 A | A=28-301 |
| 7TSW | X-ray | 2.40 A | A/B/C/D/E/F=28-301 |
| 7W3O | X-ray | 2.46 A | A/B/C/D/E=27-301 |

**Structure Assessment**: PDB experimental structures (5 entries) + high-quality AlphaFold, very high confidence

PAE image data not yet available (local image not generated or not reliably fetched), structural assessment based on AlphaFold pLDDT statistics.

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR001834 |  |
| IPR008333 |  |
| IPR017927 |  |
| IPR001709 |  |
| IPR039261 |  |
| IPR001433 |  |
| IPR017938 |  |

| Pfam | Description |
|------|-------------|
| PF00970 |  |
| PF00175 |  |

**Domain Assessment**: Limited domain annotation, but AlphaFold predicts identifiable fold domains

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| CYB5B | 0.999 | 0.289 | -- |
| CYB5A | 0.999 | 0.254 | -- |
| SUOX | 0.951 | 0.0 | -- |
| MARC1 | 0.937 | 0.0 | -- |
| HBA2 | 0.923 | 0.299 | -- |
| DHODH | 0.912 | 0.469 | -- |
| HBA1 | 0.89 | 0.051 | -- |
| DPYD | 0.878 | 0.469 | -- |
| UMPS | 0.857 | 0.0 | -- |
| HBB | 0.847 | 0.0 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| PRKAB1 | psi-mi:"MI:0006"(anti bait coimmunopreci | pubmed:17353931 | psi-mi:"MI:0915"(physical asso | -- |
| 21125" | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:15502298 | psi-mi:"MI:0407"(direct intera | -- |
| Cav1 | psi-mi:"MI:0006"(anti bait coimmunopreci | pubmed:15293782|imex:IM-2 | psi-mi:"MI:0915"(physical asso | -- |
| Acsl1 | psi-mi:"MI:0029"(cosedimentation through | pubmed:20391537|imex:IM-2 | psi-mi:"MI:0403"(colocalizatio | -- |
| 1C | psi-mi:"MI:0096"(pull down) | imex:IM-15828|pubmed:2259 | psi-mi:"MI:0914"(association) | -- |
| P/V | psi-mi:"MI:0096"(pull down) | pubmed:21911578|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| PDHA1 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.1 | psi-mi:"MI:0914"(association) | -- |
| SDHA | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.1 | psi-mi:"MI:0914"(association) | -- |

#### UniProt Interactions
- ADAM33 (3 experiments)
- AGTRAP (3 experiments)
- AIG1 (3 experiments)
- ALG8 (3 experiments)
- AQP6 (3 experiments)
- ASGR1 (3 experiments)
- BNIP2 (3 experiments)
- CANX (2 experiments)
- CDIPT (3 experiments)
- CERS4 (3 experiments)

**PPI Assessment**: Sparse PPI network (15 STRING partners), possibly independent function protein

### 8. Scoring Overview

| Dimension | Score | Weight | Weighted | Summary |
|------|------|------|------|------|
| Nuclear Localization | 4/10 | x4 | 16 | Weak nuclear localization evidence |
| Protein Size | 10/10 | x1 | 10 | Medium (301 aa), convenient for biochemical experiments |
| Research Novelty | 6/10 | x5 | 30 | Some research (PubMed=88 papers), but nuclear function may be underexplored |
| 3D Structure | 10/10 | x3 | 30 | High quality (pLDDT 93.8), 89% high confidence, 3% disordered |
| Regulatory Domains | 6/10 | x2 | 12 | Limited domain annotation, but AlphaFold predicts identifiab |
| PPI Network | 3/10 | x3 | 9 | Sparse PPI network (15 STRING partners), possibly independen |
| **Weighted Total** | | | **110.0/180** | |
| **Normalized Total** | | | **60.1/100** | |

### 9. Final Decision

**SCORED: 60.1/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 88 papers, Some research space
- Medium (301 aa), convenient for biochemical experiments
- Sufficient structural data (PDB experimental + AlphaFold)

**Weaknesses:**
- Nuclear localization evidence weak, HPA IF validation needed
- Limited domain annotation
- Sparse PPI network

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/P00387
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CYB5R3%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P00387
- STRING: https://string-db.org/cgi/network?identifiers=CYB5R3&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CYB5R3

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Endoplasmic reticulum (supported)。来源: https://www.proteinatlas.org/ENSG00000100243-CYB5R3/subcellular

![](https://images.proteinatlas.org/1566/20_F9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/1566/20_F9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/1566/21_F9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/1566/21_F9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/1566/2239_B6_24_blue_red_green.jpg)
![](https://images.proteinatlas.org/1566/2239_B6_39_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P00387 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 40..152; /note="FAD-binding FR-type"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00716" |
| InterPro | IPR001834;IPR008333;IPR017927;IPR001709;IPR039261;IPR001433;IPR017938; |
| Pfam | PF00970;PF00175; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000100243-CYB5R3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CANX | Intact, Biogrid, Opencell | true |
| FUNDC2 | Intact, Biogrid | true |
| RPN2 | Biogrid, Opencell | true |
| RTN4 | Biogrid, Opencell | true |
| STOM | Intact, Biogrid | true |
| TMED10 | Biogrid, Opencell | true |
| VAPA | Biogrid, Opencell | true |
| VDAC1 | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
