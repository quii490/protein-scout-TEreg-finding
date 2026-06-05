---
type: protein-evaluation
gene: "DCLRE1C"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 7
---

## DCLRE1C (Protein artemis) -- Evaluation Report

### 1. Basic Info

| Property | Value |
|------|-----|
| **UniProt ID** | Q96SD1 |
| **Protein Name** | Protein artemis |
| **Aliases** | ARTEMIS; ASCID; SCIDA; SNM1C |
| **Length** | 692 aa |
| **Mass** | 78.4 kDa |
| **AlphaFold mean pLDDT** | 69.4 |
| **AlphaFold pLDDT >90** | 46.1% |
| **AlphaFold pLDDT <50** | 39.7% |
| **PubMed (strict)** | 69 |
| **Function** | Nuclease involved in DNA non-homologous end joining (NHEJ); required for double-strand break repair and V(D)J recombination (PubMed:11336668, PubMed:11955432, PubMed:12055248, PubMed:14744996, PubMed:15071507, PubMed:15574326, PubMed:15936993). Required for V(D)J recombination, the process by which  |

### 2. Nuclear Localization Evidence

#### UniProt Subcellular Location
Nucleus

#### GO Cellular Component
- **Golgi apparatus** (IDA:HPA)
- **nonhomologous end joining complex** (IDA:UniProtKB)
- **nucleoplasm** (IDA:HPA)
- **nucleus** (IBA:GO_Central)

#### HPA Subcellular Localization
- **Main location**: Nucleoplasm
- **Additional locations**: Golgi apparatus
- **Reliability (IF)**: Supported
- **IF Display Images Available**: NO

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 69 |

**Key Papers:**
- PMID:36546626 -- Lentiviral Gene Therapy for Artemis-Deficient SCID. (The New England journal of medicine, 2022 Dec 22)
- PMID:31717670 -- NK Cells from RAG- or DCLRE1C-Deficient Patients Inhibit HCMV. (Microorganisms, 2019 Nov 10)
- PMID:38397417 -- Dclre1c-Mutation-Induced Immunocompromised Mice Are a Novel Model for Human Xenograft Research. (Biomolecules, 2024 Feb 2)
- PMID:19953608 -- The most frequent DCLRE1C (ARTEMIS) mutations are based on homologous recombination events. (Human mutation, 2010 Feb)
- PMID:34406419 -- Compound heterozygous DCLRE1C mutations lead to clinically typical Severe Combined Immunodeficiency presenting with Graf (Immunogenetics, 2021 Dec)


**Research Volume Assessment**: Moderate (<100 papers), some research foundation but unexplored niches remain

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 69.4
- pLDDT >90: 46.1%, 70-90: 9.0%, 50-70: 5.2%, <50: 39.7%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| 3W1B | X-ray | 2.40 A | B=485-495 |
| 3W1G | X-ray | 2.55 A | B=485-495 |
| 4HTP | X-ray | 2.25 A | C/E=485-495 |
| 6TT5 | X-ray | 1.50 A | AAA=1-361 |
| 6WNL | X-ray | 2.37 A | A/B=2-368 |
| 6WO0 | X-ray | 1.97 A | A=2-368 |
| 7ABS | X-ray | 1.97 A | A=2-368 |
| 7AF1 | X-ray | 1.70 A | A=1-361 |
| 7AFS | X-ray | 1.70 A | A=1-361 |
| 7AFU | X-ray | 1.56 A | A=1-361 |

**Structure Assessment**: AlphaFold low confidence (pLDDT 69.4), normal for novel proteins

PAE image data not yet available (local image not generated or not reliably fetched), structural assessment based on AlphaFold pLDDT statistics.

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR011084 |  |
| IPR036866 |  |

| Pfam | Description |
|------|-------------|
| PF07522 |  |

**Domain Assessment**: Sparse domain annotation, normal for novel proteins

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| PRKDC | 0.999 | 0.98 | -- |
| XRCC5 | 0.998 | 0.942 | -- |
| XRCC6 | 0.997 | 0.903 | -- |
| LIG4 | 0.997 | 0.626 | -- |
| NHEJ1 | 0.992 | 0.0 | -- |
| XRCC4 | 0.983 | 0.292 | -- |
| ATM | 0.956 | 0.292 | -- |
| MSH2 | 0.944 | 0.188 | -- |
| ERCC5 | 0.944 | 0.109 | -- |
| ERCC1 | 0.943 | 0.0 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| ZSWIM8 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:28514442|doi:10.10 | psi-mi:"MI:0914"(association) | -- |
| ANKRD28 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:28514442|doi:10.10 | psi-mi:"MI:0914"(association) | -- |
| PRKAB2 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:28514442|doi:10.10 | psi-mi:"MI:0914"(association) | -- |
| PPP6R2 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:28514442|doi:10.10 | psi-mi:"MI:0914"(association) | -- |
| PRKACB | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:28514442|doi:10.10 | psi-mi:"MI:0914"(association) | -- |
| CDC27 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:28514442|doi:10.10 | psi-mi:"MI:0914"(association) | -- |
| MTHFR | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:28514442|doi:10.10 | psi-mi:"MI:0914"(association) | -- |
| PRKAG1 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:28514442|doi:10.10 | psi-mi:"MI:0914"(association) | -- |

#### UniProt Interactions
- LIG4 (16 experiments)
- PRKDC (5 experiments)

**PPI Assessment**: Sparse PPI network (15 STRING partners), possibly independent function protein

### 8. Scoring Overview

| Dimension | Score | Weight | Weighted | Summary |
|------|------|------|------|------|
| Nuclear Localization | 7/10 | x4 | 28 | Mainly nuclear localization, some cytoplasmic signal |
| Protein Size | 10/10 | x1 | 10 | Medium (692 aa), convenient for biochemical experiments |
| Research Novelty | 6/10 | x5 | 30 | Some research (PubMed=69 papers), but nuclear function may be underexplored |
| 3D Structure | 6/10 | x3 | 18 | Moderate quality (pLDDT 69.4), 46% high confidence, 39% disordered |
| Regulatory Domains | 4/10 | x2 | 8 | Sparse domain annotation, normal for novel proteins |
| PPI Network | 3/10 | x3 | 9 | Sparse PPI network (15 STRING partners), possibly independen |
| **Weighted Total** | | | **105.5/180** | |
| **Normalized Total** | | | **57.7/100** | |

### 9. Final Decision

**SCORED: 57.7/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 69 papers, Some research space
- Medium (692 aa), convenient for biochemical experiments
- AlphaFold structure usable

**Weaknesses:**
- Nuclear localization needs further HPA confirmation
- Limited domain annotation
- Sparse PPI network

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q96SD1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22DCLRE1C%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96SD1
- STRING: https://string-db.org/cgi/network?identifiers=DCLRE1C&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/DCLRE1C

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000152457-DCLRE1C/subcellular

![](https://images.proteinatlas.org/69295/1360_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/69295/1360_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/69295/1367_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/69295/1367_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/69295/1547_H7_2_red_green.jpg)
![](https://images.proteinatlas.org/69295/1547_H7_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
