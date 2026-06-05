---
type: protein-evaluation
gene: "COPS8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 7
---

## COPS8 (COP9 signalosome complex subunit 8) -- Evaluation Report

### 1. Basic Info

| Property | Value |
|------|-----|
| **UniProt ID** | Q99627 |
| **Protein Name** | COP9 signalosome complex subunit 8 |
| **Aliases** | CSN8 |
| **Length** | 209 aa |
| **Mass** | 23.2 kDa |
| **AlphaFold mean pLDDT** | 85.1 |
| **AlphaFold pLDDT >90** | 71.3% |
| **AlphaFold pLDDT <50** | 11.5% |
| **PubMed (strict)** | 18 |
| **Function** | Component of the COP9 signalosome complex (CSN), a complex involved in various cellular and developmental processes. The CSN complex is an essential regulator of the ubiquitin (Ubl) conjugation pathway by mediating the deneddylation of the cullin subunits of SCF-type E3 ligase complexes, leading to  |

### 2. Nuclear Localization Evidence

#### UniProt Subcellular Location
Cytoplasm; Nucleus

#### GO Cellular Component
- **COP9 signalosome** (IDA:UniProtKB)
- **cytoplasm** (IDA:ComplexPortal)
- **cytosol** (IDA:HPA)
- **extracellular exosome** (HDA:UniProtKB)
- **nucleoplasm** (IDA:HPA)
- **nucleus** (IDA:ComplexPortal)
- **perinuclear region of cytoplasm** (IDA:UniProtKB)

#### HPA Subcellular Localization
- **Main location**: Nucleoplasm
- **Additional locations**: Cytosol
- **Reliability (IF)**: Supported
- **IF Display Images Available**: NO

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 18 |

**Key Papers:**
- PMID:34994476 -- Exosome-like nanoparticles from Mulberry bark prevent DSS-induced colitis via the AhR/COPS8 pathway. (EMBO reports, 2022 Feb 3)
- PMID:32578441 -- COP9 Signalosome Suppresses RIPK1-RIPK3-Mediated Cardiomyocyte Necroptosis in Mice. (Circulation. Heart failure, 2020 Aug)
- PMID:34262479 -- Cullin Deneddylation Suppresses the Necroptotic Pathway in Cardiomyocytes. (Frontiers in physiology, 2021)
- PMID:31550462 -- CENP-A Ubiquitylation Is Indispensable to Cell Viability. (Developmental cell, 2019 Sep 23)
- PMID:28861005 -- Murine Myocardial Transcriptome Analysis Reveals a Critical Role of COPS8 in the Gene Expression of Cullin-RING Ligase S (Frontiers in physiology, 2017)


**Research Volume Assessment**: Low (<50 papers), ample research space

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 85.1
- pLDDT >90: 71.3%, 70-90: 12.0%, 50-70: 5.3%, <50: 11.5%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| 4D10 | X-ray | 3.80 A | H/P=2-209 |
| 4D18 | X-ray | 4.08 A | H/P=1-209 |
| 4WSN | X-ray | 5.50 A | H/P/X/f/n/v=1-209 |
| 6R6H | EM | 8.40 A | H=1-209 |
| 6R7F | EM | 8.20 A | H=1-209 |
| 6R7H | EM | 8.80 A | H=11-209 |
| 6R7I | EM | 5.90 A | H=1-209 |
| 6R7N | EM | 6.50 A | H=11-209 |
| 8H38 | EM | 4.25 A | H=1-209 |
| 8H3A | EM | 7.51 A | H=1-209 |

**Structure Assessment**: PDB experimental structures (11 entries) + high-quality AlphaFold, very high confidence

PAE image data not yet available (local image not generated or not reliably fetched), structural assessment based on AlphaFold pLDDT statistics.

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR033205 |  |
| IPR033464 |  |
| IPR000717 |  |

| Pfam | Description |
|------|-------------|
| PF10075 |  |

**Domain Assessment**: Limited domain annotation, but AlphaFold predicts identifiable fold domains

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| COPS2 | 0.999 | 0.993 | -- |
| COPS7A | 0.999 | 0.995 | -- |
| COPS6 | 0.999 | 0.993 | -- |
| COPS3 | 0.999 | 0.996 | -- |
| GPS1 | 0.999 | 0.996 | -- |
| COPS5 | 0.999 | 0.993 | -- |
| COPS7B | 0.999 | 0.992 | -- |
| COPS4 | 0.999 | 0.991 | -- |
| COPS9 | 0.987 | 0.626 | -- |
| CUL4A | 0.986 | 0.847 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| COPS5 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:18850735|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| vpr | psi-mi:"MI:0007"(anti tag coimmunoprecip | imex:IM-17346|pubmed:2219 | psi-mi:"MI:0914"(association) | -- |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:16396496|mint:MINT | psi-mi:"MI:0914"(association) | -- |
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecip | imex:IM-12079|pubmed:1961 | psi-mi:"MI:0914"(association) | -- |
| CHM | psi-mi:"MI:0007"(anti tag coimmunoprecip | imex:IM-12079|pubmed:1961 | psi-mi:"MI:0914"(association) | -- |
| DCUN1D1 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| CUL2 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |

#### UniProt Interactions
- COPS2 (11 experiments)
- COPS3 (19 experiments)
- COPS4 (7 experiments)
- COPS5 (15 experiments)
- COPS6 (19 experiments)
- COPS7B (5 experiments)
- CUL2 (9 experiments)
- CUL4A (9 experiments)
- CUL4B (11 experiments)
- DCAF11 (5 experiments)

**PPI Assessment**: Sparse PPI network (15 STRING partners), possibly independent function protein

### 8. Scoring Overview

| Dimension | Score | Weight | Weighted | Summary |
|------|------|------|------|------|
| Nuclear Localization | 7/10 | x4 | 28 | Mainly nuclear localization, some cytoplasmic signal |
| Protein Size | 10/10 | x1 | 10 | Medium (209 aa), convenient for biochemical experiments |
| Research Novelty | 10/10 | x5 | 50 | Extremely novel (PubMed=18 papers), nearly unstudied, huge exploration space |
| 3D Structure | 10/10 | x3 | 30 | High quality (pLDDT 85.1), 71% high confidence, 11% disordered |
| Regulatory Domains | 6/10 | x2 | 12 | Limited domain annotation, but AlphaFold predicts identifiab |
| PPI Network | 3/10 | x3 | 9 | Sparse PPI network (15 STRING partners), possibly independen |
| **Weighted Total** | | | **142.0/180** | |
| **Normalized Total** | | | **77.6/100** | |

### 9. Final Decision

**SCORED: 77.6/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 18 papers, Extremely high research novelty
- Medium (209 aa), convenient for biochemical experiments
- Sufficient structural data (PDB experimental + AlphaFold)

**Weaknesses:**
- Nuclear localization needs further HPA confirmation
- Limited domain annotation
- Sparse PPI network

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q99627
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22COPS8%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99627
- STRING: https://string-db.org/cgi/network?identifiers=COPS8&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/COPS8

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000198612-COPS8/subcellular

![](https://images.proteinatlas.org/36485/2183_H11_26_red_green.jpg)
![](https://images.proteinatlas.org/36485/2183_H11_57_red_green.jpg)
![](https://images.proteinatlas.org/36485/403_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/36485/403_C11_2_red_green.jpg)
![](https://images.proteinatlas.org/36485/406_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/36485/406_C11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
