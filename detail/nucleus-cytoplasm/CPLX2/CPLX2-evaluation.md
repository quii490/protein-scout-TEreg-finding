---
type: protein-evaluation
gene: "CPLX2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 4
---

## CPLX2 (Complexin-2) -- Evaluation Report

### 1. Basic Info

| Property | Value |
|------|-----|
| **UniProt ID** | Q6PUV4 |
| **Protein Name** | Complexin-2 |
| **Aliases** | CPLX2 |
| **Length** | 134 aa |
| **Mass** | 15.4 kDa |
| **AlphaFold mean pLDDT** | 70.0 |
| **AlphaFold pLDDT >90** | 17.2% |
| **AlphaFold pLDDT <50** | 9.0% |
| **PubMed (strict)** | 50 |
| **Function** | Negatively regulates the formation of synaptic vesicle clustering at active zone to the presynaptic membrane in postmitotic neurons. Positively regulates a late step in exocytosis of various cytoplasmic vesicles, such as synaptic vesicles and other secretory vesicles. Also involved in mast cell exoc |

### 2. Nuclear Localization Evidence

#### UniProt Subcellular Location
Cytoplasm, cytosol; Presynapse; Nucleus; Perikaryon

#### GO Cellular Component
- **calyx of Held** (IEA:Ensembl)
- **cytosol** (IEA:UniProtKB-SubCell)
- **dendrite** (IEA:Ensembl)
- **glutamatergic synapse** (IEA:Ensembl)
- **nucleus** (IEA:UniProtKB-SubCell)
- **perikaryon** (IEA:UniProtKB-SubCell)
- **postsynapse** (IEA:Ensembl)
- **SNARE complex** (IBA:GO_Central)

#### HPA Subcellular Localization
- **Main location**: Vesicles
- **Additional locations**: None
- **Reliability (IF)**: Uncertain
- **IF Display Images Available**: YES

HPA IF display images available, reliability: Uncertain.

### 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF display images available, reliability: Uncertain.

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 50 |

**Key Papers:**
- PMID:40355240 -- The role of CPLX2 and SNAP25 genes in the rehabilitation of colorectal cancer liver metastases: CPLX2, SNAP25 in colorec (Medicine, 2025 May 9)
- PMID:40229859 -- Gene signatures and immune correlations in Parkinson's disease Braak stages. (European journal of medical research, 2025 Apr 15)
- PMID:33627638 -- Chronic mild stress-induced protein dysregulations correlated with susceptibility and resiliency to depression or anxiet (Translational psychiatry, 2021 Feb 24)
- PMID:38427133 -- CPLX2 is a novel tumor suppressor and improves the prognosis in glioma. (Journal of neuro-oncology, 2024 Mar)
- PMID:16162394 -- Structural organization of the human complexin 2 gene (CPLX2) and aspects of its functional activity. (Gene, 2005 Oct 10)


**Research Volume Assessment**: Low (<50 papers), ample research space

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 70.0
- pLDDT >90: 17.2%, 70-90: 32.1%, 50-70: 41.8%, <50: 9.0%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| None | -- | -- | -- |

**Structure Assessment**: AlphaFold moderate quality (pLDDT 70.0), ordered region 49%

PAE image data not yet available (local image not generated or not reliably fetched), structural assessment based on AlphaFold pLDDT statistics.

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR008849 |  |

| Pfam | Description |
|------|-------------|
| PF05835 |  |

**Domain Assessment**: Limited domain annotation, but AlphaFold predicts identifiable fold domains

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| VAMP2 | 0.971 | 0.094 | -- |
| CPLX4 | 0.958 | 0.0 | -- |
| STX1A | 0.956 | 0.321 | -- |
| CPLX1 | 0.953 | 0.421 | -- |
| SNAP25 | 0.947 | 0.311 | -- |
| CPLX3 | 0.929 | 0.096 | -- |
| NEUROD2 | 0.902 | 0.0 | -- |
| SYT1 | 0.839 | 0.05 | -- |
| STX3 | 0.836 | 0.081 | -- |
| SNAP23 | 0.819 | 0.057 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| PCBD1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-2 | psi-mi:"MI:0915"(physical asso | -- |
| ETS1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-2 | psi-mi:"MI:0915"(physical asso | -- |
| CPLX1 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:28514442|doi:10.10 | psi-mi:"MI:0914"(association) | -- |
| NDRG4 | psi-mi:"MI:1112"(two hybrid prey pooling | pubmed:32296183|imex:IM-2 | psi-mi:"MI:0915"(physical asso | -- |
| TSFM | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-2 | psi-mi:"MI:0915"(physical asso | -- |
| PBX3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-2 | psi-mi:"MI:0915"(physical asso | -- |
| MYG1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-2 | psi-mi:"MI:0915"(physical asso | -- |
| DEGS1 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:28514442|doi:10.10 | psi-mi:"MI:0914"(association) | -- |

#### UniProt Interactions
- MYG1 (3 experiments)
- NDRG4 (3 experiments)
- PBX3 (3 experiments)
- TSFM (3 experiments)

**PPI Assessment**: Sparse PPI network (15 STRING partners), possibly independent function protein

### 8. Scoring Overview

| Dimension | Score | Weight | Weighted | Summary |
|------|------|------|------|------|
| Nuclear Localization | 4/10 | x4 | 16 | Weak nuclear localization evidence |
| Protein Size | 8/10 | x1 | 8 | Small (134 aa), suitable for structural studies |
| Research Novelty | 8/10 | x5 | 40 | Very novel (PubMed=50 papers), only limited foundational research |
| 3D Structure | 7/10 | x3 | 21 | Good quality (pLDDT 70.0), 17% high confidence, 9% disordered |
| Regulatory Domains | 6/10 | x2 | 12 | Limited domain annotation, but AlphaFold predicts identifiab |
| PPI Network | 3/10 | x3 | 9 | Sparse PPI network (15 STRING partners), possibly independen |
| **Weighted Total** | | | **107.0/180** | |
| **Normalized Total** | | | **58.5/100** | |

### 9. Final Decision

**SCORED: 58.5/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 50 papers, Extremely high research novelty
- Small (134 aa), suitable for structural studies
- AlphaFold structure usable

**Weaknesses:**
- Nuclear localization evidence weak, HPA IF validation needed
- Limited domain annotation
- Sparse PPI network

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q6PUV4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CPLX2%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6PUV4
- STRING: https://string-db.org/cgi/network?identifiers=CPLX2&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CPLX2

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (uncertain)。来源: https://www.proteinatlas.org/ENSG00000145920-CPLX2/subcellular

![](https://images.proteinatlas.org/71191/1405_C6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/71191/1405_C6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/71191/1408_C6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/71191/1408_C6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/71191/1476_C1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/71191/1476_C1_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6PUV4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008849; |
| Pfam | PF05835; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000145920-CPLX2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CPLX1 | Bioplex | false |
| DHX16 | Bioplex | false |
| MYG1 | Intact | false |
| SRP54 | Bioplex | false |
| TSFM | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
