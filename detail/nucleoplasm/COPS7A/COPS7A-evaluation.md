---
type: protein-evaluation
gene: "COPS7A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 7
---

## COPS7A (COP9 signalosome complex subunit 7a) -- Evaluation Report

### 1. Basic Info

| Property | Value |
|------|-----|
| **UniProt ID** | Q9UBW8 |
| **Protein Name** | COP9 signalosome complex subunit 7a |
| **Aliases** | CSN7A; DERP10 |
| **Length** | 275 aa |
| **Mass** | 30.3 kDa |
| **AlphaFold mean pLDDT** | 84.6 |
| **AlphaFold pLDDT >90** | 71.3% |
| **AlphaFold pLDDT <50** | 17.5% |
| **PubMed (strict)** | 15 |
| **Function** | Component of the COP9 signalosome complex (CSN), a complex involved in various cellular and developmental processes. The CSN complex is an essential regulator of the ubiquitin (Ubl) conjugation pathway by mediating the deneddylation of the cullin subunits of SCF-type E3 ligase complexes, leading to  |

### 2. Nuclear Localization Evidence

#### UniProt Subcellular Location
Cytoplasm; Nucleus

#### GO Cellular Component
- **COP9 signalosome** (IDA:UniProtKB)
- **cytoplasm** (IDA:ComplexPortal)
- **cytosol** (IDA:HPA)
- **nucleoplasm** (IDA:HPA)
- **nucleus** (IDA:ComplexPortal)

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
| Strict | 15 |

**Key Papers:**
- PMID:33041871 -- Proteomic Analysis of Atrial Appendages Revealed the Pathophysiological Changes of Atrial Fibrillation. (Frontiers in physiology, 2020)
- PMID:36471356 -- Bioinformatics analysis identifies potential hub genes and crucial pathways in the pathogenesis of asthenozoospermia. (BMC medical genomics, 2022 Dec 5)
- PMID:31409899 -- Long non-coding RNA KRT19P3 suppresses proliferation and metastasis through COPS7A-mediated NF-κB pathway in gastric can (Oncogene, 2019 Nov)
- PMID:30350918 -- Blood-based dynamic genomic signature for obsessive-compulsive disorder. (American journal of medical genetics. Part B, Neuropsychiatric genetics : the official publication of the International Society of Psychiatric Genetics, 2018 Dec)
- PMID:36042172 -- Identification of Potential Biomarkers Associated with Dilated Cardiomyopathy by Weighted Gene Coexpression Network Anal (Frontiers in bioscience (Landmark edition), 2022 Aug 17)


**Research Volume Assessment**: Low (<50 papers), ample research space

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 84.6
- pLDDT >90: 71.3%, 70-90: 8.7%, 50-70: 2.5%, <50: 17.5%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| 4D10 | X-ray | 3.80 A | G/O=1-218 |
| 4D18 | X-ray | 4.08 A | G/O=1-218 |
| 4WSN | X-ray | 5.50 A | G/O/W/e/m/u=1-218 |

**Structure Assessment**: High-quality AlphaFold prediction (pLDDT 84.6), fold confidence high, PDB 3 entries verified

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
| COPS3 | 0.999 | 0.996 | -- |
| COPS6 | 0.999 | 0.994 | -- |
| COPS2 | 0.999 | 0.995 | -- |
| GPS1 | 0.999 | 0.991 | -- |
| COPS5 | 0.999 | 0.993 | -- |
| COPS8 | 0.999 | 0.995 | -- |
| COPS4 | 0.999 | 0.997 | -- |
| COPS7B | 0.987 | 0.8 | -- |
| COPS9 | 0.966 | 0.478 | -- |
| CUL4A | 0.945 | 0.828 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| TOM1L1 | psi-mi:"MI:0398"(two hybrid pooling appr | pubmed:16169070|imex:IM-1 | psi-mi:"MI:0915"(physical asso | -- |
| PPBP | psi-mi:"MI:0398"(two hybrid pooling appr | pubmed:16169070|imex:IM-1 | psi-mi:"MI:0915"(physical asso | -- |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:18850735|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| SLX4IP | psi-mi:"MI:0007"(anti tag coimmunoprecip | imex:IM-12200|pubmed:1959 | psi-mi:"MI:0914"(association) | -- |
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecip | imex:IM-12079|pubmed:1961 | psi-mi:"MI:0914"(association) | -- |
| Ddb1 | psi-mi:"MI:0676"(tandem affinity purific | imex:IM-11719|pubmed:2036 | psi-mi:"MI:0915"(physical asso | -- |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| CUL2 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |

#### UniProt Interactions
- COPS3 (13 experiments)
- NFE2L2 (2 experiments)

**PPI Assessment**: Sparse PPI network (15 STRING partners), possibly independent function protein

### 8. Scoring Overview

| Dimension | Score | Weight | Weighted | Summary |
|------|------|------|------|------|
| Nuclear Localization | 7/10 | x4 | 28 | Mainly nuclear localization, some cytoplasmic signal |
| Protein Size | 10/10 | x1 | 10 | Medium (275 aa), convenient for biochemical experiments |
| Research Novelty | 10/10 | x5 | 50 | Extremely novel (PubMed=15 papers), nearly unstudied, huge exploration space |
| 3D Structure | 9/10 | x3 | 27 | High quality (pLDDT 84.6), 71% high confidence, 17% disordered |
| Regulatory Domains | 6/10 | x2 | 12 | Limited domain annotation, but AlphaFold predicts identifiab |
| PPI Network | 3/10 | x3 | 9 | Sparse PPI network (15 STRING partners), possibly independen |
| **Weighted Total** | | | **139.0/180** | |
| **Normalized Total** | | | **76.0/100** | |

### 9. Final Decision

**SCORED: 76.0/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 15 papers, Extremely high research novelty
- Medium (275 aa), convenient for biochemical experiments
- Sufficient structural data (PDB experimental + AlphaFold)

**Weaknesses:**
- Nuclear localization needs further HPA confirmation
- Limited domain annotation
- Sparse PPI network

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9UBW8
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22COPS7A%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UBW8
- STRING: https://string-db.org/cgi/network?identifiers=COPS7A&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/COPS7A

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000111652-COPS7A/subcellular

![](https://images.proteinatlas.org/26915/298_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/26915/298_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/26915/299_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/26915/299_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/26915/300_B6_3_red_green.jpg)
![](https://images.proteinatlas.org/26915/300_B6_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
