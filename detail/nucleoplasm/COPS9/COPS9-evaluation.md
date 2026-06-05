---
type: protein-evaluation
gene: "COPS9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 7
---

## COPS9 (COP9 signalosome complex subunit 9) -- Evaluation Report

### 1. Basic Info

| Property | Value |
|------|-----|
| **UniProt ID** | Q8WXC6 |
| **Protein Name** | COP9 signalosome complex subunit 9 |
| **Aliases** | MYEOV2 |
| **Length** | 57 aa |
| **Mass** | 6.2 kDa |
| **AlphaFold mean pLDDT** | 62.4 |
| **AlphaFold pLDDT >90** | 0% |
| **AlphaFold pLDDT <50** | 7.0% |
| **PubMed (strict)** | 4 |
| **Function** | Component of the COP9 signalosome complex (CSN), a complex involved in various cellular and developmental processes. The CSN complex is an essential regulator of the ubiquitin (Ubl) conjugation pathway by mediating the deneddylation of the cullin subunits of SCF-type E3 ligase complexes, leading to  |

### 2. Nuclear Localization Evidence

#### UniProt Subcellular Location
Nucleus; Cytoplasm; Nucleus, nucleoplasm; Nucleus, nucleoplasm

#### GO Cellular Component
- **chromatin** (IDA:UniProtKB)
- **COP9 signalosome** (IDA:UniProtKB)
- **cytoplasm** (IDA:UniProtKB)
- **nucleoplasm** (IDA:UniProtKB)
- **nucleus** (IDA:UniProtKB)

#### HPA Subcellular Localization
- **Main location**: Nucleoplasm; Cytosol
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
| Strict | 4 |

**Key Papers:**
- PMID:34630710 -- Analysis of expression profiles and prognostic value of COP9 signalosome subunits for patients with head and neck squamo (Oncology letters, 2021 Nov)
- PMID:39763868 -- Crosslinking-mediated Interactome Analysis Identified PHD2-HIF1α Interaction Hotspots and the Role of PHD2 in Regulating (bioRxiv : the preprint server for biology, 2024 Dec 17)
- PMID:38466642 -- COP9 signalosome complex is a prognostic biomarker and corresponds with immune infiltration in hepatocellular carcinoma. (Aging, 2024 Mar 11)
- PMID:16122798 -- Expression of the cyclin-dependent kinase inhibitor p27 and its deregulation in mouse B cell lymphomas. (Leukemia research, 2006 Feb)


**Research Volume Assessment**: Very low (<10 papers), nearly unstudied, excellent candidate for exploring novel nuclear protein function

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 62.4
- pLDDT >90: 0%, 70-90: 17.5%, 50-70: 75.4%, <50: 7.0%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| None | -- | -- | -- |

**Structure Assessment**: AlphaFold low confidence (pLDDT 62.4), normal for novel proteins

PAE image data not yet available (local image not generated or not reliably fetched), structural assessment based on AlphaFold pLDDT statistics.

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR029391 |  |

| Pfam | Description |
|------|-------------|
| PF15004 |  |

**Domain Assessment**: Sparse domain annotation, normal for novel proteins

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| COPS8 | 0.987 | 0.626 | -- |
| COPS6 | 0.985 | 0.717 | -- |
| COPS5 | 0.983 | 0.729 | -- |
| COPS3 | 0.982 | 0.796 | -- |
| GPS1 | 0.975 | 0.722 | -- |
| COPS2 | 0.973 | 0.64 | -- |
| COPS4 | 0.968 | 0.497 | -- |
| COPS7A | 0.966 | 0.478 | -- |
| COPS7B | 0.961 | 0.482 | -- |
| GRB2 | 0.9 | 0.0 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecip | imex:IM-12079|pubmed:1961 | psi-mi:"MI:0914"(association) | -- |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| CUL4B | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| NEDD8 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| CUL1 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| CUL4A | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |

#### UniProt Interactions
- UBASH3A (3 experiments)

**PPI Assessment**: Sparse PPI network (15 STRING partners), possibly independent function protein

### 8. Scoring Overview

| Dimension | Score | Weight | Weighted | Summary |
|------|------|------|------|------|
| Nuclear Localization | 7/10 | x4 | 28 | Mainly nuclear localization, some cytoplasmic signal |
| Protein Size | 5/10 | x1 | 5 | Very small (57 aa), limited domains |
| Research Novelty | 10/10 | x5 | 50 | Extremely novel (PubMed=4 papers), nearly unstudied, huge exploration space |
| 3D Structure | 6/10 | x3 | 18 | Moderate quality (pLDDT 62.4), 0% high confidence, 7% disordered |
| Regulatory Domains | 4/10 | x2 | 8 | Sparse domain annotation, normal for novel proteins |
| PPI Network | 3/10 | x3 | 9 | Sparse PPI network (15 STRING partners), possibly independen |
| **Weighted Total** | | | **119.0/180** | |
| **Normalized Total** | | | **65.0/100** | |

### 9. Final Decision

**SCORED: 65.0/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 4 papers, Extremely high research novelty
- Very small (57 aa), limited domains
- AlphaFold structure usable

**Weaknesses:**
- Nuclear localization needs further HPA confirmation
- Limited domain annotation
- Sparse PPI network

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q8WXC6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22COPS9%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WXC6
- STRING: https://string-db.org/cgi/network?identifiers=COPS9&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/COPS9

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000172428-COPS9/subcellular

![](https://images.proteinatlas.org/44845/574_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/44845/574_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/44845/580_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/44845/580_A2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
